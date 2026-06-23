from log_generator import LogGenerator
from utils import is_valid_hostname_or_ip, is_valid_url, validate_positive_int


def prompt_choice() -> str:
    print("Choose the log generation mode:")
    print("1) SSH login attempts")
    print("2) NGINX request simulation")
    choice = input("Select 1 or 2: ").strip()
    if choice not in {"1", "2"}:
        raise ValueError("Please enter 1 for SSH or 2 for NGINX")
    return choice


def prompt_ssh() -> None:
    host = input("Enter the SSH host (hostname or IP): ").strip()
    username = input("Enter the SSH username (Leave blank for default 'vboxuser'): ").strip() or "vboxuser"
    attempts = input("Enter the number of login attempts: ").strip()
    mode = input("Enter mode [mixed, spray, bruteforce] (default mixed): ").strip().lower() or "mixed"

    print("\nValidating SSH inputs...\n")
    if not is_valid_hostname_or_ip(host):
        raise ValueError("SSH host must be a valid hostname or IP address")

    attempts_value = validate_positive_int(attempts, "login attempts")
    LogGenerator.generate_ssh_logs(host, username, attempts_value, mode)


def prompt_nginx() -> None:
    target = input("Enter the NGINX target URL (http:// or https://): ").strip()
    requests_count = input("Enter the number of requests to send: ").strip()
    mode = input("Enter mode [mixed, normal, scan, sqli, xss, dos] (default mixed): ").strip().lower() or "mixed"

    print("\nValidating NGINX inputs...\n")
    if not is_valid_url(target):
        raise ValueError("NGINX target must be a valid http:// or https:// URL")

    requests_count_value = validate_positive_int(requests_count, "requests count")
    LogGenerator.generate_nginx_logs(target, requests_count_value, mode)


def main() -> None:
    try:
        choice = prompt_choice()
        if choice == "1":
            prompt_ssh()
        else:
            prompt_nginx()
    except ValueError as error:
        print(f"Input validation failed: {error}")


if __name__ == "__main__":
    main()
