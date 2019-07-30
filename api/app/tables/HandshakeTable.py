import logging

from fastapi import HTTPException

from starlette.status import HTTP_409_CONFLICT

import sqlalchemy as sa
from sqlalchemy import Boolean, Column, DateTime, Integer, Unicode, Table, String, PickleType
from app.tables import dbMetadata

from asyncpg.exceptions import UniqueViolationError

# database connection
from app import db

from app.helpers import Password
from app.helpers import TableOp

from app.models.User import UserIn, UserNewIn

log = logging.getLogger(__name__)

table = Table(
    'handshake',
    dbMetadata,
    Column('user_id', Integer, primary_key=True),
    Column('type', String, nullable=False),
    Column('response', PickleType, nullable=False)
)
