import React, { useCallback, useState } from 'react';
import { View, StyleSheet, TouchableOpacity, Alert, ScrollView } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useFocusEffect, useLocalSearchParams, useRouter } from 'expo-router';
import { Body, Button, Caption, Card, H1, H2, H3, Label, Screen } from '@/src/ui';
import { api, AnalysisResult, Profile } from '@/src/api';
import { colors, fonts, radius, spacing } from '@/src/theme';

export default function ProfileDetail() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const router = useRouter();
  const [profile, setProfile] = useState<Profile | null>(null);
  const [analysis, setAnalysis] = useState<AnalysisResult | null>(null);
  const [loading, setLoading] = useState(true);

  const load = useCallback(async () => {
    if (!id) return;
    setLoading(true);
    try {
      const [p, a] = await Promise.all([api.getProfile(id), api.getAnalysis(id)]);
      setProfile(p); setAnalysis(a);
    } catch (e: any) {
      Alert.alert('Hata', e.message);
    } finally {
      setLoading(false);
    }
  }, [id]);

  useFocusEffect(useCallback(() => { load(); }, [load]));

  const handleDelete = () => {
    Alert.alert('Profili sil', 'Bu profil ve analizler silinecek. Emin misiniz?', [
      { text: 'Vazgeç', style: 'cancel' },
      {
        text: 'Sil', style: 'destructive', onPress: async () => {
          await api.deleteProfile(id!);
          router.replace('/');
        }
      },
    ]);
  };

  if (!profile || !analysis) {
    return (
      <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
          <Body>{loading ? 'Yükleniyor...' : 'Profil bulunamadı.'}</Body>
        </View>
      </SafeAreaView>
    );
  }

  const total = analysis.maternal_burden_score + analysis.paternal_burden_score + analysis.self_burden_score;
  const matPct = total ? Math.round((analysis.maternal_burden_score / total) * 100) : 0;
  const patPct = total ? Math.round((analysis.paternal_burden_score / total) * 100) : 0;
  const selfPct = total ? 100 - matPct - patPct : 0;

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <Screen>
        <ScrollView showsVerticalScrollIndicator={false} contentContainerStyle={{ paddingBottom: spacing.xl }}>
          <View style={{ flexDirection: 'row', justifyContent: 'space-between', paddingTop: spacing.sm }}>
            <TouchableOpacity onPress={() => router.replace('/')} testID="home-btn">
              <Body style={{ color: colors.accentSage }}>‹ Ana sayfa</Body>
            </TouchableOpacity>
            <TouchableOpacity onPress={handleDelete} testID="delete-btn">
              <Caption style={{ color: colors.errorVow }}>Sil</Caption>
            </TouchableOpacity>
          </View>

          <View style={{ marginTop: spacing.md }}>
            <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>SOY TESPİT RAPORU</Caption>
            <H1 style={{ fontSize: 36, marginTop: spacing.xs }}>{profile.first_name} {profile.last_name}</H1>
            <Caption>{profile.gender === 'erkek' ? '♂ Erkek' : '♀ Kadın'} · Doğum: {profile.birth_date}</Caption>
          </View>

          <Card style={{ marginTop: spacing.lg }}>
            <Label style={{ marginBottom: spacing.sm }}>SOY YÜKÜ DAĞILIMI</Label>
            <View style={styles.barRow}>
              <View style={[styles.bar, { flex: matPct || 0.001, backgroundColor: colors.maternalPrimary, borderTopLeftRadius: 6, borderBottomLeftRadius: 6 }]} />
              <View style={[styles.bar, { flex: patPct || 0.001, backgroundColor: colors.paternalPrimary }]} />
              <View style={[styles.bar, { flex: selfPct || 0.001, backgroundColor: colors.textPrimary, borderTopRightRadius: 6, borderBottomRightRadius: 6 }]} />
            </View>
            <View style={{ flexDirection: 'row', justifyContent: 'space-between', marginTop: spacing.sm }}>
              <View style={styles.legend}>
                <View style={[styles.dot, { backgroundColor: colors.maternalPrimary }]} />
                <Caption>Anne: {analysis.maternal_burden_score} ({matPct}%)</Caption>
              </View>
              <View style={styles.legend}>
                <View style={[styles.dot, { backgroundColor: colors.paternalPrimary }]} />
                <Caption>Baba: {analysis.paternal_burden_score} ({patPct}%)</Caption>
              </View>
              <View style={styles.legend}>
                <View style={[styles.dot, { backgroundColor: colors.textPrimary }]} />
                <Caption>Kendi: {analysis.self_burden_score} ({selfPct}%)</Caption>
              </View>
            </View>
          </Card>

          <View style={{ flexDirection: 'row', gap: spacing.sm, marginTop: spacing.sm }}>
            <Button title="Zihin Haritası" onPress={() => router.push(`/mindmap/${id}`)} style={{ flex: 1 }} testID="mindmap-btn" />
            <Button title="Detaylı Analiz" onPress={() => router.push(`/analysis/${id}`)} variant="secondary" style={{ flex: 1 }} testID="analysis-btn" />
          </View>

          <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>BASKIN MANEVİ İZLER</Label>
          {analysis.dominant_categories.length === 0 ? (
            <Card><Caption style={{ textAlign: 'center' }}>Henüz belirgin bir iz tespit edilmedi.</Caption></Card>
          ) : (
            analysis.dominant_categories.map((c) => (
              <Card key={c.category} style={styles.dominantCard}>
                <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
                  <Body style={{ fontFamily: fonts.bodySemi, flex: 1 }}>{c.label}</Body>
                  <View style={styles.scorePill}><Caption style={{ color: colors.bgPrimary, fontFamily: fonts.bodyBold }}>{c.score}</Caption></View>
                </View>
              </Card>
            ))
          )}

          <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>TESPİT EDİLEN HASTALIK BAĞLANTILARI ({analysis.matches.length})</Label>
          {analysis.matches.length === 0 ? (
            <Card><Caption style={{ textAlign: 'center' }}>Mevcut sağlık bilgilerinize göre veritabanında eşleşme bulunamadı. Daha fazla detay ekleyin.</Caption></Card>
          ) : (
            analysis.matches.slice(0, 5).map((m, i) => (
              <Card key={i}>
                <H3 style={{ fontSize: 18 }}>{m.disease}</H3>
                <Caption style={{ marginBottom: spacing.sm }}>{m.category} · Skor: {m.total_score}</Caption>
                {m.matched_causes.slice(0, 3).map((c, j) => (
                  <View key={j} style={{ flexDirection: 'row', marginBottom: 4 }}>
                    <View style={[styles.sideTag, { backgroundColor: c.source_side === 'maternal' ? colors.maternalLight : c.source_side === 'paternal' ? colors.paternalLight : colors.bgSecondary }]}>
                      <Caption style={{ color: c.source_side === 'maternal' ? colors.maternalPrimary : c.source_side === 'paternal' ? colors.paternalPrimary : colors.textPrimary, fontSize: 10 }}>
                        {c.source_side === 'maternal' ? 'A' : c.source_side === 'paternal' ? 'B' : 'K'}
                      </Caption>
                    </View>
                    <Caption style={{ flex: 1 }}>{c.category_label}</Caption>
                  </View>
                ))}
              </Card>
            ))
          )}

          {analysis.matches.length > 5 && (
            <Button title={`Hepsini gör (${analysis.matches.length})`} variant="ghost" onPress={() => router.push(`/analysis/${id}`)} />
          )}
        </ScrollView>
      </Screen>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  barRow: { flexDirection: 'row', height: 12, overflow: 'hidden', borderRadius: 6 },
  bar: { height: 12 },
  legend: { flexDirection: 'row', alignItems: 'center', gap: 6 },
  dot: { width: 8, height: 8, borderRadius: 4 },
  dominantCard: { paddingVertical: spacing.sm + 2 },
  scorePill: { backgroundColor: colors.textPrimary, paddingHorizontal: 10, paddingVertical: 4, borderRadius: radius.round, minWidth: 36, alignItems: 'center' },
  sideTag: { width: 18, height: 18, borderRadius: 9, alignItems: 'center', justifyContent: 'center', marginRight: 6 },
});
