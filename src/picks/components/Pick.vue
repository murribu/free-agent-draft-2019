<template>
  <div class="columns is-centered">
    <div class="column is-full is-three-quarters-desktop">
      <div class="columns">
        <div class="column is-1">{{ rank }}</div>
        <div class="column is-5">{{ pick ? pick.availablePlayer.player.first_name + " " + pick.availablePlayer.player.last_name + " (" + pick.overUnder + " " + pick.availablePlayer.projectedamount + "M)" : '' }}</div>
        <div class="column is-2">
          <button class="button is-danger" v-if="canRemove" @click.prevent="remove">&times;</button>
          <button class="button is-info" v-if="canMoveUp" @click.prevent="moveup">&uarr;</button>
          <div v-if="pick && pick.availablePlayer && pick.availablePlayer.signedAt">
            <b>{{ points }} points</b>
            <br>
            Signed for {{ pick.availablePlayer.actualyears }} years and ${{ pick.availablePlayer.actualamount }}M
          </div>
        </div>
        <div class="column is-3">{{ pick ? prettyDate(pick.createdAt): '' }}</div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Pick',
    props: ['pick', 'rank', 'canRemove', 'canMoveUp', 'points'],
    methods: {
      remove() {
        this.$emit('remove', this.pick.playerId);
      },
      moveup() {
        this.$emit('moveup', this.pick.playerId);
      },
      prettyDate(str) {
        return new Date(str).toUTCString()
      }
    }
  }
</script>

<style scoped="true">
</style>
