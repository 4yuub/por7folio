<template>
  <div
    class="group relative overflow-hidden rounded-lg bg-code-bg p-0 border border-white/10 shadow-lg transition-all duration-500 hover:shadow-primary/5 hover:border-primary/20 animate-in">
    <!-- Header/File Info -->
    <div class="flex items-center justify-between px-4 py-2 bg-white/5 border-b border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-2 h-2 rounded-full bg-code-key"></div>
        <span class="text-[10px] font-mono text-code-comment uppercase tracking-widest">{{
          project.title.toLowerCase().replace(/\s+/g, '-') }}.js</span>
      </div>
      <div class="h-2 w-2 rounded-full bg-primary/20 group-hover:bg-primary transition-colors"></div>
    </div>

    <div class="relative p-6 font-mono text-sm leading-relaxed overflow-hidden min-h-[220px]">
      <!-- Floating Project Image (Integrated into the "code") -->
      <button v-if="project.image" @click="openCarousel(0)"
        class="absolute top-6 right-6 w-20 h-20 md:w-24 md:h-24 z-10 hidden sm:block group/preview outline-none">
        <div
          class="relative w-full h-full p-1 bg-white/5 rounded-lg border border-white/10 -rotate-2 group-hover/preview:rotate-0 group-hover/preview:scale-105 group-hover/preview:border-primary/50 transition-all duration-500">
          <img :src="project.image" :alt="project.title"
            class="w-full h-full object-cover rounded-md grayscale group-hover/preview:grayscale-0 transition-all duration-500" />
          <!-- Code Decoration -->
          <div class="absolute -top-3 -left-3 text-[9px] text-code-comment group-hover/preview:text-primary">
            /* click.to_expand() */
          </div>
        </div>
      </button>

      <div class="space-y-1 relative z-0 pr-0 sm:pr-28">
        <div class="flex gap-x-2">
          <span class="text-code-keyword">const</span>
          <span class="text-code-key">project</span>
          <span class="text-white">=</span>
          <span class="text-white">{</span>
        </div>

        <div class="pl-4 space-y-1">
          <div class="flex gap-x-2">
            <span class="text-code-key">"title"</span><span class="text-white">:</span>
            <span class="text-code-string">"{{ project.title }}"</span><span class="text-white">,</span>
          </div>

          <div class="space-y-1">
            <span class="text-code-key">"desc"</span><span class="text-white">:</span>
            <div class="pl-4">
              <span class="text-code-string leading-snug">"{{ project.description }}"</span><span
                class="text-white">,</span>
            </div>
          </div>

          <div v-if="project.github_url" class="flex flex-wrap gap-x-2">
            <span class="text-code-key">"repo"</span><span class="text-white">:</span>
            <span class="text-white">"</span>
            <a :href="project.github_url" target="_blank"
              class="text-code-string hover:underline decoration-primary/50 underline-offset-4 line-clamp-1">
              {{ project.github_url.replace(/^https?:\/\//, '') }}
            </a>
            <span class="text-white">",</span>
          </div>

          <div v-if="project.url" class="flex flex-wrap gap-x-2">
            <span class="text-code-key">"demo"</span><span class="text-white">:</span>
            <span class="text-white">"</span>
            <a :href="project.url" target="_blank"
              class="text-code-string hover:underline decoration-primary/50 underline-offset-4 line-clamp-1">
              {{ project.url.replace(/^https?:\/\//, '') }}
            </a>
            <span class="text-white">",</span>
          </div>

          <div class="flex flex-wrap gap-x-2">
            <span class="text-code-key">"stack"</span><span class="text-white">:</span>
            <span class="text-white">[</span>
            <span v-for="(tech, index) in techList" :key="tech" class="text-code-string">
              "{{ tech }}"{{ index < techList.length - 1 ? ',' : '' }} </span>
                <span class="text-white">]</span>
          </div>
        </div>

        <div class="text-white">}</div>
      </div>

      <!-- Action -->
      <div class="mt-8 flex flex-wrap items-center justify-between gap-4 pt-4 border-t border-white/5">
        <div class="flex items-center gap-6">
          <a v-if="project.github_url" :href="project.github_url" target="_blank"
            class="text-[10px] font-bold text-code-keyword hover:underline flex items-center gap-2 uppercase tracking-widest group-hover:text-primary transition-colors">
            repo.open() <span class="text-white/20">-></span>
          </a>
          <a v-if="project.url" :href="project.url" target="_blank"
            class="text-[10px] font-bold text-code-keyword hover:underline flex items-center gap-2 uppercase tracking-widest group-hover:text-primary transition-colors">
            deploy.view() <span class="text-white/20">-></span>
          </a>
          <button v-if="allGalleryImages.length > 0" @click="openCarousel(0)"
            class="text-[10px] font-bold text-code-key hover:underline flex items-center gap-2 uppercase tracking-widest group-hover:text-primary transition-colors">
            gallery.view({{ allGalleryImages.length }}) <span class="text-white/20">-></span>
          </button>
        </div>
        <div class="text-[9px] text-code-comment font-bold uppercase tracking-widest opacity-40">
          v1.0.0
        </div>
      </div>
    </div>

    <!-- Carousel Overlay -->
    <Teleport to="body">
      <Transition name="fade">
        <div v-if="showCarousel"
          class="fixed inset-0 z-[100] flex items-center justify-center bg-black/98 backdrop-blur-xl p-4 sm:p-12 font-mono outline-none"
          tabindex="0" @keydown.esc="closeCarousel" @click="closeCarousel">
          <!-- Close Button -->
          <button @click.stop="closeCarousel"
            class="absolute top-8 right-8 text-white/50 hover:text-white transition-colors z-[120] flex items-center gap-2 text-[10px] uppercase tracking-widest outline-none">
            exit.gallery() <span class="text-xl">×</span>
          </button>

          <!-- Navigation -->
          <div v-if="allGalleryImages.length > 1"
            class="absolute inset-x-0 top-1/2 -translate-y-1/2 pointer-events-none flex justify-between px-4 sm:px-12 z-[110]">
            <button @click.stop="prevImage" :disabled="currentImageIndex === 0"
              class="pointer-events-auto w-14 h-14 sm:w-20 sm:h-20 flex items-center justify-center rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white shadow-2xl transition-all transform enabled:hover:bg-primary/80 enabled:hover:scale-110 disabled:opacity-5 disabled:cursor-not-allowed outline-none">
              <ChevronLeft :size="32" stroke-width="2.5" />
            </button>
            <button @click.stop="nextImage" :disabled="currentImageIndex === allGalleryImages.length - 1"
              class="pointer-events-auto w-14 h-14 sm:w-20 sm:h-20 flex items-center justify-center rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white shadow-2xl transition-all transform enabled:hover:bg-primary/80 enabled:hover:translate-x-1 disabled:opacity-5 disabled:cursor-not-allowed outline-none">
              <ChevronRight :size="32" stroke-width="2.5" />
            </button>
          </div>

          <!-- Content -->
          <div class="relative w-full max-w-6xl aspect-video z-[100]" @click.stop>
            <Transition name="slide" mode="out-in">
              <div :key="currentImageIndex" class="w-full h-full flex flex-col items-center justify-center">
                <img :src="allGalleryImages[currentImageIndex]"
                  class="max-w-full max-h-[85vh] object-contain rounded-lg border border-white/20 shadow-2xl bg-black/40" />

                <!-- Info Bar -->
                <div class="mt-8 flex items-center gap-4 text-[10px] text-code-comment uppercase tracking-widest">
                  <span class="px-2 py-1 bg-white/5 border border-white/10 rounded">IMAGE {{ currentImageIndex + 1 }} /
                    {{ allGalleryImages.length }}</span>
                  <span class="text-white/20">|</span>
                  <span>{{ project.title }} preview</span>
                </div>
              </div>
            </Transition>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ChevronLeft, ChevronRight } from 'lucide-vue-next';
import { computed, onMounted, onUnmounted, ref } from 'vue';

const props = defineProps({
  project: {
    type: Object,
    required: true
  }
})

const techList = computed(() => {
  return props.project.technologies ? props.project.technologies.split(',').map(s => s.trim()) : []
})

// Gallery / Carousel Logic
const showCarousel = ref(false)
const currentImageIndex = ref(0)

const BACKEND_URL = import.meta.env.DEV ? 'http://localhost:8000' : ''

const fixImageUrl = (url) => {
  if (!url) return null
  if (url.startsWith('http')) return url
  return `${BACKEND_URL}${url}`
}

const allGalleryImages = computed(() => {
  const images = []
  if (props.project.image) images.push(props.project.image)
  if (props.project.images) {
    props.project.images.forEach(img => {
      images.push(fixImageUrl(img.image))
    })
  }
  return images
})

const openCarousel = (index) => {
  currentImageIndex.value = index
  showCarousel.value = true
  document.body.style.overflow = 'hidden'
  // Focus the overlay for keyboard events
  setTimeout(() => {
    const overlay = document.querySelector('.fixed.inset-0.z-\\[100\\]')
    overlay?.focus()
  }, 50)
}

const closeCarousel = () => {
  showCarousel.value = false
  document.body.style.overflow = 'auto'
}

const nextImage = () => {
  if (currentImageIndex.value < allGalleryImages.value.length - 1) {
    currentImageIndex.value++
  }
}

const prevImage = () => {
  if (currentImageIndex.value > 0) {
    currentImageIndex.value--
  }
}

// Keyboard navigation
const handleKeydown = (e) => {
  if (!showCarousel.value) return
  if (e.key === 'Escape') closeCarousel()
  if (e.key === 'ArrowRight') nextImage()
  if (e.key === 'ArrowLeft') prevImage()
}

onMounted(() => window.addEventListener('keydown', handleKeydown))
onUnmounted(() => window.removeEventListener('keydown', handleKeydown))
</script>

<style scoped>
.animate-in {
  animation: fade-in-up 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-enter-from {
  opacity: 0;
  transform: scale(0.95) translateY(10px);
}

.slide-leave-to {
  opacity: 0;
  transform: scale(1.05) translateY(-10px);
}
</style>
