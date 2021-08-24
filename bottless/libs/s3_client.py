import boto3


class S3Client:
    BUCKET = "dean-insta-clone"
    REGION = "ap-northeast-2"

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
