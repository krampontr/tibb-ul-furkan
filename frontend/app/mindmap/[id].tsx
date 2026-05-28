import React, { useCallback, useMemo, useState } from 'react';
import { View, StyleSheet, TouchableOpacity, Modal, ScrollView, useWindowDimensions } from 'react-native';
import Svg, { Circle, Line, Text as SvgText, G } from 'react-native-svg';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useFocusEffect, useLocalSearchParams, useRouter } from 'expo-router';
import { Body, Caption, Card, H2, H3, Label } from '@/src/ui';
import { api, AnalysisResult, MindMapNode } from '@/src/api';
import { colors, fonts, radius, spacing } from '@/src/theme';

type Pos = { x: number; y: number };

export default function MindMapScreen() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const router = useRouter();
  const { width } = useWindowDimensions();
  const [analysis, setAnalysis] = useState<AnalysisResult | null>(null);
  const [selected, setSelected] = useState<MindMapNode | null>(null);

  const load = useCallback(async () => {
    if (!id) return;
    const a = await api.getAnalysis(id);
    setAnalysis(a);
  }, [id]);

  useFocusEffect(useCallback(() => { load(); }, [load]));

  const { nodes, edges } = useMemo(() => {
    const nodes = analysis?.mind_map?.nodes || [];
    const edges = analysis?.mind_map?.edges || [];
    return { nodes, edges };
  }, [analysis]);

  const W = width;
  const H = 560;
  const cx = W / 2;
  const cy = H / 2;
  const radiusOuter = Math.min(W, H) * 0.36;

  // Düğümleri konumlandır
  const positions = useMemo(() => {
    const pos: Record<string, Pos> = {};
    pos['self'] = { x: cx, y: cy };
    const maternal = nodes.filter((n) => n.side === 'maternal');
    const paternal = nodes.filter((n) => n.side === 'paternal');

    // Anne soyu: sol yarım daire (π/2 → 3π/2)
    maternal.forEach((n, i) => {
      const angle = Math.PI / 2 + (Math.PI / (maternal.length + 1)) * (i + 1);
      pos[n.id] = {
        x: cx + Math.cos(angle) * radiusOuter,
        y: cy + Math.sin(angle) * radiusOuter,
      };
    });
    // Baba soyu: sağ yarım daire (-π/2 → π/2)
    paternal.forEach((n, i) => {
      const angle = -Math.PI / 2 + (Math.PI / (paternal.length + 1)) * (i + 1);
      pos[n.id] = {
        x: cx + Math.cos(angle) * radiusOuter,
        y: cy + Math.sin(angle) * radiusOuter,
      };
    });
    return pos;
  }, [nodes, cx, cy, radiusOuter]);

  if (!analysis) {
    return (
      <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
          <Body>Zihin haritası hazırlanıyor…</Body>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: colors.bgPrimary }}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} testID="back-btn">
          <Body style={{ color: colors.accentSage }}>‹ Geri</Body>
        </TouchableOpacity>
        <View style={{ alignItems: 'center' }}>
          <Caption style={{ color: colors.accentSage, letterSpacing: 2 }}>ZİHİN HARİTASI</Caption>
          <H3>Soy Yükü Ağı</H3>
        </View>
        <View style={{ width: 60 }} />
      </View>

      <View style={styles.legend}>
        <View style={styles.legendItem}>
          <View style={[styles.dot, { backgroundColor: colors.maternalPrimary }]} />
          <Caption>Anne soyu</Caption>
        </View>
        <View style={styles.legendItem}>
          <View style={[styles.dot, { backgroundColor: colors.paternalPrimary }]} />
          <Caption>Baba soyu</Caption>
        </View>
        <View style={styles.legendItem}>
          <View style={[styles.dot, { backgroundColor: colors.textPrimary }]} />
          <Caption>Kendisi</Caption>
        </View>
      </View>

      <ScrollView>
        <Svg width={W} height={H}>
          {/* Edges */}
          {edges.map((e, i) => {
            const from = positions[e.from];
            const to = positions[e.to];
            if (!from || !to) return null;
            const stroke = e.side === 'maternal' ? colors.maternalPrimary : e.side === 'paternal' ? colors.paternalPrimary : colors.textSecondary;
            return <Line key={i} x1={from.x} y1={from.y} x2={to.x} y2={to.y} stroke={stroke} strokeWidth={1.4} strokeOpacity={0.5} />;
          })}
          {/* Nodes */}
          {nodes.map((n) => {
            const p = positions[n.id];
            if (!p) return null;
            const isSelf = n.type === 'self';
            const fill = n.side === 'maternal' ? colors.maternalLight : n.side === 'paternal' ? colors.paternalLight : colors.bgCard;
            const stroke = n.side === 'maternal' ? colors.maternalPrimary : n.side === 'paternal' ? colors.paternalPrimary : colors.textPrimary;
            const r = isSelf ? 38 : 28;
            // Sorun varsa kırmızı halo
            const hasIssue = (n.unfulfilled_vows?.length || 0) > 0 || (n.sins_admitted?.length || 0) > 0 || (n.diseases?.length || 0) > 0;
            return (
              <G key={n.id} onPress={() => setSelected(n)}>
                {hasIssue && (
                  <Circle cx={p.x} cy={p.y} r={r + 5} fill="transparent" stroke={colors.errorVow} strokeWidth={1} strokeOpacity={0.35} strokeDasharray="3,3" />
                )}
                <Circle cx={p.x} cy={p.y} r={r} fill={fill} stroke={stroke} strokeWidth={2} />
                <SvgText
                  x={p.x}
                  y={p.y + 4}
                  fontSize={isSelf ? 12 : 10}
                  fontWeight="600"
                  textAnchor="middle"
                  fill={stroke}
                >
                  {isSelf ? n.label.split(' ')[0] : (n.relation || n.label).slice(0, 10)}
                </SvgText>
              </G>
            );
          })}
        </Svg>

        <View style={{ paddingHorizontal: spacing.lg, marginTop: spacing.md }}>
          <Caption style={{ color: colors.textSecondary, textAlign: 'center', fontStyle: 'italic' }}>
            Bir düğüme dokunarak o atanın yaşadığı olaylar, yarım kalan adaklar ve manevi izleri görüntüleyin.
          </Caption>
        </View>

        <View style={{ paddingHorizontal: spacing.lg, marginTop: spacing.lg }}>
          <Label style={{ marginBottom: spacing.sm }}>SOY YÜKÜ ENVANTERİ</Label>
          {nodes.filter((n) => n.id !== 'self').map((n) => (
            <TouchableOpacity key={n.id} onPress={() => setSelected(n)} testID={`node-${n.id}`}>
              <Card style={[styles.invCard, { borderLeftColor: n.side === 'maternal' ? colors.maternalPrimary : colors.paternalPrimary }]}>
                <H3 style={{ fontSize: 16 }}>{n.relation || n.label}</H3>
                <Caption style={{ color: n.side === 'maternal' ? colors.maternalPrimary : colors.paternalPrimary }}>
                  {n.side === 'maternal' ? 'Anne soyu' : 'Baba soyu'}{n.label && n.relation ? ` · ${n.label}` : ''}
                </Caption>
                {((n.diseases?.length || 0) + (n.unfulfilled_vows?.length || 0) + (n.events?.length || 0) + (n.sins_admitted?.length || 0)) === 0 ? (
                  <Caption style={{ marginTop: 4 }}>Detay girilmedi</Caption>
                ) : (
                  <Caption style={{ marginTop: 4 }}>
                    {n.diseases?.length || 0} hastalık · {n.unfulfilled_vows?.length || 0} yarım adak · {n.events?.length || 0} olay · {n.sins_admitted?.length || 0} günah
                  </Caption>
                )}
              </Card>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>

      <NodeDetailModal node={selected} onClose={() => setSelected(null)} />
    </SafeAreaView>
  );
}

function NodeDetailModal({ node, onClose }: { node: MindMapNode | null; onClose: () => void }) {
  if (!node) return null;
  const isSelf = node.type === 'self';
  const sideColor = node.side === 'maternal' ? colors.maternalPrimary : node.side === 'paternal' ? colors.paternalPrimary : colors.textPrimary;
  const sideBg = node.side === 'maternal' ? colors.maternalLight : node.side === 'paternal' ? colors.paternalLight : colors.bgSecondary;

  return (
    <Modal visible={!!node} animationType="slide" transparent onRequestClose={onClose}>
      <View style={styles.modalBackdrop}>
        <View style={styles.modalCard}>
          <SafeAreaView edges={['bottom']}>
            <ScrollView style={{ maxHeight: 540 }} contentContainerStyle={{ padding: spacing.lg }}>
              <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <View style={{ flex: 1 }}>
                  <View style={[styles.sideBadge, { backgroundColor: sideBg }]}>
                    <Caption style={{ color: sideColor, fontFamily: fonts.bodySemi }}>
                      {isSelf ? 'KENDİSİ' : node.side === 'maternal' ? 'ANNE SOYU' : 'BABA SOYU'}
                    </Caption>
                  </View>
                  <H2 style={{ color: sideColor, marginTop: spacing.sm }}>{node.label}</H2>
                  {node.relation && !isSelf && <Caption>{node.relation}</Caption>}
                </View>
                <TouchableOpacity onPress={onClose} testID="modal-close"><Body style={{ fontSize: 26 }}>×</Body></TouchableOpacity>
              </View>

              {(node.diseases?.length || 0) > 0 && (
                <View style={styles.section}>
                  <Label style={{ marginBottom: spacing.sm }}>HASTALIKLARI</Label>
                  {node.diseases!.map((d, i) => <Caption key={i}>· {d}</Caption>)}
                </View>
              )}

              {(node.allergies?.length || 0) > 0 && (
                <View style={styles.section}>
                  <Label style={{ marginBottom: spacing.sm }}>ALERJİLER</Label>
                  {node.allergies!.map((d, i) => <Caption key={i}>· {d}</Caption>)}
                </View>
              )}

              {(node.events?.length || 0) > 0 && (
                <View style={styles.section}>
                  <Label style={{ marginBottom: spacing.sm }}>YAŞADIĞI OLAYLAR</Label>
                  {node.events!.map((d, i) => <Caption key={i}>· {d}</Caption>)}
                </View>
              )}

              {(node.unfulfilled_vows?.length || 0) > 0 && (
                <View style={styles.section}>
                  <Label style={{ marginBottom: spacing.sm, color: colors.errorVow }}>YARIM KALAN ADAKLAR</Label>
                  {node.unfulfilled_vows!.map((d, i) => <Caption key={i} style={{ color: colors.errorVow }}>⌛ {d}</Caption>)}
                </View>
              )}

              {(node.vows?.length || 0) > 0 && (
                <View style={styles.section}>
                  <Label style={{ marginBottom: spacing.sm, color: colors.errorVow }}>YARIM ADAKLAR</Label>
                  {node.vows!.map((d, i) => <Caption key={i} style={{ color: colors.errorVow }}>⌛ {d}</Caption>)}
                </View>
              )}

              {(node.sins_admitted?.length || 0) > 0 && (
                <View style={styles.section}>
                  <Label style={{ marginBottom: spacing.sm }}>BİLİNEN GÜNAHLAR</Label>
                  {node.sins_admitted!.map((d, i) => <Caption key={i}>· {d}</Caption>)}
                </View>
              )}

              {((node.diseases?.length || 0) + (node.events?.length || 0) + (node.unfulfilled_vows?.length || 0) + (node.sins_admitted?.length || 0) + (node.allergies?.length || 0) + (node.vows?.length || 0)) === 0 && (
                <Caption style={{ marginTop: spacing.md, textAlign: 'center' }}>Bu düğüm için ayrıntı eklenmemiş.</Caption>
              )}

              <Caption style={{ marginTop: spacing.lg, fontStyle: 'italic', textAlign: 'center', color: colors.textSecondary }}>
                {isSelf ? 'Soy izleriniz bugüne sızıyor — anne ve baba taraflarından gelen yükleri gözden geçirin.' : 'Bu atadan size sızan yük, hastalık-sebep eşleştirmesinde değerlendirildi.'}
              </Caption>
            </ScrollView>
          </SafeAreaView>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingHorizontal: spacing.lg, paddingVertical: spacing.sm },
  legend: { flexDirection: 'row', justifyContent: 'center', gap: spacing.lg, paddingBottom: spacing.sm },
  legendItem: { flexDirection: 'row', alignItems: 'center', gap: 6 },
  dot: { width: 8, height: 8, borderRadius: 4 },
  invCard: { borderLeftWidth: 4 },
  modalBackdrop: { flex: 1, backgroundColor: 'rgba(44,53,49,0.55)', justifyContent: 'flex-end' },
  modalCard: { backgroundColor: colors.bgPrimary, borderTopLeftRadius: 24, borderTopRightRadius: 24, maxHeight: '88%' },
  sideBadge: { paddingHorizontal: 10, paddingVertical: 4, borderRadius: radius.round, alignSelf: 'flex-start' },
  section: { marginTop: spacing.lg },
});
