<template>
  <div class="absolute flex flex-row w-full h-32 mt-8 flex-nowrap">
    <nav class="flex flex-row items-center justify-between w-full h-32">
      <div id="menu" class="flex flex-row items-center justify-between w-1/3 p-8 bg-blue-300 flex-nowrap space-x-4 custom-round-r">
        <div>
          <a href="#" class="content-1">Blog</a>
        </div>
        <div>
          <a href="#">Tutorials</a>
        </div>
        <div>
          <a href="#">About</a>
        </div>
        <div>
          <a href="#">Newsletter</a>
        </div>
      </div>
      <div id="brand" class="items-center justify-center w-1/3 text-center">
        <h1 class="dislay-1">dev projects</h1>
      </div>
      <div id="search" class="flex flex-row items-center justify-between w-1/3 p-8 bg-blue-300 flex-nowrap space-x-4 custom-round-l">
        <input type="text" name="search-box" placeholder="Search...">
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  
}
</script>

<style>
  .custom-round-r {
    border-radius: 0 1.75rem 1.75rem 0;
    background: linear-gradient(45deg, #0f0c29, #302b63);
  }

  .custom-round-l {
    border-radius: 1.75rem 0 0 1.75rem;
    background: linear-gradient(45deg, #302b63, #0f0c29);
  }

  #menu a {
    @apply text-gray-300;
    font-family: 'Fira Code', monospace;
    font-size: 1.25rem;
    font-weight: 500;
  }

  #brand h1 {
    font-family: 'Montserrat Alternates', sans-serif;
    text-transform: uppercase;
    font-weight: 600;
    font-size: 3rem;
  }
</style>
