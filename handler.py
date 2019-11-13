import json
import requests

def main(event, context):
    r = requests.get("https://www.google.com")
    if r.status_code == 200:
        response = {
            'statusCode': 200,
            'body': json.dumps('Hello from Google!'),
            # 'event': json.dumps(event),
            # 'context_func_name': json.dumps(context.function_name)
        }
    else:
        response = {
            'statusCode': 500,
            'body': json.dumps('Something went wrong!'),
        }
    print(response)
    return response

if __name__ == "__main__":
    main('', '')