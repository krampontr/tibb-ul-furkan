import React, { useState } from 'react';
import { View, StyleSheet, KeyboardAvoidingView, Platform, ScrollView, TouchableOpacity, Alert } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { Body, Button, Caption, Card, H2, H3, Input, Label, ProgressBar } from '@/src/ui';
import { useFormStore } from '@/src/formStore';
import { formApi } from '@/src/formApi';
import { colors, fonts, radius, spacing } from '@/src/theme';

const YN_KEYS: Array<{ key: keyof ReturnType<typeof useFormStore.getState>; label: string }> = [
  { key: 'adak_yemin', label: 'Geçmişte adak adamış mı? Yemin edip bozmuş mu?' },
  { key: 'muska_okunmus_su', label: 'Muska takmış mı? Okunmuş su içmiş mi?' },
  { key: 'miras_sorunu', label: 'Akrabalar arası miras sorunu var mı?' },
  { key: 'beddua_hak_haram', label: 'Herhangi birine beddua veya hak haram etmiş mi?' },
  { key: 'intihar', label: 'İntihar girişimi oldu mu?' },
  { key: 'anne_baba_ofke', label: 'Anne babaya karşı öfke var mı?' },
  { key: 'es_soguklugu', label: 'Eşine karşı aşırı soğukluk / evlilikte problem var mı?' },
  { key: 'sehvet', label: 'Şehvet yüksekliği var mı?' },
  { key: 'duygusallik', label: 'Duygusallık var mı?' },
  { key: 'kin', label: 'Kin – geçmişi unutamama var mı?' },
  { key: 'kusme_alinganlik', label: 'İnat – küsme – alınganlık var mı?' },
  { key: 'ofke', label: 'Öfke var mı?' },
  { key: 'nefret', label: 'Nefret duygusu var mı?' },
  { key: 'supheci', label: 'Şüphecilik var mı?' },
  { key: 'uyku_sorunu', label: 'Uykusuzluk veya çok uyuma isteği var mı?' },
  { key: 'aniden_parlama', label: 'Aniden parlama var mı?' },
  { key: 'alaycilik', label: 'Alaycılık var mı?' },
];

