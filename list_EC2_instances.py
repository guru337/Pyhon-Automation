import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# List all EC2 instances
response = ec2.describe_instances()

print("EC2 Instances:")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}, Type: {instance['InstanceType']}, Public IP: {instance.get('PublicIpAddress', 'N/A')}")
