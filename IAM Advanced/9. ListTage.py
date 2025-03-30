import boto3

iam_client = boto3.client('iam')

response = iam_client.list_users()

for user in response['Users']:
    user_name = user['UserName']
    tags = iam_client.list_user_tags(UserName=user_name)['Tags']
    print(f"User : {user}, Tags : {tags}")