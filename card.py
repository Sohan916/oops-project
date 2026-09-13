from datetime import datetime, timezone

from utils import new_id


class Card:
    def __init__(self, title: str, description: str) -> None:
        self.id = new_id()
        self.title = title
        self.description = description
        self.created_at = datetime.now(tz=timezone.utc)
