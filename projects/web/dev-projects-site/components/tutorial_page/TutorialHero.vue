<template>
  <div class="relative text-gray-600 body-font h-120 md:h-140 inset-x-0 top-0 z-0" id="hero-main">
    <div class="absolute z-0 inset-x-0 -bottom-2 md:-bottom-8">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
        <path fill="#e0e6ec" fill-opacity="1" d="M0,128L24,112C48,96,96,64,144,85.3C192,107,240,181,288,202.7C336,224,384,192,432,181.3C480,171,528,181,576,197.3C624,213,672,235,720,245.3C768,256,816,256,864,245.3C912,235,960,213,1008,176C1056,139,1104,85,1152,64C1200,43,1248,53,1296,80C1344,107,1392,149,1416,170.7L1440,192L1440,320L1416,320C1392,320,1344,320,1296,320C1248,320,1200,320,1152,320C1104,320,1056,320,1008,320C960,320,912,320,864,320C816,320,768,320,720,320C672,320,624,320,576,320C528,320,480,320,432,320C384,320,336,320,288,320C240,320,192,320,144,320C96,320,48,320,24,320L0,320Z"></path>
      </svg>
    </div>
    <div class="absolute container mx-auto md:ml-24 flex h-full px-5 py-24 md:flex-row flex-col items-center z-10" id="hero-container">
      <div class="hidden md:flex lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0">
      </div>
          <div class="flex flex-col p-4 items-start text-left items-center rounded-lg bg-gray-100" id="hero-text-container">
            <h1 class="w-full sm:text-4xl text-3xl mb-4 font-medium text-center md:text-left text-gray-900">
              Welcome to Dev Project
            </h1>
            <p class="mb-8 leading-relaxed">Copper mug try-hard pitchfork pour-over freegan heirloom neutra air plant cold-pressed tacos poke beard tote bag. Heirloom echo park mlkshk tote bag selvage hot chicken authentic tumeric truffaut hexagon try-hard chambray.</p>
            <div class="flex w-full justify-center md:justify-start">
              <button class="flex flex-row flex-nowrap items-center w-2/3 md:w-1/3 ml-4 inline-flex text-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-gray-200 rounded text-lg text-center">
                Find out more!
              </button>
            </div>
          </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Hero',
  components: {
    Carousel,
    Slide
  }
}
</script>

<style lang="scss">
  #hero-main {
    background: linear-gradient(45deg,#86fde8,#acb6e5);
  }

  #hero-text-container {
    box-shadow: -4px 4px 20px rgba(10, 10, 10, .5),
               -8px 8px 0px #86fde8,
               -12px 12px 20px rgba(10, 10, 10, .5);
  }
</style>
