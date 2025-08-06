import re

# Common passwords list
COMMON_PASSWORDS = ["123456", "password", "qwerty", "letmein", "admin"]

# Helper functions to reduce complexity
def has_upper(password):
    return bool(re.search(r"[A-Z]", password))

def has_lower(password):
    return bool(re.search(r"[a-z]", password))

def has_digit(password):
    return bool(re.search(r"\d", password))

def has_special(password):
    return bool(re.search(r"[@$!%*?&]", password))


def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase
    if has_upper(password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase
    if has_lower(password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Numbers
    if has_digit(password):
        score += 1
    else:
        suggestions.append("Add numbers")

    # Special characters
    if has_special(password):
        score += 1
    else:
        suggestions.append("Add special characters (@$!%*?&)")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid common passwords")
        score = 1  # Force weak

    # Final strength result
    if score <= 2:
        strength = "Weak ❌"
    elif score < 5:
        strength = "Medium ⚠️"
    else:
        strength = "Strong ✅"

    return strength, suggestions


# ✅ This part actually runs the function
if __name__ == "__main__":
    pwd = input("Enter a password: ")
    strength, tips = check_password_strength(pwd)

    print(f"🔐 Password Strength: {strength}")
    if tips:
        print("💡 Suggestions:")
        for t in tips:
            print(f" - {t}")
