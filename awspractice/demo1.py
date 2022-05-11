import boto3
client=boto3.client('s3')
s3=boto3.resource('s3')
# bucket=s3.create_bucket(Bucket='jimmybuck1',CreateBucketConfiguration={
#     'LocationConstraint':'ap-south-1'
# })

# FILE UPLOAD TO BUCKET:----
s3.meta.client.upload_file('S:\Aroha_tech\python\python_assignment\mock1.py','jimmybuck1','demo1.py')