export default function AnalizForm() {
  const router = useRouter();
  const state = useFormStore();
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    setLoading(true);
    try {
      const submission = await formApi.create({
        ad_soyad: state.ad_soyad,
        yas: state.yas,
        tlf: state.tlf,
        medeni_durum: state.medeni_durum,
        cocuk_sayisi: state.cocuk_sayisi,
        memleket: state.memleket,
        dogum_tarihi: state.dogum_tarihi,
        cinsiyet: state.cinsiyet || undefined,
        anne_durum: state.anne_durum, baba_durum: state.baba_durum,
        anneanne_durum: state.anneanne_durum, anne_babasi_durum: state.anne_babasi_durum,
        babaanne_durum: state.babaanne_durum, baba_babasi_durum: state.baba_babasi_durum,
        zekat_veriyor: state.zekat_veriyor, faizli_kredi: state.faizli_kredi,
        anne_hastalik: state.anne_hastalik, baba_hastalik: state.baba_hastalik,
        cocuk_hastalik: state.cocuk_hastalik,
        rahatsizliklar: state.rahatsizliklar,
        adak_yemin: state.adak_yemin, muska_okunmus_su: state.muska_okunmus_su,
        miras_sorunu: state.miras_sorunu, beddua_hak_haram: state.beddua_hak_haram,
        intihar: state.intihar, anne_baba_ofke: state.anne_baba_ofke,
        es_soguklugu: state.es_soguklugu, sehvet: state.sehvet,
        duygusallik: state.duygusallik, kin: state.kin,
        kusme_alinganlik: state.kusme_alinganlik, ofke: state.ofke,
        nefret: state.nefret, supheci: state.supheci,
        uyku_sorunu: state.uyku_sorunu, aniden_parlama: state.aniden_parlama,
        alaycilik: state.alaycilik,
      });
      router.replace(`/analiz/sonuc/${submission.id}`);
    } catch (e: any) {
      Alert.alert('Hata', e.message || 'Form gönderilemedi');
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined} style={{ flex: 1 }}>
        <View style={styles.body}>
          <Caption style={{ color: colors.accentSage }}>2. AŞAMA / 2</Caption>
          <View style={{ marginTop: spacing.xs, marginBottom: spacing.lg }}><ProgressBar step={2} total={2} /></View>
          <H2>Tespit Formu</H2>
          <Body style={{ color: colors.textSecondary, marginTop: 4 }}>Aile büyükleri, mali durum, hastalıklar ve manevi sorular.</Body>

          <ScrollView contentContainerStyle={{ paddingBottom: spacing.xxl }} keyboardShouldPersistTaps="handled" showsVerticalScrollIndicator>
            <Card>
              <H3 style={{ fontSize: 16 }}>Aile Büyükleri</H3>
              <Caption style={{ marginBottom: spacing.sm }}>Sağ mı / vefat mı? Notlarınızı yazın.</Caption>
              <Input label="ANNE" value={state.anne_durum} onChangeText={(t) => state.set({ anne_durum: t })} placeholder="Örn: Sağ, 60 yaşında" />
              <Input label="BABA" value={state.baba_durum} onChangeText={(t) => state.set({ baba_durum: t })} placeholder="Örn: Vefat etti, 2015" />
              <Input label="ANNEANNE" value={state.anneanne_durum} onChangeText={(t) => state.set({ anneanne_durum: t })} placeholder="Sağ / Vefat" />
              <Input label="ANNENİN BABASI" value={state.anne_babasi_durum} onChangeText={(t) => state.set({ anne_babasi_durum: t })} placeholder="Sağ / Vefat" />
              <Input label="BABAANNE" value={state.babaanne_durum} onChangeText={(t) => state.set({ babaanne_durum: t })} placeholder="Sağ / Vefat" />
              <Input label="BABANIN BABASI" value={state.baba_babasi_durum} onChangeText={(t) => state.set({ baba_babasi_durum: t })} placeholder="Sağ / Vefat" />
            </Card>

            <Card>
              <H3 style={{ fontSize: 16 }}>Mali Durum</H3>
              <Input label="ZEKAT VERİYOR MU?" value={state.zekat_veriyor} onChangeText={(t) => state.set({ zekat_veriyor: t })} placeholder="Evet / Hayır / Bilmiyorum" />
              <Input label="FAİZLİ KREDİ ÇEKTİ Mİ?" value={state.faizli_kredi} onChangeText={(t) => state.set({ faizli_kredi: t })} placeholder="Evet / Hayır + açıklama" />
            </Card>

            <Card>
              <H3 style={{ fontSize: 16 }}>Ailedeki Hastalıklar</H3>
              <Input label="ANNEDE HASTALIK VAR MI?" value={state.anne_hastalik} onChangeText={(t) => state.set({ anne_hastalik: t })} placeholder="Örn: Şeker, tansiyon, yok" multiline />
              <Input label="BABADA HASTALIK VAR MI?" value={state.baba_hastalik} onChangeText={(t) => state.set({ baba_hastalik: t })} placeholder="Örn: Kalp, astım, yok" multiline />
              <Input label="ÇOCUKLARDA HASTALIK VAR MI?" value={state.cocuk_hastalik} onChangeText={(t) => state.set({ cocuk_hastalik: t })} placeholder="Örn: Yok / hangi çocukta ne" multiline />
            </Card>

            <Card>
              <H3 style={{ fontSize: 16 }}>Yaşanılan Ruhsal ve Fiziksel Rahatsızlıklar</H3>
              <Caption style={{ marginBottom: spacing.sm }}>Mevcut hastalıklar, semptomlar, korkular, geçmiş travmalar — serbest yazın.</Caption>
              <Input value={state.rahatsizliklar} onChangeText={(t) => state.set({ rahatsizliklar: t })} placeholder="Örn: Sürekli migren, panik atak, baş ağrısı, eşle iletişim problemi…" multiline style={{ minHeight: 100, textAlignVertical: 'top' }} />
            </Card>

            <Card>
              <H3 style={{ fontSize: 16 }}>Sorular</H3>
              <Caption style={{ marginBottom: spacing.sm }}>Her soruyu cevaplayın: var ise "Evet" + açıklama, yok ise "Yok".</Caption>
              {YN_KEYS.map((q) => (
                <View key={q.key as string} style={{ marginBottom: spacing.sm }}>
                  <Caption style={styles.qLabel}>{q.label}</Caption>
                  <View style={{ flexDirection: 'row', gap: spacing.xs, marginBottom: 4 }}>
                    <YnPill active={isYes(state[q.key] as string)} label="Evet" onPress={() => state.set({ [q.key]: 'Evet' } as any)} />
                    <YnPill active={isNo(state[q.key] as string)} label="Yok" onPress={() => state.set({ [q.key]: 'Yok' } as any)} />
                  </View>
                  <Input value={state[q.key] as string} onChangeText={(t) => state.set({ [q.key]: t } as any)} placeholder="Açıklama (opsiyonel)" />
                </View>
              ))}
            </Card>
          </ScrollView>

          <View style={styles.footer}>
            <View style={{ flexDirection: 'row', gap: spacing.sm }}>
              <Button title="Geri" variant="secondary" onPress={() => router.back()} style={{ flex: 1 }} testID="back-btn" />
              <Button title={loading ? 'Gönderiliyor…' : 'Analizi Başlat'} onPress={submit} disabled={loading} style={{ flex: 1.4 }} testID="submit-btn" />
            </View>
          </View>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

function isYes(v?: string) { return !!v && v.trim().toLowerCase().startsWith('evet'); }
function isNo(v?: string) { return !!v && ['yok', 'hayır', 'hayir'].includes(v.trim().toLowerCase()); }

function YnPill({ active, label, onPress }: { active: boolean; label: string; onPress: () => void }) {
  return (
    <TouchableOpacity onPress={onPress} style={[styles.pill, active && styles.pillActive]}>
      <Caption style={[{ color: colors.textPrimary, fontFamily: fonts.bodyMedium }, active && { color: colors.bgPrimary }]}>{label}</Caption>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  body: { flex: 1, paddingHorizontal: spacing.lg, paddingTop: spacing.md },
  qLabel: { fontFamily: fonts.bodyMedium, color: colors.textPrimary, fontSize: 13, marginBottom: 4 },
  pill: { paddingHorizontal: 14, paddingVertical: 6, borderRadius: radius.round, borderWidth: 1, borderColor: colors.borderSubtle, backgroundColor: colors.bgCard },
  pillActive: { backgroundColor: colors.textPrimary, borderColor: colors.textPrimary },
  footer: { paddingBottom: spacing.md, paddingTop: spacing.sm },
});
