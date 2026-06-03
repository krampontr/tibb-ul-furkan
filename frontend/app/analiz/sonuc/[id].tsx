import React, { useCallback, useEffect, useState } from 'react';
import { View, StyleSheet, ScrollView, TouchableOpacity, ActivityIndicator, Alert } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { Body, Button, Caption, Card, H1, H2, H3, Label } from '@/src/ui';
import { formApi, FormSubmission } from '@/src/formApi';
import { colors, fonts, radius, spacing } from '@/src/theme';

export default function AnalizSonuc() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const router = useRouter();
  const [submission, setSubmission] = useState<FormSubmission | null>(null);
  const [running, setRunning] = useState(false);
  const [analysis, setAnalysis] = useState<string | null>(null);

  const load = useCallback(async () => {
    if (!id) return;
    const s = await formApi.get(id);
    setSubmission(s);
    if (s.ai_analysis) setAnalysis(s.ai_analysis);
  }, [id]);

  useEffect(() => { load(); }, [load]);

  const runAnalysis = async () => {
    if (!id) return;
    setRunning(true);
    try {
      const res = await formApi.analyze(id);
      setAnalysis(res.ai_analysis);
    } catch (e: any) {
      Alert.alert('Analiz yapılamadı', e.message || 'Lütfen tekrar deneyin.');
    } finally {
      setRunning(false);
    }
  };

  // İlk açılışta otomatik başlat
  useEffect(() => {
    if (submission && !submission.ai_analysis && !analysis && !running) {
      runAnalysis();
    }
  }, [submission]);

  if (!submission) {
    return (
      <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
          <Body>Yükleniyor…</Body>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.replace('/')} testID="home-btn">
          <Body style={{ color: colors.accentSage }}>‹ Ana sayfa</Body>
        </TouchableOpacity>
        <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>ANALİZ</Caption>
        <View style={{ width: 70 }} />
      </View>

      <ScrollView contentContainerStyle={{ paddingHorizontal: spacing.lg, paddingBottom: spacing.xxl }}>
        <H1 style={{ fontSize: 32, marginTop: spacing.sm }}>{submission.ad_soyad}</H1>
        <Caption>{submission.cinsiyet === 'erkek' ? '♂ Erkek' : submission.cinsiyet === 'kadın' ? '♀ Kadın' : ''} · Doğum: {submission.dogum_tarihi}</Caption>

        {running && (
          <Card style={{ marginTop: spacing.lg, backgroundColor: colors.bgSecondary, borderColor: colors.accentSage, alignItems: 'center', paddingVertical: spacing.lg }}>
            <ActivityIndicator color={colors.textPrimary} />
            <Body style={{ marginTop: spacing.sm, fontStyle: 'italic' }}>Yapay zekâ tespitleri hazırlıyor…</Body>
            <Caption style={{ marginTop: 4, color: colors.textSecondary }}>Bu işlem 15-30 saniye sürebilir.</Caption>
          </Card>
        )}

        {analysis && !running && (
          <Card style={{ marginTop: spacing.lg, backgroundColor: colors.bgSecondary, borderColor: colors.accentSage }}>
            <Label style={{ color: colors.accentSage, marginBottom: spacing.sm }}>✦ OLASI TESPİTLER</Label>
            <Body style={{ lineHeight: 24 }}>{analysis}</Body>
          </Card>
        )}

        {!analysis && !running && (
          <Button title="✦ Analizi Başlat" onPress={runAnalysis} style={{ marginTop: spacing.lg }} testID="run-analysis" />
        )}

        {analysis && !running && (
          <Button title="↻ Tekrar Analiz Et" variant="secondary" onPress={runAnalysis} style={{ marginTop: spacing.md }} />
        )}

        <Caption style={{ marginTop: spacing.lg, color: colors.textSecondary, textAlign: 'center', fontStyle: 'italic' }}>
          Bu içerik tıbbi tavsiye değildir, yalnızca manevi yönden olası işaretleri sunar.
        </Caption>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingHorizontal: spacing.lg, paddingVertical: spacing.sm },
});
