# README
This document provides an overview of the concepts covered in this directory.

## Data Security and Logging in Python

## 1. What Is PII, non-PII, and Personal Data?
- **Personal Data**: Refers to information related to an identified or identifiable individual. It can include simple identifiers like names or numbers, as well as more complex identifiers like IP addresses or cookie identifiers.
- **Personally Identifiable Information (PII)**: A subset of personal data that directly identifies an individual. Examples include social security numbers, email addresses, and phone numbers.
- **Non-PII**: Information that does not directly identify an individual. For instance, website visit data or anonymous user behavior.

## 2. Logging Documentation
Python's `logging` module provides a flexible event logging system for applications and libraries. Key points:
- Use `logging.getLogger(__name__)` to create a logger.
- Replace `print` statements with logging methods (`debug`, `info`, `warning`, `error`, `critical`).
- Configure logging levels, destinations (console or file), and formats.
- Check out the [official Python logging documentation](https://docs.python.org/3/library/logging.html) for detailed information.

## 3. Bcrypt Package
- **Overview**: Bcrypt is a password-hashing function designed to securely store passwords. It uses the Blowfish cipher and includes a salt to protect against rainbow table attacks.

## 4. Logging to Files, Setting Levels, and Formatting
- **Basics**: Replace `print` statements with logs. Configure logging levels, filenames, and formats using `basicConfig()`.
- **Advanced**: Explore loggers, handlers, and formatters. Customize log messages and manage log records. See the [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html) for practical examples.