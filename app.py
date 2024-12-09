import streamlit as st

# In-memory user database
CREDENTIALS = {
    "user": {"username": "user", "password": "user123"},
    "doctor": {"username": "doctor", "password": "doctor123"}
}

st.set_page_config(page_title="Clinical Assistant", layout="wide")

# Session state
if "role" not in st.session_state:
    st.session_state.role = None

# Login Function
def login(username, password, role):
    if role in CREDENTIALS:
        if CREDENTIALS[role]["username"] == username and CREDENTIALS[role]["password"] == password:
            st.session_state.role = role
            return True
    return False

# Login Page
if st.session_state.role is None:
    st.title("Login")

    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox("Login as:", ["User", "Doctor"])
    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

    login_button = st.button("Login")

    if login_button:
        if login(username, password, role.lower()):
            st.success(f"Logged in as {role}")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# User Dashboard
if st.session_state.role == "user":
    st.title("Chatbot Interface")
    st.write("Welcome to the Clinical Assistant Chatbot!")
    user_message = st.text_input("Type your message:")
    if st.button("Send"):
        st.write(f"Chatbot reply to: {user_message}")

# Doctor Dashboard
if st.session_state.role == "doctor":
    st.title("Doctor Dashboard")
    st.write("Welcome to the Doctor's Dashboard!")
    st.write("Here you can manage your appointments, view patient records, and more.")
