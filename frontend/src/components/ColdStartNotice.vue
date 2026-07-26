<template>
  <Transition enter-active-class="transition-all duration-500 ease-out" enter-from-class="opacity-0 translate-y-4"
    enter-to-class="opacity-100 translate-y-0" leave-active-class="transition-all duration-300 ease-in"
    leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-4">
    <div v-if="visible"
      class="fixed bottom-6 right-6 z-50 w-[calc(100%-3rem)] max-w-sm rounded-lg overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.3)] border border-white/10 bg-code-bg font-mono">
      <!-- Terminal Header -->
      <div class="flex items-center gap-2 px-4 py-2.5 bg-white/5 border-b border-white/10">
        <div class="flex gap-1.5">
          <div class="w-2.5 h-2.5 rounded-full bg-[#ffbd2e]/70"></div>
          <div class="w-2.5 h-2.5 rounded-full bg-[#ffbd2e]/40"></div>
          <div class="w-2.5 h-2.5 rounded-full bg-[#ffbd2e]/20"></div>
        </div>
        <span class="text-[10px] text-code-comment uppercase tracking-widest ml-1">server.status</span>
        <span class="ml-auto text-[10px] text-code-number tabular-nums">{{ elapsedLabel }}</span>
      </div>

      <!-- Content -->
      <div class="flex items-start gap-3 p-4">
        <Loader2 :size="16" class="mt-0.5 shrink-0 animate-spin text-primary" stroke-width="2.5" />
        <div class="space-y-1.5 min-w-0">
          <p class="text-xs text-code-string leading-relaxed">
            <span class="text-code-keyword">&gt;</span> {{ currentMessage }}
          </p>
          <p class="text-[10px] text-code-comment leading-relaxed">
            No need to refresh, this can take up to a minute.
          </p>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { Loader2 } from 'lucide-vue-next'
import { computed, onUnmounted, ref, watch } from 'vue'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  }
})

const MESSAGES = [
  'backend is idle, waking it up...',
  'server is starting up...',
  'this can take up to a minute...',
  'still booting, almost there...',
  'thanks for hanging in there...',
  'just a bit longer...'
]

const elapsedSeconds = ref(0)
const messageIndex = ref(0)
let tickTimer = null

const elapsedLabel = computed(() => `${elapsedSeconds.value}s`)
const currentMessage = computed(() => MESSAGES[messageIndex.value % MESSAGES.length])

const stopTicking = () => {
  if (tickTimer) {
    clearInterval(tickTimer)
    tickTimer = null
  }
}

watch(() => props.visible, (isVisible) => {
  stopTicking()
  elapsedSeconds.value = 0
  messageIndex.value = 0

  if (isVisible) {
    tickTimer = setInterval(() => {
      elapsedSeconds.value += 1
      if (elapsedSeconds.value % 8 === 0) {
        messageIndex.value += 1
      }
    }, 1000)
  }
}, { immediate: true })

onUnmounted(stopTicking)
</script>
