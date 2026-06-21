# register.py
# A simple registration window built with Tkinter (Python's built-in GUI library).
# Run it with:  python register.py

import tkinter as tk
from tkinter import ttk

# Pretend database of users (username: password)
users = {
    "vivek": "1234",
    "admin": "admin123",
}

# ---- Colors / theme ----
BG = "#0d1117"
CARD = "#161b22"
ACCENT = "#238636"
ACCENT_HOVER = "#2ea043"
TEXT = "#c9d1d9"
MUTED = "#8b949e"
FIELD_BG = "#1c2128"


def register():
    """Validate the form fields and 'create' the account."""
    username = username_var.get().strip()
    password = password_var.get()
    confirm = confirm_var.get()

    # --- validation ---
    if not username or not password:
        show_status("Please fill in all fields.", error=True)
        return
    if username in users:
        show_status("That username is already taken.", error=True)
        return
    if len(password) < 4:
        show_status("Password must be at least 4 characters.", error=True)
        return
    if password != confirm:
        show_status("Passwords do not match.", error=True)
        return

    # --- success ---
    users[username] = password
    show_status(f"Account created for {username}!  ✅", error=False)
    username_var.set("")
    password_var.set("")
    confirm_var.set("")


def show_status(message, error=False):
    status_label.config(
        text=message,
        fg="#f85149" if error else "#3fb950",
    )


def toggle_passwords():
    """Show or hide the password characters."""
    char = "" if show_var.get() else "•"
    password_entry.config(show=char)
    confirm_entry.config(show=char)


# ---- Window ----
root = tk.Tk()
root.title("Register")
root.geometry("380x460")
root.configure(bg=BG)
root.resizable(False, False)

# Card frame
card = tk.Frame(root, bg=CARD, padx=30, pady=30)
card.place(relx=0.5, rely=0.5, anchor="center", width=320, height=400)

# Title
tk.Label(card, text="Create Account", bg=CARD, fg="#ffffff",
         font=("Segoe UI", 18, "bold")).pack(pady=(0, 4))
tk.Label(card, text="Sign up to get started", bg=CARD, fg=MUTED,
         font=("Segoe UI", 10)).pack(pady=(0, 20))

# Form variables
username_var = tk.StringVar()
password_var = tk.StringVar()
confirm_var = tk.StringVar()
show_var = tk.BooleanVar(value=False)


def make_field(label_text, variable, hide=False):
    tk.Label(card, text=label_text, bg=CARD, fg=TEXT,
             font=("Segoe UI", 9), anchor="w").pack(fill="x")
    entry = tk.Entry(card, textvariable=variable, bg=FIELD_BG, fg=TEXT,
                     insertbackground=TEXT, relief="flat",
                     font=("Segoe UI", 11), show="•" if hide else "")
    entry.pack(fill="x", ipady=6, pady=(2, 12))
    return entry


username_entry = make_field("Username", username_var)
password_entry = make_field("Password", password_var, hide=True)
confirm_entry = make_field("Confirm Password", confirm_var, hide=True)

# Show password checkbox
tk.Checkbutton(card, text="Show password", variable=show_var,
               command=toggle_passwords, bg=CARD, fg=MUTED,
               selectcolor=CARD, activebackground=CARD,
               activeforeground=TEXT, font=("Segoe UI", 9),
               bd=0, highlightthickness=0).pack(anchor="w")

# Register button (with hover effect)
register_btn = tk.Button(card, text="Register", command=register,
                         bg=ACCENT, fg="white", activebackground=ACCENT_HOVER,
                         activeforeground="white", relief="flat",
                         font=("Segoe UI", 11, "bold"), cursor="hand2")
register_btn.pack(fill="x", ipady=8, pady=(14, 8))
register_btn.bind("<Enter>", lambda e: register_btn.config(bg=ACCENT_HOVER))
register_btn.bind("<Leave>", lambda e: register_btn.config(bg=ACCENT))

# Status message
status_label = tk.Label(card, text="", bg=CARD, fg=MUTED,
                        font=("Segoe UI", 9), wraplength=260)
status_label.pack(pady=(4, 0))

# Press Enter to submit
root.bind("<Return>", lambda e: register())

root.mainloop()
