import boto3

# Create an IAM client
iam = boto3.client('iam')

# Define the user name
user_name = "new-user123"

try:
    # Create the IAM user
    response = iam.create_user(UserName=user_name)
    print(f"IAM User '{user_name}' created successfully!")

except Exception as e:
    print(f"Error creating user: {e}")
