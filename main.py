print("Программа «MoneyBall API»\nВерсия: 1.0")
print("\nРазработчики:\n Xaker Su - mcg76\n Максим Удачин - Bruno99")
print("\nНаш Веб-Сайт: http://vk.com/dev.corp.python\n")
##Глобальная хуйня##
global money
money = 0
##База данных v.1##

moneydb = {
    "nick": "money"
}
users = ["admin:229"]
userik = {
	   "nick": "привелегия"
}
vip = []
elite = []
admin = ["admin"]

##Регистрация##
print("\nЧтобы начать работать с программой, зарегистрируйтесь в нашей системе:\n")
user = str(input("Пользователь: "))
passw = str(input("Пароль: "))
saves = user,":",passw
users.append(saves)
snickmoney = moneydb.fromkeys([user], money)
don = "Пользователь"
if not user == admin:
 print("Загрузка....")
else:
 print("Здраствуйте Администратор!")
#if user in moneydb:
 #money = moneydb[user]
if user in users:
 print("Wrong!Error 404")
else:
 print("\nРегистрация завершена, как: \n Пользователь - ",user,"\n Пароль - ",passw)
 print("\nПроверка завершена, пользователь «",user,"» присуствует в Базе Данных.")
##Команды нахуй##
def helps():
 print("Говно залупа")
def addmoneys():
 while True:
  try:
   addmoney = int(input("\nДобавьте сумму на ваш баланс: "))
  except ValueError:
   print("Ошибка ввода, пожалуйста используйте цифры!")
   print("\nПовторная попытка: ")
   continue
  finally:
   break
   kek = addmoney + money
   moneydb[user] = kek
commands = {'/helps': helps,'/addmoney': addmoneys}
while True:
 comsend = input("Введите команду:")
 command = comsend
 if command in commands:
  commands[comsend]()
 else:
  print("Хуйню ввел")
  continue
