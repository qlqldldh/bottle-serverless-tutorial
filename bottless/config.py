import os
from os import environ as env
from pathlib import Path

STAGE = env.get("STAGE", "development")
ROOT_PATH = Path(__file__).parent.parent
ENV_PATH = os.path.join(ROOT_PATH, ".envs", f".env.{STAGE}")
