<template>
  <div class="relative flex flex-col items-center body-font tutorialFeatured">
    <div class="container flex flex-wrap flex-col md:flex-row w-screen px-1 py-24">
      <div class="flex flex-col w-full text-center mb-20">
        <h1 class="sm:text-3xl text-2xl font-medium title-font text-gray-900 mb-4">Learn with us!</h1>
        <p class="text-base leading-relaxed px-2 md:px-0 xl:w-2/4 lg:w-3/4 mx-auto text-gray-500s">
          Sometimes the best way to learn is to teach others. Our tutorials are here for you and us to continue to grow our skillset and try something new.
        </p>
        <div class="flex mt-6 justify-center">
          <div class="w-16 h-1 rounded-full bg-indigo-500 inline-flex"></div>
        </div>
      </div>
      <div class="flex flex-col md:flex-row flex-wrap md:flex-nowrap w-screen items-center md:-mx-4 md:-mb-10 -mt-12 md:-mt-4 space-y-8 md:space-y-0 md:space-x-8">
        <FeaturedCard v-for="tutorial in featuredTutorials" :key="tutorial.index" :title="tutorial.title" :description="tutorial.description" :tags="tutorial.tags" />
      </div>
      <OutlineButton text="See All" />
    </div>
  </div>
</template>

<script>
import FeaturedCard from '@/components/core/FeaturedCard'
import OutlineButton from '@/components/cta/OutlineButton'

export default {
  name: 'TutorialFeature',
  components: [
    FeaturedCard,
    OutlineButton
  ],
  props: [
    'featuredTutorials'
  ]
}
</script>

<style>
  .tutorialFeatured {
    background-color: #e0e6ec;
  }

  .nue-card {
    @apply rounded-lg;
    background-color: #f0f3f6;
    box-shadow: -4px -4px 10px rgba(255, 255, 255, .75),
                5px 5px 20px rgba(0, 0, 100, .1),
                inset 5px 5px 25px rgba(255, 255, 255, .75),
                inset -4px -4px 10px rgba(0, 0, 100, .1);
  }
</style>
