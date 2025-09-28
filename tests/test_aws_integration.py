# tests/test_aws_integration.py
import boto3
from moto import mock_aws
from aws.aws_integration import ensure_s3_bucket, ensure_sns_topic

@mock_aws
def test_ensure_s3_bucket():
    region = "us-east-1"
    bucket = "cloudmind-test-bucket-12345"
    ensure_s3_bucket(bucket, region)
    s3 = boto3.client("s3", region_name=region)
    s3.head_bucket(Bucket=bucket)

@mock_aws
def test_ensure_sns_topic():
    region = "us-east-1"
    arn = ensure_sns_topic("cloudmind-test-topic", region)
    assert arn.startswith("arn:aws:sns")
