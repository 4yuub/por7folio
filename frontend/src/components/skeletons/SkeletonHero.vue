<template>
  <section class="flex flex-col items-center justify-center pt-24 lg:pt-24 px-4">
    <div
      class="w-full max-w-4xl rounded-lg overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.3)] border border-white/10 bg-code-bg">
      <!-- Terminal Header -->
      <div class="flex items-center gap-2 px-4 py-3 bg-white/5 border-b border-white/10">
        <div class="flex gap-1.5">
          <div class="w-3 h-3 rounded-full bg-[#ff5f56]/40"></div>
          <div class="w-3 h-3 rounded-full bg-[#ffbd2e]/40"></div>
          <div class="w-3 h-3 rounded-full bg-[#27c93f]/40"></div>
        </div>
        <div class="mx-auto">
          <div class="h-3 w-40 rounded bg-white/5 skeleton-shimmer"></div>
        </div>
      </div>

      <!-- Terminal Content -->
      <div class="relative p-6 md:p-12 font-mono text-sm md:text-base leading-relaxed overflow-hidden">
        <!-- Profile Image Placeholder -->
        <div class="absolute top-8 right-8 w-24 h-24 md:w-32 md:h-32 z-10 hidden sm:block">
          <div class="w-full h-full p-1 bg-white/5 rounded-xl border border-white/10 rotate-3">
            <div class="w-full h-full rounded-lg bg-white/5 skeleton-shimmer"></div>
          </div>
        </div>

        <div class="space-y-1 relative z-0">
          <!-- const profile = { -->
          <div class="flex items-center gap-x-2">
            <div class="h-4 w-10 rounded bg-code-keyword/20 skeleton-shimmer"></div>
            <div class="h-4 w-14 rounded bg-code-key/20 skeleton-shimmer"></div>
            <div class="h-4 w-3 rounded bg-white/10 skeleton-shimmer"></div>
            <div class="h-4 w-3 rounded bg-white/10 skeleton-shimmer"></div>
          </div>

          <div class="pl-6 space-y-2 py-2">
            <!-- "name": "..." -->
            <div class="flex items-center gap-x-2">
              <div class="h-4 w-12 rounded bg-code-key/20 skeleton-shimmer"></div>
              <div class="h-4 w-2 rounded bg-white/10"></div>
              <div class="h-4 w-36 rounded bg-code-string/15 skeleton-shimmer"></div>
            </div>
            <!-- "role": "..." -->
            <div class="flex items-center gap-x-2">
              <div class="h-4 w-10 rounded bg-code-key/20 skeleton-shimmer"></div>
              <div class="h-4 w-2 rounded bg-white/10"></div>
              <div class="h-4 w-44 rounded bg-code-string/15 skeleton-shimmer"></div>
            </div>
            <!-- "bio": "..." -->
            <div class="flex items-center gap-x-2">
              <div class="h-4 w-8 rounded bg-code-key/20 skeleton-shimmer"></div>
              <div class="h-4 w-2 rounded bg-white/10"></div>
              <div class="h-4 w-64 rounded bg-code-string/15 skeleton-shimmer"></div>
            </div>
            <!-- "links": [...] -->
            <div class="flex items-center gap-x-2">
              <div class="h-4 w-12 rounded bg-code-key/20 skeleton-shimmer"></div>
              <div class="h-4 w-2 rounded bg-white/10"></div>
              <div class="h-4 w-4 rounded bg-white/10"></div>
            </div>
            <div class="pl-6 space-y-2">
              <div class="h-4 w-48 rounded bg-code-string/15 skeleton-shimmer"></div>
              <div class="h-4 w-40 rounded bg-code-string/15 skeleton-shimmer"></div>
            </div>
            <div class="h-4 w-2 rounded bg-white/10"></div>
          </div>

          <div class="h-4 w-3 rounded bg-white/10"></div>
        </div>

        <!-- Terminal Actions -->
        <div class="mt-12 pt-8 border-t border-white/5 flex gap-8">
          <div class="flex items-center gap-3">
            <div class="h-3 w-5 rounded bg-white/5"></div>
            <div class="h-4 w-36 rounded bg-code-keyword/15 skeleton-shimmer"></div>
          </div>
          <div class="flex items-center gap-3">
            <div class="h-3 w-5 rounded bg-white/5"></div>
            <div class="h-4 w-28 rounded bg-code-string/15 skeleton-shimmer"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
