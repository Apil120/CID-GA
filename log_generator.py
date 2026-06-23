import random
import time
from concurrent.futures import ThreadPoolExecutor

import paramiko
import requests

from utils import (
    RandomStringGenerator,
    is_valid_hostname_or_ip,
    is_valid_url,
    validate_positive_int,
)


class LogGenerator:
    SSH_MODES = {"mixed", "spray", "bruteforce"}
    NGINX_MODES = {"mixed", "normal", "scan", "sqli", "xss", "dos"}

    @staticmethod
    def generate_ssh_logs(
        host: str, username: str = "vboxuser", attempts: int = 50, mode: str = "mixed"
    ):
        if not is_valid_hostname_or_ip(host):
            raise ValueError("SSH host must be a valid hostname or IP address")

        if not isinstance(username, str) or not username.strip():
            raise ValueError("SSH username must be a non-empty string")

        attempts = validate_positive_int(attempts, "attempts")
        mode = mode.strip().lower() if isinstance(mode, str) else "mixed"

        if mode not in LogGenerator.SSH_MODES:
            raise ValueError(
                f"SSH mode must be one of: {', '.join(sorted(LogGenerator.SSH_MODES))}"
            )

        users = [username, "root", "admin", "ubuntu", "test"]

        for i in range(attempts):
            current_user = (
                random.choice(users) if mode in {"spray", "mixed"} else username
            )
            print(f"[SSH] Attempt {i + 1}/{attempts} (user={current_user})")

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                client.connect(
                    host,
                    username=current_user,
                    password=RandomStringGenerator().generate(),
                    timeout=5,
                )
                print(f"[SSH] Connected unexpectedly with user={current_user}")

            except paramiko.AuthenticationException:
                print(f"[SSH] Failed login ({current_user})")

            except Exception as e:
                print(f"[SSH] Error: {e}")

            finally:
                try:
                    client.close()
                except Exception:
                    pass

            if mode == "spray":
                time.sleep(random.uniform(0.1, 0.5))
            elif mode == "bruteforce":
                time.sleep(random.uniform(0.5, 2))
            else:
                time.sleep(random.uniform(0.1, 3))

    @staticmethod
    def generate_nginx_logs(
        target: str, requests_count: int = 250, mode: str = "mixed"
    ):
        if not is_valid_url(target):
            raise ValueError("NGINX target must be a valid http:// or https:// URL")

        requests_count = validate_positive_int(requests_count, "requests_count")
        mode = mode.strip().lower() if isinstance(mode, str) else "mixed"

        if mode not in LogGenerator.NGINX_MODES:
            raise ValueError(
                f"NGINX mode must be one of: {', '.join(sorted(LogGenerator.NGINX_MODES))}"
            )

        target = target.rstrip("/")

        NORMAL = ["/", "/about", "/products", "/login"]
        SCAN = ["/admin", "/wp-admin", "/phpmyadmin", "/.env", "/backup.zip"]
        SQLI = [
            "/login?id=1' OR '1'='1",
            "/product?id=1 UNION SELECT 1",
            "/user?id=1'--",
        ]
        XSS = [
            "/search?q=<script>alert(1)</script>",
            "/comment?text=<img src=x onerror=alert(1)>",
        ]
        USER_AGENTS = ["Mozilla/5.0", "sqlmap/1.8", "Nikto/2.5.0", "curl/8.0"]

        def get_path() -> str:
            if mode == "normal":
                return random.choice(NORMAL)
            if mode == "scan":
                return random.choice(SCAN)
            if mode == "sqli":
                return random.choice(SQLI)
            if mode == "xss":
                return random.choice(XSS)
            if mode == "dos":
                return random.choice(NORMAL + SCAN)
            attack_type = random.choice([NORMAL, SCAN, SQLI, XSS])
            return random.choice(attack_type)

        def make_request(i: int) -> None:
            path = get_path()
            try:
                response = requests.get(
                    target + path,
                    headers={"User-Agent": random.choice(USER_AGENTS)},
                    timeout=5,
                )
                print(f"[WEB] {i} | {response.status_code} | {path}")
            except Exception as e:
                print(f"[WEB] Error: {e}")

        generated = 0
        while generated < requests_count:
            burst = mode == "dos" or random.random() < 0.15
            if burst:
                burst_size = min(random.randint(20, 75), requests_count - generated)
                print(f"\n[WEB] BURST {burst_size}\n")
                with ThreadPoolExecutor(max_workers=25) as executor:
                    for _ in range(burst_size):
                        generated += 1
                        executor.submit(make_request, generated)
                time.sleep(random.uniform(0.5, 2))
            else:
                generated += 1
                make_request(generated)
                time.sleep(random.uniform(1, 5))
