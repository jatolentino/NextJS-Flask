import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='your-region')
table = dynamodb.Table('TextFiles')

def store_file(file_id, content):
    table.put_item(
        Item={
            'FileID': file_id,
            'Content': content
        }
    )

def retrieve_file(file_id):
    response = table.get_item(
        Key={
            'FileID': file_id
        }
    )
    return response['Item']['Content'] if 'Item' in response else None
