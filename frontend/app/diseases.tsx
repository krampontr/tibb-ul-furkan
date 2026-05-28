import React, { useEffect, useState } from 'react';
import { View, StyleSheet, TouchableOpacity, ScrollView, FlatList, TextInput } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { Body, Caption, Card, H2, H3, Label } from '@/src/ui';
import { api } from '@/src/api';
import { colors, fonts, radius, spacing } from '@/src/theme';

type Disease = {
  name: string;
  category: string;
  symptoms: string[];
  causes: { category: string; weight: number; detail: string }[];
  remedy: string;
};

export default function DiseasesLibrary() {
  const router = useRouter();
  const [diseases, setDiseases] = useState<Disease[]>([]);
  const [labels, setLabels] = useState<Record<string, string>>({});
  const [q, setQ] = useState('');
  const [selected, setSelected] = useState<Disease | null>(null);

  useEffect(() => {
    api.listDiseases().then(setDiseases).catch(() => {});
    api.listCauseCategories().then(setLabels).catch(() => {});
  }, []);

  const filtered = diseases.filter((d) =>
    !q.trim() ||
    d.name.toLowerCase().includes(q.toLowerCase()) ||
    d.category.toLowerCase().includes(q.toLowerCase()) ||
    d.symptoms.some((s) => s.toLowerCase().includes(q.toLowerCase()))
  );

  if (selected) {
    return (
      <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
        <View style={styles.header}>
          <TouchableOpacity onPress={() => setSelected(null)} testID="back-btn">
            <Body style={{ color: colors.accentSage }}>‹ Liste</Body>
          </TouchableOpacity>
          <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>HASTALIK DETAYI</Caption>
          <View style={{ width: 60 }} />
        </View>
        <ScrollView contentContainerStyle={{ paddingHorizontal: spacing.lg, paddingBottom: spacing.xl }}>
          <H2 style={{ marginTop: spacing.sm }}>{selected.name}</H2>
          <Caption style={{ color: colors.textSecondary, marginTop: 4 }}>{selected.category}</Caption>

          <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>SEMPTOMLAR</Label>
          {selected.symptoms.map((s, i) => <Caption key={i}>· {s}</Caption>)}

          <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>MANEVİ SEBEPLER</Label>
          {selected.causes.map((c, i) => (
            <Card key={i} style={{ paddingVertical: spacing.sm + 2 }}>
              <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
                <Body style={{ fontFamily: fonts.bodySemi, flex: 1 }}>{labels[c.category] || c.category}</Body>
                <View style={styles.weightPill}><Caption style={{ color: colors.bgPrimary, fontFamily: fonts.bodyBold }}>{c.weight}</Caption></View>
              </View>
              <Caption style={{ marginTop: 4 }}>{c.detail}</Caption>
            </Card>
          ))}

          <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>ÖNERİLEN MANEVİ KEFARET</Label>
          <Body style={{ fontStyle: 'italic', color: colors.textSecondary }}>{selected.remedy}</Body>
        </ScrollView>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} testID="back-btn">
          <Body style={{ color: colors.accentSage }}>‹ Geri</Body>
        </TouchableOpacity>
        <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>KÜTÜPHANE</Caption>
        <View style={{ width: 60 }} />
      </View>

      <View style={{ paddingHorizontal: spacing.lg }}>
        <H2>Hastalık Rehberi</H2>
        <Caption style={{ color: colors.textSecondary, marginTop: 4, marginBottom: spacing.md }}>
          {diseases.length} hastalığın manevi izleri ve önerilen kefaretleri.
        </Caption>
        <TextInput
          placeholder="Hastalık veya semptom ara…"
          placeholderTextColor={colors.accentSage}
          value={q}
          onChangeText={setQ}
          style={styles.search}
          testID="search-input"
        />
      </View>

      <FlatList
        data={filtered}
        keyExtractor={(d) => d.name}
        contentContainerStyle={{ paddingHorizontal: spacing.lg, paddingBottom: spacing.xl }}
        renderItem={({ item }) => (
          <TouchableOpacity onPress={() => setSelected(item)} testID={`disease-${item.name}`}>
            <Card>
              <H3 style={{ fontSize: 17 }}>{item.name}</H3>
              <Caption>{item.category} · {item.causes.length} sebep</Caption>
            </Card>
          </TouchableOpacity>
        )}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingHorizontal: spacing.lg, paddingVertical: spacing.sm },
  search: {
    backgroundColor: colors.bgCard,
    borderWidth: 1,
    borderColor: colors.borderSubtle,
    borderRadius: radius.md,
    paddingHorizontal: spacing.md,
    paddingVertical: 12,
    fontFamily: fonts.body,
    fontSize: 15,
    color: colors.textPrimary,
    marginBottom: spacing.md,
  },
  weightPill: { backgroundColor: colors.textPrimary, paddingHorizontal: 10, paddingVertical: 3, borderRadius: radius.round, minWidth: 30, alignItems: 'center' },
});
