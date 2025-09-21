# bank.py
import os
import pickle
import datetime as dt


class Bank:
    data = []

    @classmethod
    def __update(cls):
        """Save current bank data into pickle file"""
        with open("data.pkl", "wb") as f:
            pickle.dump(cls.data, f)

    @classmethod
    def __load(cls):
        """Load bank data from pickle file"""
        if os.path.exists("data.pkl"):
            with open("data.pkl", "rb") as f:
                cls.data = pickle.load(f)

    @classmethod
    def createAccount(cls, name, age, email, pin):
        cls.__load()
        accnumber = 1000 + len(cls.data) + 1
        userdata = {
            "accountNo.": accnumber,
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "balance": 0,
            "createDate": str(dt.datetime.now()),
        }
        cls.data.append(userdata)
        cls.__update()
        return userdata

    @classmethod
    def deposit(cls, accnumber, pin, amount):
        cls.__load()
        userdata = [i for i in cls.data if i["accountNo."] == accnumber and i["pin"] == pin]
        if not userdata:
            return False, "Invalid account or pin"
        if amount <= 0:
            return False, "Invalid amount"
        userdata[0]["balance"] += amount
        cls.__update()
        return True, userdata[0]

    @classmethod
    def withdraw(cls, accnumber, pin, amount):
        cls.__load()
        userdata = [i for i in cls.data if i["accountNo."] == accnumber and i["pin"] == pin]
        if not userdata:
            return False, "Invalid account or pin"
        if amount <= 0 or amount > userdata[0]["balance"]:
            return False, "Invalid or insufficient balance"
        userdata[0]["balance"] -= amount
        cls.__update()
        return True, userdata[0]

    @classmethod
    def showdetail(cls, accnumber, pin):
        cls.__load()
        userdata = [i for i in cls.data if i["accountNo."] == accnumber and i["pin"] == pin]
        if not userdata:
            return None
        return userdata[0]

    @classmethod
    def deleteAccount(cls, accnumber, pin):
        cls.__load()
        userdata = [i for i in cls.data if i["accountNo."] == accnumber and i["pin"] == pin]
        if not userdata:
            return False
        cls.data.remove(userdata[0])
        cls.__update()
        return True
