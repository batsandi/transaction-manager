from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app import crud
from app.models import TransactionCreate, TransactionRead, TransactionUpdate, User
from app.database import get_db
from app.api.deps import get_current_active_user

router = APIRouter()


@router.post("/", response_model=TransactionRead, status_code=status.HTTP_201_CREATED)
def create_transaction(
    *,
    db: Session = Depends(get_db),
    transaction_in: TransactionCreate,
    current_user: User = Depends(get_current_active_user)
):
    """
    Create new transaction.
    """
    transaction = crud.create_transaction(db=db, transaction=transaction_in, owner_id=current_user.id)
    return transaction


@router.get("/", response_model=list[TransactionRead])
def read_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieve all transactions for the current user.
    """
    transactions = crud.get_transactions_by_owner(db=db, owner_id=current_user.id)
    return transactions


@router.get("/{transaction_id}", response_model=TransactionRead)
def read_transaction_by_id(
    *,
    db: Session = Depends(get_db),
    transaction_id: int,
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieve a specific transaction by its ID.
    """
    db_transaction = crud.get_transaction_by_id(db=db, transaction_id=transaction_id)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if db_transaction.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    return db_transaction


@router.put("/{transaction_id}", response_model=TransactionRead)
def update_transaction(
    *,
    db: Session = Depends(get_db),
    transaction_id: int,
    transaction_in: TransactionUpdate,
    current_user: User = Depends(get_current_active_user)
):
    """
    Update a transaction's status.
    """
    print(f' {'#'*10} updating transaction {transaction_id} with data: {transaction_in}')
    db_transaction = crud.get_transaction_by_id(db=db, transaction_id=transaction_id)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if db_transaction.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    transaction = crud.update_transaction_status(db=db, db_transaction=db_transaction, transaction_in=transaction_in)
    return transaction
