import boto3

# Define bucket name (must be globally unique)
bucket_name = "my-unique-bucket-name-8884960"  # Change this to a unique name

# Create an S3 client
s3 = boto3.client('s3')

# Create the S3 bucket
try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}  # Change region if needed
    )
    print(f"S3 Bucket '{bucket_name}' created successfully!")
except Exception as e:
    print(f"Error creating bucket: {e}")
