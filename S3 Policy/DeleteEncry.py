import boto3


def delete_encryption():

    s3_client = boto3.client('s3')
    response = s3_client.delete_bucket_encryption(Bucket='parwizforogh-12')
    print(response)



delete_encryption()