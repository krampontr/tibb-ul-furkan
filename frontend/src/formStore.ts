import { create } from 'zustand';

export type FormData = {
  ad_soyad: string;
  yas: string;
  tlf: string;
  medeni_durum: string;
  cocuk_sayisi: string;
  memleket: string;
  dogum_tarihi: string;
  cinsiyet: 'erkek' | 'kadın' | '';
  anne_durum: string;
  baba_durum: string;
  anneanne_durum: string;
  anne_babasi_durum: string;
  babaanne_durum: string;
  baba_babasi_durum: string;
  zekat_veriyor: string;
  faizli_kredi: string;
  anne_hastalik: string;
  baba_hastalik: string;
  cocuk_hastalik: string;
  rahatsizliklar: string;
  adak_yemin: string;
  muska_okunmus_su: string;
  miras_sorunu: string;
  beddua_hak_haram: string;
  intihar: string;
  anne_baba_ofke: string;
  es_soguklugu: string;
  sehvet: string;
  duygusallik: string;
  kin: string;
  kusme_alinganlik: string;
  ofke: string;
  nefret: string;
  supheci: string;
  uyku_sorunu: string;
  aniden_parlama: string;
  alaycilik: string;
};

type State = FormData & {
  set: (partial: Partial<FormData>) => void;
  reset: () => void;
};

const initial: FormData = {
  ad_soyad: '', yas: '', tlf: '', medeni_durum: '', cocuk_sayisi: '',
  memleket: '', dogum_tarihi: '', cinsiyet: '',
  anne_durum: '', baba_durum: '', anneanne_durum: '',
  anne_babasi_durum: '', babaanne_durum: '', baba_babasi_durum: '',
  zekat_veriyor: '', faizli_kredi: '',
  anne_hastalik: '', baba_hastalik: '', cocuk_hastalik: '',
  rahatsizliklar: '',
  adak_yemin: '', muska_okunmus_su: '', miras_sorunu: '', beddua_hak_haram: '',
  intihar: '', anne_baba_ofke: '', es_soguklugu: '', sehvet: '',
  duygusallik: '', kin: '', kusme_alinganlik: '', ofke: '',
  nefret: '', supheci: '', uyku_sorunu: '', aniden_parlama: '', alaycilik: '',
};

export const useFormStore = create<State>((set) => ({
  ...initial,
  set: (partial) => set(partial),
  reset: () => set(initial),
}));
