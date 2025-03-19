import boto3

# Create an IAM client
iam = boto3.client('iam')

# List IAM users
response = iam.list_users()

# Print the list of users
print("IAM Users:")
for user in response['Users']:
    print(f"Username: {user['UserName']}, Created On: {user['CreateDate']}")
