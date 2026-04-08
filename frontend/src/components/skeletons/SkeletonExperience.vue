<template>
  <div class="max-w-3xl mx-auto space-y-16">
    <div v-for="n in 2" :key="n" class="relative pl-12 border-l-2 border-border/40"
      :class="{ 'last:border-l-transparent': n === 2 }">
      <!-- Company Dot -->
      <div
        class="absolute -left-[11px] top-0 h-5 w-5 rounded-full border-2 border-primary/20 bg-background z-10 flex items-center justify-center">
        <div class="w-2 h-2 rounded-full bg-primary/20"></div>
      </div>

      <div class="space-y-10">
        <!-- Company header -->
        <div class="flex items-center gap-4 -mt-1.5">
          <div class="h-10 w-10 rounded-xl bg-white/10 border border-border/50 skeleton-shimmer"></div>
          <div class="flex flex-col gap-1.5">
            <div class="h-6 w-36 rounded bg-white/10 skeleton-shimmer"></div>
            <div class="h-3 w-20 rounded bg-white/5 skeleton-shimmer"></div>
          </div>
        </div>

        <!-- Experience tiles -->
        <div class="space-y-10">
          <div v-for="t in (n === 1 ? 2 : 1)" :key="t" class="relative pl-6 pb-8">
            <!-- Sub-timeline dot -->
            <div
              class="absolute -left-[30px] top-2 h-3 w-3 rounded-full border-2 border-primary/20 bg-background z-10">
            </div>
            <div class="flex flex-col space-y-2">
              <div class="h-3 w-32 rounded bg-primary/15 skeleton-shimmer"></div>
              <div class="h-5 w-48 rounded bg-white/10 skeleton-shimmer"></div>
              <div class="space-y-1.5 pt-1">
                <div class="h-3 w-full max-w-md rounded bg-white/5 skeleton-shimmer"></div>
                <div class="h-3 w-4/5 max-w-sm rounded bg-white/5 skeleton-shimmer"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
