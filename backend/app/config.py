import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://azegha:Azegha2002#@db:5432/social_media_db")
