import json
import lambdalogging
import boto3
import config

LOG = lambdalogging.getLogger(__name__)
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    """Lambda function handler."""
    """LOG.info('Received event: %s', event)"""
    
    for record in event['Records']:
        LOG.info('Received event: %s', record['body'])
        dynamodb.put_item(TableName=config.TABLE_NAME, Item={'Id':{'N':'0003'},'Source':{'S':'LambdaFunction'},'Message':{'S':record['body']}})

