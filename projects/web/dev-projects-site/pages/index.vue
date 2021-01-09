<template>
  <div id="main-home" class="flex flex-col min-h-screen flex-nowrap">
    <Hero />
    <BlogStart />
    <TutorialFeature />
    <Creators />
  </div>
</template>

<script>
import Hero from '@/components/homepage/Hero'
import BlogStart from '@/components/homepage/BlogStart'
import TutorialFeature from '@/components/homepage/TutorialFeature'
import Creators from '@/components/homepage/Creators'

export default {
  components: {
    Hero,
    BlogStart,
    TutorialFeature,
    Creators
  }
}
</script>

<style>

</style>
