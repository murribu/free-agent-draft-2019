<template>
  <div class="bd-main-container container">
    <section class="hero is-primary">
      <div class="hero-body">
        <p class="title">Picks</p>
      </div>
    </section>
    <div class="columns is-centered">
      <div class="column is-half-desktop is-two-thirds-tablet" style="text-align: center;">
        <div class="columns is-centered">
          <div class="column is-5">
            <div class="field">
              <label class="label" for="player">Player</label>
              <div class="control">
                <div class="select">
                  <select v-model="pick.playerId" id="player">
                    <option v-for="player in filteredAvailablePlayers" :value="player.id">{{ player && player.player ? player.player.first_name + " " + player.player.last_name + " (" + player.projectedyears + " years, " + player.projectedamount + "M)": '' }}</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <div class="column is-3">
            <div class="field">
              <label class="label" for="overUnder">Over/Under</label>
              <div class="control">
                <div class="select">
                  <select v-model="pick.overUnder" id="overUnder">
                    <option value="under">Under</option>
                    <option value="over">Over</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <div class="column is-2 has-text-right has-text-left-mobile">
            <div class="field" style="margin-top: 32px;">
              <button @click.prevent="create" class="button is-dark">Choose</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="columns is-centered">
      <div class="column is-full is-half-desktop">
        <div class="columns">
          <div class="column is-1">&nbsp;</div>
          <div class="column is-5"><b>Total</b></div>
          <div class="column is-2"><b>{{ totalPoints }} points</b></div>
          <div class="column is-3"><b>Last Update</b></div>
        </div>
      </div>
    </div>
    <a-pick
      v-for="i in 10"
      :key="i"
      :pick="getPickByRank(i)"
      :rank="i"
      :canRemove="canRemove(i)"
      :canMoveUp="canMoveUp(i)"
      :points="points(i)"
      @remove="remove"
      @moveup="moveup"
    />
  </div>
</template>

<script>
  import Vue from 'vue'
  import AmplifyStore from '../../store/store'

  import { CreatePick, ListPicks, DeletePick, GetAvailablePlayers, SwitchPicks } from './persist/graphqlActions';

  import Pick from './Pick'

  Vue.component('a-pick', Pick)

  export default {
    name: 'Picks',
    data () {
      return {
        pick: { playerId: '', overUnder: 'under' },
        picks: [],
        logger: {},
        actions: {
          create: CreatePick,
          list: ListPicks,
          delete: DeletePick,
          listavailable: GetAvailablePlayers,
          switch: SwitchPicks
        },
        availablePlayers: []
      }
    },
    created() {
      this.logger = new this.$Amplify.Logger('NOTES_component')
      this.$Amplify.API.graphql(this.$Amplify.graphqlOperation(this.actions.listavailable, {}))
        .then((res) => {
          this.availablePlayers = res.data.getAvailablePlayers;
          this.pick.playerId = this.filteredAvailablePlayers[0].id;
          this.listPicks();
        })
        .catch((e) => {
          this.logger.info(`Error listing available players`, e);
        })
    },
    computed: {
      userId: function() { return AmplifyStore.state.userId },
      filteredAvailablePlayers() {
        var self = this;
        return this.availablePlayers
          .filter(p => self.picks.filter(pick => pick.playerId === p.id).length === 0)
          .sort((a,b) => a.projectedamount > b.projectedamount ? -1 : 1)
      },
      totalPoints() {
        var totalPoints = 0;
        for (var rank = 1; rank <= 10; rank++) {
          totalPoints += this.points(rank);
        }
        return totalPoints;
      }
    },
    methods: {
      points(rank) {
        var pick = this.getPickByRank(rank);
        if (!pick || !pick.availablePlayer || !pick.availablePlayer.signedAt) return 0;
        return (10 - pick.rank) * (pick.overUnder === 'over' ? 1 : -1) * (pick.availablePlayer.actualamount - pick.availablePlayer.projectedamount)
      },
      getPickByRank(rank) {
        var self = this;
        return this.picks
          .find(p => p.rank == rank);
      },
      canRemove(rank) {
        var pick = this.getPickByRank(rank);
        return pick && pick.availablePlayer && !pick.availablePlayer.signedAt;
      },
      canMoveUp(rank) {
        if (rank === 1) return false;
        var previousPick = this.getPickByRank(rank - 1);
        return this.canRemove(rank) && previousPick && previousPick.availablePlayer && !previousPick.availablePlayer.signedAt;
      },
      listPicks() {
        this.$Amplify.API.graphql(this.$Amplify.graphqlOperation(this.actions.list, {}))
          .then((res) => {
            this.picks = res.data.getMyPicks;
            this.pick.playerId = this.filteredAvailablePlayers[0].id;
            this.logger.info(`Picks successfully listed`, res);
          })
          .catch((e) => {
            this.logger.error(`Error listing picks`, e)
          })
      },
      create() {
        var rank = 1;
        for (var r = 1; r <= 10; r++) {
          if (this.picks.filter(p => p.rank == r).length === 0) {
            rank = r;
            break;
          }
        }
        this.$Amplify.API.graphql(this.$Amplify.graphqlOperation(this.actions.create, {playerId: this.pick.playerId, overUnder: this.pick.overUnder, rank }))
          .then((res) => {
            this.logger.info(`Pick created`, res);
            this.listPicks();
          })
          .catch((e) => {
            this.logger.error(`Error creating Pick`, e)
          })
      },
      remove(playerId) {
        this.$Amplify.API.graphql(this.$Amplify.graphqlOperation(this.actions.delete, {playerId}))
          .then((res) => {
            this.logger.info(`Pick ${playerId} removed`, res);
            this.listPicks();
          })
          .catch((e) => {
            this.logger.error(`Error removing Pick ${playerId}`, e)
          })
      },
      moveup(playerId) {
        var pick = this.picks.find(p => p.playerId === playerId);
        this.$Amplify.API.graphql(this.$Amplify.graphqlOperation(this.actions.switch, { rank1: pick.rank, rank2: pick.rank - 1}))
          .then((res) => {
            this.logger.info(`Picks switched`, res);
            this.picks = res.data.switchPicks;
          })
          .catch((e) => {
            this.logger.error(`Error switching Picks`, e);
          })
      }
    }
  }
</script>

<style scoped="true">
  div.select, div.select > select {
    width: 100%;
  }
</style>
