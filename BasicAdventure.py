import random
import time
import bat as ba
import boss as bo
import player as p
import rooms as r
import squeleton as s


def main():

    ## Criação de personagem 
    print("\033[34mBem vindo ao BasicAdventure! Um jogo genérico de aventura, feito como um teste para exercitar conceitos de Python, divirta-se!\n","_"*125,"\033[m")
    time.sleep(2)
    choice_1 = input("Escolha entre as classes guerreiro ou mago, digite \"g\" ou \"m\": \nMagos dão mais dano, mas têm menos vida. ").lower()
    player = p.player()
    boss = bo.boss()
    boss.name = input("Quem é seu maior inimigo? ")

    match choice_1:
        case 'g':
            player.p_class = "Guerrreiro"
            player.name = input("Escolha seu nome: ")
            player.life = 60
            player.strength = 10
            player.attack_type = "Golpe de espada"
        case 'm':
            player.p_class = "Mago"
            player.name = input("Escolha seu nome: ")
            player.life = 40
            player.strength = 15
            player.attack_type = "Bola de fogo"
        case _:
            print("\033[31mDigite apenas g ou m!\033[m")
            main()

    ## Criação de salas e inimigos

    fst_room = r.rooms()
    s_room = r.rooms()
    t_room = r.rooms()
    fth_room = r.rooms()

    fst_room.name = "Primeira Sala"
    fst_room.bat = True
    fst_room.chest = True

    s_room.name = "Segunda Sala"
    s_room.corner = True
    s_room.squeleton = True

    t_room.name = "Terceira Sala"
    t_room.bat = True
    t_room.chest = True
    t_room.key = False

    fth_room.name = "Quarta Sala"
    fth_room.squeleton1 = True
    fth_room.squeleton2 = True
    fth_room.corner = True
    fth_room.chest = True
    fth_room.bat = True

    bat_1 = ba.bat()
    bat_2 = ba.bat()
    squeleton_1 = s.squeleton()
    squeleton_2 = s.squeleton()
    squeleton_3 = s.squeleton()

    ## Iniciar o jogo

    print("\nVocê acorda em uma sala escura sem se lembrar do que ocorreu na noite anterior, com uma dor irritante na cabeça.\n")
    time.sleep(2)
    print(f"Isso lhe enfurece mas te enche de energia, agora você lembra que seu nome é {player.name} e você é um {player.p_class} destemido.\n")
    time.sleep(2)
    print(f"Isso deve ser coisa do {boss.name}, vou encontrá-lo!\n")
    time.sleep(2)
    print("Você observa a sala ao seu redor para achar uma saída.")
    time.sleep(2)


    def death(): 
        print("\033[31mVocê morreu...\033[m")
        main()


    def show_status():
        print(f"\033[31mVida: {player.life}\033[m\n\033[34mForça: {player.strength}\033[m")


    def boss_room():
            print("\033[35mOlá.")
            time.sleep(2)
            print("\033[35mQue bom que você veio...")
            time.sleep(2)
            print(f"\033[35mSinceramente, eu estou cansado de todo esse ódio entre nós, {player.name}.")
            time.sleep(2)
            print("\033[35mPor quê não deixamos isso pra trás?")
            time.sleep(2)
            choice_6 = input(f"Você tem duas Opções:\n\033[34m1- Fazer as pazes\033[m\n\033[31m2- Lutar até a morte com {boss.name}\033[m\n"
                             "Digite \033[34m1\033[m ou \033[31m2\033[m para responder")
            
            match choice_6:
                case "1":
                    def ending():    
                        print("Mensagem fofa de pazes, jogo zerado pacifista")
                        choice_7 = input("Jogar de novo? Digite s ou n para responder: ")
                        match choice_7:
                            case "s":
                                main()
                            case "n":
                                print("Obrigado por jogar!")
                            case _:
                                print("\033[31mEntrada inválida!\033[m")
                                time.sleep(2)
                                ending()
                    ending()

                case _:
                    print("\033[31mEntrada inválida!\033[m")
                    time.sleep(2)
                    boss_room()


    def fourth_room():
        print("_"*20,"\nQuarta sala.")
        show_status()
        time.sleep(2)    
        print("Você tem 5 opções:\n1- Ir à segunda sala.\n2- Ir à terceira sala.\n3- Há dois esqueletos em frente a uma porta, lutar?\n4- Há um canto escuro, explorar?"
                        "\n5- Abrir baú.")
        time.sleep(2)    
        choice_4 = input("Digite 1, 2, 3, 4 ou 5 para escolher sua ação. ").lower()

        match choice_4:
            case "1":
                print("Você decide ir á  segunda sala.")
                time.sleep(2)
                second_room()
                
            case "2":
                print("Você decide ir à terceira sala.")
                time.sleep(2)
                third_room()
                
            case "3":
                print("Você decide enfrentar os dois esqueletos!")
                time.sleep(2)
                if fth_room.squeleton1 == True and fth_room.squeleton2 == True:
                    print('_'*20)
                    print("Entrando em batalha! ")
                    time.sleep(2)
                        
                    while squeleton_2.life > 0 and player.life > 0:
                        print(f"Você ataca com {player.attack_type}! ")
                        squeleton_2.life -= player.strength
                        time.sleep(2)
                        print(f"O esqueleto te ataca com {squeleton_2.attack_type}")
                        player.life -= squeleton_2.strength
                        time.sleep(2)
                    fth_room.squeleton1 = False
                        
                    if squeleton_2.life <= 0:
                        print("Você matou o primeiro esqueleto! ")
                        print('_'*20)
                        time.sleep(2)

                    if player.life <= 0:
                        death()

                    print('_'*20)
                    print("Entrando em batalha! ")
                    time.sleep(2)
                    
                    while squeleton_3.life > 0 and player.life > 0:
                        print(f"Você ataca com {player.attack_type}! ")
                        squeleton_3.life -= player.strength
                        time.sleep(2)
                        print(f"O esqueleto te ataca com {squeleton_3.attack_type}")
                        player.life -= squeleton_3.strength
                        time.sleep(2)
                    fth_room.squeleton2 = False
                        
                    if squeleton_3.life <= 0:
                        print("Você matou o segundo esqueleto! ")
                        time.sleep(2)

                    if player.life <= 0:
                        death()
                        
                if t_room.key == True:
                    time.sleep(2)
                    print("Você encontrou uma porta trancada, deseja abrir e entrar?\n\033[31mAviso! Essa decisão te levará ao fim do jogo!\033[m")
                    time.sleep(2)
                    choice_5 = input("Digite \"s\" ou \"n\", para sim ou não. " ).lower()
                        
                    match choice_5:
                        case "s":
                            time.sleep(2)
                            print("Você decide entrar na sala.")
                            time.sleep(2)
                            boss_room()
                        case "n":
                            time.sleep(2)
                            print("Voltando a explorar.")
                            time.sleep(2)
                            fourth_room()
                else: 
                    time.sleep(2)
                    print("Você encontrou uma porta, mas está trancada, continue explorando...")
                    time.sleep(2)
                    fourth_room()

            case "4":
                print("Você decide explorar o canto escuro...")
                time.sleep(2)
                
                if fth_room.corner == True:
                    print("Você achou um item de força, sua força aumenta!")
                    player.strength += random.randint(1,5)
                    fth_room.corner = False
                    fourth_room()

                else:
                    time.sleep(2)
                    print("Não tem nada aqui...")
                    time.sleep(2)
                    fourth_room()
            
            case "5":
                print("Você decide abrir o baú.")
                time.sleep(2)

                if fth_room.chest == True:
                    print("Você achou uma poção de cura! ")
                    player.life += random.randint(5,20)
                    fth_room.chest = False
                    fourth_room()

                else:
                    time.sleep(2)
                    print("Está vazio...")
                    time.sleep(2)
                    fourth_room()
            
            case _:
                    print("\033[31mEntrada inválida!\033[m")
                    time.sleep(2)
                    fourth_room()

                            
    def third_room():
            print("_"*20,"\nTerceira sala.")
            show_status()
            time.sleep(2)    
            print("Você tem 5 opções:\n1- Ir à primeira sala.\n2- Ir à segunda sala.\n3- Abrir a porta à sua frente.\n4- Há um canto escuro, explorar?"
                            "\n5- Abrir o baú.")
            time.sleep(2)    
            choice_4 = input("Digite 1, 2, 3, 4 ou 5 para escolher sua ação. ")

            match choice_4:
                case "1":
                    print("Você decide ir á  primeira sala")
                    time.sleep(2)
                    first_room()
                
                case "2":
                    print("Você decide ir à segunda sala.")
                    time.sleep(2)
                    second_room()

                case "3":
                    print("Você decide abrir a porta a sua frente.")
                    time.sleep(2)
                    fourth_room()

                case "4":
                    print("Você decide explorar o canto escuro...")
                    time.sleep(2)
                    print("Você achou um morcego!")
                    time.sleep(2)
                    
                    if t_room.bat == True:
                        print('_'*20)
                        print("Entrando em batalha! ")
                        time.sleep(2)
                        
                        while bat_2.life > 0 and player.life > 0:
                            print(f"Você ataca com {player.attack_type}! ")
                            bat_2.life -= player.strength
                            time.sleep(2)
                            print(f"O morcego te ataca com {bat_2.attack_type}")
                            player.life -= bat_1.strength
                            time.sleep(2)
                        t_room.bat = False
                        
                        if bat_2.life <= 0:
                            print("Você matou o morcego! ")
                            time.sleep(2)
                            third_room()

                        if player.life <= 0:
                            death()
                        
                    else:
                        time.sleep(2)
                        print("Ele já estava morto... ")
                        time.sleep(2)
                        third_room()
                    
                case "5":
                    print("Você decide abrir o baú...")
                    time.sleep(2)
                    print("Você abre o baú.")
                    time.sleep(2)
                    
                    if t_room.chest == True:
                        print("Vocẽ achou uma chave! ")
                        t_room.key = True
                        t_room.chest = False
                        time.sleep(2)
                        third_room()
                    
                    else:
                        print("O baú está vazio...")
                        time.sleep(2)
                        third_room()

                case _:
                    print("\033[31mEntrada inválida!\033[m")
                    time.sleep(2)
                    third_room()


    def first_room():
        print("_"*20,"\nPrimeira sala.\n")
        show_status()
        time.sleep(2)
        print("Você tem 4 opções:\n1- Abrir a porta à sua direita.\n2- Abrir a porta à sua frente.\n3- Há um canto escuro, explorar?"
              "\n4- Abrir o baú á sua esquerda.")
        time.sleep(2)    
        choice_2 = input("Digite 1, 2, 3 ou 4 para escolher sua ação. ")
        
        match choice_2:
            case "1":
                print("Você escolhe entrar na porta a sua direita. ")
                time.sleep(2)
                second_room()
            
            case "2":
                print("Você escolhe entrar na porta à sua frente. ")
                time.sleep(2)
                third_room()
            
            case "3":
                print("Você decide explorar o canto escuro...")
                time.sleep(2)
                print("Você achou um morcego!")
                time.sleep(2)
                
                if fst_room.bat == True:
                    print('_'*20)
                    print("Entrando em batalha! ")
                    time.sleep(2)
                    
                    while bat_1.life > 0 and player.life > 0:
                        print(f"Você ataca com {player.attack_type}! ")
                        bat_1.life -= player.strength
                        time.sleep(2)
                        print(f"O morcego te ataca com {bat_1.attack_type}")
                        player.life -= bat_1.strength
                        time.sleep(2)
                    fst_room.bat = False
                    
                    if bat_1.life <= 0:
                        print("Você matou o morcego! ")
                        time.sleep(2)
                        first_room()

                    if player.life <= 0:
                        death()

                else:
                    time.sleep(2)
                    print("Ele já estava morto... ")
                    time.sleep(2)
                    first_room()

            case "4":  
                print("Você decide abrir o baú...")
                time.sleep(2)
                print("Você abre o baú.")
                time.sleep(2)
                
                if fst_room.chest == True:
                    print("Vocẽ achou uma poção de vida! ")
                    player.life += random.randint(5,20)
                    fst_room.chest = False
                    time.sleep(2)
                    first_room()
                
                else:
                    print("O baú está vazio...")
                    time.sleep(2)
                    first_room()

            case _:
                print("\033[31mEntrada inválida!\033[m")
                time.sleep(2)
                first_room()


    def second_room():
        print("_"*20,"\nSegunda sala.")
        show_status()
        time.sleep(2)    
        print("Você tem 5 opções:\n1- Ir à primeira sala.\n2- Abrir a porta à sua direita.\n3- Abrir a porta à sua frente.\n4- Há um canto escuro, explorar?"
                        "\n5- Conversar com uma figura humanóide presente.")
        time.sleep(2)    
        choice_3 = input("Digite 1, 2, 3, 4 ou 5 para escolher sua ação. ").lower()
        
        match choice_3:
            case "1":
                print("Você decide voltar.")
                first_room()
            
            case "2":
                print("Você escolhe entrar na porta a sua direita. ")
                time.sleep(2)
                third_room()
            
            case "3":
                print("Você escolhe entrar na porta à sua frente. ")
                time.sleep(2)
                fourth_room()
            
            case "4":
                print("Você decide explorar o canto escuro...")
                time.sleep(2)
                
                if s_room.corner == True:
                    print("Você achou um item de força, sua força aumenta!")
                    player.strength += random.randint(1,5)
                    s_room.corner = False
                    second_room()

                else:
                    time.sleep(2)
                    print("Não tem nada aqui...")
                    time.sleep(2)
                    second_room()

            case "5":  
                print("Você decide falar com a figura humanóide...")
                time.sleep(2)
                print("Você achou um esqueleto!")
                time.sleep(2)
                
                if s_room.squeleton == True:
                    print('_'*20)
                    print("Entrando em batalha! ")
                    time.sleep(2)
                    
                    while squeleton_1.life > 0 and player.life > 0:
                        print(f"Você ataca com {player.attack_type}! ")
                        squeleton_1.life -= player.strength
                        time.sleep(2)
                        print(f"O esqueleto te ataca com {squeleton_1.attack_type}")
                        player.life -= squeleton_1.strength
                        time.sleep(2)
                    s_room.squeleton = False
                    
                    if squeleton_1.life <= 0:
                        print("Você matou o esqueleto! ")
                        time.sleep(2)
                        second_room()

                    if player.life <= 0:
                        death()

                else:
                    time.sleep(2)
                    print("Ele já estava morto...")
                    time.sleep(2)
                    second_room()

            case _:
                print("\033[31mEntrada inválida!\033[m")
                time.sleep(2)
                second_room()


    first_room() ## Comando que inicializa o jogo


if __name__ == '__main__':
    main()
