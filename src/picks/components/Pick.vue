<template>
  <div class="columns is-centered">
    <div class="column is-full is-half-desktop">
      <div class="columns">
        <div class="column">{{ rank }}</div>
        <div class="column is-two-thirds-desktop">{{ pick ? pick.availablePlayer.player.first_name + " " + pick.availablePlayer.player.last_name + " (" + pick.overUnder + " " + pick.availablePlayer.projectedamount + "M)" : '' }}</div>
        <div class="column"><button class="button is-danger" v-if="pick" @click.prevent="remove">&times;</button></div>
        <div class="column"><button class="button is-info" v-if="pick && pick.rank > 1" @click.prevent="moveup">&uarr;</button></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Pick',
    props: ['pick', 'rank'],
    methods: {
      remove() {
        this.$emit('remove', this.pick.playerId);
      },
      moveup() {
        this.$emit('moveup', this.pick.playerId);
      }
    }
  }
</script>

<style scoped="true">
</style>
