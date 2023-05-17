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
            player.life = 100
            player.strength = 10
            player.attack_type = "Golpe de espada"
        case 'm':
            player.p_class = "Mago"
            player.name = input("Escolha seu nome: ")
            player.life = 70
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
    bat_3 = ba.bat()
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


    def boss_room():
            # A fazer
            print()


    def fourth_room():
        print("_"*20,"\nQuarta sala.")
        time.sleep(2)    
        print("Você tem 5 opções:\nIr à segunda sala.\nIr à terceira sala.\nHá dois esqueletos em frente a uma porta, lutar?\nHá um canto escuro, explorar?"
                        "\nAbrir baú.")
        time.sleep(2)    
        choice_4 = input("Digite p1, p2, 2e, ce ou ba, respectivamente, para escolher sua ação. ").lower()

        match choice_4:
            case "p1":
                print("Você decide ir á  segunda sala.")
                time.sleep(2)
                second_room()
                
            case "p2":
                print("Você decide ir à terceira sala.")
                time.sleep(2)
                third_room()
                
            case "2e":
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

                    elif player.life <= 0:
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
                        print('_'*20)
                        time.sleep(2)

                    elif player.life <= 0:
                        death()
                        
                if t_room.key == True:
                    time.sleep(2)
                    print("Você encontrou uma porta trancada, deseja abrir e entrar?\n\033[31mAviso! Essa decisão te levará ao fim do jogo!\033[m")
                    time.sleep(2)
                    choice_5 = input("Digite \"s\" ou \"n\", para sim ou não.").lower()
                        
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

            case "ce":
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
            
            case "ba":
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
                    third_room()

            

                            
    def third_room():
            print("_"*20,"\nTerceira sala.")
            time.sleep(2)    
            print("Você tem 5 opções:\nIr à primeira sala.\nIr à segunda sala.\nAbrir a porta à sua frente.\nHá um canto escuro, explorar?"
                            "\nAbrir o baú.")
            time.sleep(2)    
            choice_4 = input("Digite p1, p2, p3, ce ou ba, respectivamente, para escolher sua ação. ")

            match choice_4:
                case "p1":
                    print("Você decide ir á  primeira sala")
                    time.sleep(2)
                    first_room()
                
                case "p2":
                    print("Você decide ir à segunda sala.")
                    time.sleep(2)
                    second_room()

                case "p3":
                    print("Você decide abrir a porta a sua frente.")
                    time.sleep(2)
                    fourth_room()

                case "ce":
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
                            print('_'*20)
                            time.sleep(2)
                            third_room()

                        elif player.life <= 0:
                            death()
                        
                    else:
                        time.sleep(2)
                        print("Ele já estava morto... ")
                        time.sleep(2)
                        first_room()
                    
                case "ba":
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
        print("_"*20,"\nPrimeira sala.\nVocê tem 4 opções:\nAbrir a porta à sua direita.\nAbrir a porta à sua frente.\nHá um canto escuro, explorar?"
                        "\nAbrir o baú á sua esquerda.")
        time.sleep(2)    
        choice_2 = input("Digite p1, p2, ce ou ba, respectivamente, para escolher sua ação. ").lower()
        
        match choice_2:
            case "p1":
                print("Você escolhe entrar na porta a sua direita. ")
                time.sleep(2)
                second_room()
            
            case "p2":
                print("Você escolhe entrar na porta à sua frente. ")
                time.sleep(2)
                third_room()
            
            case "ce":
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
                        print('_'*20)
                        time.sleep(2)
                        first_room()

                    elif player.life <= 0:
                        death()

                else:
                    time.sleep(2)
                    print("Ele já estava morto... ")
                    time.sleep(2)
                    first_room()

            case "ba":  
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
        time.sleep(2)    
        print("Você tem 5 opções:\nIr à primeira sala.\nAbrir a porta à sua direita.\nAbrir a porta à sua frente.\nHá um canto escuro, explorar?"
                        "\nConversar com uma figura humanóide presente.")
        time.sleep(2)    
        choice_3 = input("Digite p1, p2, p3, ce ou fh, respectivamente, para escolher sua ação. ").lower()
        
        match choice_3:
            case "p1":
                print("Você decide voltar.")
                first_room()
            
            case "p2":
                print("Você escolhe entrar na porta a sua direita. ")
                time.sleep(2)
                third_room()
            
            case "p3":
                print("Você escolhe entrar na porta à sua frente. ")
                time.sleep(2)
                fourth_room()
            
            case "ce":
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

            case "fh":  
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
                        print('_'*20)
                        time.sleep(2)
                        second_room()

                    elif player.life <= 0:
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


    def death(): 
        print("\033[31mVocê morreu...\033[m")
        main()


if __name__ == '__main__':
    main()