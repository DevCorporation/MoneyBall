print("Программа «MoneyBall API»\nВерсия: 0.3")
print("\nРазработчики:\n Xaker Su - mcg76\n Максим Удачин - Bruno99")
print("\nНаш Веб-Сайт: http://vk.com/dev.corp.python\n")


##База данных v.1##

moneydb = {
    "nick": "money"
}
users = []

##Регистрация##

print("\nЧтобы начать работать с программой, зарегистрируйтесь в нашей системе:\n")
user = str(input("Пользователь: "))
passw = str(input("Пароль: "))
saves = user,":",passw
users.append(saves)
money = 0
snickmoney = moneydb.fromkeys([user], money)

#if user in moneydb:
 #money = moneydb[user]
print("\nРегистрация завершена, как: \n Пользователь - ",user,"\n Пароль - ",passw)
if user in users:
 print("Wrong!Error 404")
else:
 print("\nПроверка завершена, пользователь «",user,"» присутсвует в Базе Данных.")
 
##Добавление денег##

try:
 addmoney = int(input("\nДобавьте сумму на ваш баланс: "))
 money += addmoney
except ValueError:
 print("Ошибка ввода, пожалуйста используйте цифры!")
 print("\nПовторная попытка: ")
 addmoney = int(input(" Добавьте сумму на ваш баланс: "))
 money += addmoney
 
 ##Проверка Баланса##
moneys = str(input("\nВведите команду на проверку баланса: "))
if moneys == "/money":
 print("\nПользователь «",user,"», Баланс: ",money,"\n\n")
else:
 print("Команда не совпадает!")
 print("Повторите ввод команды:")
 moneys = str(input("\nВведите команду на проверку баланса: "))
 if moneys == "/money":
  print("\nПользователь «",user,"», Баланс: ",money,"\n\n")
 else:
  print("\nКритическая ошибка, попытка закончена.\n\n")

# Конец программы(Дно) #
print("----------"*5,"\n     Работа программы завершена! ©DevCorp\n","----------"*5)
