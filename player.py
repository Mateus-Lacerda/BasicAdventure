from BasicAdventure import main

class player:
    
    def __init__(self, p_class):
        self.p_class = p_class

        if p_class == 'g':
            self.p_class = "Guerrreiro"
            self.name = input("Escolha seu nome: ")
            self.life = 70
            self.strength = 15
            self.attack_type = "Golpe de espada"
        
        elif p_class == 'm':
            self.p_class = "Mago"
            self.name = input("Escolha seu nome: ")
            self.life = 50
            self.strength = 20
            self.attack_type = "Bola de fogo"
        
        else: 
            print("\033[31mDigite apenas g ou m!\033[m")
            main()
