import os
from os import environ as env
from pathlib import Path

STAGE = env.get("STAGE", "development")
ROOT_PATH = Path(__file__).parent.parent
ENV_PATH = os.path.join(ROOT_PATH, ".envs", f".env.{STAGE}")

SERVER_HOST = env.get("SERVER_HOST", "127.0.0.1")
SERVER_PORT = env.get("SERVER_PORT", 8080)
DEBUG = env.get("DEBUG", True)
