import os

from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")
