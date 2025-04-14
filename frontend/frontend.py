import streamlit as st
import requests

backend_url = "http://127.0.0.1:5000"  # Adjust based on where Flask is running

# Predefined NFT ID
REQUIRED_NFT_ID = "1234"

st.title("Career Counseling")

# Display the required NFT ID
st.info(f"Required NFT ID for all sessions: {REQUIRED_NFT_ID}")

# Register a session
st.header("Register Session")
counselor = st.text_input("Enter your address (Counselor)")
nft_id = st.text_input("Enter required NFT ID", value=REQUIRED_NFT_ID)
aptos_amount = st.number_input("Enter Aptos amount for session", min_value=0.0, step=0.1, format="%.2f")

if st.button("Register Session"):
    response = requests.post(f"{backend_url}/register_session", 
                           json={"counselor": counselor, "nft_id": nft_id, "aptos_amount": aptos_amount})
    if response.status_code == 200:
        st.success("Session registered successfully!")
    else:
        st.error("Failed to register session")

# Book a session
st.header("Book a Session")
user = st.text_input("Enter your address (User)")
counselor_to_book = st.text_input("Enter Counselor's address")
user_nft_id = st.text_input("Enter your NFT ID", value=REQUIRED_NFT_ID)
booking_aptos_amount = st.number_input("Enter Aptos amount to pay", min_value=0.0, step=0.1, format="%.2f")

if st.button("Book Session"):
    response = requests.post(f"{backend_url}/book_session", 
                           json={"user": user, "counselor": counselor_to_book, "nft_id": user_nft_id, "aptos_amount": booking_aptos_amount})
    st.json(response.json())
