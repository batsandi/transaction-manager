from sqlmodel import Session, select
from app.core.security import get_password_hash
from app.models import TransactionUpdate, User, UserCreate, Transaction, TransactionCreate

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

def get_transaction_by_id(db: Session, transaction_id: int) -> Transaction | None:
    """
    Fetches a single transaction by its ID.
    """
    return db.get(Transaction, transaction_id)


def get_transactions_by_owner(db: Session, owner_id: int) -> list[Transaction]:
    """
    Fetches all transactions for a specific owner.
    """
    statement = select(Transaction).where(Transaction.owner_id == owner_id)
    return db.exec(statement).all()


def create_transaction(db: Session, transaction: TransactionCreate, owner_id: int) -> Transaction:
    """
    Creates a new transaction linked to an owner.
    """
    # Create a new Transaction object from the input schema and owner_id
    db_transaction = Transaction(**transaction.model_dump(), owner_id=owner_id)
    
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def update_transaction_status(db: Session, db_transaction: Transaction, transaction_in: TransactionUpdate) -> Transaction:
    """
    Updates the status of an existing transaction.
    """
    # Get the new data from the input model
    update_data = transaction_in.model_dump(exclude_unset=True)

    # Update the status field on the existing database object
    db_transaction.status = update_data["status"]
    
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction