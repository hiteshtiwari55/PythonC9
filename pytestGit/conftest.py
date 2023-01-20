import pytest
import boto3
import os
#from config import config 

"""
ACCESS_KEY=config.ACCESS_KEY
SECRET_KEY=config.SECRET_KEY
AWS_REGION=config.AWS_REGION
"""
ACCESS_KEY=os.environ['ACCESS_KEY']
SECRET_KEY=os.environ['SECRET_KEY']
AWS_REGION="eu-west-2"


@pytest.fixture
def test_setup():
    return 'Hell!! First one Pre-Requisite'

@pytest.fixture
def s3_connection():
    s3_resource=boto3.resource("s3",aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,
                               region_name=AWS_REGION)
    return s3_resource