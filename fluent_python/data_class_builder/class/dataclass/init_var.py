from dataclasses import dataclass, InitVar
from typing import Optional

class DatabaseType:
    def lookup(self, key: str) -> Optional[int]:
        # Simulate a lookup from a database
        return 42 if key == 'j' else None

# Assume this is your external database instance
my_database = DatabaseType()

@dataclass
class C:
    i: int
    j: Optional[int] = None
    database: InitVar[DatabaseType] = None  # This is an init-only variable

    def __post_init__(self, database: DatabaseType):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

# Create an instance of C, passing the database for initialization
c = C(10, database=my_database)

print(c)  # C(i=10, j=42)
