<script setup lang="ts">
// Marka şeridi her slaytta tekrar edecek. 260 slaytta aynı div'i elle
// kopyalamamak için Slidev'in global katmanı kullanılıyor: bu dosya
// otomatik olarak her slaydın üstüne bindirilir.
//
// Logo <img> yerine satır içi SVG: currentColor'ı miras aldığı için
// zemin değişirse renk kendiliğinden uyuyor, ayrıca ek istek yapmıyor.
// Aynı işaretin bağımsız kopyası public/gorseller/logo.svg içinde.
import { computed } from 'vue'
const nav = computed(() => $slidev.nav)
</script>

<template>
  <footer class="ky-altbilgi">
    <span class="ky-altbilgi__sol">
      <svg class="ky-logo" viewBox="0 0 40 40" aria-hidden="true">
        <path fill="currentColor" d="M20 4 L35.5 33 L20 25.8 L4.5 33 Z" />
      </svg>
      <span class="ky-altbilgi__marka">İHA Otonom Sistemler</span>
    </span>
    <span>{{ nav.currentPage }} / {{ nav.total }}</span>
  </footer>
</template>
