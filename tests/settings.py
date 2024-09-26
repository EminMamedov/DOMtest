import os
from dotenv import load_dotenv
from pathlib import Path

ENV_PATH = Path(__file__).parent.parent.parent / "env"

load_dotenv(ENV_PATH / ".env-local-dev-stand")

API_URL = os.getenv('API_URL_PETSTORE')

