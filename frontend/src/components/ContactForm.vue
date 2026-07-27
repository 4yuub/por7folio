<template>
  <div class="animate-in w-full max-w-4xl mx-auto">
    <div class="flex flex-col md:flex-row gap-16 md:gap-24">
      <!-- Info Column -->
      <div class="md:w-1/3 space-y-8">
        <div class="space-y-4">
          <h3 class="text-3xl font-black tracking-tight text-cozy-charcoal dark:text-white leading-none font-mono">
            /connect
          </h3>
          <p class="text-muted-foreground font-medium text-sm leading-relaxed">
            I'm currently looking for new opportunities and collaborations. Feel free to reach out.
          </p>
        </div>

        <div class="space-y-4 font-mono">
          <div class="flex flex-col">
            <span class="text-[10px] text-code-comment uppercase tracking-widest">Email</span>
            <a href="mailto:catch-all@4yuub.com" class="text-sm text-primary hover:underline">catch-all@4yuub.com</a>
          </div>
          <div class="flex flex-col">
            <span class="text-[10px] text-code-comment uppercase tracking-widest">Local-Time</span>
            <span class="text-sm text-cozy-charcoal dark:text-white">{{ currentTime }}</span>
          </div>
        </div>
      </div>

      <!-- Form Column -->
      <form @submit.prevent="handleSubmit" class="flex-1 space-y-8">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-8">
          <div class="space-y-2">
            <label for="name"
              class="text-[10px] font-mono font-bold uppercase tracking-widest text-code-comment">Name</label>
            <input v-model="form.name" type="text" id="name" required
              class="w-full bg-transparent border-b border-border/60 px-4 py-2 text-base text-muted-foreground focus:border-primary outline-none transition-all placeholder:text-white/20 font-mono rounded-t-md"
              placeholder="e.g. Satoshi Nakamoto" />
          </div>
          <div class="space-y-2">
            <label for="email"
              class="text-[10px] font-mono font-bold uppercase tracking-widest text-code-comment">Email</label>
            <input v-model="form.email" type="email" id="email" required
              class="w-full bg-transparent border-b border-border/60 px-4 py-2 text-base text-muted-foreground focus:border-primary outline-none transition-all placeholder:text-white/20 font-mono rounded-t-md"
              placeholder="satoshi@bitcoin.org" />
          </div>
        </div>

        <div class="space-y-2">
          <label for="message"
            class="text-[10px] font-mono font-bold uppercase tracking-widest text-code-comment">Message</label>
          <textarea v-model="form.message" id="message" required rows="3"
            class="w-full bg-transparent border-b border-border/60 px-4 py-2 text-base text-muted-foreground focus:border-primary outline-none transition-all placeholder:text-white/20 resize-none font-mono rounded-t-md"
            placeholder="What's on your mind?"></textarea>
        </div>

        <div class="pt-4">
          <button type="submit" :disabled="loading"
            class="group flex items-center gap-4 text-sm font-mono font-black text-primary hover:text-primary/70 transition-all disabled:opacity-50 uppercase tracking-widest">
            <span>{{ loading ? 'await send()' : 'execute.send_message()' }}</span>
            <span class="text-lg group-hover:translate-x-1 transition-transform">→</span>
          </button>
        </div>

        <div v-if="status"
          :class="['mt-8 p-4 rounded-lg text-xs font-mono border', status.type === 'success' ? 'bg-green-500/5 border-green-500/20 text-green-600' : 'bg-red-500/5 border-red-500/20 text-red-600']">
          {{ status.type === 'success' ? '> success: ' : '> error: ' }}{{ status.message }}
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { onUnmounted, ref } from 'vue'

const form = ref({
  name: '',
  email: '',
  subject: 'New Inquiry from Portfolio',
  message: ''
})

const loading = ref(false)
const status = ref(null)

const currentTime = ref(new Date().toLocaleTimeString())
const clockTimer = setInterval(() => {
  currentTime.value = new Date().toLocaleTimeString()
}, 1000)
onUnmounted(() => clearInterval(clockTimer))

const handleSubmit = async () => {
  loading.value = true
  status.value = null

  try {
    const API_BASE = import.meta.env.DEV ? 'http://localhost:8000/api' : '/api'
    const response = await fetch(`${API_BASE}/contact/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(form.value)
    })

    if (response.ok) {
      status.value = { type: 'success', message: 'Message received. I will reach out soon.' }
      form.value = { name: '', email: '', subject: 'New Inquiry from Portfolio', message: '' }
    } else {
      const data = await response.json()
      status.value = { type: 'error', message: 'Something went wrong. Please try again.' }
    }
  } catch (error) {
    status.value = { type: 'error', message: 'Network error. Please try again.' }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.animate-in {
  animation: fade-in-up 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
