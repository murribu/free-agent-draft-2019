<template>
  <div class="container">
    <section class="hero is-primary">
      <div class="hero-body">
        <p class="title">Actuals</p>
        <p class="subtitle">How many millions did these millionaires get?</p>
      </div>
    </section>
    <hr class="hr">
    <div class="content">
      <p v-if="loading">Loading...</p>
      <p v-if="!loading && signedPlayers.length === 0">There are no results yet. Check back later</p>
      <p v-if="!loading && signedPlayers.length > 0">
        <div class="columns">
          <div class="column is-2"><b>Name</b></div>
          <div class="column is-2"><b>Projected Contract</b></div>
          <div class="column is-2"><b>Actual Contract</b></div>
          <div class="column is-2"><b>Difference</b></div>
          <div class="column is-2"><b>When</b></div>
        </div>
        <div class="columns" v-for="player in signedPlayers">
          <div class="column is-2">
            {{ player.player.first_name + " " + player.player.last_name }}
          </div>
          <div class="column is-2">{{ player.projectedyears }} years, ${{ player.projectedamount }}M</div>
          <div class="column is-2">{{ player.actualyears }} years, ${{ player.actualamount }}M</div>
          <div class="column is-2">{{ player.actualamount - player.projectedamount }}</div>
          <div class="column is-2">{{ prettyDate(player.signedAt) }}</div>
        </div>
      </p>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import { GetSignedPlayers } from './persist/graphqlActions';

  export default {
    name: 'Actuals',
    data() {
      return {
        loading: true,
        actions: {
          list: GetSignedPlayers
        },
        signedPlayers: []
      }
    },
    created() {
      this.logger = new this.$Amplify.Logger('ACUTALS_component')
      this.$Amplify.API.graphql(this.$Amplify.graphqlOperation(this.actions.list, {}))
        .then((res) => {
          console.log(res);
          this.signedPlayers = res.data.getSignedPlayers;
          this.loading = false;
        })
        .catch((e) => {
          this.logger.info(`Error listing available players`, e);
          this.loading = false;
        })
    },
    methods: {
      prettyDate(str) {
        return new Date(str).toUTCString()
      }
    }
  }
</script>
