const CreatePick = `mutation addPick($playerId: String!, $overUnder: String!, $rank: Int!) {
  addPick(playerId: $playerId, overUnder: $overUnder, rank: $rank ) {
    playerId
    overUnder
    rank
  }
}`;

const ListPicks = `query GetMyPicks {
  getMyPicks {
    playerId
    pickId
    rank
    overUnder
    createdAt
  }
}`

const DeletePick = `mutation RemovePick($playerId: String!) {
  removePick(playerId: $playerId){
    playerId
  }
}`;

const GetAvailablePlayers = `query GetAvailablePlayers {
  getAvailablePlayers {
    player {
      first_name
      last_name
      mlb
      fangraphs
      twitter_handle
    }
    id
    projectedyears
    projectedamount
    actualyears
    actualamount
  }
}`

export {
  CreatePick,
  ListPicks,
  DeletePick,
  GetAvailablePlayers
}
