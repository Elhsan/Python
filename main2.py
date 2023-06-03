import random
import pygame

# Приветствие
print("Добро пожаловать в програму Elshan_Game")
name = input("Как вас зовут: ")

# Именя пользователя
if name == "Elshan":
    print("Здавствуйте Elshan ака!", end='\n' )
elif name == "Alisher":
    print("Здавствуйте Алишер ака!", end='\n' )
else:
    print("Здавствуйте",name, end='!\n' )




# Секретный промокод для игры в змейку
promo = input("У вас есть промокод на нашу игру 'Змейка': ")
if promo == "да" or promo == "Да":
    proverka_promo = input("Введите промокод: ")
    if proverka_promo == "F8G4K9L2":
        print("Здавствуйте Создатель!", end='\n' )
        print("вы написали секретный код! \nвыберите настройки игры!")
        import time
        import random
        pygame.init()
        white = (255, 255, 255)
        yellow = (255, 255, 102)
        black = (0, 0, 0)
        red = (213, 50, 80)
        green = (0, 255, 0)
        blue = (50, 153, 213)
        dis_width = 800
        dis_height = 600
        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Змейка от Elshan_Game')
        clock = pygame.time.Clock()
        snake_block = 10
        snake_speed = 0
        vopros_skorost_zmeyki = input("Выберите сложность игры (1 - легий, 2 - средний, 3- сложный)\n")
        if vopros_skorost_zmeyki == "1":
            snake_speed = 7
        if vopros_skorost_zmeyki == "2":
            snake_speed = 13
        if vopros_skorost_zmeyki == "3":
            snake_speed = 18
        font_style = pygame.font.SysFont("1.jpg", 25)
        score_font = pygame.font.SysFont("comicsansms", 35)

        def Your_score(score):
           value = score_font.render("Ваш счёт: " + str(score), True, yellow)
           dis.blit(value, [0, 0])

        def our_snake(snake_block, snake_list):
           for x in snake_list:
               pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

        def message(msg, color):
           mesg = font_style.render(msg, True, color)
           dis.blit(mesg, [dis_width / 6, dis_height / 3])

        def gameLoop():
           game_over = False
           game_close = False
           x1 = dis_width / 2
           y1 = dis_height / 2
           x1_change = 0
           y1_change = 0
           snake_List = []
           Length_of_snake = 1
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           while not game_over:
               while game_close == True:
                   dis.fill(blue)
                   message("Вы проиграли! Нажмите Q для выхода\n или C для повторной игры", red)
                   Your_score(Length_of_snake - 1)
                   pygame.display.update()
                   for event in pygame.event.get():
                       if event.type == pygame.KEYDOWN:
                           if event.key == pygame.K_q:
                               game_over = True
                               game_close = False
                           if event.key == pygame.K_c:
                               gameLoop()
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       game_over = True
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_LEFT:
                           x1_change = -snake_block
                           y1_change = 0
                       elif event.key == pygame.K_RIGHT:
                           x1_change = snake_block
                           y1_change = 0
                       elif event.key == pygame.K_UP:
                           y1_change = -snake_block
                           x1_change = 0
                       elif event.key == pygame.K_DOWN:
                           y1_change = snake_block
                           x1_change = 0
               if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                   game_close = True
               x1 += x1_change
               y1 += y1_change
               dis.fill(blue)
               pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
               snake_Head = []
               snake_Head.append(x1)
               snake_Head.append(y1)
               snake_List.append(snake_Head)
               if len(snake_List) > Length_of_snake:
                   del snake_List[0]
               for x in snake_List[:-1]:
                   if x == snake_Head:
                       game_close = True
               our_snake(snake_block, snake_List)
               Your_score(Length_of_snake - 1)
               pygame.display.update()
               if x1 == foodx and y1 == foody:
                   foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                   foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                   Length_of_snake += 1
               clock.tick(snake_speed)
           pygame.quit()
           quit()
        gameLoop()
else:
    print("Хорошо")



# Обычное приложение
vopros_Polzovatelya = None
while vopros_Polzovatelya not in [1, 2]:
    vopros_Polzovatelya = int(input("Выберите опцию  (1 - зарегестрироваться 2 - войти в акаунт)\n   "))
    if int(vopros_Polzovatelya) == 1:
        reg_login = input("Введите адрес электронной почты: ")
        reg_parol = input("Введите проль: ")
        reg_parol2 = input("Введите проль повторно: ")
        prov_reg_parol = len(str(reg_parol))
        if int(prov_reg_parol) >= 8 and reg_login.endswith("@gmail.com"):
            if reg_parol == reg_parol2:
                print('Вы успешно зарегистрировались!') 
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
        else:
            print("Ваши пароль или логин неправильно введены")
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
                
 
        elif login_proverka != login and int(parol_proverka) != password:
            print("Логин или пароль неверны")
