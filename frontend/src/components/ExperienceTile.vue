<template>
  <div class="relative pl-6 pb-8 group animate-in last:pb-0">
    <!-- Sub-Timeline Dot -->
    <div class="absolute -left-[30px] top-2 h-3 w-3 rounded-full border-2 border-primary/40 bg-background z-10 transition-all duration-300 group-hover:scale-125 group-hover:border-primary group-hover:bg-primary/10"></div>

    <div class="flex flex-col space-y-1">
      <!-- Date -->
      <span class="text-[9px] font-black uppercase tracking-widest text-primary/60">
        {{ formatDate(experience.start_date) }} — {{ experience.is_current ? 'Present' : (experience.end_date ? formatDate(experience.end_date) : '') }}
      </span>

      <!-- Title & Company -->
      <h4 class="text-lg font-black tracking-tight text-cozy-charcoal dark:text-white leading-tight">
        {{ experience.role }}
      </h4>

      <!-- Description -->
      <p class="text-sm leading-relaxed text-muted-foreground/70 font-medium whitespace-pre-line max-w-2xl">
        {{ experience.description }}
      </p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  experience: {
    type: Object,
    required: true
  }
})

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { month: 'short', year: 'numeric' })
}
</script>

<style scoped>
.animate-in {
  animation: fade-in-right 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fade-in-right {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}
</style>
