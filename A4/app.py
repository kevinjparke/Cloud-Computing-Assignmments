import json
import boto3
import os

conn_queue_url = 'https://sqs.us-east-1.amazonaws.com/638997125533/ConnectQueue'
sub_queue_url = 'https://sqs.us-east-1.amazonaws.com/638997125533/SubscribeQueue'
pub_queue_url = 'https://sqs.us-east-1.amazonaws.com/638997125533/PublishQueue'

sqs = boto3.client('sqs')


def lambda_handler(event, context):
    queue_type = event['type']
    response = {}

    if queue_type == "CONNECT":
        message = get_sqs_message(conn_queue_url)['Messages'][0]
        body = json.loads(message['Body'])
        response = make_conn_resp(body)
    elif queue_type == "PUBLISH":
        message = get_sqs_message(pub_queue_url)['Messages'][0]
        body = json.loads(message['Body'])
        response = make_pub_resp(body)
    else:
        message = get_sqs_message(sub_queue_url)['Messages'][0]
        body = json.loads(message['Body'])
        response = make_sub_resp(body)

    return response


def make_conn_resp(message):
    return {
        "type": "CONNACK",
        "returnCode": 0,
        "username": message['username'],
        "password": message['password']
    }


def make_pub_resp(message):
    return {
        "type": "PUBACK",
        "returnCode": 0,
        "payload": {
            "key": message['payload']['key'],
            "value": message['payload']['value']
        }
    }


def make_sub_resp(message):
    return {
        "type": "SUBACK",
        "returnCode": 0
    }


def get_sqs_message(url):
    message = sqs.receive_message(
        QueueUrl=url,
        MaxNumberOfMessages=1,
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    receipt_handle = message['Messages'][0]['ReceiptHandle']
    delete_sqs_message(url, receipt_handle)

    return message


def delete_sqs_message(url, receipt_handle):
    response = sqs.delete_message(
        QueueUrl=url,
        ReceiptHandle=receipt_handle
    )