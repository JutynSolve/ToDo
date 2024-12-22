import datetime

import pytest
from uuid import UUID
from freezegun import freeze_time
from unittest.mock import patch

from core.todos.create_todo import init_todo


def test_create_basic_valid_todo():
    mock_uuid = UUID("a404473b-1b00-436b-bc1a-6a4716a3e0ee")

    with freeze_time("2024-12-12"), patch("uuid.uuid4", return_value=mock_uuid):
        todo = init_todo(name="learn flask")

        assert todo == {
            "name": "learn flask",
            "status": "pending",
            "id": mock_uuid,
            "created_at": datetime.datetime(2024, 12, 12)
        }


def test_create_todo_with_empty_name():
    with pytest.raises(ValueError, match="Task name is required"):
        init_todo(name="")


def test_create_todo_invalid_name():
    with pytest.raises(ValueError, match="Task name is required"):
        init_todo(name=" ")


@pytest.mark.skip(reason="Not implemented yet")
def test_create_todo_with_all_options():
    with freeze_time("2024-12-12"):
        datetime_start = datetime.datetime.now() + datetime.timedelta(days=1)
        data = {
            "name": "learn flask",
            "description": "from video",
            "start_dt": datetime_start,
            "duration": datetime.timedelta(minutes=10),
            "estimated_duration": datetime.timedelta(minutes=10),
            "type": "workshop",
            "priority": "critical",
        }

        todo = init_todo(**data)

        assert todo == {
            **data,
            "id": 1,
            "status": "pending",
            "created_at": datetime.datetime(2024, 12, 12),
        }


def test_create_todo_with_past_start_date():
    pass


def test_create_todo_with_non_positive_duration():
    pass


def test_create_todo_with_non_positive_estimated_duration():
    pass
