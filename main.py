import paramiko
import time
from utils import RandomStringGenerator

##-----CONSTANTS------------------------------------------------------------------
USER = "vboxuser"

HOST = input("Enter the SSH server IP address: ")

LOOP_COUNT = int(input("Enter the number of login attempts: "))

for i in range(LOOP_COUNT):
    try:
        print(f"Attempt {i+1}: Trying to login with a random password...")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(
            HOST,
            username=USER,
            password=RandomStringGenerator().generate(),
            timeout=5
        )

    except paramiko.AuthenticationException:
        print(f"Attempt {i+1}: Failed login")

    except Exception as e:
        print(f"Attempt {i+1}: Error occurred - {e}")

    finally:
        try:
            client.close()
        except Exception as e:
            print(f"Attempt {i+1}: Error occurred while closing connection - {e}")

    time.sleep(1)