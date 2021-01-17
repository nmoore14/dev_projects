<template>
  <div id="main-container" class="absolute flex flex-col w-full">
    <Navbar />
    <Nuxt />
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/core/Navbar'
import Footer from '@/components/core/Footer'

export default {

}
</script>

<style>
  #main-container {
    background-color: #f0f3f6;
  }
</style>
