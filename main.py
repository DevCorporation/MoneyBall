print("By mcg76&Bruno99")
print("MoneyBall API.v1")
##База данных v1##
moneydb = {
    "nick": "money"
}
users = ["keker:123"]
##Мини-Авторизация##
user = str(input("NickName: "))
print(user)
passw = str(input("Passwords: "))
print(passw)
saves = user,":",passw
users.append(saves)
money = 0
snickmoney = moneydb.fromkeys([user], money)
#if user in moneydb:
 #money = moneydb[user]
print("Save on BD", snickmoney)
if user in users:
 print("Wrong!Error 404")
else:
 print("You are auto as ",user)
##Добавление денег##
try:
 addmoneyu = str(input("Adding momey to: "))
 print(addmoneyu)
 addmoneyv = str(input("Adding money: "))
 print(addmoneyv)
 money = addmoneyv + money
except ValueError:
 print("Error ValueError..system is crashing")
finally:
 print("Please enter a number value")
##debug##
print(moneydb)
print(user)
print(users)
print(money)
