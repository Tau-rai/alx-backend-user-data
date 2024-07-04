#!/usr/bin/env python3
"""Module for filtering sensitive data"""


from typing import List
import re
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


# database credentials
DB_NAME = os.getenv("PERSONAL_DATA_DB_NAME")
DB_USERNAME = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
DB_PASSWORD = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
DB_HOST = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")


PII_FIELDS = (
    "name", "email", "phone_number", "address", "social_security_number")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
            ) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records"""
        format_message = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, format_message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    user_data = logging.getLogger()
    user_data.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    user_data.addHandler(handler)
    return user_data


def get_db() -> MySQLConnection:
    """Returns a database connection"""
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection


# Configure logging
logging.basicConfig(level=logging.INFO, format='[HOLBERTON] user_data INFO %(asctime)s: %(message)s')


def main():
    """retrieves and displays users data"""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    filtered_fields = {'name', 'email', 'phone', 'ssn', 'password'}
    for row in rows:
        filtered_data = {key: '***' if key in filtered_fields else value for key, value in row.items()}
        formatted_data = "; ".join(f"{key}={value}" for key, value in filtered_data.items())
        logging.info(formatted_data)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
