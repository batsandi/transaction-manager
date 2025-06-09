from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from datetime import timedelta
from pydantic import BaseModel

from app import crud
from app.models import UserCreate, UserRead
from app.core import security
from app.database import get_db
from app.core.config import settings

class Token(BaseModel):
    access_token: str
    token_type: str

# new router for authentication-related endpoints
router = APIRouter()

@router.post("/users/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_new_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user in the system.
    """
    # Check if a user with this username already exists
    user = crud.get_user_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="A user with this username already exists.",
        )

    new_user = crud.create_user(db=db, user=user_in)
    return new_user

@router.post("/login/access-token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """
    Authenticate a user with username and password, and return a JWT access token.
    """
    user = crud.get_user_by_username(db, username=form_data.username)
    
    # Check if user exists and the password is correct
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # If credentials are valid, create an access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}