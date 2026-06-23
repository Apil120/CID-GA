import ipaddress
import random
import re
import string
from urllib.parse import urlparse


class RandomStringGenerator:
    """Generate random strings containing letters, digits, and punctuation."""

    def __init__(self):
        self.length = random.randint(5, 50)
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate(self) -> str:
        return ''.join(random.choice(self.characters) for _ in range(self.length))


def is_valid_hostname_or_ip(value: str) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False

    candidate = value.strip()

    try:
        ipaddress.ip_address(candidate)
        return True
    except ValueError:
        pass

    if len(candidate) > 253:
        return False

    if candidate.endswith('.'):
        candidate = candidate[:-1]

    labels = candidate.split('.')
    for label in labels:
        if not (1 <= len(label) <= 63):
            return False
        if not re.match(r'^[A-Za-z0-9-]+$', label):
            return False
        if label[0] == '-' or label[-1] == '-':
            return False

    return True


def is_valid_url(value: str) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False

    url = urlparse(value.strip())
    return url.scheme in ('http', 'https') and bool(url.netloc)


def validate_positive_int(value, name: str = 'value') -> int:
    if isinstance(value, str):
        value = value.strip()
        if not value.isdigit():
            raise ValueError(f'{name} must be a positive integer')
        value = int(value)
    elif not isinstance(value, int):
        raise ValueError(f'{name} must be a positive integer')

    if value < 1:
        raise ValueError(f'{name} must be greater than 0')

    return value
