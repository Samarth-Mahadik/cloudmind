# tests/test_boto.py
import boto3
from moto import mock_aws  # updated import for new Moto versions

@mock_aws
def test_get_caller_identity_mocked():
    sts = boto3.client("sts", region_name="us-east-1")
    identity = sts.get_caller_identity()
    
    # Basic assertions
    assert "Account" in identity
    assert identity["Account"] is not None
