import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { View, StyleSheet, TouchableOpacity, Alert, Platform, ScrollView, TextInput } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import * as Haptics from 'expo-haptics';
import { Body, Button, Caption, Card, H1, H2, H3, Label } from '@/src/ui';
import { colors, fonts, radius, spacing } from '@/src/theme';
import { storage } from '@/src/utils/storage';

const STORAGE_KEY = 'zikirmatik_v2';

type ZikirRecord = {
  id: string;
  name: string;
  target: number;
  count: number;
  is_preset: boolean;
  last_used?: string;
};

type SavedState = {
  records: ZikirRecord[];
  active_id: string | null;
};

const PRESETS: { name: string; target: number }[] = [
  { name: 'Sübhânallah', target: 33 },
  { name: 'Elhamdülillah', target: 33 },
  { name: 'Allâhu Ekber', target: 34 },
  { name: 'Lâ ilâhe illallah', target: 100 },
  { name: 'Estağfirullah', target: 100 },
  { name: 'Salavat', target: 100 },
];

const uuid = () => Math.random().toString(36).slice(2) + Date.now().toString(36);

const initialRecords = (): ZikirRecord[] =>
  PRESETS.map((p) => ({
    id: `preset_${p.name}`,
    name: p.name,
    target: p.target,
    count: 0,
    is_preset: true,
  }));

