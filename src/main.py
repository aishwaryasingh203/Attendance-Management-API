from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

# Import from 'src' directly, not 'Submission.src'
from src.database import engine, get_db
from src import models, schemas
from src.hashing import Hash

# Database tables create karna
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Password limit safety
    safe_password = user.password[:72]
    hashed_password = Hash.bcrypt(safe_password)
    
    new_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
        institution_id=user.institution_id
    )
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User created successfully!", "user_id": new_user.id}
    except IntegrityError:
        db.rollback() 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered. Try a different one."
        )

@app.get("/users/", response_model=list[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users