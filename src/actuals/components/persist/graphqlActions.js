const GetSignedPlayers = `query GetSignedPlayers {
  getSignedPlayers {
    player {
      first_name
      last_name
      mlb
      fangraphs
      bbref
      rotoworld
      espn
      yahoo
      twitter_handle
      fantrax
    }
    id
    projectedyears
    projectedamount
    actualyears
    actualamount
    signedAt
  }
}`

export {
  GetSignedPlayers
}
