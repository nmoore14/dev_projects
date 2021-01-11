<template>
  <button :id="title"
    class="inline-flex text-indigo-500 border border-indigo-500 py-2 px-6 mt-4 focus:outline-none hover:text-white hover:bg-indigo-600 rounded text-lg"
    v-tilt='{speed: 300, perspective: 600, scale: 1.05}'
  >
    {{ text }}
  </button>
</template>

<script>
export default {
  name: 'AniOutlineButton',
  props: {
    title: String,
    text: String,
    route: String,
  }
}
</script>

<style>

</style>
