import time
import random
import os
import database
import register

cursor = database.cursor
game = True
contw = True

#region functions
def cls():
    os.system('cls')
#endregion
print("Welcome to Dice Game ! ")
time.sleep(1)
lr = int(input("Login/Register (1-0) :"))

if lr == 0:
    register.reg()

#region login
userName = input("Username : ")
password = input("Password : ")
cursor.execute(f"SELECT ID FROM user_accounts WHERE userName = '{userName}' AND password = '{password}'")
IDdb = cursor.fetchone()
ID = IDdb[0]
#endregion
#region game
while game:
    cursor.execute(f"SELECT * FROM user_details WHERE ID = '{ID}'")
    result = cursor.fetchone()
    cursor.execute(f"SELECT * FROM user_accounts WHERE ID = '{ID}'")
    result2 =cursor.fetchone()
    cls()
    bux = result[1]
    win = result[2]
    lose = result[3]
    age = result2[3]
    dice = round(random.uniform(0, 100), 2)
    print(f"ID = {ID}\t Win = {win}\nUsername: {userName}\t Lose = {lose}\nAge : {age} \nBux = {round(bux, 2)}")
    bet = int(input("Bet : "))
    diceplayer = int(input("Dice (0-94) : "))
    multiplier = 94 / diceplayer
    gain = (bet * multiplier) - bet
    print("Loading...")
    time.sleep(2)
    print(f"Dice is = {dice}")
    if diceplayer < dice:
        print("You Lose !")
        bux -= bet
        lose += 1
    else:
        print("You Win")
        bux += gain
        win += 1
    cursor.execute(f"UPDATE user_details SET bux ='{bux}',win = '{win}', lose = '{lose}' WHERE ID ='{ID}'")
    database.db.commit()
    time.sleep(2)
    cont = int(input("Do you want continue ? (1/0) :"))
    if cont == 0:
        print("Thanks for Game !")
        time.sleep(2)
        game = False
        exit(0)
    elif cont == 1:
        cls()
    else:
        print("Wrong Key ! Exiting...")
        time.sleep(2)
        game = False
        exit(0)

#endregion
