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
  <div class="container">
    <section class="hero is-primary">
      <div class="hero-body">
        <p class="title">Effectively Wild</p>
        <p class="subtitle">Free Agent Draft 2019</p>
      </div>
    </section>
    <hr class="hr">
    <h1 class="title">
      The Game
    </h1>
    <div class="content">
      <p>
        How good are you at predicting the 2019 MLB Free Agent Landscape?
      </p>
      <p>
        Using <a href="https://www.mlbtraderumors.com/2018/11/mlb-free-agent-predictions-2019.html" target="_new">MLB Trade Rumors</a>'s predictions, <a href="/picks" @click.prevent="picks">choose</a> the over or under on 10 contract predictions. Rank your over/unders in order of your confidence.
      </p>
      <p>
        For example, if you take the under on Bryce Harper's 420M contract, and he ends up getting a 402M contract, you get 18 points multiplied by your confidence in your pick. First position equals 10 confidence points, second position equals 9, etc. So if you put Harper as your second pick, your score for that pick would be 18 * 9 = 162.
      </p>
      <p>
        You don't have to make 10 picks. If you get a pick wrong, you lose points.
      </p>
      <p>
        Once a player's contract is known, you cannot update a pick involving them anymore. This will be dependent on how quickly I can enter this information. Please don't try to cheat. There are no prizes for winning.
      </p>
    </div>
    <hr class="hr">
    <h1 class="title">
      Background
    </h1>
    <div class="content">
      <p>
        The idea came from <a href="https://www.fangraphs.com/blogs/effectively-wild-episode-1293-offseason-draft-day/">this Effectively Wild episode</a>. They did a simple draft, but I thought it'd be fun to have a larger-scale competition.
      </p>
    </div>

  </div>
</template>

<script>

export default {
  name: 'Home',
  data () {
    return {}
  },
  methods: {
    picks() {
      this.$router.push('/picks');
    }
  }
}
</script>
