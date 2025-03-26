from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

    @abstractmethod
    def close(self):
        pass


# Concrete Product 1: PostgreSQL
class PostgreSQL(Database):
    def connect(self):
        return "Connected to PostgreSQL"

    def execute_query(self, query):
        return f"Executing '{query}' on PostgreSQL"

    def close(self):
        return "PostgreSQL connection closed"


# Concrete Product 2: MySQL
class MySQL(Database):
    def connect(self):
        return "Connected to MySQL"

    def execute_query(self, query):
        return f"Executing '{query}' on MySQL"

    def close(self):
        return "MySQL connection closed"


# Concrete Product 3: MongoDB
class MongoDB(Database):
    def connect(self):
        return "Connected to MongoDB"

    def execute_query(self, query):
        return f"Executing '{query}' on MongoDB"

    def close(self):
        return "MongoDB connection closed"


# Abstract Factory
class DatabaseFactory(ABC):
    @abstractmethod
    def create_database(self):
        pass


# Concrete Factory for PostgreSQL
class PostgreSQLFactory(DatabaseFactory):
    def create_database(self):
        return PostgreSQL()


# Concrete Factory for MySQL
class MySQLFactory(DatabaseFactory):
    def create_database(self):
        return MySQL()


# Concrete Factory for MongoDB
class MongoDBFactory(DatabaseFactory):
    def create_database(self):
        return MongoDB()


# Client Code: Backend selecting a database dynamically
def get_database_factory(db_type):
    factories = {
        "postgresql": PostgreSQLFactory(),
        "mysql": MySQLFactory(),
        "mongodb": MongoDBFactory()
    }

    factory = factories.get(db_type)

    if not factory:
        raise ValueError("Unsupported database type")

    return factory


# Simulating environment configuration
db_type = input("Enter database type (postgresql/mysql/mongodb): ").strip().lower()

# Get the appropriate factory
factory = get_database_factory(db_type)

# Create a database instance
database = factory.create_database()

# Simulate database operations
print(database.connect())
print(database.execute_query("SELECT * FROM users"))
print(database.close())
