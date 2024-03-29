from typing import List


class MySQLConnection:
    def execute(self, query: str) -> List[str]:
        return [f"MySQL executou a query `{query}`"]


class MySQLDatabase:
    def connect(self, connection_url: str) -> MySQLConnection:
        if connection_url == "":
            raise ValueError("Invalid connection")
        return MySQLConnection()
