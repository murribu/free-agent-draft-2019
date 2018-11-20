import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

# event["playerId", "overUnder", "rank", "userId", "pickId"]
def lambda_handler(event, context):
  print(event)
  dynamo = boto3.resource('dynamodb')
  picks_table = dynamo.Table(os.environ["picks_table"])
  available_players_table = dynamo.Table(os.environ["available_players_table"])

  response = available_players_table.query(KeyConditionExpression=Key('id').eq(event["playerId"]))
  items = response['Items']
  return_error = {
    "playerId": "",
    "overUnder": "",
    "rank": 0,
    "userId": "",
    "pickId": ""
  }
  if len(items) > 0:
    if not 'signedAt' in items[0]:
      picks_table.put_item(Item=event)
      return event
    else:
      return_error["pickId"] = "This player has already signed a contract"
      return return_error
  return_error["pickId"] = "This player does not exist"
  return return_error
