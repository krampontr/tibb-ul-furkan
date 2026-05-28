import React, { useCallback, useEffect, useState } from 'react';
import { View, StyleSheet, TouchableOpacity, Alert, Platform } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import * as Haptics from 'expo-haptics';
import { Body, Button, Caption, Card, H1, H2, Label } from '@/src/ui';
import { colors, fonts, radius, spacing } from '@/src/theme';
import { storage } from '@/src/utils/storage';

const STORAGE_KEY = 'zikirmatik_state';
const PRESETS = [
  { label: 'Sübhânallah', target: 33 },
  { label: 'Elhamdülillah', target: 33 },
  { label: 'Allâhu Ekber', target: 34 },
  { label: 'Lâ ilâhe illallah', target: 100 },
  { label: 'Estağfirullah', target: 100 },
  { label: 'Salavat', target: 100 },
  { label: 'Serbest', target: 1000 },
];

type Saved = { count: number; target: number; zikir: string };

export default function Zikirmatik() {
  const router = useRouter();
  const [count, setCount] = useState(0);
  const [target, setTarget] = useState(33);
  const [zikir, setZikir] = useState('Sübhânallah');
  const [loaded, setLoaded] = useState(false);

  // İlk açılışta state'i yükle
  useEffect(() => {
    (async () => {
      const s = await storage.getItem<string>(STORAGE_KEY, '');
      if (s) {
        try {
          const parsed: Saved = typeof s === 'string' ? JSON.parse(s) : (s as any);
          setCount(parsed.count || 0);
          setTarget(parsed.target || 33);
          setZikir(parsed.zikir || 'Sübhânallah');
        } catch {}
      }
      setLoaded(true);
    })();
  }, []);

  // Değişikliklerde kaydet
  useEffect(() => {
    if (!loaded) return;
    storage.setItem(STORAGE_KEY, JSON.stringify({ count, target, zikir }));
  }, [count, target, zikir, loaded]);

  const tap = useCallback(() => {
    if (count >= 1000) return;
    if (Platform.OS !== 'web') {
      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light).catch(() => {});
    }
    setCount((c) => {
      const next = Math.min(c + 1, 1000);
      // Hedefe ulaştığında güçlü titreşim
      if (next === target && Platform.OS !== 'web') {
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success).catch(() => {});
      }
      return next;
    });
  }, [count, target]);

  const reset = () => {
    Alert.alert('Sayacı sıfırla', `Mevcut sayı: ${count}. Sıfırlamak istiyor musunuz?`, [
      { text: 'Vazgeç', style: 'cancel' },
      { text: 'Sıfırla', style: 'destructive', onPress: () => setCount(0) },
    ]);
  };

  const choosePreset = (p: { label: string; target: number }) => {
    if (count > 0) {
      Alert.alert('Yeni zikir', `Mevcut sayı (${count}) sıfırlanacak. Devam edilsin mi?`, [
        { text: 'Vazgeç', style: 'cancel' },
        { text: 'Tamam', onPress: () => { setZikir(p.label); setTarget(p.target); setCount(0); } },
      ]);
    } else {
      setZikir(p.label); setTarget(p.target); setCount(0);
    }
  };

  const pct = Math.min((count / target) * 100, 100);
  const reached = count >= target;
  const maxed = count >= 1000;

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} testID="back-btn">
          <Body style={{ color: colors.accentSage }}>‹ Geri</Body>
        </TouchableOpacity>
        <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>DİJİTAL TESBİH</Caption>
        <TouchableOpacity onPress={reset} testID="reset-btn">
          <Caption style={{ color: colors.errorVow }}>↺ Sıfırla</Caption>
        </TouchableOpacity>
      </View>

      <View style={styles.body}>
        <View style={{ alignItems: 'center', marginBottom: spacing.lg }}>
          <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>ŞU AN ÇEKTİĞİNİZ</Caption>
          <H2 style={{ marginTop: spacing.xs }}>{zikir}</H2>
          <Caption style={{ marginTop: 4 }}>Hedef: {target}</Caption>
        </View>

        <TouchableOpacity activeOpacity={0.85} onPress={tap} disabled={maxed} style={styles.bead} testID="tap-bead">
          <View style={styles.beadInner}>
            <View style={styles.beadCenter}>
              <H1 style={[styles.countText, { color: reached ? colors.accentSage : colors.textPrimary }]}>{count}</H1>
              <Caption style={{ color: colors.textSecondary, marginTop: 2 }}>/{target}</Caption>
            </View>
            {/* Progress ring as background */}
            <View style={[styles.beadProgress, { transform: [{ rotate: `${(pct / 100) * 360}deg` }] }]} />
          </View>
        </TouchableOpacity>

        {reached && !maxed && (
          <Caption style={{ marginTop: spacing.md, textAlign: 'center', color: colors.accentSage, fontFamily: fonts.bodyMedium }}>
            ✓ Hedefe ulaştınız. Devam edebilir veya yeni zikir seçebilirsiniz.
          </Caption>
        )}
        {maxed && (
          <Caption style={{ marginTop: spacing.md, textAlign: 'center', color: colors.errorVow }}>
            Üst sınır 1000'e ulaştınız. Lütfen sıfırlayıp devam edin.
          </Caption>
        )}

        <View style={{ flexDirection: 'row', gap: spacing.sm, marginTop: spacing.lg }}>
          <Button title="−1" variant="secondary" onPress={() => setCount((c) => Math.max(0, c - 1))} style={{ flex: 1 }} testID="decrement-btn" />
          <Button title={reached ? 'Yeni Tur' : '+10'} variant="secondary" onPress={() => setCount((c) => Math.min(1000, c + 10))} style={{ flex: 1 }} testID="plus10-btn" />
        </View>

        <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>HAZIR ZİKİRLER</Label>
        <View style={styles.presetWrap}>
          {PRESETS.map((p) => (
            <TouchableOpacity key={p.label} onPress={() => choosePreset(p)} testID={`preset-${p.label}`}>
              <View style={[styles.preset, zikir === p.label && styles.presetActive]}>
                <Caption style={[{ color: colors.textPrimary, fontFamily: fonts.bodyMedium }, zikir === p.label && { color: colors.bgPrimary }]}>
                  {p.label}
                </Caption>
                <Caption style={[{ color: colors.textSecondary, fontSize: 10 }, zikir === p.label && { color: colors.bgSecondary }]}>
                  {p.target}
                </Caption>
              </View>
            </TouchableOpacity>
          ))}
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingHorizontal: spacing.lg, paddingVertical: spacing.sm },
  body: { flex: 1, paddingHorizontal: spacing.lg, paddingTop: spacing.md },
  bead: {
    alignSelf: 'center',
    width: 240,
    height: 240,
    borderRadius: 120,
    backgroundColor: colors.bgSecondary,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: colors.borderSubtle,
    shadowColor: colors.textPrimary,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.08,
    shadowRadius: 12,
    elevation: 3,
  },
  beadInner: {
    width: 200, height: 200, borderRadius: 100,
    backgroundColor: colors.bgCard,
    borderWidth: 2,
    borderColor: colors.accentSage,
    alignItems: 'center',
    justifyContent: 'center',
  },
  beadCenter: { alignItems: 'center', justifyContent: 'center' },
  beadProgress: { position: 'absolute', width: 0, height: 0 },
  countText: { fontSize: 64, lineHeight: 70 },
  presetWrap: { flexDirection: 'row', flexWrap: 'wrap' },
  preset: {
    paddingHorizontal: 12,
    paddingVertical: 8,
    borderRadius: radius.round,
    borderWidth: 1,
    borderColor: colors.borderSubtle,
    backgroundColor: colors.bgCard,
    marginRight: spacing.sm,
    marginBottom: spacing.sm,
    alignItems: 'center',
  },
  presetActive: { backgroundColor: colors.textPrimary, borderColor: colors.textPrimary },
});
