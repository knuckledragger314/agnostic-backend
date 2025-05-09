# import boto3
# from botocore.exceptions import ClientError
print("Hello from trivia-backend")

# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/



def handler(event, context):
    print("Received event:", event)
    return {
        "statusCode": 200,
        "body": "Hello from Lambda!"
    }


# def get_secret():
#
#     secret_name = "chaz/access"
#     region_name = "us-east-1"
#
#     # Create a Secrets Manager client
#     session = boto3.session.Session()
#     client = session.client(
#         service_name='secretsmanager',
#         region_name=region_name
#     )
#
#     try:
#         get_secret_value_response = client.get_secret_value(
#             SecretId=secret_name
#         )
#     except ClientError as e:
#         # For a list of exceptions thrown, see
#         # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
#         raise e
#
#     secret = get_secret_value_response['SecretString']
#
#     # Your code goes here.
