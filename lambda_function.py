import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from the backend API!')
    }
# Convert to zip --> zip lambda_function.zip lambda_function.py
