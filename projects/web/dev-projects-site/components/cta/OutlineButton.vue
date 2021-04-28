<template>
  <button :id="title"
    class="relative flex mx-auto mt-16 border-0 py-2 px-8 focus:outline-none rounded text-lg btn-secondary"
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

<style lang="scss">
  .btn-secondary {
    background-color: rgba(0, 0, 0, 0.0);
    border: .1rem solid;
    @apply border-indigo-500;
    color: #333;
    z-index: 0;

    &:before {
      position: absolute;
      content: '';
      width: 105%;
      height: 105%;
      @apply bg-indigo-500;
      border-radius: .25rem;
      z-index: -1;
      opacity: .25;
      transform: translate(-10px, -2px);
      transition: ease-in-out .2s;
    }

    &:hover {
      color: white;
    }

    &:hover::before {
      transform: translate(-25px, -5px);
      opacity: .8;
    }
  }

</style>
