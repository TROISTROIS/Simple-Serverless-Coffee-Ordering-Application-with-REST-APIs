import json
import boto3

sqs = boto3.client('sqs')
queue_url = "YOUR-QUEUE-URL"

def lambda_handler(event, context):
    # TODO implement
    try:
        print(event)
        order_details = json.loads(event['body'])
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(order_details))
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"},
            'body': json.dumps({'message': 'Order submitted to queue successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'Error': str(e)})
        }

# {"body": "{\"productName\": \"Test Product 3\", \"quantity\": 1}"} 
#  aws lambda invoke --function-name submit-order-coffee-shop --payload fileb://input.json output.json --profile IAMAdmin-GEN