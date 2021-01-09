<template>
  <div class="text-gray-600 body-font mt-4">
    <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center rounded-lg" id="hero-container">
      <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0">
      </div>
      <div class="flex flex-col p-4 items-start text-left items-center rounded-lg bg-gray-100" id="hero-text-container">
        <h1 class="w-full title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">
          Welcome to Dev Project
        </h1>
        <p class="mb-8 leading-relaxed">Copper mug try-hard pitchfork pour-over freegan heirloom neutra air plant cold-pressed tacos poke beard tote bag. Heirloom echo park mlkshk tote bag selvage hot chicken authentic tumeric truffaut hexagon try-hard chambray.</p>
        <div class="flex justify-center">
          <button class="inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">Button</button>
          <button class="ml-4 inline-flex text-gray-700 bg-gray-100 border-0 py-2 px-6 focus:outline-none hover:bg-gray-200 rounded text-lg">Button</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Hero'
}
</script>

<style>
  #hero-container {
    background-image: url('../../assets/images/teal-city.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: bottom;
  }

  #hero-text-container {
    box-shadow: -4px 4px 20px rgba(10, 10, 10, .5),
               -8px 8px 0px #86fde8,
               -12px 12px 20px rgba(10, 10, 10, .5);
  }
</style>
