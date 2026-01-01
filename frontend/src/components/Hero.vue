<template>
  <section class="flex flex-col items-center justify-center pt-24 lg:pt-24 animate-in px-4">
    <!-- Terminal Window -->
    <div
      class="w-full max-w-4xl rounded-lg overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.3)] border border-white/10 bg-code-bg group/terminal transition-all duration-700">
      <!-- Terminal Header -->
      <div class="flex items-center gap-2 px-4 py-3 bg-white/5 border-b border-white/10">
        <div class="flex gap-1.5">
          <div class="w-3 h-3 rounded-full bg-[#ff5f56]"></div>
          <div class="w-3 h-3 rounded-full bg-[#ffbd2e]"></div>
          <div class="w-3 h-3 rounded-full bg-[#27c93f]"></div>
        </div>
        <div class="mx-auto text-[10px] font-mono text-code-comment select-none uppercase tracking-widest opacity-50">
          kernel::ayoub-karafi.json</div>
      </div>

      <!-- Terminal Content -->
      <div class="relative p-6 md:p-12 font-mono text-sm md:text-base leading-relaxed overflow-hidden">
        <!-- Floating Profile Image (Integrated into the "code") -->
        <div v-if="profile?.profile_picture"
          class="absolute top-8 right-8 w-24 h-24 md:w-32 md:h-32 z-10 hidden sm:block">
          <div
            class="relative w-full h-full p-1 bg-white/5 rounded-xl border border-white/10 rotate-3 group-hover/terminal:rotate-0 transition-transform duration-500">
            <img :src="profile.profile_picture" :alt="profile.name"
              class="w-full h-full object-cover rounded-lg grayscale hover:grayscale-0 transition-all duration-500" />
            <!-- Code Decoration -->
            <div class="absolute -top-3 -left-3 text-[10px] text-code-comment">/* avatar.px */</div>
          </div>
        </div>

        <div class="space-y-1 relative z-0">
          <div class="flex flex-wrap items-center gap-x-2">
            <span class="text-code-keyword">const</span>
            <span class="text-code-key">profile</span>
            <span class="text-white">=</span>
            <span class="text-white">{</span>
          </div>

          <div class="pl-6 space-y-1">
            <div class="flex flex-wrap gap-x-2">
              <span class="text-code-key">"name"</span><span class="text-white">:</span>
              <span class="text-code-string">"{{ profile?.name || 'Ayoub Karafi' }}"</span><span
                class="text-white">,</span>
            </div>

            <div class="flex flex-wrap gap-x-2">
              <span class="text-code-key">"role"</span><span class="text-white">:</span>
              <span class="text-code-string">"{{ profile?.title || 'Software Engineer' }}"</span><span
                class="text-white">,</span>
            </div>

            <div class="flex flex-wrap gap-x-2">
              <span class="text-code-key">"bio"</span><span class="text-white">:</span>
              <span class="text-code-string">"{{ profile?.bio || 'Building scalable digital experiences.'
              }}"</span><span class="text-white">,</span>
            </div>

            <div v-if="profile?.languages && profile.languages.length > 0" class="flex flex-wrap gap-x-2">
              <span class="text-code-key">"languages"</span><span class="text-white">:</span>
              <span class="text-white">[</span>
              <span v-for="(lang, index) in profile.languages" :key="lang.id" class="text-code-string">
                "{{ lang.name + ' (' + lang.proficiency + ')' }}"{{ index < profile.languages.length - 1 ? ',' : '' }}
                  </span>
                  <span class="text-white">],</span>
            </div>

            <div class="flex flex-wrap gap-x-2">
              <span class="text-code-key">"links"</span><span class="text-white">:</span>
              <span class="text-white">[</span>
            </div>
            <div class="pl-6 flex items-center gap-2">
              <span class="text-white">"</span>
              <a :href="profile?.linkedin || '#'" target="_blank"
                class="text-code-string hover:underline decoration-primary/50 underline-offset-4">
                {{ profile?.linkedin || 'linkedin.com/in/4yuub' }}
              </a>
              <span class="text-white">",</span>
            </div>
            <div class="pl-6 flex items-center gap-2">
              <span class="text-white">"</span>
              <a :href="profile?.github || '#'" target="_blank"
                class="text-code-string hover:underline decoration-primary/50 underline-offset-4">
                {{ profile?.github || 'github.com/4yuub' }}
              </a>
              <span class="text-white">"</span>
            </div>
            <div class="pl-0">
              <span class="text-white">]</span>
            </div>
          </div>

          <div class="text-white">}</div>
        </div>

        <!-- Terminal Actions -->
        <div class="mt-12 pt-8 border-t border-white/5 flex flex-wrap gap-8">
          <a href="#projects" class="group/btn flex items-center gap-3">
            <span class="text-code-comment text-xs">01</span>
            <span class="text-code-keyword group-hover/btn:underline flex items-center gap-2">
              profile.viewProjects() <span class="text-white opacity-20">-></span>
            </span>
          </a>
          <a href="#contact" class="group/btn flex items-center gap-3">
            <span class="text-code-comment text-xs">02</span>
            <span class="text-code-string group-hover/btn:underline flex items-center gap-2">
              profile.contact() <span class="text-white opacity-20">-></span>
            </span>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  profile: {
    type: Object,
    default: null
  }
})
</script>

<style scoped>
.animate-in {
  animation: fade-in 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fade-in {
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
