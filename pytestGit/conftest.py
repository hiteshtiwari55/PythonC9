import pytest
import boto3
import os
#from config import config 

"""
ACCESS_KEY=config.ACCESS_KEY
SECRET_KEY=config.SECRET_KEY
AWS_REGION=config.AWS_REGION

ACCESS_KEY=os.environ['ACCESS_KEY']
SECRET_KEY=os.environ['SECRET_KEY']
AWS_REGION="eu-west-2"
"""
@pytest.fixture
def get_aws_sts_assume_role_credentials():
    sts_client = boto3.client("sts")
    aws_assume_role_arn = os.environ['AWS_ASSUME_ROLE_ARN']
    print(aws_assume_role_arn)
    
    credentials = sts_client.assume_role(
        RoleArn="aws_assume_role_arn", RoleSessionName="MySessionName", DurationSeconds=3600)

    return credentials["Credentials"]

@pytest.fixture
def test_setup():
    return 'Hell!! First one Pre-Requisite'

@pytest.fixture
def s3_connection(get_aws_sts_assume_role_credentials):
    credentials = get_aws_sts_assume_role_credentials
    AWS_REGION="eu-west-2"
    s3_resource=boto3.resource("s3",aws_access_key_id=credentials["AccessKeyId"],
    aws_secret_access_key=credentials["SecretAccessKey"],
    aws_session_token=credentials["SessionToken"],
    region_name=AWS_REGION)
    return s3_resource
