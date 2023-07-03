# Bounceless Python API

This Python client allows you to interact with the Bounceless.io API for email verification. The client supports the following features:

1. Single email verification
2. Bulk email verification from a CSV file
3. Fetching verification results for a file

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/bounceless/Bounceless-Python.git
```

## Usage

Import the necessary classes from the `emailverify` module:

```python
from emailverify import BouncelessOne, BouncelessBulk
```

### Single Email Verification

Use the `BouncelessOne` class to verify a single email. You will need to provide your API key and the email you wish to verify:

```python
def verify_single_email():
    # Replace 'YOUR_KEY' with your actual API key
    # Replace 'test@email.com' with the actual email you want to verify
    bounceless_one = BouncelessOne('YOUR_KEY', 'test@email.com')
    response = bounceless_one.control()
    print(response)
```

### Bulk Email Verification

Use the `BouncelessBulk` class to verify a bulk of emails from a CSV file. Provide your API key and the path to the CSV file:

```python
def verify_bulk_emails():
    # Replace 'YOUR_KEY' with your actual API key
    # Replace 'path/to/file.csv' with the actual path to your CSV file
    bounceless_bulk = BouncelessBulk('YOUR_KEY', 'path/to/file.csv')
    bounceless_bulk.upload()
```

### Fetching Verification Results

After a bulk upload, fetch the verification results using the `get_info()` method from the `BouncelessBulk` class. This method can also be used independently by providing the ID of a previously uploaded file:

```python
def get_bulk_info():
    # Replace 'YOUR_KEY' with your actual API key
    # Replace 'FILE_ID' with the actual ID of your uploaded file
    bounceless_bulk = BouncelessBulk('YOUR_KEY', 'FILE_ID')
    response = bounceless_bulk.get_info()
    print(response)
```

Finally, call these functions in your main script:

```python
if __name__ == '__main__':
    verify_single_email()
    verify_bulk_emails()
    get_bulk_info()
```

## License

This project is licensed under the terms of the MIT license.
