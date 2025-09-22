from fastapi import FastAPI, Depends, HTTPException
from openai import models
from sqlalchemy.orm import Session
from app import schemas, crud, services, models
from app.database import get_db, engine
from app.models import Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8501",
    "http://localhost:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/generate", response_model=schemas.ContentResponse)
def generate_content(request: schemas.ContentRequest, db:Session=Depends(get_db)):
    try:
        generated_text = services.generate_content(
            prompt=request.prompt,
            platform=request.platform,
            tone = request.tone,
            content_type=request.content_type
        )
        db_content = crud.create_generated_content(db, request, generated_text)
        return db_content
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate/{content_id}", response_model=schemas.ContentResponse)
def read_content(content_id:int, db:Session=Depends(get_db)):
    db_content = db.query(models.GeneratedContent).get(content_id)
    if db_content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_content
