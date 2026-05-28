import React, { useState } from 'react';
import { View, StyleSheet, KeyboardAvoidingView, Platform, TouchableOpacity, Modal } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { Body, Button, Caption, Card, Chip, H2, H3, Input, KeyboardScroll, Label, ProgressBar, Screen } from '@/src/ui';
import { useOnboarding } from '@/src/store';
import { colors, fonts, radius, spacing } from '@/src/theme';
import type { Ancestor } from '@/src/api';

const RELATIONS = [
  { id: 'anne', label: 'Anne', side: 'maternal' as const },
  { id: 'anneanne', label: 'Anneanne', side: 'maternal' as const },
  { id: 'dede_anne', label: 'Anne tarafı dede', side: 'maternal' as const },
  { id: 'baba', label: 'Baba', side: 'paternal' as const },
  { id: 'babaanne', label: 'Babaanne', side: 'paternal' as const },
  { id: 'dede_baba', label: 'Baba tarafı dede', side: 'paternal' as const },
  { id: 'diger_anne', label: 'Diğer (Anne soyu)', side: 'maternal' as const },
  { id: 'diger_baba', label: 'Diğer (Baba soyu)', side: 'paternal' as const },
];

export default function FamilyStage() {
  const router = useRouter();
  const { ancestors, set } = useOnboarding();
  const [modal, setModal] = useState(false);
  const [editing, setEditing] = useState<Ancestor | null>(null);

  const openAdd = (relation: string, side: 'maternal' | 'paternal') => {
    setEditing({
      relation,
      side,
      name: '',
      diseases: [],
      events: [],
      unfulfilled_vows: [],
      sins_admitted: [],
      is_alive: true,
    });
    setModal(true);
  };

  const saveAncestor = () => {
    if (!editing) return;
    set({ ancestors: [...ancestors, editing] });
    setEditing(null);
    setModal(false);
  };

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined} style={{ flex: 1 }}>
        <Screen>
          <View style={{ paddingTop: spacing.md }}>
            <Caption style={{ color: colors.accentSage }}>3. AŞAMA / 4</Caption>
            <View style={{ marginTop: spacing.xs, marginBottom: spacing.lg }}>
              <ProgressBar step={3} total={4} />
            </View>
            <H2>Aile & Soy Ağacı</H2>
            <Body style={{ color: colors.textSecondary, marginTop: spacing.xs }}>
              Anne, baba ve ataların hastalıkları, yaşadıkları olaylar ve bilinen günahları.
            </Body>
          </View>

          <KeyboardScroll>
            <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm, color: colors.maternalPrimary }}>ANNE SOYU</Label>
            <View style={styles.chipWrap}>
              {RELATIONS.filter((r) => r.side === 'maternal').map((r) => (
                <TouchableOpacity key={r.id} onPress={() => openAdd(r.label, r.side)} testID={`add-rel-${r.id}`}>
                  <View style={[styles.relChip, { backgroundColor: colors.maternalLight, borderColor: colors.maternalPrimary }]}>
                    <Body style={{ color: colors.maternalPrimary, fontFamily: fonts.bodyMedium, fontSize: 13 }}>+ {r.label}</Body>
                  </View>
                </TouchableOpacity>
              ))}
            </View>

            <Label style={{ marginTop: spacing.md, marginBottom: spacing.sm, color: colors.paternalPrimary }}>BABA SOYU</Label>
            <View style={styles.chipWrap}>
              {RELATIONS.filter((r) => r.side === 'paternal').map((r) => (
                <TouchableOpacity key={r.id} onPress={() => openAdd(r.label, r.side)} testID={`add-rel-${r.id}`}>
                  <View style={[styles.relChip, { backgroundColor: colors.paternalLight, borderColor: colors.paternalPrimary }]}>
                    <Body style={{ color: colors.paternalPrimary, fontFamily: fonts.bodyMedium, fontSize: 13 }}>+ {r.label}</Body>
                  </View>
                </TouchableOpacity>
              ))}
            </View>

            <Label style={{ marginTop: spacing.lg, marginBottom: spacing.sm }}>EKLENEN ATALAR ({ancestors.length})</Label>
            {ancestors.length === 0 ? (
              <Card><Caption style={{ textAlign: 'center' }}>Henüz ata eklenmedi.</Caption></Card>
            ) : (
              ancestors.map((a, i) => (
                <Card key={i} style={[styles.ancestorCard, { borderLeftColor: a.side === 'maternal' ? colors.maternalPrimary : colors.paternalPrimary }]}>
                  <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                    <View style={{ flex: 1 }}>
                      <H3 style={{ fontSize: 18 }}>{a.relation}{a.name ? ` · ${a.name}` : ''}</H3>
                      <Caption style={{ color: a.side === 'maternal' ? colors.maternalPrimary : colors.paternalPrimary }}>
                        {a.side === 'maternal' ? 'Anne soyu' : 'Baba soyu'}
                      </Caption>
                      {(a.diseases?.length || 0) > 0 && <Caption style={{ marginTop: 4 }}>Hastalıklar: {a.diseases?.join(', ')}</Caption>}
                      {(a.events?.length || 0) > 0 && <Caption>Olaylar: {a.events?.join(', ')}</Caption>}
                      {(a.unfulfilled_vows?.length || 0) > 0 && <Caption style={{ color: colors.errorVow }}>Yarım adak: {a.unfulfilled_vows?.join(', ')}</Caption>}
                      {(a.sins_admitted?.length || 0) > 0 && <Caption>Bilinen günahlar: {a.sins_admitted?.join(', ')}</Caption>}
                    </View>
                    <TouchableOpacity onPress={() => set({ ancestors: ancestors.filter((_, x) => x !== i) })} testID={`remove-ancestor-${i}`}>
                      <Body style={{ color: colors.errorVow, fontSize: 20 }}>×</Body>
                    </TouchableOpacity>
                  </View>
                </Card>
              ))
            )}
          </KeyboardScroll>

          <View style={styles.footer}>
            <View style={{ flexDirection: 'row', gap: spacing.sm }}>
              <Button title="Geri" variant="secondary" onPress={() => router.back()} style={{ flex: 1 }} testID="back-btn" />
              <Button title="Devam Et" onPress={() => router.push('/onboarding/spirituality')} style={{ flex: 1 }} testID="next-btn" />
            </View>
          </View>
        </Screen>
      </KeyboardAvoidingView>

      <AncestorEditModal
        visible={modal}
        ancestor={editing}
        onChange={(a) => setEditing(a)}
        onClose={() => { setEditing(null); setModal(false); }}
        onSave={saveAncestor}
      />
    </SafeAreaView>
  );
}

