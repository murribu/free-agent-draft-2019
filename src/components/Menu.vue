/*
 * Copyright 2017-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with
 * the License. A copy of the License is located at
 *
 *     http://aws.amazon.com/apache2.0/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 * CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions
 * and limitations under the License.
 */

<template>
  <div class="navbar is-info" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" v-on:click="home">Home</a>
      <a role="button" class="navbar-burger" :class="{'is-active': expanded}" aria-label="menu" aria-expanded="false" @click.prevent="expanded = !expanded">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div class="navbar-menu" :class="{'is-active': expanded}">
      <div class="navbar-start">
        <a class="navbar-item" v-on:click="picks">Picks</a>
        <a class="navbar-item" v-on:click="actuals">Actuals</a>
        <a class="navbar-item" v-on:click="leaderboard">Leaderboard</a>
      </div>
      <div class="navbar-end">
        <a class="navbar-item" v-on:click="profile" v-if="user">Profile</a>
        <amplify-sign-out v-if="user"></amplify-sign-out>
      </div>
    </div>
  </div>
</template>

<script>
import { Auth, Hub } from 'aws-amplify';
import AmplifyStore from '../store/store';


export default {
  name: 'Menu',
  data () {
    return {
      expanded: false
    }
  },
  computed: {
    user() {
      return AmplifyStore.state.user
    }
  },
  methods: {
    home: function() {
        this.$router.push('/')
    },
    picks: function() {
        this.$router.push('/picks')
    },
    actuals: function() {
        this.$router.push('/actuals')
    },
    leaderboard: function() {
        this.$router.push('/leaderboard')
    },
    profile: function() {
        this.$router.push('/profile')
    },
    signOut: function() {
        this.$router.push('/auth/signOut')
    }
  }
}
</script>
