import React, { useCallback, useEffect, useState } from 'react';
import { View, StyleSheet, TouchableOpacity, Alert, KeyboardAvoidingView, Platform, ScrollView, Modal } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { Body, Button, Caption, Card, H2, H3, Input, Label } from '@/src/ui';
import { colors, fonts, radius, spacing } from '@/src/theme';
import { storage } from '@/src/utils/storage';

const STORAGE_KEY = 'kefaret_list_v1';

type KefaretType = {
  key: string;
  label: string;
  icon: string;
  unit: string;
  needsAmount: boolean;
};

const TYPES: KefaretType[] = [
  { key: 'istigfar', label: 'İstiğfar', icon: '☾', unit: 'kez', needsAmount: true },
  { key: 'fakir_doyurma', label: 'Fakir Doyurma', icon: '✦', unit: 'kişi', needsAmount: true },
  { key: 'hayvan_besleme', label: 'Hayvan Besleme', icon: '✦', unit: 'kez/kg', needsAmount: true },
  { key: 'pekmez_dagitma', label: 'Pekmez Dağıtma', icon: '✦', unit: 'kg', needsAmount: true },
  { key: 'zekat_kefareti', label: 'Zekât Kefareti', icon: '✦', unit: 'TL', needsAmount: true },
  { key: 'kuran_hatim', label: 'Kur\'an / Hatim', icon: '✦', unit: 'kez', needsAmount: true },
  { key: 'oruc', label: 'Oruç', icon: '✦', unit: 'gün', needsAmount: true },
  { key: 'sadaka', label: 'Sadaka', icon: '✦', unit: 'TL', needsAmount: true },
  { key: 'ziyaret', label: 'Mübarek Yer Ziyareti', icon: '✦', unit: 'kez', needsAmount: false },
  { key: 'helallesme', label: 'Helalleşme', icon: '✦', unit: 'kişi', needsAmount: false },
  { key: 'diger', label: 'Diğer (Serbest)', icon: '+', unit: '', needsAmount: false },
];

type KefaretItem = {
  id: string;
  name: string; // kullanıcının yazdığı başlık ("İstiğfar" gibi)
  type_key: string;
  amount?: number;
  unit?: string;
  note?: string;
  created_at: string;
};

const uuid = () => Math.random().toString(36).slice(2) + Date.now().toString(36);

