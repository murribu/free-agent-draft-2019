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
    availablePlayer {
      player {
        first_name
        last_name
      }
      projectedamount
      projectedyears
      actualyears
      actualamount
      signedAt
    }
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
    signedAt
  }
}`

const SwitchPicks = `mutation SwitchPicks ($rank1: Int!, $rank2: Int!) {
  switchPicks (rank1: $rank1, rank2: $rank2) {
    playerId
    pickId
    rank
    overUnder
    createdAt
    availablePlayer {
      player {
        first_name
        last_name
      }
      projectedamount
      projectedyears
      actualyears
      actualamount
      signedAt
    }
  }
}`;

export {
  CreatePick,
  ListPicks,
  DeletePick,
  GetAvailablePlayers,
  SwitchPicks
}
