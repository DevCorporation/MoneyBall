print("This is console module")
print("Программа «MoneyBall API»\nВерсия: 0.5")
print("\nРазработчики:\n Xaker Su - mcg76\n Максим Удачин - Bruno99")
print("\nНаш Веб-Сайт: http://vk.com/dev.corp.python\n")


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
money = 0
snickmoney = moneydb.fromkeys([user], money)
don = "Пользователь"
if user == admin:
 print("Загрузка....")
else:
 print("Здраствуйте Администратор!")
#if user in moneydb:
 #money = moneydb[user]
print("\nРегистрация завершена, как: \n Пользователь - ",user,"\n Пароль - ",passw)
if user in users:
 print("Wrong!Error 404")
else:
 print("\nПроверка завершена, пользователь «",user,"» присутсвует в Базе Данных.")

##Добавление денег##
if not user in admin:
 print("доступ к добавлению денег запрещен!")
else:
 don = "Администратор"
 print("Вы может изменить баланс!")
 try:
  addmoney = int(input("\nДобавьте сумму на ваш баланс: "))
  money += addmoney
 except ValueError:
  print("Ошибка ввода, пожалуйста используйте цифры!")
  print("\nПовторная попытка: ")
  addmoney = int(input(" Добавьте сумму на ваш баланс: "))
  kek = addmoney + money
  moneydb[user] = kek
 ##Проверка Баланса##
while True:
 moneys = str(input("\nВведите команду на проверку баланса(Не знаете команды?пропишите /help): "))
 if moneys == "/money":
  print("\nПользователь «",user,"», Баланс: ",money,",Доступ: ",don,"\n\n")
 else:
  print("Команда не совпадает!")
  print("Повторите ввод команды:")
  break
  if not moneys == "/quit":
   print("Exiting..")
   raise ValueError
  else:
   continue
 ##return сюда!!
# Конец программы(Дно) #
print("----------"*5,"\n     Работа программы завершена! ©DevCorp\n","----------"*5)
