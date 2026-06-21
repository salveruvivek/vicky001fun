# login_page.py
# A simple login program for Git practice.

# Pretend database of users (username: password)
users = {
    "vivek": "1234",
    "admin": "admin123",
}


def login():
    """Ask for a username and password, then check them."""
    print("=== Login Page ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print(f"Welcome, {username}! You are logged in.")
        return True
    else:
        print("Invalid username or password.")
        return False


def main():
    attempts = 3
    while attempts > 0:
        if login():
            break
        attempts -= 1
        print(f"Attempts left: {attempts}\n")
    else:
        print("Too many failed attempts. Goodbye.")


if __name__ == "__main__":
    main()
