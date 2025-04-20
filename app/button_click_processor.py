
def handler(event, context):
    print("Button click event received:", event)
    return {
        "statusCode": 200,
        "body": "Button click recorded!"
    }
