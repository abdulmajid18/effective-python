from abc import ABC, abstractmethod


# Abstract Database Product
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


# Abstract Cache Product
class Cache(ABC):
    @abstractmethod
    def store(self, key, value):
        pass


# Concrete Database Implementations
class PostgreSQL(Database):
    def connect(self):
        return "Connected to PostgreSQL"


class MySQL(Database):
    def connect(self):
        return "Connected to MySQL"


# Concrete Cache Implementations
class Redis(Cache):
    def store(self, key, value):
        return f"Stored {key}: {value} in Redis"


class Memcached(Cache):
    def store(self, key, value):
        return f"Stored {key}: {value} in Memcached"


# Abstract Factory with Lazy Initialization
class BackendFactory(ABC):
    def __init__(self):
        self._database = None  # Placeholder for lazy initialization
        self._cache = None  # Placeholder for lazy initialization

    @abstractmethod
    def create_database(self):
        pass

    @abstractmethod
    def create_cache(self):
        pass


# Concrete Factory 1: PostgreSQL + Redis
class PostgreSQLRedisFactory(BackendFactory):
    def create_database(self):
        if self._database is None:  # Lazy initialization
            print("Creating PostgreSQL instance...")
            self._database = PostgreSQL()
        return self._database

    def create_cache(self):
        if self._cache is None:  # Lazy initialization
            print("Creating Redis instance...")
            self._cache = Redis()
        return self._cache


# Concrete Factory 2: MySQL + Memcached
class MySQLMemcachedFactory(BackendFactory):
    def create_database(self):
        if self._database is None:  # Lazy initialization
            print("Creating MySQL instance...")
            self._database = MySQL()
        return self._database

    def create_cache(self):
        if self._cache is None:  # Lazy initialization
            print("Creating Memcached instance...")
            self._cache = Memcached()
        return self._cache


# Function to select the correct factory
def get_backend_factory(service_type):
    factories = {
        "postgresql_redis": PostgreSQLRedisFactory(),
        "mysql_memcached": MySQLMemcachedFactory()
    }

    factory = factories.get(service_type)
    if not factory:
        raise ValueError("Unsupported backend configuration")

    return factory


# Client Code
if __name__ == "__main__":
    service_type = input("Enter backend type (postgresql_redis/mysql_memcached): ").strip().lower()

    # Get the correct factory
    factory = get_backend_factory(service_type)

    # Lazy Initialization in Action
    print("\n--- Only creating database now ---")
    db = factory.create_database()
    print(db.connect())

    print("\n--- Only creating cache now ---")
    cache = factory.create_cache()
    print(cache.store("session_id", "abc123"))
