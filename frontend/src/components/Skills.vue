<template>
  <div class="animate-in">
    <div
      class="group relative overflow-hidden rounded-lg bg-code-bg p-0 border border-white/10 shadow-lg transition-all duration-500 hover:shadow-primary/5 hover:border-primary/20">
      <!-- Header/File Info -->
      <div class="flex items-center justify-between px-4 py-2 bg-white/5 border-b border-white/10">
        <div class="flex items-center gap-2">
          <div class="w-2 h-2 rounded-full bg-code-key"></div>
          <span class="text-[10px] font-mono text-code-comment uppercase tracking-widest">Skills.Inventory.json</span>
        </div>
        <div class="flex gap-1.5">
          <div class="h-2 w-2 rounded-full bg-white/5"></div>
          <div class="h-2 w-2 rounded-full bg-white/5"></div>
          <div class="h-2 w-2 rounded-full bg-white/5"></div>
        </div>
      </div>

      <div class="p-6 font-mono text-sm leading-relaxed">
        <div class="flex gap-x-2">
          <span class="text-white">{</span>
        </div>

        <div class="pl-4 space-y-4 py-2">
          <div v-for="(skills, category) in groupedSkills" :key="category">
            <div class="flex gap-x-2">
              <span class="text-code-key">"{{ category }}"</span><span class="text-white">:</span>
              <span class="text-white">[</span>
            </div>
            <div class="pl-4 flex flex-wrap gap-x-4 gap-y-1">
              <div v-for="(skill, index) in skills" :key="skill.id" class="flex gap-x-1">
                <span class="text-code-string">"{{ skill.name }}"</span>
                <span v-if="index < skills.length - 1" class="text-white">,</span>
              </div>
            </div>
            <div class="text-white">],</div>
          </div>
        </div>

        <div class="text-white">}</div>
      </div>

      <!-- Footer Action -->
      <div class="p-4 bg-white/5 border-t border-white/10 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <span class="text-[10px] text-code-comment uppercase tracking-widest font-bold">status: optimized</span>
          <span class="text-white/10">|</span>
          <span class="text-[10px] text-code-comment uppercase tracking-widest font-bold">count: {{ skills.length
          }}</span>
        </div>
        <div class="text-[9px] text-code-comment font-bold uppercase tracking-widest opacity-40">
          stack.v3
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  skills: {
    type: Array,
    required: true
  }
})

const CATEGORY_MAP = {
  'Backend': 'backend',
  'Frontend': 'frontend',
  'DevOps': 'devops',
  'Data/AI': 'data-science',
  'Other': 'misc'
}

const groupedSkills = computed(() => {
  const grouped = {}
  props.skills.forEach(skill => {
    const cat = skill.category || 'Other'
    if (!grouped[cat]) grouped[cat] = []
    grouped[cat].push(skill)
  })

  // Sort in a specific order if needed
  const order = ['Frontend', 'Backend', 'DevOps', 'Data/AI', 'Other']
  const sortedGrouped = {}
  order.forEach(cat => {
    if (grouped[cat]) sortedGrouped[cat] = grouped[cat]
  })

  // Add any other categories that might be there
  Object.keys(grouped).forEach(cat => {
    if (!sortedGrouped[cat]) sortedGrouped[cat] = grouped[cat]
  })

  return sortedGrouped
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