export default function Zikirmatik() {
  const router = useRouter();
  const [records, setRecords] = useState<ZikirRecord[]>(initialRecords());
  const [activeId, setActiveId] = useState<string | null>(null);
  const [loaded, setLoaded] = useState(false);
  const [customName, setCustomName] = useState('');
  const [customTarget, setCustomTarget] = useState('33');

  // Yükle
  useEffect(() => {
    (async () => {
      const raw = await storage.getItem<string>(STORAGE_KEY, '');
      if (raw) {
        try {
          const parsed: SavedState = typeof raw === 'string' ? JSON.parse(raw) : (raw as any);
          if (parsed?.records?.length) {
            // Preset'leri her zaman tut, kullanıcı kayıtlarını birleştir
            const merged = [...parsed.records];
            for (const p of initialRecords()) {
              if (!merged.find((r) => r.id === p.id)) merged.push(p);
            }
            setRecords(merged);
          }
          setActiveId(parsed?.active_id ?? null);
        } catch {}
      }
      setLoaded(true);
    })();
  }, []);

  // Kaydet
  useEffect(() => {
    if (!loaded) return;
    storage.setItem(STORAGE_KEY, JSON.stringify({ records, active_id: activeId }));
  }, [records, activeId, loaded]);

  const active = useMemo(() => records.find((r) => r.id === activeId) || null, [records, activeId]);
  const totalCount = useMemo(() => records.reduce((s, r) => s + (r.count || 0), 0), [records]);

  const updateActive = (mut: (r: ZikirRecord) => ZikirRecord) => {
    if (!activeId) return;
    setRecords((prev) => prev.map((r) => (r.id === activeId ? mut(r) : r)));
  };

  const tap = useCallback(() => {
    if (!active) return;
    if (active.count >= 1000) return;
    if (Platform.OS !== 'web') {
      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light).catch(() => {});
    }
    updateActive((r) => {
      const next = Math.min(r.count + 1, 1000);
      if (next === r.target && Platform.OS !== 'web') {
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success).catch(() => {});
      }
      return { ...r, count: next, last_used: new Date().toISOString() };
    });
  }, [active, activeId]);

  const resetActive = () => {
    if (!active) return;
    Alert.alert('Sıfırla', `"${active.name}" sayacı (${active.count}) sıfırlanacak. Emin misiniz?`, [
      { text: 'Vazgeç', style: 'cancel' },
      { text: 'Sıfırla', style: 'destructive', onPress: () => updateActive((r) => ({ ...r, count: 0 })) },
    ]);
  };

  const cancelActive = () => {
    setActiveId(null);
  };

  const selectZikir = (id: string) => {
    setActiveId(id);
  };

  const removeRecord = (id: string) => {
    const r = records.find((x) => x.id === id);
    if (!r) return;
    Alert.alert(
      r.is_preset ? 'Sayacı sıfırla' : 'Zikri sil',
      r.is_preset
        ? `"${r.name}" sayacı (${r.count}) sıfırlanacak.`
        : `"${r.name}" zikrini geçmişten silmek istiyor musunuz?`,
      [
        { text: 'Vazgeç', style: 'cancel' },
        {
          text: r.is_preset ? 'Sıfırla' : 'Sil',
          style: 'destructive',
          onPress: () => {
            if (r.is_preset) {
              setRecords((prev) => prev.map((x) => (x.id === id ? { ...x, count: 0 } : x)));
            } else {
              setRecords((prev) => prev.filter((x) => x.id !== id));
              if (activeId === id) setActiveId(null);
            }
          },
        },
      ]
    );
  };

  const addCustomZikir = () => {
    const name = customName.trim();
    if (!name) {
      Alert.alert('Eksik bilgi', 'Lütfen zikir adını yazın.');
      return;
    }
    const target = Math.max(1, Math.min(1000, parseInt(customTarget) || 33));
    const newRec: ZikirRecord = {
      id: uuid(),
      name,
      target,
      count: 0,
      is_preset: false,
    };
    setRecords((prev) => [newRec, ...prev]);
    setActiveId(newRec.id);
    setCustomName('');
    setCustomTarget('33');
  };

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} testID="back-btn">
          <Body style={{ color: colors.accentSage }}>‹ Geri</Body>
        </TouchableOpacity>
        <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>DİJİTAL TESBİH</Caption>
        <View style={{ width: 50 }} />
      </View>

      <ScrollView
        style={{ flex: 1 }}
        contentContainerStyle={{ paddingHorizontal: spacing.lg, paddingBottom: spacing.xxl }}
        keyboardShouldPersistTaps="handled"
        showsVerticalScrollIndicator
      >
        {/* Aktif sayaç bölümü */}
        {active ? (
          <View style={{ alignItems: 'center', marginTop: spacing.md }}>
            <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>ŞU AN ÇEKTİĞİNİZ</Caption>
            <H2 style={{ marginTop: spacing.xs, textAlign: 'center' }}>{active.name}</H2>
            <Caption style={{ marginTop: 4 }}>Hedef: {active.target}</Caption>

            <TouchableOpacity
              activeOpacity={0.85}
              onPress={tap}
              disabled={active.count >= 1000}
              style={styles.bead}
              testID="tap-bead"
            >
              <View style={styles.beadInner}>
                <H1 style={[styles.countText, { color: active.count >= active.target ? colors.accentSage : colors.textPrimary }]}>
                  {active.count}
                </H1>
                <Caption style={{ color: colors.textSecondary, marginTop: 2 }}>/{active.target}</Caption>
              </View>
            </TouchableOpacity>

            {active.count >= active.target && active.count < 1000 && (
              <Caption style={{ marginTop: spacing.md, textAlign: 'center', color: colors.accentSage, fontFamily: fonts.bodyMedium }}>
                ✓ Hedefe ulaştınız. Devam edebilir veya yeni zikir seçebilirsiniz.
              </Caption>
            )}
            {active.count >= 1000 && (
              <Caption style={{ marginTop: spacing.md, textAlign: 'center', color: colors.errorVow }}>
                Üst sınır 1000&apos;e ulaştınız. Sıfırlayıp devam edebilirsiniz.
              </Caption>
            )}

            <View style={{ flexDirection: 'row', gap: spacing.sm, marginTop: spacing.lg, width: '100%' }}>
              <Button title="−1" variant="secondary" onPress={() => updateActive((r) => ({ ...r, count: Math.max(0, r.count - 1) }))} style={{ flex: 1 }} testID="decrement-btn" />
              <Button title="+10" variant="secondary" onPress={() => updateActive((r) => ({ ...r, count: Math.min(1000, r.count + 10) }))} style={{ flex: 1 }} testID="plus10-btn" />
            </View>
            <View style={{ flexDirection: 'row', gap: spacing.sm, marginTop: spacing.sm, width: '100%' }}>
              <Button title="↺ Sıfırla" variant="secondary" onPress={resetActive} style={{ flex: 1 }} testID="reset-btn" />
              <Button title="✕ Seçimi İptal Et" variant="secondary" onPress={cancelActive} style={{ flex: 1 }} testID="cancel-active-btn" />
            </View>
          </View>
        ) : (
          <Card style={{ marginTop: spacing.md, alignItems: 'center', paddingVertical: spacing.xl, backgroundColor: colors.bgSecondary, borderColor: colors.accentSage }}>
            <Body style={{ fontSize: 32, color: colors.accentSage }}>☾</Body>
            <H3 style={{ marginTop: spacing.sm }}>Bir zikir seçin</H3>
            <Caption style={{ marginTop: 4, textAlign: 'center' }}>
              Aşağıdan hazır bir zikir seçin veya kendi zikrinizi oluşturun.
            </Caption>
          </Card>
        )}

        {/* Özel zikir ekle */}
        <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>KENDİ ZİKRİNİZİ EKLEYİN</Label>
        <Card>
          <View style={{ flexDirection: 'row', gap: spacing.sm, alignItems: 'flex-end' }}>
            <View style={{ flex: 2 }}>
              <Caption style={styles.miniLabel}>ZİKİR ADI</Caption>
              <TextInput
                value={customName}
                onChangeText={setCustomName}
                placeholder="Örn: Yâ Vedûd, Hasbiyallah"
                placeholderTextColor={colors.accentSage}
                style={styles.input}
                testID="custom-name"
              />
            </View>
            <View style={{ flex: 1 }}>
              <Caption style={styles.miniLabel}>HEDEF</Caption>
              <TextInput
                value={customTarget}
                onChangeText={(t) => setCustomTarget(t.replace(/\D/g, ''))}
                keyboardType="number-pad"
                placeholder="33"
                placeholderTextColor={colors.accentSage}
                style={styles.input}
                testID="custom-target"
              />
            </View>
          </View>
          <Button title="+ Zikir Oluştur ve Başla" onPress={addCustomZikir} style={{ marginTop: spacing.md }} testID="add-custom-zikir" />
        </Card>

        {/* Zikir listesi - hazır + özel + geçmiş */}
        <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginTop: spacing.lg, marginBottom: spacing.sm }}>
          <Label>ZİKİRLERİM & GEÇMİŞ</Label>
          <Caption style={{ color: colors.accentSage, fontFamily: fonts.bodyMedium }}>
            Toplam: {totalCount.toLocaleString('tr-TR')}
          </Caption>
        </View>

        {records.map((r) => {
          const isActive = r.id === activeId;
          const pct = Math.min(100, (r.count / r.target) * 100);
          return (
            <TouchableOpacity key={r.id} onPress={() => selectZikir(r.id)} testID={`zikir-${r.id}`}>
              <Card style={[styles.rowCard, isActive && styles.rowCardActive]}>
                <View style={{ flex: 1 }}>
                  <View style={{ flexDirection: 'row', alignItems: 'center' }}>
                    {isActive && <Body style={{ color: colors.accentSage, marginRight: 6 }}>●</Body>}
                    <H3 style={{ fontSize: 16, flex: 1 }}>{r.name}</H3>
                    {!r.is_preset && (
                      <View style={styles.customBadge}>
                        <Caption style={{ color: colors.bgPrimary, fontSize: 9, fontFamily: fonts.bodyBold }}>ÖZEL</Caption>
                      </View>
                    )}
                  </View>
                  <Caption style={{ marginTop: 2 }}>
                    {r.count.toLocaleString('tr-TR')} / {r.target} {r.count >= r.target ? '· ✓ Hedef tamam' : ''}
                  </Caption>
                  <View style={styles.progressBar}>
                    <View style={[styles.progressFill, { width: `${pct}%`, backgroundColor: r.count >= r.target ? colors.accentSage : colors.textPrimary }]} />
                  </View>
                  {r.last_used && (
                    <Caption style={{ color: colors.accentSage, fontSize: 10, marginTop: 4 }}>
                      Son: {new Date(r.last_used).toLocaleString('tr-TR', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' })}
                    </Caption>
                  )}
                </View>
                <TouchableOpacity onPress={() => removeRecord(r.id)} hitSlop={8} style={{ paddingLeft: 8 }} testID={`remove-${r.id}`}>
                  <Body style={{ color: colors.errorVow, fontSize: 20 }}>{r.is_preset ? '↺' : '×'}</Body>
                </TouchableOpacity>
              </Card>
            </TouchableOpacity>
          );
        })}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingHorizontal: spacing.lg, paddingVertical: spacing.sm },
  bead: {
    width: 200, height: 200, borderRadius: 100,
    backgroundColor: colors.bgSecondary,
    alignItems: 'center', justifyContent: 'center',
    borderWidth: 1, borderColor: colors.borderSubtle,
    marginTop: spacing.lg,
    shadowColor: colors.textPrimary,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.08,
    shadowRadius: 12,
    elevation: 3,
  },
  beadInner: {
    width: 170, height: 170, borderRadius: 85,
    backgroundColor: colors.bgCard,
    borderWidth: 2, borderColor: colors.accentSage,
    alignItems: 'center', justifyContent: 'center',
  },
  countText: { fontSize: 56, lineHeight: 62 },
  miniLabel: {
    fontFamily: fonts.bodyMedium, fontSize: 10, color: colors.textSecondary,
    textTransform: 'uppercase', letterSpacing: 1, marginBottom: 4,
  },
  input: {
    fontFamily: fonts.body, fontSize: 15, color: colors.textPrimary,
    borderBottomWidth: 1, borderBottomColor: colors.borderSubtle,
    paddingVertical: 6,
  },
  rowCard: { flexDirection: 'row', alignItems: 'center', paddingVertical: spacing.sm + 2 },
  rowCardActive: { borderColor: colors.accentSage, borderWidth: 1.5, backgroundColor: colors.bgSecondary },
  customBadge: {
    backgroundColor: colors.maternalPrimary,
    paddingHorizontal: 6, paddingVertical: 2,
    borderRadius: radius.round, marginLeft: 6,
  },
  progressBar: {
    height: 4, width: '100%',
    backgroundColor: colors.bgSecondary,
    borderRadius: 2, marginTop: 6, overflow: 'hidden',
  },
  progressFill: { height: 4, borderRadius: 2 },
});
