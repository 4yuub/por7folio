<template>
  <div class="min-h-screen bg-[#fafafa] dark:bg-[#0b0f1a] selection:bg-primary/20">
    <div class="container mx-auto px-6 py-12 space-y-32">
      <Hero :profile="profile" />

      <!-- Projects Section -->
      <section id="projects" class="space-y-16">
        <div class="space-y-4">
          <div class="flex items-center gap-4">
            <h2 class="text-2xl font-mono font-black text-cozy-charcoal dark:text-white uppercase tracking-tighter">
              <span class="text-primary">GET</span> /projects
            </h2>
            <div class="flex-1 h-px bg-border/50"></div>
          </div>
        </div>

        <div v-if="projects.length" class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
          <ProjectCard v-for="project in projects" :key="project.id" :project="project" />
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
          <div v-for="company in companies" :key="company.id" class="relative pl-12 border-l-2 border-border/40 last:border-l-transparent">
            <!-- Company Big Dot -->
            <div class="absolute -left-[11px] top-0 h-5 w-5 rounded-full border-2 border-primary bg-background z-10 flex items-center justify-center">
              <div class="w-2 h-2 rounded-full bg-primary animate-pulse"></div>
            </div>
            
            <div class="space-y-10">
              <div class="flex items-center gap-4 -mt-1.5">
                <img v-if="company.logo" :src="company.logo" :alt="company.name" class="h-10 w-10 rounded-xl object-contain bg-white p-1.5 border border-border/50 shadow-sm" />
                <div class="flex flex-col">
                  <h3 class="text-2xl font-black text-cozy-charcoal dark:text-white tracking-tight leading-none">{{ company.name }}</h3>
                  <span class="text-[10px] font-mono text-code-comment uppercase tracking-widest mt-1">Organization</span>
                </div>
              </div>

              <div class="space-y-10">
                <ExperienceTile v-for="exp in company.experiences" :key="exp.id" :experience="exp" />
              </div>
            </div>
          </div>
        </div>
        <p v-else class="text-center font-mono text-muted-foreground animate-pulse text-sm">Fetching experience.log...</p>
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
import { computed, onMounted, ref } from 'vue'

const projects = ref([])
const companies = ref([])
const profile = ref(null)

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

const BACKEND_URL = 'http://localhost:8000'

const fixImageUrl = (url) => {
  if (!url) return null
  if (url.startsWith('http')) return url
  return `${BACKEND_URL}${url}`
}

onMounted(async () => {
  try {
    const projRes = await fetch(`${BACKEND_URL}/api/projects/`)
    const projData = await projRes.json()
    projects.value = projData.map(p => ({
      ...p,
      image: fixImageUrl(p.cropped_image || p.image)
    }))

    const compRes = await fetch(`${BACKEND_URL}/api/companies/`)
    const compData = await compRes.json()
    companies.value = compData.map(c => ({
      ...c,
      logo: fixImageUrl(c.logo)
    }))

    const profRes = await fetch(`${BACKEND_URL}/api/profile/`)
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
