import datetime
from typing import Any

import uuid


def init_todo(name: str) -> dict[str, str | uuid.UUID | datetime.datetime]:
    """
    Initialize a new to-do task with the given name. The provided name will be
    processed to remove leading and trailing spaces. The task will be assigned a
    default status of "pending", a unique identifier, and a timestamp indicating
    its creation time.

    :param name: The name of the to-do task. Must be a non-empty string.
    :type name: str
    :raises ValueError: If the provided name is an empty string after trimming.
    :return: A dictionary containing the task's name, status, unique ID, and
        creation timestamp.
    :rtype: dict[str, str | uuid.UUID | datetime.datetime]
    """
    cleaned_name: str = name.strip()

    if cleaned_name == "":
        raise ValueError("Task name is required")

    return {
        "name": name,
        "status": "pending",
        "id": uuid.uuid4(),
        "created_at": datetime.datetime.now(),
    }
