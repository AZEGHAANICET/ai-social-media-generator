from sqlalchemy.orm import Session
from app import models, schemas


def create_generated_content(db:Session, content: schemas.ContentRequest, generated_text: str):


    db_content = models.GeneratedContent(
        platform=content.platform,
        tone = content.tone,
        content_type=content.content_type,
        generated_text = generated_text,
        prompt = content.prompt,
    )

    db.add(db_content)
    db.commit()
    db.refresh(db_content)

    return db_content