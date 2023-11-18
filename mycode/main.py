import boto3

# Replace these values with your own AWS credentials
aws_access_key = '****ACCESS_KEY****'
aws_secret_key = '****SECRET_KEY****'
region_name = 'us-west-1'  # e.g., 'us-west-1'

print("running code now.")

# Initialize the S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region_name)

# File to upload
file_name = 'your_image.jpg'  
bucket_name = 'my-first-aws-bucket' 

# Upload file to the specified bucket
try:
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"{file_name} uploaded successfully to {bucket_name}")
except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# Now, download this file under a new name
try:
    s3.download_file(bucket_name,file_name,"same_image.jpg")
    print(f"{file_name} downloaded successfully from {bucket_name}")
except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Finally, cleanup your container - delete the file that was uploaded
try:
    s3.delete_object(Bucket=bucket_name,Key=file_name)
    print(f"{file_name} deleted successfully from {bucket_name}")
except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

