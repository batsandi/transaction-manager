from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone


# base user model schema
class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)

# create schema incl. the unhashed pwd
class UserCreate(UserBase):
    password: str

# Database table model for the User.
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str

    # one-to-many relationship with Transaction
    transactions: list["Transaction"] = Relationship(back_populates="owner")

# For reading user data from the API (remove the password).
class UserRead(UserBase):
    id: int


# base transaction schema
class TransactionBase(SQLModel):
    beneficiary: str
    amount: float
    transaction_type: str
    status: str = "sent"

# For creating a new transaction
class TransactionCreate(TransactionBase):
    pass

# Schema for updating a transaction's status
class TransactionUpdate(SQLModel):
    status: str | None = None

# Database table model for the Transaction
class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    # Foreign key relationship to the User model.
    owner_id: int = Field(foreign_key="user.id")
    
    owner: User = Relationship(back_populates="transactions")

# API read schema
class TransactionRead(TransactionBase):
    id: int
    date: datetime
    owner_id: int