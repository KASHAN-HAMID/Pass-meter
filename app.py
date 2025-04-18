import re
import random
import string
import pyperclipt
import streamlit as st

# Set Page Configurations
st.set_page_config(page_title="Password Strength Meter", layout="centered")

# Custom Dark Theme UI with Animations
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: white;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        background: -webkit-linear-gradient(45deg, #ff8c00, #ff0000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: flicker 1.5s infinite alternate;
    }
    @keyframes flicker {
        0% { opacity: 1; }
        100% { opacity: 0.8; }
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff8c00, #ff0000);
        color: white;
        border: none;
        padding: 12px 25px;
        border-radius: 30px;
        font-size: 1.1em;
        font-weight: bold;
        transition: all 0.4s ease;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #ff0000, #ff8c00);
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.6);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Password Strength Checker
def check_password_strength(password):
    score = 0
    messages = []
    
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        return "✅ Strong Password!", messages
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", messages
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", messages

# Generate Strong Password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

# UI Components
st.markdown("<h1 class='title'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength 🔍"):
    if password:
        strength, feedback = check_password_strength(password)
        st.success(strength)
        for msg in feedback:
            st.warning(msg)
    else:
        st.error("Please enter a password!")

# Generate Strong Password
if st.button("Generate Strong Password 🔑"):
    strong_password = generate_password()
    st.text_area("Your Strong Password:", strong_password, height=50)
    if st.button("Copy Password 📋"):
        pyperclip.copy(strong_password)
        st.success("Password copied to clipboard!")
