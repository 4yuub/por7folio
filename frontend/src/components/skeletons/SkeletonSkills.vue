<template>
  <div
    class="group relative overflow-hidden rounded-lg bg-code-bg p-0 border border-white/10 shadow-lg">
    <!-- Header/File Info -->
    <div class="flex items-center justify-between px-4 py-2 bg-white/5 border-b border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-2 h-2 rounded-full bg-code-key/30"></div>
        <div class="h-3 w-36 rounded bg-white/5 skeleton-shimmer"></div>
      </div>
      <div class="flex gap-1.5">
        <div class="h-2 w-2 rounded-full bg-white/5"></div>
        <div class="h-2 w-2 rounded-full bg-white/5"></div>
        <div class="h-2 w-2 rounded-full bg-white/5"></div>
      </div>
    </div>

    <!-- Content -->
    <div class="p-6 font-mono text-sm leading-relaxed">
      <div class="h-4 w-3 rounded bg-white/10 mb-3"></div>

      <div class="pl-4 space-y-5 py-2">
        <!-- Category rows -->
        <div v-for="n in 4" :key="n" class="space-y-2">
          <div class="flex items-center gap-x-2">
            <div class="h-4 rounded bg-code-key/20 skeleton-shimmer" :style="{ width: ['80px', '72px', '64px', '56px'][n - 1] }"></div>
            <div class="h-4 w-2 rounded bg-white/10"></div>
            <div class="h-4 w-3 rounded bg-white/10"></div>
          </div>
          <div class="pl-4 flex flex-wrap gap-x-4 gap-y-1">
            <div v-for="s in [3, 4, 3, 2][n - 1]" :key="s"
              class="h-4 rounded bg-code-string/15 skeleton-shimmer"
              :style="{ width: `${40 + Math.random() * 40}px` }">
            </div>
          </div>
          <div class="h-4 w-4 rounded bg-white/10"></div>
        </div>
      </div>

      <div class="h-4 w-3 rounded bg-white/10 mt-2"></div>
    </div>

    <!-- Footer -->
    <div class="p-4 bg-white/5 border-t border-white/10 flex items-center justify-between">
      <div class="flex items-center gap-4">
        <div class="h-3 w-28 rounded bg-white/5 skeleton-shimmer"></div>
        <div class="h-3 w-px bg-white/10"></div>
        <div class="h-3 w-16 rounded bg-white/5 skeleton-shimmer"></div>
      </div>
      <div class="h-3 w-12 rounded bg-white/5"></div>
    </div>
  </div>
</template>
