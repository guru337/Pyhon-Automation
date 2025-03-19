import boto3

# Create an EC2 resource
ec2 = boto3.resource('ec2')

# Define EC2 instance parameters
instances = ec2.create_instances(
    ImageId='ami-00bb6a80f01f03502',  # Replace with a valid AMI ID
    InstanceType='t2.micro',          # Instance type
    KeyName='ubuntu key pair',          # Replace with your key pair name
    MinCount=1,
    MaxCount=1,
)

# Print instance ID
print(f"EC2 Instance {instances[0].id} created successfully!")
