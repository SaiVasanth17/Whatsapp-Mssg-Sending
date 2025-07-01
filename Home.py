import streamlit as st
import pandas as pd
import pywhatkit
import time

st.title("📲 WhatsApp Automation Tool")

# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel File with 'Phone' column", type=["xlsx"])

# Enter message
message = st.text_area("Enter the message to send:")

if uploaded_file is not None and message:
    df = pd.read_excel(uploaded_file)
    numbers = df['Phone'].astype(str).tolist()

    if st.button("Send WhatsApp Messages"):
        for number in numbers:
            try:
                if not number.startswith('+'):
                    number = '+' + number

                current_time = time.localtime()
                hour = current_time.tm_hour
                minute = current_time.tm_min + 1

                pywhatkit.sendwhatmsg(number, message, hour, minute, wait_time=10, tab_close=True)
                st.success(f"Scheduled message to {number}")
                time.sleep(15)

            except Exception as e:
                st.error(f"Failed to send message to {number}: {e}")
