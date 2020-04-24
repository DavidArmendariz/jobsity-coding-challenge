from app import db
from app.models import Chatroom, User
from sqlalchemy.exc import IntegrityError
import pytest


def test_chatroom_name_is_unique():
    """
    Test idea: 
    1. Create a chatroom called "Test chatroom" if it does not exist
    2. Try to add another one with the same name
    3. Check if IntegrityError is raised
    """
    chatroom = Chatroom(chatroom_name="Test chatroom")
    with pytest.raises(IntegrityError):
        db.session.add(chatroom)
        db.session.commit()
