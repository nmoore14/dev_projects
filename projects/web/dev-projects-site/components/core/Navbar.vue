<template>
  <header class="fixed md:absolute w-full text-gray-600 body-font z-100">
    <div class="container flex flex-wrap flex-row justify-between align-center items-center py-2 px-4 md:p-5">
      <a class="flex title-font font-medium items-center text-gray-900" id="brand-link">
        <svg width="28" height="28" stroke="none" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" preserveAspectRatio="xMidYMid meet" data-attributes-set=",xmlns:xlink,xmlns,viewBox,preserveAspectRatio">
          <path xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" d="M2 6a2 2 0 012-2h4l2 2h4a2 2 0 012 2v1H8a3 3 0 00-3 3v1.5a1.5 1.5 0 01-3 0V6z" clip-rule="evenodd"></path>
          <path xmlns="http://www.w3.org/2000/svg" d="M6 12a2 2 0 012-2h8a2 2 0 012 2v2a2 2 0 01-2 2H2h2a2 2 0 002-2v-2z"></path>
        </svg>
        <span class="ml-3 text-xl font-display-logo font-bold">[{ DEV PROJECT }]</span>
      </a>
      <nav class="hidden md:flex md:flex-row md:mr-auto md:ml-4 md:py-1 md:pl-4 md:border-l md:border-gray-400	flex flex-wrap items-center text-base justify-center">
        <a class="mr-5 hover:text-gray-900">First Link</a>
        <a class="mr-5 hover:text-gray-900">Second Link</a>
        <a class="mr-5 hover:text-gray-900">Third Link</a>
        <a class="mr-5 hover:text-gray-900">Fourth Link</a>
      </nav>
      <button class="flex flex-col md:hidden bg-indigo-500 rounded-xl px-4">
        <svg width="30px" height="30px" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" :color="buttonColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path>
        </svg>
      </button>
    </div>
  </header>
</template>

<script>
export default {
  data () {
    return {
      buttonColor: '#ffffff'
    }
  }
}
</script>

<style>
  #brand-link svg {
    fill: #2f2f2f;
  }
</style>
