import streamlit as st
from chatgpt import Bank   # Step 1 ka class import kar rahe hain

st.title("🏦 Bank Management System")

bank = Bank()

menu = ["Create Account", "Deposit Money", "Withdraw Money", "Account Details", "Update Account", "Delete Account"]
choice = st.sidebar.selectbox("Select Option", menu)

if choice == "Create Account":
    st.subheader("➕ Create New Account")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=1)
    email = st.text_input("Enter Email")
    pin = st.text_input("Enter 4-digit PIN", type="password")
    if st.button("Create"):
        if name and age and email and pin:
            st.success(bank.create_account(name, int(age), email, int(pin)))
        else:
            st.warning("⚠️ Please fill all details.")

elif choice == "Deposit Money":
    st.subheader("💰 Deposit Money")
    acc = st.text_input("Enter Account No.")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter Amount", min_value=1)
    if st.button("Deposit"):
        st.success(bank.deposit_money(acc, int(pin), amount))

elif choice == "Withdraw Money":
    st.subheader("💸 Withdraw Money")
    acc = st.text_input("Enter Account No.")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter Amount", min_value=1)
    if st.button("Withdraw"):
        st.success(bank.withdraw_money(acc, int(pin), amount))

elif choice == "Account Details":
    st.subheader("📑 Account Details")
    acc = st.text_input("Enter Account No.")
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Show Details"):
        details = bank.details(acc, int(pin))
        if details:
            st.json(details)
        else:
            st.error("❌ No account found.")

elif choice == "Update Account":
    st.subheader("✏️ Update Account Details")
    acc = st.text_input("Enter Account No.")
    pin = st.text_input("Enter PIN", type="password")
    new_name = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")
    if st.button("Update"):
        st.success(bank.update_det(acc, int(pin), new_name, new_email, new_pin))

elif choice == "Delete Account":
    st.subheader("🗑️ Delete Account")
    acc = st.text_input("Enter Account No.")
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Delete"):
        st.success(bank.delete(acc, int(pin)))


# streamlit run frontend.py type this command in terminal to run the code