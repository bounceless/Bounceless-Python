# Bounceless Python API

This is a Python client for interacting with the Bounceless.io API for email verification. It provides two main features: 

1. Verifying a single email
2. Bulk verifying emails from a CSV file

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/bounceless/Bounceless-Python.git
```

## Usage

First, import the necessary classes from the `emailverify` module:

```python
from emailverify import BouncelessOne, BouncelessBulk
```

### Single Email Verification

To verify a single email, you can use the `BouncelessOne` class. You will need to provide your API key and the email you want to verify:

```python
def verify_single_email():
    # Replace 'YOUR_KEY' with your actual API key
    # Replace 'test@email.com' with the actual email you want to verify
    bounceless_one = BouncelessOne('YOUR_KEY', 'test@email.com')
    response = bounceless_one.control()
    print(response)
```

### Bulk Email Verification

To verify a bulk of emails from a CSV file, you can use the `BouncelessBulk` class. You will need to provide your API key and the path to the CSV file:

```python
def verify_bulk_emails():
    # Replace 'YOUR_KEY' with your actual API key
    # Replace 'path/to/file.csv' with the actual path to your CSV file
    bounceless_bulk = BouncelessBulk('YOUR_KEY', 'path/to/file.csv')
    bounceless_bulk.upload()
    response = bounceless_bulk.get_info()
    print(response)
```

Finally, call these functions in your main script:

```python
if __name__ == '__main__':
    verify_single_email()
    verify_bulk_emails()
```

## License

This project is licensed under the terms of the MIT license.
