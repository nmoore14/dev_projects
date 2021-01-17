<template>
  <div class="relative text-gray-600 body-font h-120 md:h-140 inset-x-0 top-0 z-0" id="hero-main">
    <div class="absolute z-0 inset-x-0 -bottom-2 md:-bottom-8">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
        <path fill="#f0f3f6" fill-opacity="1" d="M0,64L7.7,64C15.5,64,31,64,46,96C61.9,128,77,192,93,197.3C108.4,203,124,149,139,138.7C154.8,128,170,160,186,181.3C201.3,203,217,213,232,213.3C247.7,213,263,203,279,192C294.2,181,310,171,325,186.7C340.6,203,356,245,372,234.7C387.1,224,403,160,418,122.7C433.5,85,449,75,465,90.7C480,107,495,149,511,149.3C526.5,149,542,107,557,96C572.9,85,588,107,604,128C619.4,149,635,171,650,160C665.8,149,681,107,697,122.7C712.3,139,728,213,743,218.7C758.7,224,774,160,790,160C805.2,160,821,224,836,229.3C851.6,235,867,181,883,138.7C898.1,96,914,64,929,42.7C944.5,21,960,11,975,48C991,85,1006,171,1022,202.7C1037.4,235,1053,213,1068,218.7C1083.9,224,1099,256,1115,261.3C1130.3,267,1146,245,1161,218.7C1176.8,192,1192,160,1208,138.7C1223.2,117,1239,107,1254,106.7C1269.7,107,1285,117,1301,106.7C1316.1,96,1332,64,1347,80C1362.6,96,1378,160,1394,176C1409,192,1425,160,1432,144L1440,128L1440,320L1432.3,320C1424.5,320,1409,320,1394,320C1378.1,320,1363,320,1347,320C1331.6,320,1316,320,1301,320C1285.2,320,1270,320,1254,320C1238.7,320,1223,320,1208,320C1192.3,320,1177,320,1161,320C1145.8,320,1130,320,1115,320C1099.4,320,1084,320,1068,320C1052.9,320,1037,320,1022,320C1006.5,320,991,320,975,320C960,320,945,320,929,320C913.5,320,898,320,883,320C867.1,320,852,320,836,320C820.6,320,805,320,790,320C774.2,320,759,320,743,320C727.7,320,712,320,697,320C681.3,320,666,320,650,320C634.8,320,619,320,604,320C588.4,320,573,320,557,320C541.9,320,526,320,511,320C495.5,320,480,320,465,320C449,320,434,320,418,320C402.6,320,387,320,372,320C356.1,320,341,320,325,320C309.7,320,294,320,279,320C263.2,320,248,320,232,320C216.8,320,201,320,186,320C170.3,320,155,320,139,320C123.9,320,108,320,93,320C77.4,320,62,320,46,320C31,320,15,320,8,320L0,320Z"></path>
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
  name: 'Hero'
}
</script>

<style>
  #hero-main {
    background: linear-gradient(45deg,#86fde8,#acb6e5);
  }

  #hero-text-container {
    box-shadow: -4px 4px 20px rgba(10, 10, 10, .5),
               -8px 8px 0px #86fde8,
               -12px 12px 20px rgba(10, 10, 10, .5);
  }
</style>
