<template>
  <div
    class="group relative overflow-hidden rounded-lg bg-code-bg p-0 border border-white/10 shadow-lg">
    <!-- Header/File Info -->
    <div class="flex items-center justify-between px-4 py-2 bg-white/5 border-b border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-2 h-2 rounded-full bg-code-key/30"></div>
        <div class="h-3 w-32 rounded bg-white/5 skeleton-shimmer"></div>
      </div>
      <div class="h-2 w-2 rounded-full bg-white/5"></div>
    </div>

    <!-- Content -->
    <div class="relative p-6 font-mono text-sm leading-relaxed overflow-hidden min-h-[220px]">
      <!-- Image placeholder -->
      <div class="absolute top-4 right-4 w-20 h-20 sm:w-24 sm:h-24 hidden sm:block">
        <div class="w-full h-full rounded-lg bg-white/5 border border-white/10 skeleton-shimmer"></div>
      </div>

      <div class="space-y-1 pr-0 sm:pr-28">
        <!-- const project = { -->
        <div class="flex items-center gap-x-2">
          <div class="h-4 w-10 rounded bg-code-keyword/20 skeleton-shimmer"></div>
          <div class="h-4 w-14 rounded bg-code-key/20 skeleton-shimmer"></div>
          <div class="h-4 w-3 rounded bg-white/10"></div>
          <div class="h-4 w-3 rounded bg-white/10"></div>
        </div>

        <div class="pl-4 space-y-2 py-2">
          <!-- "title": "..." -->
          <div class="flex items-center gap-x-2">
            <div class="h-4 w-10 rounded bg-code-key/20 skeleton-shimmer"></div>
            <div class="h-4 w-2 rounded bg-white/10"></div>
            <div class="h-4 w-32 rounded bg-code-string/15 skeleton-shimmer"></div>
          </div>
          <!-- "description": "..." -->
          <div class="flex items-center gap-x-2">
            <div class="h-4 w-20 rounded bg-code-key/20 skeleton-shimmer"></div>
            <div class="h-4 w-2 rounded bg-white/10"></div>
            <div class="h-4 w-56 rounded bg-code-string/15 skeleton-shimmer"></div>
          </div>
          <!-- "repo": "..." -->
          <div class="flex items-center gap-x-2">
            <div class="h-4 w-10 rounded bg-code-key/20 skeleton-shimmer"></div>
            <div class="h-4 w-2 rounded bg-white/10"></div>
            <div class="h-4 w-44 rounded bg-code-string/15 skeleton-shimmer"></div>
          </div>
          <!-- "tech": [...] -->
          <div class="flex items-center gap-x-2">
            <div class="h-4 w-10 rounded bg-code-key/20 skeleton-shimmer"></div>
            <div class="h-4 w-2 rounded bg-white/10"></div>
            <div class="h-4 w-4 rounded bg-white/10"></div>
            <div class="h-4 w-16 rounded bg-code-string/15 skeleton-shimmer"></div>
            <div class="h-4 w-14 rounded bg-code-string/15 skeleton-shimmer"></div>
            <div class="h-4 w-20 rounded bg-code-string/15 skeleton-shimmer"></div>
            <div class="h-4 w-4 rounded bg-white/10"></div>
          </div>
        </div>

        <div class="h-4 w-3 rounded bg-white/10"></div>
      </div>

      <!-- Action bar -->
      <div class="mt-8 flex items-center justify-between pt-4 border-t border-white/5">
        <div class="flex items-center gap-6">
          <div class="h-4 w-20 rounded bg-code-keyword/15 skeleton-shimmer"></div>
          <div class="h-4 w-24 rounded bg-code-string/15 skeleton-shimmer"></div>
        </div>
        <div class="h-3 w-10 rounded bg-white/5"></div>
      </div>
    </div>
  </div>
</template>
