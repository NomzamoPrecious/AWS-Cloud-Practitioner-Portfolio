import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

import json
import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        name = body.get('name', 'No Name')
        email = body.get('email', 'No Email')
        message = body.get('message', 'No Message')

        # Send email via SES
        ses.send_email(
            Source='nomzamopreciousdhlamini@gmail.com',          # Sender
            Destination={'ToAddresses': ['nomzamopreciousdhlamini@gmail.com']},  # Receiver
            Message={
                'Subject': {'Data': f'New Message from {name}'},
                'Body': {'Text': {'Data': f"Email: {email}\nMessage: {message}"}}
            }
        )

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'},
            'body': json.dumps({'message': 'Message sent successfully!'})
        }

    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Failed to send message. Please try again.'})
        }