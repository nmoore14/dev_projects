<template>
  <div class="flex flex-col items-center body-font">
    <div class="container flex flex-wrap flex-row w-screen px-1 py-24">
      <div class="flex flex-col w-full text-center mb-20">
        <h1 class="sm:text-3xl text-2xl font-medium title-font text-gray-900 mb-4">Learn with us!</h1>
        <p class="text-base leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto text-gray-500s">Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine, ramps microdosing banh mi pug.</p>
        <div class="flex mt-6 justify-center">
          <div class="w-16 h-1 rounded-full bg-indigo-500 inline-flex"></div>
        </div>
      </div>
      <div class="flex flex-row flex-wrap md:flex-nowrap w-screen items-center sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6 space-x-8">
        <FeaturedCard v-for="tutorial in featuredTutorials" :key="tutorial.index" :title="tutorial.title" :description="tutorial.description" :tags="tutorial.tags" />
      </div>
      <button class="flex mx-auto mt-16 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">See All</button>
    </div>
  </div>
</template>

<script>
import FeaturedCard from '@/components/core/FeaturedCard'

export default {
  name: 'TutorialFeature',
  components: [
    FeaturedCard
  ],
  props: [
    'featuredTutorials'
  ]
}
</script>

<style>
  .nue-card {
    @apply rounded-lg;
    background-color: #f0f3f6;
    box-shadow: -4px -4px 10px rgba(255, 255, 255, .75),
                5px 5px 20px rgba(0, 0, 100, .1),
                inset 5px 5px 25px rgba(255, 255, 255, .75),
                inset -4px -4px 10px rgba(0, 0, 100, .1);
  }
</style>
