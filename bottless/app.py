from bottle import run, default_app

from bottless.libs.s3_client import S3Client

app = default_app()

FAKE_DATA = {
    "username": "qlqldldh",
    "posts_count": 111,
    "followers_count": 99,
    "followings_count": 99,
    "description": "hello world",
}

@app.route("/profile", method=["GET"])
def profile():
    s3_client = S3Client()
    profile_img = s3_client.get_profile_img(username="dean")
    profile_data = FAKE_DATA
    profile_data.update({"profile_img": profile_img})

    return profile_data


if __name__ == "__main__":
    # TODO: implements REST API with bottle framework
    # TODO: deploy to AWS Lambda (Serverless) with zappa
    from bottless.config import ENV_PATH
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=ENV_PATH)

    run(app=app, host="localhost", port=8080, debug=True)
