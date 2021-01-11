<template>
  <button :id="title"
    class="inline-flex text-indigo-500 border border-indigo-500 py-2 px-6 mt-4 focus:outline-none hover:text-white hover:bg-indigo-600 rounded text-lg"
  >
    {{ text }}
  </button>
</template>

<script>
export default {
  name: 'OutlineButton',
  props: {
    title: String,
    text: String,
    route: String,
  }
}
</script>

<style>

</style>
