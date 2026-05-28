import React, { useState } from 'react';
import { View, StyleSheet, TouchableOpacity, KeyboardAvoidingView, Platform } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { Body, Button, Caption, H2, Input, KeyboardScroll, Label, ProgressBar, Screen } from '@/src/ui';
import { useOnboarding } from '@/src/store';
import { colors, fonts, radius, spacing } from '@/src/theme';

export default function PersonalStage() {
  const router = useRouter();
  const { first_name, last_name, birth_date, gender, set } = useOnboarding();
  const [error, setError] = useState('');

  const onNext = () => {
    if (!first_name.trim() || !last_name.trim() || !birth_date.trim() || !gender) {
      setError('Lütfen tüm alanları doldurun.');
      return;
    }
    setError('');
    router.push('/onboarding/health');
  };

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined} style={{ flex: 1 }}>
        <Screen>
          <View style={{ paddingTop: spacing.md }}>
            <Caption style={{ color: colors.accentSage }}>1. AŞAMA / 4</Caption>
            <View style={{ marginTop: spacing.xs, marginBottom: spacing.lg }}>
              <ProgressBar step={1} total={4} />
            </View>
            <H2>Kişisel Bilgiler</H2>
            <Body style={{ color: colors.textSecondary, marginTop: spacing.xs }}>
              Adınız, doğum tarihiniz ve cinsiyetiniz analizin temelidir.
            </Body>
          </View>

          <KeyboardScroll>
            <View style={{ marginTop: spacing.lg }}>
              <Input label="Adınız" value={first_name} onChangeText={(t) => set({ first_name: t })} placeholder="Örn: Ahmet" testID="input-first-name" />
              <Input label="Soyadınız" value={last_name} onChangeText={(t) => set({ last_name: t })} placeholder="Örn: Yılmaz" testID="input-last-name" />
              <Input label="Doğum Tarihi" value={birth_date} onChangeText={(t) => set({ birth_date: t })} placeholder="GG.AA.YYYY" testID="input-birth-date" />

              <Label style={{ marginTop: spacing.md, marginBottom: spacing.sm }}>CİNSİYET</Label>
              <View style={{ flexDirection: 'row', gap: spacing.sm }}>
                {(['erkek', 'kadın'] as const).map((g) => (
                  <TouchableOpacity
                    key={g}
                    onPress={() => set({ gender: g })}
                    style={[styles.genderBtn, gender === g && styles.genderBtnActive]}
                    testID={`gender-${g}`}
                  >
                    <Body style={[styles.genderText, gender === g && { color: colors.bgPrimary }]}>
                      {g === 'erkek' ? '♂  Erkek' : '♀  Kadın'}
                    </Body>
                  </TouchableOpacity>
                ))}
              </View>

              {error ? (
                <View style={styles.errorBox} testID="validation-error">
                  <Body style={{ color: colors.errorVow }}>⚠ {error}</Body>
                </View>
              ) : null}
            </View>
          </KeyboardScroll>

          <View style={styles.footer}>
            <Button title="Devam Et" onPress={onNext} testID="next-btn" />
          </View>
        </Screen>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  genderBtn: {
    flex: 1,
    paddingVertical: 16,
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: colors.borderSubtle,
    alignItems: 'center',
    backgroundColor: colors.bgCard,
  },
  genderBtnActive: { backgroundColor: colors.textPrimary, borderColor: colors.textPrimary },
  genderText: { fontFamily: fonts.bodyMedium },
  errorBox: {
    marginTop: spacing.md,
    padding: spacing.md,
    borderRadius: radius.md,
    backgroundColor: '#F8E1DE',
    borderWidth: 1,
    borderColor: colors.errorVow,
  },
  footer: { paddingBottom: spacing.md, paddingTop: spacing.sm },
});
