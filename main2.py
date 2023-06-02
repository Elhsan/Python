import random

print("Добро пожаловать в програму Elshan_Game")
name = input("Как вас зовут: ")

if name == "Elshan2009":
    print("Здавствуйте Создатель!", end='\n' )
elif name == "Alisher":
    print("Здавствуйте Алишер ака!", end='\n' )
else:
    print("Здавствуйте",name, end='!\n' )




vopros_Polzovatelya = None
while vopros_Polzovatelya not in [1, 2]:
    vopros_Polzovatelya = int(input("Выберите опцию  (1 - зарегестрироваться 2 - войти в акаунт)\n   "))
    if int(vopros_Polzovatelya) == 1:
        reg_login = input("Введите адрес электронной почты: ")
        reg_parol = input("Введите проль: ")
        reg_parol2 = input("Введите проль повторно: ")
        if reg_parol == reg_parol2:
            print("Вы успешно зарегестрировались")
            vopros_Polzovatelya2 = None
            while vopros_Polzovatelya2 not in [1, 2, 3]:
                vopros_Polzovatelya2 = int(input("Выберите опцию (1 - игра угадай число, 2 - камень ножница или бумага, 3 - настройки): ")) 
                if vopros_Polzovatelya2 == 1:
                    print("Вы вошли в игру угадай число")
                    print("Добро пожаловать в игру угадай число для Python!")

                    secret_number = random.randint(1, 10) 
                    guess = None
                    tries = 0

                    while guess != secret_number:
                        guess = input("Угадайте число от 1 до 10: ")
                        tries += 1

                        if not guess.isdigit():
                            print("Пожалуйста, введите число")
                            continue
                        
                        guess = int(guess)

                        if guess > secret_number:
                            print("Меньше...")
                        elif guess < secret_number:
                            print("Больше...")
                        else:
                            print("Правильно! Вы угадали число за", tries, "попыток.")
                elif vopros_Polzovatelya2 == 2:
                   print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!\n")
                   while True:
                       print("Выберите: камень (к), ножницы (н) или бумагу (б): ")
                       player_choice = input().lower()
                   
                       if player_choice not in ('к', 'н', 'б'):
                           print("Вы выбрали неверный вариант, попробуйте еще раз!")
                           continue
                       
                       computer_choice = random.choice(['к', 'н', 'б'])
                       print("Компьютер выбрал", computer_choice)
                   
                       if player_choice == computer_choice:
                           print("Ничья!")
                       elif (player_choice == 'к' and computer_choice == 'н') or (player_choice == 'н' and computer_choice == 'б') or (player_choice == 'б' and computer_choice == 'к'):
                           print("Вы выиграли!")
                       else:
                           print("Вы проиграли!")
                   
                       play_again = input("Хотите сыграть еще раз? (да/нет): ")
                       if play_again.lower() != 'да':
                           break
                elif vopros_Polzovatelya2 == 3:
                    print("Вы вошли в Настройки здесь пока ничего нет")
                

        elif reg_parol != reg_parol2:
            print("Ваши пароль не савподают!!!")
    
    if int(vopros_Polzovatelya) == 2:
    
        login = "Elshanaliev2009"
        password = 123456789

        login_Alisher_aka = "AlisherXujanov"
        password_Alisher_aka = 12345
    
        login_proverka = input("Введите адрес электронной почты: ")
        parol_proverka = input("Введите проль: ")
    
        if  login == login_proverka and password == int(parol_proverka) or login_proverka == login_Alisher_aka and password_Alisher_aka == int(parol_proverka):
            print("вы вошли в акаунт!")

            vopros_Polzovatelya2 = None
            while vopros_Polzovatelya2 not in [1, 2, 3]:
                vopros_Polzovatelya2 = int(input("Выберите опцию (1 - игра угадай число, 2 - настройки): "))

                if vopros_Polzovatelya2 == 1:
                    print("Вы вошли в игру угадай число")
                    print("Добро пожаловать в игру угадай число для Python!")

                    secret_number = random.randint(1, 10) 
                    guess = None
                    tries = 0

                    while guess != secret_number:
                        guess = input("Угадайте число от 1 до 10: ")
                        tries += 1

                        if not guess.isdigit():
                            print("Пожалуйста, введите число")
                            continue
                        
                        guess = int(guess)

                        if guess > secret_number:
                            print("Меньше...")
                        elif guess < secret_number:
                            print("Больше...")
                        else:
                            print("Правильно! Вы угадали число за", tries, "попыток.")
                elif vopros_Polzovatelya2 == 2:
                   print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!\n")
                   while True:
                       print("Выберите: камень (к), ножницы (н) или бумагу (б): ")
                       player_choice = input().lower()
                   
                       if player_choice not in ('к', 'н', 'б'):
                           print("Вы выбрали неверный вариант, попробуйте еще раз!")
                           continue
                       
                       computer_choice = random.choice(['к', 'н', 'б'])
                       print("Компьютер выбрал", computer_choice)
                   
                       if player_choice == computer_choice:
                           print("Ничья!")
                       elif (player_choice == 'к' and computer_choice == 'н') or (player_choice == 'н' and computer_choice == 'б') or (player_choice == 'б' and computer_choice == 'к'):
                           print("Вы выиграли!")
                       else:
                           print("Вы проиграли!")
                   
                       play_again = input("Хотите сыграть еще раз? (да/нет): ")
                       if play_again.lower() != 'да':
                           break
                elif vopros_Polzovatelya2 == 3:
                    print("Вы вошли в Настройки здесь пока ничего нет")
                
 
        elif login_proverka != login and int(parol_proverka) != password:
            print("Логин или пароль неверны")
    
        else:
            print("EROR")
