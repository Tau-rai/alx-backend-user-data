#!/usr/bin/env python3
"""Module for filtering sensitive data"""


from typing import List
import re
import logging


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
