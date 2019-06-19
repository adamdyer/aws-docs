import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1'
            }
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True

create_bucket("uniquename")
