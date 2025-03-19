import boto3
import secrets
import string

# Generate a random password
def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

# Initialize IAM client
iam = boto3.client('iam')

# IAM Username
user_name = "TestUser"  # Change to the actual username

# Generate new password
new_password = generate_password()

try:
    # Update IAM user password
    iam.update_login_profile(UserName=user_name, Password=new_password, PasswordResetRequired=True)
    print(f"Password for IAM user '{user_name}' has been rotated successfully!")
    print(f"New Password: {new_password}")  # ⚠️ Securely store this instead of printing it

except Exception as e:
    print(f"Error rotating password: {e}")
