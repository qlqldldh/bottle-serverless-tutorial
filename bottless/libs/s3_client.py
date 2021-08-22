import boto3
from os import environ as env


class S3Client:
    BUCKET = "dean-insta-clone"
    REGION = "ap-northeast-2"
    AWS_ACCESS_KEY = env.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env.get("AWS_SECRET_ACCESS_KEY")

    def __init__(self):
        self.__s3_client = boto3.client(
            service_name="s3",
            aws_access_key_id=self.AWS_ACCESS_KEY,
            aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
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
