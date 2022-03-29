import database
import time
def reg():
    cursor = database.cursor
    userName = input("Username : ")
    password = input("Password : ")
    age = int(input("Age : "))
    if age < 18:
        print("You can't play")
        time.sleep(2)
        exit(0)
    cursor.execute("INSERT INTO user_accounts (userName, password , age) VALUES (%s, %s, %s)", (userName, password, age))
    cursor.execute(f"SELECT ID FROM user_accounts WHERE userName = '{userName}' AND password = '{password}'")
    IDdb = cursor.fetchone()
    ID = IDdb[0]
    cursor.execute("INSERT INTO user_details (ID, bux) VALUES (%s,%s)", (ID,10000))
    database.db.commit()
    print("Register Successful ! You can Login.")
    time.sleep(2)
    exit(0)