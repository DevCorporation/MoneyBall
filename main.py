print("Программа «MoneyBall API»\nВерсия: 3.0")
print("\nРазработчики:\n Xaker Su - mcg76\n Максим Удачин - Bruno99")
print("\nНаш Веб-Сайт: http://vk.com/dev.corp.python\n")
##Глобальная хуйня##
import time
global money
money = 0
##База данных v.1##
moneydb = {'kok': 200}
users = {'keker': 123,'admin': 229}
userik = {
	   "nick": "привелегия"
}
vip = []
elite = []
admin = ["admin"]
##Регистрация##
print("\nЧтобы начать работать с программой, зарегистрируйтесь в нашей системе:\n")
user = str(input("Пользователь: "))
while True:
 try:
  passw = int(input("Пароль: "))
  break
 except ValueError:
  print("Пожалуйста используйте цифры")
  continue
if user in users:
 print("Вы уже зарегистрированы")
 print("Сейчас проверю тебя и введеные данные")
 time.sleep(2)
 if not users[user] == passw:
   print("Ошибка!!!Неверные данные")
   don = "Аноним"
   print("Сейчас вы в режиме: ",don)
 else:
   print("Логин завершен как: ",user,)
   ##V3.1##
   ##Добавить базу данных как файл##
else:
 print("\nРегистрация завершена, как: \n Пользователь - ",user,"\n Пароль - ",passw)
 ##users = dict(user, passw)
 other = user,passw
 users.update([other])
 mymoney = user,0
 moneydb.update([mymoney])
don = "Пользователь"
if not user == "admin":
 print("Загрузка....")
else:
 if users[user] == passw:
  print("Здраствуйте Администратор!")
  don = "Администратор"
 else:
  print("Вы не являйтесь Администратором,ваш статус будет назначен как <Аноним>")
  don = "Аноним"
#if user in moneydb:
 #money = moneydb[user]
##Команды##
def status():
 print("Режим: ",don)
 moneyy = moneydb.get(user)
 if moneyy == None:
  print("Ошибка при получении баланса")
 else:
  print("Баланс: ",moneyy)
def dbcheck():
 print("База денег:",moneydb)
 print("Пользователи:",users)
def helps():
 print("/addmoney ,/helps,/getbd,/stats")
"""
 while True:
  try:
   if don == "Администратор":
    addmoneyus = input("Кому дать? ")
    addmoney = int(input("\nДобавьте сумму на баланс: "))
    print(addmoneyus)
   else:
    print("К сожалению доступ закрыт Администратором")
  except ValueError:
   print("Ошибка ввода, пожалуйста используйте цифры!")
   print("\nПовторная попытка: ")
   continue
  finally:
   ##WARNING РАБОТАЕТ##
    try:
     money = money+addmoney
     adm = addmoneys,money
     moneydb.update([adm])
    except UnboundLocalError:
     print("Нужно иметь права Администратора для достура к этому пункту")
    finally:
     break
     """
commands = {'/helps': helps,'/stats': status,'/getbd': dbcheck}
while True:
 comsend = input("Введите команду:")
 command = comsend
 if command in commands:
  commands[comsend]()
 else:
  print("Не найдено....")
  continue
