import uuid
from datetime import datetime

class Expense:
    def __init__(self, title: str, amount: float):
        """Initializes a new Expense instance with a unique ID and timestamps."""
        self.id = str(uuid.uuid4())  # Generate unique ID
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()  # Store creation timestamp
        self.updated_at = self.created_at  # Initially, updated_at = created_at

    def update(self, title: str = None, amount: float = None):
        """Updates the title and/or amount and refreshes the updated_at timestamp."""
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()  # Update timestamp

    def to_dict(self):
        """Returns a dictionary representation of the expense with currency format."""
        return {
            "id": self.id,
            "title": self.title,
            "amount": f"${self.amount:.2f}",  
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


    @staticmethod
    def validate_title(title):
        """Validates that the title is a non-empty string."""
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        return title.strip()

    @staticmethod
    def validate_amount(amount):
        """Validates that the amount is a positive float."""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a positive number.")
        return float(amount)
