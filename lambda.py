#this lambda function is useful to storage dynamodb to s3 automatic

import boto3
import json
import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            new_data = record['dynamodb']['NewImage']
            
            # Convert DynamoDB JSON format to regular dict
            feedback = {k: list(v.values())[0] for k, v in new_data.items()}
            
            now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"feedback_{feedback.get('id', 'noid')}_{now}.json"
            
            s3.put_object(
                Bucket='cloudwithvivek-feedback-backup',
                Key=file_name,
                Body=json.dumps(feedback, indent=2)
            )
    
    return {
        'statusCode': 200,
        'body': 'Feedback backed up to S3'
    }
