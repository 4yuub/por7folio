<template>
  <div
    class="group relative overflow-hidden rounded-xl bg-code-bg p-0 border border-white/10 shadow-lg transition-all duration-500 hover:shadow-primary/10 hover:border-primary/30 animate-in">
    <!-- Header/File Info -->
    <div class="flex items-center justify-between px-4 py-2 bg-white/5 border-b border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-2 h-2 rounded-full bg-code-key"></div>
        <span class="text-[10px] font-mono text-code-comment">{{ project.title.toLowerCase().replace(/\s+/g, '-') }}.js</span>
      </div>
      <div class="h-2 w-2 rounded-full bg-primary/20 group-hover:bg-primary transition-colors"></div>
    </div>

    <div class="p-6 font-mono text-sm leading-relaxed">
      <div class="space-y-1">
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
            <span class="text-code-key">"description"</span><span class="text-white">:</span>
            <div class="pl-4">
              <span class="text-code-string">"{{ project.description }}"</span><span class="text-white">,</span>
            </div>
          </div>

          <div class="flex flex-wrap gap-x-2">
            <span class="text-code-key">"stack"</span><span class="text-white">:</span>
            <span class="text-white">[</span>
            <span v-for="(tech, index) in techList" :key="tech" class="text-code-string">
              "{{ tech }}"{{ index < techList.length - 1 ? ',' : '' }}
            </span>
            <span class="text-white">]</span>
          </div>
        </div>

        <div class="text-white">}</div>
      </div>

      <!-- Action -->
      <div class="mt-6 flex items-center justify-between">
        <a v-if="project.url" :href="project.url" target="_blank"
          class="text-xs font-bold text-code-keyword hover:underline flex items-center gap-2 uppercase tracking-widest">
          deploy.view()
        </a>
        <div class="text-[10px] text-code-comment font-bold uppercase tracking-widest">
          v1.0.0
        </div>
      </div>
    </div>

    <!-- Hover Image Overlay (Subtle) -->
    <div v-if="project.image" 
      class="absolute inset-0 pointer-events-none opacity-0 group-hover:opacity-10 transition-opacity duration-500">
      <img :src="project.image" :alt="project.title" class="w-full h-full object-cover grayscale" />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  project: {
    type: Object,
    required: true
  }
})

const techList = computed(() => {
  return props.project.technologies ? props.project.technologies.split(',').map(s => s.trim()) : []
})
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
</style>
