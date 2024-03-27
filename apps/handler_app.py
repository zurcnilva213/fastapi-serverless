import os

from src.bot.sqs_processor import SQSProcessor

queue_url = os.environ.get('QUEUE_URL')


def lambda_handler(event, context):
    for record in event['Records']:
        message_body = record['body']
        processor = SQSProcessor(body=message_body)
        processor.run()
    return {
        'statusCode': 200,
        'body': 'result'
    }