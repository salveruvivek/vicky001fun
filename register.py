# register.py
# Register a new user. Companion to login_page.py — good for Git practice.

# Pretend database of users (username: password)
users = {
    "vivek": "1234",
    "admin": "admin123",
}


def register():
    """Ask for a new username and password, then add it to users."""
    print("=== Register ===")
    username = input("Choose a username: ")

    if username in users:
        print("That username is already taken.")
        return False

    password = input("Choose a password: ")
    confirm = input("Confirm password: ")

    if password != confirm:
        print("Passwords do not match.")
        return False

    users[username] = password
    print(f"Account created for {username}!")
    return True


if __name__ == "__main__":
    register()
    print("Current users:", list(users.keys()))
