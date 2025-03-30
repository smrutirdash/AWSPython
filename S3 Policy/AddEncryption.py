import boto3


def set_encryption():

    s3_client = boto3.client('s3')

    response = s3_client.put_bucket_encryption(
        Bucket="parwizforogh-12",
        ServerSideEncryptionConfiguration={
            "Rules":[
                {"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm" : "AES256"}}
            ]
        }
    )

    print(response)



set_encryption()