import json
import boto3
import base64
import uuid

s3 = boto3.client('s3')
ses = boto3.client('ses', region_name='us-east-1')
BUCKET = 'khushi-file-share-bucket'
SENDER = 'khushidm2003@gmail.com'

def lambda_handler(event, context):
    # Handle CORS preflight for REST API (method is in event['httpMethod'], not nested)
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'message': 'CORS preflight passed'})
        }

    try:
        body = json.loads(event['body'])
        file_data = base64.b64decode(body['fileContent'])
        file_name = f"{uuid.uuid4()}_{body['fileName']}"
        recipient = body['recipientEmail']

        # Upload file to S3
        s3.put_object(Bucket=BUCKET, Key=file_name, Body=file_data)

        # Generate a signed download URL
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET, 'Key': file_name},
            ExpiresIn=300  # Link valid for 5 minutes
        )

        # Send email using SES
        ses.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [recipient]},
            Message={
                'Subject': {'Data': 'Your File Download Link'},
                'Body': {'Text': {'Data': f'Here is your download link (valid for 5 mins):\n{url}'}}
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'message': 'Email sent!'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'error': str(e)})
        }