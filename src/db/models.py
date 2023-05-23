import uuid

from sqlalchemy import Column, String, UUID, ForeignKey

from .db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    access_token = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)


class Audio(Base):
    __tablename__ = 'audios'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    path_to_file = Column(String(255))
    filename = Column(String(155), nullable=False)