export default function Kefaret() {
  const router = useRouter();
  const [items, setItems] = useState<KefaretItem[]>([]);
  const [loaded, setLoaded] = useState(false);
  const [editor, setEditor] = useState<{ open: boolean; draft: KefaretItem | null }>({ open: false, draft: null });

  useEffect(() => {
    (async () => {
      const s = await storage.getItem<string>(STORAGE_KEY, '');
      if (s) {
        try {
          const parsed = typeof s === 'string' ? JSON.parse(s) : (s as any);
          if (Array.isArray(parsed)) setItems(parsed);
        } catch {}
      }
      setLoaded(true);
    })();
  }, []);

  useEffect(() => {
    if (!loaded) return;
    storage.setItem(STORAGE_KEY, JSON.stringify(items));
  }, [items, loaded]);

  const openNew = (t: KefaretType) => {
    setEditor({
      open: true,
      draft: {
        id: uuid(),
        name: t.label,
        type_key: t.key,
        amount: t.needsAmount ? 0 : undefined,
        unit: t.unit,
        note: '',
        created_at: new Date().toISOString(),
      },
    });
  };

  const openEdit = (it: KefaretItem) => setEditor({ open: true, draft: { ...it } });

  const save = (draft: KefaretItem) => {
    setItems((prev) => {
      const idx = prev.findIndex((p) => p.id === draft.id);
      if (idx >= 0) {
        const next = [...prev]; next[idx] = draft; return next;
      }
      return [draft, ...prev];
    });
    setEditor({ open: false, draft: null });
  };

  const remove = (id: string) => {
    Alert.alert('Kefareti sil', 'Bu kayıt silinecek. Emin misiniz?', [
      { text: 'Vazgeç', style: 'cancel' },
      { text: 'Sil', style: 'destructive', onPress: () => setItems((prev) => prev.filter((p) => p.id !== id)) },
    ]);
  };

  // Toplam istatistikler
  const totalCount = items.length;
  const totalAmount = items.reduce((s, i) => s + (i.amount || 0), 0);

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} testID="back-btn">
          <Body style={{ color: colors.accentSage }}>‹ Geri</Body>
        </TouchableOpacity>
        <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>KEFARETLERİM</Caption>
        <View style={{ width: 60 }} />
      </View>

      <ScrollView contentContainerStyle={{ paddingHorizontal: spacing.lg, paddingBottom: spacing.xxl }}>
        <H2>Çabalamalarım</H2>
        <Caption style={{ color: colors.textSecondary, marginTop: 4, fontStyle: 'italic' }}>
          Yerine getirdiğiniz kefaretler, sadakalar ve manevi çabaları kaydedin.
        </Caption>

        <Card style={{ marginTop: spacing.md, backgroundColor: colors.bgSecondary, borderColor: colors.accentSage }}>
          <View style={{ flexDirection: 'row', justifyContent: 'space-around' }}>
            <View style={{ alignItems: 'center' }}>
              <H3 style={{ fontSize: 28, color: colors.textPrimary }}>{totalCount}</H3>
              <Caption>Toplam Kayıt</Caption>
            </View>
            <View style={{ width: 1, backgroundColor: colors.borderSubtle }} />
            <View style={{ alignItems: 'center' }}>
              <H3 style={{ fontSize: 28, color: colors.textPrimary }}>{totalAmount.toLocaleString('tr-TR')}</H3>
              <Caption>Toplam Adet/Miktar</Caption>
            </View>
          </View>
        </Card>

        <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>YENİ KEFARET EKLE</Label>
        <View style={styles.typesWrap}>
          {TYPES.map((t) => (
            <TouchableOpacity key={t.key} onPress={() => openNew(t)} testID={`type-${t.key}`}>
              <View style={styles.typeCard}>
                <Body style={{ fontSize: 18, color: colors.accentSage }}>{t.icon}</Body>
                <Caption style={{ marginTop: 4, fontFamily: fonts.bodyMedium, color: colors.textPrimary, textAlign: 'center' }}>
                  {t.label}
                </Caption>
              </View>
            </TouchableOpacity>
          ))}
        </View>

        <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>KAYITLARIM ({items.length})</Label>
        {items.length === 0 ? (
          <Card>
            <Caption style={{ textAlign: 'center', color: colors.textSecondary }}>
              Henüz kayıt yok. Yukarıdan bir kefaret türü seçin.
            </Caption>
          </Card>
        ) : (
          items.map((it) => (
            <TouchableOpacity key={it.id} onPress={() => openEdit(it)} testID={`item-${it.id}`}>
              <Card style={{ flexDirection: 'row', alignItems: 'center' }}>
                <View style={styles.itemDot}>
                  <Body style={{ color: colors.accentSage, fontSize: 16 }}>✦</Body>
                </View>
                <View style={{ flex: 1, marginLeft: spacing.md }}>
                  <H3 style={{ fontSize: 16 }}>{it.name}</H3>
                  <Caption>
                    {it.amount ? `${it.amount.toLocaleString('tr-TR')} ${it.unit || ''}` : 'Adet belirtilmedi'}
                    {it.note ? ` · ${it.note}` : ''}
                  </Caption>
                  <Caption style={{ color: colors.accentSage, fontSize: 10, marginTop: 2 }}>
                    {new Date(it.created_at).toLocaleDateString('tr-TR')}
                  </Caption>
                </View>
                <TouchableOpacity onPress={() => remove(it.id)} hitSlop={10} testID={`remove-${it.id}`}>
                  <Body style={{ color: colors.errorVow, fontSize: 20, paddingHorizontal: 6 }}>×</Body>
                </TouchableOpacity>
              </Card>
            </TouchableOpacity>
          ))
        )}
      </ScrollView>

      <KefaretEditor
        state={editor}
        onClose={() => setEditor({ open: false, draft: null })}
        onSave={save}
      />
    </SafeAreaView>
  );
}

