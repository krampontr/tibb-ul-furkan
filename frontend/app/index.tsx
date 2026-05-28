import React, { useCallback, useState } from 'react';
import { View, StyleSheet, TouchableOpacity, RefreshControl, ImageBackground, ScrollView } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useFocusEffect, useRouter } from 'expo-router';
import { Body, Button, Caption, Card, H1, H3, Label } from '@/src/ui';
import { api, Profile } from '@/src/api';
import { colors, fonts, radius, spacing } from '@/src/theme';
import { useOnboarding } from '@/src/store';

const PATTERN_URL = 'https://static.prod-images.emergentagent.com/jobs/a8e0387a-3118-42ae-a69b-79e3d2f34d2c/images/94e5609f6cf42b3524e9ba410942cfc792b2971de9c67cea6dab6426d058193c.png';

export default function Home() {
  const router = useRouter();
  const reset = useOnboarding((s) => s.reset);
  const [profiles, setProfiles] = useState<Profile[]>([]);
  const [loading, setLoading] = useState(false);

  const load = useCallback(async () => {
    setLoading(true);
    try {
      const data = await api.listProfiles();
      setProfiles(data);
    } catch (e) {
      console.warn('Profile load failed', e);
    } finally {
      setLoading(false);
    }
  }, []);

  useFocusEffect(useCallback(() => { load(); }, [load]));

  const startNew = () => {
    reset();
    router.push('/onboarding/personal');
  };

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <ScrollView
        style={{ flex: 1, backgroundColor: colors.bgPrimary }}
        contentContainerStyle={{ paddingBottom: spacing.xxl }}
        showsVerticalScrollIndicator
        refreshControl={<RefreshControl refreshing={loading} onRefresh={load} tintColor={colors.textPrimary} />}
      >
        <ImageBackground
          source={{ uri: PATTERN_URL }}
          imageStyle={{ opacity: 0.08, resizeMode: 'cover' }}
          style={styles.hero}
        >
          <View style={styles.heroInner}>
            <Caption style={{ letterSpacing: 4, color: colors.accentSage }}>ﺗﺐ ﺍﻟﻔﺮﻗﺎﻥ</Caption>
            <H1 style={styles.title} testID="app-title">Tıbb-ul Furkan</H1>
            <Body style={styles.subtitle}>
              Şifaya açılan kapı, genetik yüklerden arınma vakti
            </Body>
          </View>
        </ImageBackground>

        <View style={{ paddingHorizontal: spacing.lg }}>
          <View style={styles.actionsRow}>
            <Button title="Yeni Soy Analizi" onPress={startNew} testID="start-analysis-btn" style={{ flex: 1 }} />
          </View>

          {/* Hızlı modüller: Tesbih & Kefaret */}
          <View style={styles.quickRow}>
            <TouchableOpacity style={{ flex: 1 }} onPress={() => router.push('/zikirmatik')} testID="zikirmatik-btn">
              <View style={[styles.quickCard, { backgroundColor: colors.bgSecondary, borderColor: colors.accentSage }]}>
                <Body style={{ fontSize: 28, color: colors.accentSage, fontFamily: fonts.bodyBold }}>☾</Body>
                <H3 style={{ fontSize: 16, marginTop: 4 }}>Dijital Tesbih</H3>
                <Caption>Zikirmatik · 1000&apos;e kadar</Caption>
              </View>
            </TouchableOpacity>
            <TouchableOpacity style={{ flex: 1, marginLeft: spacing.sm }} onPress={() => router.push('/kefaret')} testID="kefaret-btn">
              <View style={[styles.quickCard, { backgroundColor: colors.maternalLight, borderColor: colors.maternalPrimary }]}>
                <Body style={{ fontSize: 28, color: colors.maternalPrimary, fontFamily: fonts.bodyBold }}>✦</Body>
                <H3 style={{ fontSize: 16, marginTop: 4, color: colors.maternalPrimary }}>Kefaretlerim</H3>
                <Caption style={{ color: colors.maternalPrimary }}>Çabalamalarım</Caption>
              </View>
            </TouchableOpacity>
          </View>

          <TouchableOpacity onPress={() => router.push('/diseases')} testID="diseases-library-btn">
            <Card style={styles.libraryCard}>
              <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' }}>
                <View style={{ flex: 1 }}>
                  <Label style={{ color: colors.accentSage, marginBottom: 4 }}>KÜTÜPHANE</Label>
                  <H3>Hastalık & Soy Yükü Rehberi</H3>
                  <Caption style={{ marginTop: 4 }}>50+ hastalığın manevi izleri ve kefaretleri</Caption>
                </View>
                <Body style={{ fontSize: 24, color: colors.accentSage }}>›</Body>
              </View>
            </Card>
          </TouchableOpacity>

          <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>KAYITLI PROFİLLER ({profiles.length})</Label>

          {profiles.length === 0 && !loading ? (
            <Card>
              <Body style={{ color: colors.textSecondary, textAlign: 'center' }}>
                Henüz analiz başlatmadınız. Yeni bir soy analizi başlatın.
              </Body>
            </Card>
          ) : (
            profiles.map((item) => (
              <TouchableOpacity key={item.id} onPress={() => router.push(`/profile/${item.id}`)} testID={`profile-${item.id}`}>
                <Card style={styles.profileCard}>
                  <View style={styles.avatar}>
                    <Body style={{ color: colors.bgPrimary, fontFamily: fonts.bodyBold }}>
                      {(item.first_name?.[0] || '?').toUpperCase()}
                    </Body>
                  </View>
                  <View style={{ flex: 1, marginLeft: spacing.md }}>
                    <H3 style={{ fontSize: 18 }}>{item.first_name} {item.last_name}</H3>
                    <Caption>{item.gender === 'erkek' ? '♂ Erkek' : '♀ Kadın'} · {item.ancestors?.length || 0} ata · {(item.animal_vows?.length || 0) + (item.action_vows?.length || 0)} adak</Caption>
                  </View>
                  <Body style={{ fontSize: 24, color: colors.accentSage }}>›</Body>
                </Card>
              </TouchableOpacity>
            ))
          )}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  hero: {
    height: 260,
    backgroundColor: colors.bgSecondary,
    marginBottom: spacing.lg,
  },
  heroInner: {
    flex: 1,
    paddingHorizontal: spacing.lg,
    justifyContent: 'flex-end',
    paddingBottom: spacing.lg,
  },
  title: { fontSize: 42, marginTop: spacing.sm },
  subtitle: { color: colors.textSecondary, marginTop: spacing.xs, fontFamily: fonts.body, fontStyle: 'italic' },
  actionsRow: { flexDirection: 'row', marginBottom: spacing.md },
  quickRow: { flexDirection: 'row', marginBottom: spacing.md },
  quickCard: {
    padding: spacing.md,
    borderRadius: radius.md,
    borderWidth: 1,
    alignItems: 'flex-start',
    minHeight: 110,
  },
  libraryCard: { marginTop: spacing.xs },
  profileCard: { flexDirection: 'row', alignItems: 'center' },
  avatar: {
    width: 48,
    height: 48,
    borderRadius: radius.round,
    backgroundColor: colors.textPrimary,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
