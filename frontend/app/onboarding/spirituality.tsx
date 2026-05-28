import React, { useState } from 'react';
import { View, StyleSheet, KeyboardAvoidingView, Platform, TouchableOpacity, Alert } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { Body, Button, Caption, Card, Chip, H2, H3, Input, KeyboardScroll, Label, ProgressBar, Screen } from '@/src/ui';
import { useOnboarding } from '@/src/store';
import { api } from '@/src/api';
import { colors, fonts, radius, spacing } from '@/src/theme';

const ANIMAL_TYPES = ['Koyun', 'Koç', 'Keçi', 'İnek', 'Boğa', 'Tavuk', 'Horoz', 'Kuzu'];
const ACTION_TYPES = ['Oruç', 'Namaz', "Kur'an Okuma", 'Hatim', 'Yasin', 'Şifa Okuması', 'Ziyaret', 'Hac', 'Umre'];
const ISSUE_TYPES = ['Açıkta kaldı', 'Çalındı', 'Usulsüz kesildi', 'Başkası tarafından yendi'];

export default function SpiritualityStage() {
  const router = useRouter();
  const state = useOnboarding();
  const { has_animals, animals_kept, animal_vows, action_vows, set, toCreatePayload } = state;
  const [animal, setAnimal] = useState('');
  const [vowAnimal, setVowAnimal] = useState('');
  const [vowQty, setVowQty] = useState('1');
  const [vowFulfilled, setVowFulfilled] = useState(false);
  const [vowIssue, setVowIssue] = useState('');
  const [actionType, setActionType] = useState('');
  const [actionDesc, setActionDesc] = useState('');
  const [actionFulfilled, setActionFulfilled] = useState(false);
  const [loading, setLoading] = useState(false);

  const addAnimal = () => { if (animal.trim()) { set({ animals_kept: [...animals_kept, animal.trim()] }); setAnimal(''); } };
  const addAnimalVow = () => {
    if (!vowAnimal.trim()) return;
    set({ animal_vows: [...animal_vows, { animal: vowAnimal.trim(), quantity: parseInt(vowQty) || 1, fulfilled: vowFulfilled, issue: vowIssue || undefined }] });
    setVowAnimal(''); setVowQty('1'); setVowFulfilled(false); setVowIssue('');
  };
  const addActionVow = () => {
    if (!actionType.trim()) return;
    set({ action_vows: [...action_vows, { action_type: actionType.trim(), description: actionDesc || undefined, fulfilled: actionFulfilled }] });
    setActionType(''); setActionDesc(''); setActionFulfilled(false);
  };

  const submit = async () => {
    if (!state.first_name) {
      Alert.alert('Eksik bilgi', 'Lütfen önce 1. aşamadan başlayın.');
      return;
    }
    setLoading(true);
    try {
      const payload = toCreatePayload();
      const profile = await api.createProfile(payload);
      router.replace(`/profile/${profile.id}`);
    } catch (e: any) {
      Alert.alert('Hata', e.message || 'Profil oluşturulamadı.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined} style={{ flex: 1 }}>
        <Screen>
          <View style={{ paddingTop: spacing.md }}>
            <Caption style={{ color: colors.accentSage }}>4. AŞAMA / 4</Caption>
            <View style={{ marginTop: spacing.xs, marginBottom: spacing.lg }}>
              <ProgressBar step={4} total={4} />
            </View>
            <H2>Maneviyat, Adak & Hayvanlar</H2>
            <Body style={{ color: colors.textSecondary, marginTop: spacing.xs }}>
              Beslenen hayvanlar, hayvan adakları ve eylemsel adaklar.
            </Body>
          </View>

          <KeyboardScroll>
            <Card>
              <H3 style={{ fontSize: 18 }}>Beslenen Hayvanlar</H3>
              <Caption style={{ marginTop: 4 }}>Evde veya çiftlikte beslenen, bağı olan hayvanlar var mı?</Caption>
              <View style={{ flexDirection: 'row', gap: spacing.sm, marginTop: spacing.md }}>
                {([true, false] as const).map((v) => (
                  <TouchableOpacity key={`${v}`} onPress={() => set({ has_animals: v })} style={[styles.toggleBtn, has_animals === v && styles.toggleActive]} testID={`has-animals-${v ? 'yes' : 'no'}`}>
                    <Body style={[styles.toggleText, has_animals === v && { color: colors.bgPrimary }]}>{v ? 'Evet' : 'Hayır'}</Body>
                  </TouchableOpacity>
                ))}
              </View>
              {has_animals && (
                <>
                  <View style={{ flexDirection: 'row', alignItems: 'flex-end', marginTop: spacing.md }}>
                    <Input value={animal} onChangeText={setAnimal} placeholder="Örn: 2 tavuk, 1 kedi, 5 koyun" style={{ flex: 1 }} testID="input-animal" />
                    <Button title="+ Ekle" variant="secondary" onPress={addAnimal} testID="add-animal" style={{ marginLeft: spacing.sm, marginBottom: spacing.md }} />
                  </View>
                  <View style={styles.chipWrap}>
                    {animals_kept.map((a, i) => (
                      <Chip key={i} label={a} side="self" onRemove={() => set({ animals_kept: animals_kept.filter((_, x) => x !== i) })} />
                    ))}
                  </View>
                </>
              )}
            </Card>

            <Card>
              <H3 style={{ fontSize: 18 }}>Adak Hayvanları (Kurban)</H3>
              <Caption style={{ marginTop: 4 }}>Adanmış hayvan adaklarınız var mı? Yerine getirildi mi?</Caption>

              <Label style={{ marginTop: spacing.md, marginBottom: spacing.sm }}>HAYVAN TÜRÜ</Label>
              <View style={styles.chipWrap}>
                {ANIMAL_TYPES.map((a) => (
                  <TouchableOpacity key={a} onPress={() => setVowAnimal(a)} testID={`vow-animal-${a}`}>
                    <View style={[styles.optionChip, vowAnimal === a && styles.optionChipActive]}>
                      <Caption style={[{ color: colors.textPrimary }, vowAnimal === a && { color: colors.bgPrimary }]}>{a}</Caption>
                    </View>
                  </TouchableOpacity>
                ))}
              </View>

              <View style={{ flexDirection: 'row', gap: spacing.sm }}>
                <View style={{ flex: 1 }}>
                  <Input label="ADET" value={vowQty} onChangeText={setVowQty} keyboardType="number-pad" testID="input-vow-qty" />
                </View>
              </View>

              <Label style={{ marginTop: spacing.sm, marginBottom: spacing.sm }}>DURUM</Label>
              <View style={{ flexDirection: 'row', gap: spacing.sm }}>
                <TouchableOpacity onPress={() => setVowFulfilled(true)} style={[styles.toggleBtn, vowFulfilled && styles.toggleActive]} testID="vow-fulfilled">
                  <Caption style={[{ color: colors.textPrimary }, vowFulfilled && { color: colors.bgPrimary }]}>Yerine getirildi</Caption>
                </TouchableOpacity>
                <TouchableOpacity onPress={() => setVowFulfilled(false)} style={[styles.toggleBtn, !vowFulfilled && styles.toggleActive]} testID="vow-pending">
                  <Caption style={[{ color: colors.textPrimary }, !vowFulfilled && { color: colors.bgPrimary }]}>Yarım/açıkta</Caption>
                </TouchableOpacity>
              </View>

              {!vowFulfilled && (
                <>
                  <Label style={{ marginTop: spacing.sm, marginBottom: spacing.sm }}>SORUN (varsa)</Label>
                  <View style={styles.chipWrap}>
                    {ISSUE_TYPES.map((iss) => (
                      <TouchableOpacity key={iss} onPress={() => setVowIssue(iss)}>
                        <View style={[styles.optionChip, vowIssue === iss && styles.optionChipActive]}>
                          <Caption style={[{ color: colors.textPrimary }, vowIssue === iss && { color: colors.bgPrimary }]}>{iss}</Caption>
                        </View>
                      </TouchableOpacity>
                    ))}
                  </View>
                </>
              )}

              <Button title="+ Adak Ekle" variant="secondary" onPress={addAnimalVow} testID="add-animal-vow" style={{ marginTop: spacing.sm }} />

              <View style={[styles.chipWrap, { marginTop: spacing.md }]}>
                {animal_vows.map((v, i) => (
                  <Chip
                    key={i}
                    label={`${v.animal} x${v.quantity || 1} ${v.fulfilled ? '✓' : '⌛'}${v.issue ? ` (${v.issue})` : ''}`}
                    side="self"
                    onRemove={() => set({ animal_vows: animal_vows.filter((_, x) => x !== i) })}
                    testID={`chip-vow-${i}`}
                  />
                ))}
              </View>
            </Card>

            <Card>
              <H3 style={{ fontSize: 18 }}>Eylemsel Adaklar</H3>
              <Caption style={{ marginTop: 4 }}>{`Oruç, namaz, Kur'an okuma, ziyaret, hac/umre gibi adak edilmiş eylemler.`}</Caption>

              <Label style={{ marginTop: spacing.md, marginBottom: spacing.sm }}>EYLEM</Label>
              <View style={styles.chipWrap}>
                {ACTION_TYPES.map((a) => (
                  <TouchableOpacity key={a} onPress={() => setActionType(a)} testID={`action-type-${a}`}>
                    <View style={[styles.optionChip, actionType === a && styles.optionChipActive]}>
                      <Caption style={[{ color: colors.textPrimary }, actionType === a && { color: colors.bgPrimary }]}>{a}</Caption>
                    </View>
                  </TouchableOpacity>
                ))}
              </View>

              <Input label="AÇIKLAMA (OPSİYONEL)" value={actionDesc} onChangeText={setActionDesc} placeholder="Örn: 3 hatim adağı, 7 gün oruç" testID="input-action-desc" />

              <Label style={{ marginBottom: spacing.sm }}>DURUM</Label>
              <View style={{ flexDirection: 'row', gap: spacing.sm }}>
                <TouchableOpacity onPress={() => setActionFulfilled(true)} style={[styles.toggleBtn, actionFulfilled && styles.toggleActive]} testID="action-fulfilled">
                  <Caption style={[{ color: colors.textPrimary }, actionFulfilled && { color: colors.bgPrimary }]}>Yerine getirildi</Caption>
                </TouchableOpacity>
                <TouchableOpacity onPress={() => setActionFulfilled(false)} style={[styles.toggleBtn, !actionFulfilled && styles.toggleActive]} testID="action-pending">
                  <Caption style={[{ color: colors.textPrimary }, !actionFulfilled && { color: colors.bgPrimary }]}>Yerine getirilmedi</Caption>
                </TouchableOpacity>
              </View>

              <Button title="+ Eylem Adağı Ekle" variant="secondary" onPress={addActionVow} testID="add-action-vow" style={{ marginTop: spacing.md }} />

              <View style={[styles.chipWrap, { marginTop: spacing.md }]}>
                {action_vows.map((v, i) => (
                  <Chip
                    key={i}
                    label={`${v.action_type} ${v.fulfilled ? '✓' : '⌛'}${v.description ? ` · ${v.description}` : ''}`}
                    side="self"
                    onRemove={() => set({ action_vows: action_vows.filter((_, x) => x !== i) })}
                    testID={`chip-action-vow-${i}`}
                  />
                ))}
              </View>
            </Card>
          </KeyboardScroll>

          <View style={styles.footer}>
            <View style={{ flexDirection: 'row', gap: spacing.sm }}>
              <Button title="Geri" variant="secondary" onPress={() => router.back()} style={{ flex: 1 }} testID="back-btn" />
              <Button title={loading ? 'Analiz Ediliyor…' : 'Analizi Tamamla'} onPress={submit} disabled={loading} style={{ flex: 1.4 }} testID="submit-btn" />
            </View>
          </View>
        </Screen>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  chipWrap: { flexDirection: 'row', flexWrap: 'wrap' },
  toggleBtn: {
    flex: 1,
    paddingVertical: 12,
    paddingHorizontal: spacing.md,
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: colors.borderSubtle,
    alignItems: 'center',
    backgroundColor: colors.bgCard,
  },
  toggleActive: { backgroundColor: colors.textPrimary, borderColor: colors.textPrimary },
  toggleText: { fontFamily: fonts.bodyMedium },
  optionChip: {
    paddingHorizontal: 12, paddingVertical: 7, borderRadius: radius.round, borderWidth: 1,
    borderColor: colors.borderSubtle, marginRight: spacing.sm, marginBottom: spacing.sm,
    backgroundColor: colors.bgCard,
  },
  optionChipActive: { backgroundColor: colors.textPrimary, borderColor: colors.textPrimary },
  footer: { paddingBottom: spacing.md, paddingTop: spacing.sm },
});
