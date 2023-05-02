import json

def lambda_handler(event, context):
    input_json = json.loads(event["input"])
    return input_json
