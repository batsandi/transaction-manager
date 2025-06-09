from sqlmodel import Session, select
from app.core.security import get_password_hash
from app.models import User, UserCreate

def get_user_by_username(db: Session, username: str) -> User | None:
    """
    Fetches a single user from the database by their username.
    """
    statement = select(User).where(User.username == username)
    return db.exec(statement).first()


def create_user(db: Session, user: UserCreate) -> User:
    """
    Creates a new user in the database.
    """
    # Hash the user's plain-text password before storing it.
    hashed_password = get_password_hash(user.password)

    db_user = User(
        **user.model_dump(exclude={"password"}), 
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