function KefaretEditor({ state, onClose, onSave }: { state: { open: boolean; draft: KefaretItem | null }; onClose: () => void; onSave: (i: KefaretItem) => void }) {
  const [draft, setDraft] = useState<KefaretItem | null>(state.draft);
  useEffect(() => { setDraft(state.draft); }, [state.draft]);

  if (!state.open || !draft) return null;
  const typeMeta = TYPES.find((t) => t.key === draft.type_key);

  return (
    <Modal visible={state.open} animationType="slide" transparent onRequestClose={onClose}>
      <View style={styles.backdrop}>
        <View style={styles.sheet}>
          <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined} style={{ flex: 1 }}>
            <View style={styles.sheetHeader}>
              <View style={{ flex: 1 }}>
                <H3>{draft.name || 'Yeni Kefaret'}</H3>
                <Caption>{typeMeta?.label || ''}</Caption>
              </View>
              <TouchableOpacity onPress={onClose} hitSlop={10} testID="editor-close">
                <Body style={{ fontSize: 28, color: colors.textSecondary }}>×</Body>
              </TouchableOpacity>
            </View>

            <ScrollView
              style={{ flex: 1 }}
              contentContainerStyle={{ padding: spacing.lg, paddingBottom: spacing.xxl }}
              keyboardShouldPersistTaps="handled"
              showsVerticalScrollIndicator
            >
              <Input
                label="BAŞLIK"
                value={draft.name}
                onChangeText={(t) => setDraft({ ...draft, name: t })}
                placeholder="Örn: İstiğfar, Helva dağıtma"
                testID="editor-name"
              />

              <Input
                label={`MİKTAR / ADET ${draft.unit ? `(${draft.unit})` : ''}`}
                value={draft.amount?.toString() || ''}
                onChangeText={(t) => setDraft({ ...draft, amount: parseInt(t.replace(/\D/g, '')) || 0 })}
                keyboardType="number-pad"
                placeholder="Örn: 100"
                testID="editor-amount"
              />

              <Input
                label="BİRİM (OPSİYONEL)"
                value={draft.unit || ''}
                onChangeText={(t) => setDraft({ ...draft, unit: t })}
                placeholder="kez, kişi, kg, TL, gün vb."
                testID="editor-unit"
              />

              <Input
                label="NOT (OPSİYONEL)"
                value={draft.note || ''}
                onChangeText={(t) => setDraft({ ...draft, note: t })}
                placeholder="Açıklama, kim için, hangi niyetle vb."
                multiline
                testID="editor-note"
              />
            </ScrollView>

            <SafeAreaView edges={['bottom']} style={styles.sheetFooter}>
              <View style={{ flexDirection: 'row', gap: spacing.sm, paddingHorizontal: spacing.lg, paddingTop: spacing.sm }}>
                <Button title="İptal" variant="secondary" onPress={onClose} style={{ flex: 1 }} />
                <Button title="✓ Kaydet" onPress={() => onSave(draft)} style={{ flex: 1.4 }} testID="editor-save" />
              </View>
            </SafeAreaView>
          </KeyboardAvoidingView>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingHorizontal: spacing.lg, paddingVertical: spacing.sm },
  typesWrap: { flexDirection: 'row', flexWrap: 'wrap', marginHorizontal: -4 },
  typeCard: {
    width: 100,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.sm,
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: colors.borderSubtle,
    backgroundColor: colors.bgCard,
    margin: 4,
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: 84,
  },
  itemDot: {
    width: 36, height: 36, borderRadius: 18,
    backgroundColor: colors.bgSecondary,
    borderWidth: 1, borderColor: colors.accentSage,
    alignItems: 'center', justifyContent: 'center',
  },
  backdrop: { flex: 1, backgroundColor: 'rgba(44,53,49,0.5)', justifyContent: 'flex-end' },
  sheet: { backgroundColor: colors.bgPrimary, borderTopLeftRadius: 24, borderTopRightRadius: 24, height: '85%' },
  sheetHeader: {
    flexDirection: 'row', alignItems: 'center',
    paddingHorizontal: spacing.lg, paddingVertical: spacing.md,
    borderBottomWidth: 1, borderBottomColor: colors.borderSubtle,
  },
  sheetFooter: {
    borderTopWidth: 1, borderTopColor: colors.borderSubtle,
    backgroundColor: colors.bgPrimary,
    paddingBottom: spacing.sm,
  },
});
