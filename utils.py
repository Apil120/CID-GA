import random
import string


class RandomStringGenerator:
    """A class to generate random strings of random lengths."""

    def __init__(self):
        self.length = random.randint(5, 50)
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate(self):
        """Generate a random string of random length using only the random module."""
        return ''.join(random.choice(self.characters) for _ in range(self.length))
