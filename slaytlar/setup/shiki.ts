import { defineShikiSetup } from '@slidev/types'

/**
 * Açık temaya geçildi (bkz. tema/stil.css). Slidev'in varsayılanı
 * vitesse-*: bilerek düşük kontrastlı, ekranda hoş ama H.264'ten geçince
 * tanımlayıcılar zemine karışıyordu. github-light aynı açık paleti
 * belirgin kontrastla veriyor ve referans slaytlardaki lavanta kod
 * paneliyle uyuşuyor.
 *
 * Her iki anahtar da aynı: sistem koyu temaya geçse bile slaytlar
 * değişmemeli, yoksa 8 hafta boyunca çekimler arası renk kayması olur.
 */
export default defineShikiSetup(() => ({
  themes: {
    light: 'github-light',
    dark: 'github-light',
  },
}))
