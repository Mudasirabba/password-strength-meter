import re

def check_password_strength(password):
    score = 0
    feedback = []

    # ✅ Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # ✅ Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # ✅ Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # ✅ Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # ✅ Strength Rating
    if score == 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features."
    else:
        return f"❌ Weak Password - Improve it using the suggestions below:\n" + "\n".join(feedback)

# ✅ Get user input
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)


import random
import string

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔑 Suggested Strong Password:", generate_strong_password())


import streamlit as st
import re
import random
import string

# Password Strength Function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features."
    else:
        return "❌ Weak Password - Improve it using the suggestions below:\n" + "\n".join(feedback)

# Password Generator Function
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password Strength"):
    if password:
        result = check_password_strength(password)
        st.write(result)
    else:
        st.write("⚠️ Please enter a password.")

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.write(f"🔑 Suggested Password: **{strong_password}**")
