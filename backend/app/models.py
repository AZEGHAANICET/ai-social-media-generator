from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class GeneratedContent(Base):
    __tablename__ = "generated_content"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String, index=True)
    tone = Column(String)
    prompt = Column(Text, nullable=False)
    content_type = Column(String)
    generated_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
