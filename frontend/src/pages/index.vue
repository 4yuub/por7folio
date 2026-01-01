<template>
  <div class="min-h-screen bg-[#fafafa] dark:bg-[#0b0f1a] selection:bg-primary/20">
    <div class="container mx-auto px-6 py-0 space-y-24">
      <Hero :profile="profile" />

      <!-- Projects Section -->
      <section id="projects" class="space-y-24 pt-16">
        <div class="space-y-4">
          <div class="flex items-center gap-4">
            <h2 class="text-2xl font-mono font-black text-cozy-charcoal dark:text-white uppercase tracking-tighter">
              <span class="text-primary">GET</span> /projects
            </h2>
            <div class="flex-1 h-px bg-border/50"></div>
          </div>
        </div>

        <div v-if="projects.length" class="max-w-6xl mx-auto flex flex-col gap-12">
          <div v-for="(project, index) in projects" :key="project.id" :class="[
            'w-full md:w-[85%] transition-all duration-700',
            index % 2 === 0 ? 'self-start' : 'self-end'
          ]">
            <ProjectCard :project="project" />
          </div>
        </div>
        <p v-else class="text-center font-mono text-muted-foreground animate-pulse text-sm">Loading projects.json...</p>
      </section>

      <!-- Experience Section -->
      <section id="experience" class="space-y-16">
        <div class="space-y-4">
          <div class="flex items-center gap-4">
            <h2 class="text-2xl font-mono font-black text-cozy-charcoal dark:text-white uppercase tracking-tighter">
              <span class="text-primary">GET</span> /experience
            </h2>
            <div class="flex-1 h-px bg-border/50"></div>
          </div>
        </div>

        <div v-if="companies.length" class="max-w-3xl mx-auto space-y-16">
          <div v-for="company in companies" :key="company.id"
            class="relative pl-12 border-l-2 border-border/40 last:border-l-transparent">
            <!-- Company Big Dot -->
            <div
              class="absolute -left-[11px] top-0 h-5 w-5 rounded-full border-2 border-primary bg-background z-10 flex items-center justify-center">
              <div class="w-2 h-2 rounded-full bg-primary animate-pulse"></div>
            </div>

            <div class="space-y-10">
              <div class="flex items-center gap-4 -mt-1.5">
                <img v-if="company.logo" :src="company.logo" :alt="company.name"
                  class="h-10 w-10 rounded-xl object-contain bg-white p-1.5 border border-border/50 shadow-sm" />
                <div class="flex flex-col">
                  <div class="flex items-center gap-2">
                    <h3 class="text-2xl font-black text-cozy-charcoal dark:text-white tracking-tight leading-none">{{
                      company.name }}</h3>
                    <a v-if="company.website" :href="company.website" target="_blank"
                      class="text-primary hover:text-primary/70 transition-colors">
                      <ExternalLink :size="16" stroke-width="3" />
                    </a>
                  </div>
                  <span
                    class="text-[10px] font-mono text-code-comment uppercase tracking-widest mt-1">Organization</span>
                </div>
              </div>

              <div class="space-y-10">
                <ExperienceTile v-for="exp in company.experiences" :key="exp.id" :experience="exp" />
              </div>
            </div>
          </div>
        </div>
        <p v-else class="text-center font-mono text-muted-foreground animate-pulse text-sm">Fetching experience.log...
        </p>
      </section>

      <!-- Skills Section -->
      <!-- Skills Section -->
      <section id="skills" class="space-y-16">
        <div class="space-y-4">
          <div class="flex items-center gap-4">
            <h2 class="text-2xl font-mono font-black text-cozy-charcoal dark:text-white uppercase tracking-tighter">
              <span class="text-primary">GET</span> /skills
            </h2>
            <div class="flex-1 h-px bg-border/50"></div>
          </div>
        </div>

        <div class="max-w-6xl mx-auto px-4">
          <Skills v-if="skills.length" :skills="skills" />
          <p v-else class="text-center font-mono text-muted-foreground animate-pulse text-sm">Loading skills.json...</p>
        </div>
      </section>

      <!-- Contact Section -->
      <section id="contact" class="pb-32 space-y-16">
        <div class="flex items-center gap-4">
          <h2 class="text-2xl font-mono font-black text-cozy-charcoal dark:text-white uppercase tracking-tighter">
            <span class="text-primary">POST</span> /contact
          </h2>
          <div class="flex-1 h-px bg-border/50"></div>
        </div>
        <div class="max-w-3xl mx-auto">
          <ContactForm />
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ExternalLink } from 'lucide-vue-next'
import { computed, onMounted, ref } from 'vue'
import Skills from '../components/Skills.vue'

const projects = ref([])
const companies = ref([])
const profile = ref(null)
const skills = ref([])

const allExperiences = computed(() => {
  const exps = []
  companies.value.forEach(company => {
    company.experiences.forEach(exp => {
      exps.push({
        ...exp,
        company_name: company.name
      })
    })
  })
  return exps.sort((a, b) => new Date(b.start_date) - new Date(a.start_date))
})

const BACKEND_URL = import.meta.env.DEV ? 'http://localhost:8000' : ''
const API_BASE = import.meta.env.DEV ? `${BACKEND_URL}/api` : '/api'

const fixImageUrl = (url) => {
  if (!url) return null
  if (url.startsWith('http')) return url
  return `${BACKEND_URL}${url}`
}

onMounted(async () => {
  try {
    const projRes = await fetch(`${API_BASE}/projects/`)
    const projData = await projRes.json()
    projects.value = projData.map(p => ({
      ...p,
      image: fixImageUrl(p.cropped_image || p.image)
    }))

    const compRes = await fetch(`${API_BASE}/companies/`)
    const compData = await compRes.json()
    companies.value = compData.map(c => ({
      ...c,
      logo: fixImageUrl(c.logo)
    }))

    const skillRes = await fetch(`${API_BASE}/skills/`)
    skills.value = await skillRes.json()

    const profRes = await fetch(`${API_BASE}/profile/`)
    const profData = await profRes.json()
    if (profData && profData.length > 0) {
      const rawProfile = profData[profData.length - 1]
      profile.value = {
        ...rawProfile,
        profile_picture: fixImageUrl(rawProfile.cropped_picture || rawProfile.profile_picture)
      }
    }
  } catch (error) {
    console.error('Failed to fetch data:', error)
  }
})
</script>
