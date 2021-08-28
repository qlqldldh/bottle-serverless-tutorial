import boto3
from os import environ as env


class S3Client:
    BUCKET = str(env.get("AWS_S3_BUCKET"))
    REGION = env.get("AWS_REGION")

    def __init__(self):
        self.__s3_client = boto3.client(
            service_name="s3",
            region_name=self.REGION,
        )

    def get_profile_img(self, username):
        key = f"{username}/profile/{username}_profile.jpg"
        url = self.__s3_client.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": self.BUCKET,
                "Key": key,
            },
        )

        return url
