<template>
  <div id="main-home" class="flex flex-col min-h-screen flex-nowrap">
    <Hero />
    <BlogStart />
    <TutorialFeatured :featuredTutorials="featuredTutorials" v-if="featuredTutorials"/>
    <Creators />
  </div>
</template>

<script>
import Hero from '@/components/homepage/Hero'
import BlogStart from '@/components/homepage/BlogStart'
import TutorialFeatured from '@/components/homepage/TutorialFeatured'
import Creators from '@/components/homepage/Creators'

export default {
  components: {
    Hero,
    BlogStart,
    TutorialFeatured,
    Creators
  },
  data() {
    return {
    }
  },
  async asyncData({ $content, params }) {
    const featuredTutorials = await $content('tutorials', params.slug)
    .only(['title', 'description', 'slug', 'tags', 'featured'])
    .where({featured: true})
    .sortBy('index')
    .fetch()

    return {
      featuredTutorials
    }
  },
}
</script>

<style>

</style>