function AncestorEditModal({ visible, ancestor, onChange, onClose, onSave }: {
  visible: boolean;
  ancestor: Ancestor | null;
  onChange: (a: Ancestor) => void;
  onClose: () => void;
  onSave: () => void;
}) {
  const [d, setD] = useState('');
  const [ev, setEv] = useState('');
  const [v, setV] = useState('');
  const [sin, setSin] = useState('');

  if (!ancestor) return null;
  const sideColor = ancestor.side === 'maternal' ? colors.maternalPrimary : colors.paternalPrimary;

  const addTo = (key: 'diseases' | 'events' | 'unfulfilled_vows' | 'sins_admitted', val: string, reset: () => void) => {
    if (!val.trim()) return;
    onChange({ ...ancestor, [key]: [...(ancestor[key] || []), val.trim()] });
    reset();
  };

  return (
    <Modal visible={visible} animationType="slide" transparent onRequestClose={onClose}>
      <View style={styles.modalBackdrop}>
        <View style={styles.modalCard}>
          <SafeAreaView edges={['bottom']}>
            <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
              <KeyboardScroll>
                <View style={{ padding: spacing.lg }}>
                  <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
                    <H3 style={{ color: sideColor }}>{ancestor.relation}</H3>
                    <TouchableOpacity onPress={onClose} testID="modal-close"><Body style={{ fontSize: 24 }}>×</Body></TouchableOpacity>
                  </View>

                  <Input label="İsim (opsiyonel)" value={ancestor.name || ''} onChangeText={(t) => onChange({ ...ancestor, name: t })} placeholder="Örn: Ayşe Nine" testID="ancestor-name" />

                  <Label style={{ marginTop: spacing.sm, marginBottom: spacing.sm }}>HASTALIKLARI</Label>
                  <View style={{ flexDirection: 'row', alignItems: 'flex-end' }}>
                    <Input value={d} onChangeText={setD} placeholder="Örn: Şeker" style={{ flex: 1 }} testID="ancestor-disease-input" />
                    <Button title="+" variant="secondary" onPress={() => addTo('diseases', d, () => setD(''))} style={{ marginLeft: spacing.sm, marginBottom: spacing.md, paddingHorizontal: 16 }} testID="ancestor-add-disease" />
                  </View>
                  <View style={styles.chipWrap}>
                    {ancestor.diseases?.map((it, i) => (
                      <Chip key={i} label={it} side={ancestor.side} onRemove={() => onChange({ ...ancestor, diseases: ancestor.diseases?.filter((_, x) => x !== i) })} />
                    ))}
                  </View>

                  <Label style={{ marginTop: spacing.sm, marginBottom: spacing.sm }}>YAŞADIĞI OLAYLAR</Label>
                  <View style={{ flexDirection: 'row', alignItems: 'flex-end' }}>
                    <Input value={ev} onChangeText={setEv} placeholder="Örn: Eşi vefat etti, miras kavgası" style={{ flex: 1 }} />
                    <Button title="+" variant="secondary" onPress={() => addTo('events', ev, () => setEv(''))} style={{ marginLeft: spacing.sm, marginBottom: spacing.md, paddingHorizontal: 16 }} />
                  </View>
                  <View style={styles.chipWrap}>
                    {ancestor.events?.map((it, i) => (
                      <Chip key={i} label={it} side={ancestor.side} onRemove={() => onChange({ ...ancestor, events: ancestor.events?.filter((_, x) => x !== i) })} />
                    ))}
                  </View>

                  <Label style={{ marginTop: spacing.sm, marginBottom: spacing.sm }}>YARIM KALMIŞ ADAKLAR</Label>
                  <View style={{ flexDirection: 'row', alignItems: 'flex-end' }}>
                    <Input value={v} onChangeText={setV} placeholder="Örn: Kurban adağı, hatim adağı" style={{ flex: 1 }} />
                    <Button title="+" variant="secondary" onPress={() => addTo('unfulfilled_vows', v, () => setV(''))} style={{ marginLeft: spacing.sm, marginBottom: spacing.md, paddingHorizontal: 16 }} />
                  </View>
                  <View style={styles.chipWrap}>
                    {ancestor.unfulfilled_vows?.map((it, i) => (
                      <Chip key={i} label={it} side={ancestor.side} onRemove={() => onChange({ ...ancestor, unfulfilled_vows: ancestor.unfulfilled_vows?.filter((_, x) => x !== i) })} />
                    ))}
                  </View>

                  <Label style={{ marginTop: spacing.sm, marginBottom: spacing.sm }}>BİLİNEN GÜNAHLAR / DURUMLAR</Label>
                  <View style={{ flexDirection: 'row', alignItems: 'flex-end' }}>
                    <Input value={sin} onChangeText={setSin} placeholder="Örn: Faiz alıp verdi, zekat vermedi" style={{ flex: 1 }} />
                    <Button title="+" variant="secondary" onPress={() => addTo('sins_admitted', sin, () => setSin(''))} style={{ marginLeft: spacing.sm, marginBottom: spacing.md, paddingHorizontal: 16 }} />
                  </View>
                  <View style={styles.chipWrap}>
                    {ancestor.sins_admitted?.map((it, i) => (
                      <Chip key={i} label={it} side={ancestor.side} onRemove={() => onChange({ ...ancestor, sins_admitted: ancestor.sins_admitted?.filter((_, x) => x !== i) })} />
                    ))}
                  </View>

                  <Button title="Atayı Ekle" onPress={onSave} testID="save-ancestor" style={{ marginTop: spacing.lg }} />
                </View>
              </KeyboardScroll>
            </KeyboardAvoidingView>
          </SafeAreaView>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
  chipWrap: { flexDirection: 'row', flexWrap: 'wrap' },
  relChip: { paddingHorizontal: 14, paddingVertical: 10, borderRadius: radius.round, borderWidth: 1, marginRight: spacing.sm, marginBottom: spacing.sm },
  ancestorCard: { borderLeftWidth: 4 },
  footer: { paddingBottom: spacing.md, paddingTop: spacing.sm },
  modalBackdrop: { flex: 1, backgroundColor: 'rgba(44,53,49,0.5)', justifyContent: 'flex-end' },
  modalCard: { backgroundColor: colors.bgPrimary, borderTopLeftRadius: 24, borderTopRightRadius: 24, maxHeight: '90%' },
});
