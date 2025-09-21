# app.py
import streamlit as st
from bank import Bank

st.title("🏦 Bank Management System")

menu = ["Create Account", "Deposit", "Withdraw", "Show Details", "Delete Account"]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Create Account":
    st.subheader("Open a New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=100)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")
    if st.button("Create Account"):
        if len(pin) == 4 and pin.isdigit():
            userdata = Bank.createAccount(name, age, email, pin)
            st.success(f"Account created successfully! Your Account No: {userdata['accountNo.']}")
        else:
            st.error("PIN must be exactly 4 digits")

elif choice == "Deposit":
    st.subheader("Deposit Money")
    acc = st.number_input("Account Number", min_value=1001)
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    amount = st.number_input("Amount", min_value=1)
    if st.button("Deposit"):
        success, result = Bank.deposit(acc, pin, amount)
        if success:
            st.success(f"Deposit successful! New Balance: {result['balance']}")
        else:
            st.error(result)

elif choice == "Withdraw":
    st.subheader("Withdraw Money")
    acc = st.number_input("Account Number", min_value=1001)
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    amount = st.number_input("Amount", min_value=1)
    if st.button("Withdraw"):
        success, result = Bank.withdraw(acc, pin, amount)
        if success:
            st.success(f"Withdrawal successful! New Balance: {result['balance']}")
        else:
            st.error(result)

elif choice == "Show Details":
    st.subheader("Account Details")
    acc = st.number_input("Account Number", min_value=1001)
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    if st.button("Show"):
        data = Bank.showdetail(acc, pin)
        if data:
            st.json(data)
        else:
            st.error("Invalid account or PIN")

elif choice == "Delete Account":
    st.subheader("Delete Account")
    acc = st.number_input("Account Number", min_value=1001)
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    if st.button("Delete"):
        success = Bank.deleteAccount(acc, pin)
        if success:
            st.success("Account deleted successfully")
        else:
            st.error("Invalid account or PIN")
