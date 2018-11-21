import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

# event["userId", "rank1", "rank2", "createdAt"]
def lambda_handler(event, context):
  print(event)
  dynamo = boto3.resource('dynamodb')
  picks_table = dynamo.Table(os.environ["picks_table"])
  available_players_table = dynamo.Table(os.environ["available_players_table"])
  return_error = {
    "playerId": "",
    "overUnder": "",
    "rank": 0,
    "userId": "",
    "pickId": ""
  }

  print('userId', event["userId"])
  response = picks_table.query(KeyConditionExpression=Key('userId').eq(event["userId"]))

  print('response items', response['Items'])

  picks_to_switch = [a for a in response['Items'] if int(a["rank"]) == int(event["rank1"]) or int(a["rank"]) == int(event["rank2"])]

  for pick in picks_to_switch:
    response = available_players_table.query(KeyConditionExpression=Key('id').eq(pick["playerId"]))
    items = response['Items']
    if len(items) > 0:
      if 'signedAt' in items[0]:
        return_error["pickId"] = items[0]["first_name"] + " " + items[0]["last_name"] + " has already signed a contract"
        return [return_error]
    else:
      return_error["pickId"] = pick["playerId"] + " does not exist"
      return [return_error]

  print('picks_to_switch', picks_to_switch)

  if (len(picks_to_switch) == 2):
    picks_table.update_item(
      Key={ 'playerId': picks_to_switch[0]["playerId"], 'userId': event["userId"] },
      UpdateExpression='Set #rank = :rank, createdAt = :createdAt',
      ExpressionAttributeNames = { "#rank": "rank" },
      ExpressionAttributeValues={':rank': int(picks_to_switch[1]["rank"]), ':createdAt': event["createdAt"]}
    )
    picks_table.update_item(
      Key={ 'playerId': picks_to_switch[1]["playerId"], 'userId': event["userId"] },
      UpdateExpression='Set #rank = :rank, createdAt = :createdAt',
      ExpressionAttributeNames = { "#rank": "rank" },
      ExpressionAttributeValues={':rank': int(picks_to_switch[0]["rank"]), ':createdAt': event["createdAt"]}
    )
  elif (len(picks_to_switch) == 1):
    new_rank = event["rank1"]
    if picks_to_switch[0]["rank"] == new_rank:
      new_rank = event["rank2"]

    picks_table.update_item(
      Key={ 'playerId': picks_to_switch[0]["playerId"], 'userId': event["userId"] },
      UpdateExpression='Set #rank = :rank, createdAt = :createdAt',
      ExpressionAttributeNames = { "#rank": "rank" },
      ExpressionAttributeValues={':rank': new_rank, ':createdAt': event["createdAt"]}
    )

  response = picks_table.query(KeyConditionExpression=Key('userId').eq(event["userId"]))

  return response["Items"]
