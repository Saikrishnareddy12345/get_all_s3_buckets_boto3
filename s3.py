import boto3
s3 = boto3.resource('s3')
client=boto3.client('s3')
for bucket in s3.buckets.all():
    # print(bucket.name)
    def get_location(client, bucket_name):
        response = client.get_bucket_location(Bucket=bucket_name)
        if response['LocationConstraint'] == "us-east-1" or response['LocationConstraint'] =='us-east-2' \
            or response['LocationConstraint'] =="us-west-1":
            print("BucketName=",bucket.name,"|","Region=",response['LocationConstraint'])
    
    get_location(client,bucket_name=bucket.name)
