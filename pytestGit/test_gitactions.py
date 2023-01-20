import pytest
import pandas as pd


def test_download_s3_objects(s3_connection):
    s3_resource=s3_connection
    bucket=s3_resource.Bucket("hands-on-bucket-2")
    objects = bucket.objects.all()
    for obj in objects:
       print(obj)

    