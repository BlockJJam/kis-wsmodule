import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

def get_env(name:str) -> str:
    return os.getenv(name)