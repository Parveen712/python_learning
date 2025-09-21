# ---------------- Streamlit UI ---------------- #
import streamlit as st
from bank import Bank


st.set_page_config(page_title="Bank Management System", layout="centered")
st.title("🏦 Bank Management System")

menu = st.radio("Choose an option", [
    "Create Account",
    "Deposit Money",
    "Withdraw Money",
    "Show Details",
    "Update Details",
    "Delete Account"
])

if menu == "Create Account":
    st.subheader("📝 Create a New Account")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=120)
    email = st.text_input("Enter your email")
    pin = st.text_input("Enter a 4-digit PIN", type="password")

    if st.button("Create Account"):
        if name and email and pin.isdigit():
            info, msg = Bank.create_account(name, age, email, int(pin))
            st.success(msg)
            if info:
                st.json(info)
        else:
            st.error("⚠️ Please fill all fields correctly.")

elif menu == "Deposit Money":
    st.subheader("💰 Deposit Money")
    acc = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter amount", min_value=1, max_value=10000)
    if st.button("Deposit"):
        if acc and pin:
            msg = Bank.deposit(acc, int(pin), amount)
            st.info(msg)

elif menu == "Withdraw Money":
    st.subheader("💸 Withdraw Money")
    acc = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter amount", min_value=1)
    if st.button("Withdraw"):
        if acc and pin:
            msg = Bank.withdraw(acc, int(pin), amount)
            st.info(msg)

elif menu == "Show Details":
    st.subheader("📋 Show Account Details")
    acc = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Show"):
        if acc and pin:
            data = Bank.show_detail(acc, int(pin))
            if data:
                st.json(data)
            else:
                st.error("❌ No such account exists.")

elif menu == "Update Details":
    st.subheader("✏️ Update Account Details")
    acc = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")
    new_name = st.text_input("Enter new name (optional)")
    new_email = st.text_input("Enter new email (optional)")
    new_pin = st.text_input("Enter new PIN (4-digit, optional)", type="password")

    if st.button("Update"):
        if acc and pin:
            msg = Bank.update_detail(acc, int(pin), new_name, new_email, new_pin)
            st.info(msg)

elif menu == "Delete Account":
    st.subheader("🗑️ Delete Account")
    acc = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Delete"):
        if acc and pin:
            msg = Bank.delete(acc, int(pin))
            st.warning(msg)
