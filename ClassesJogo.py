class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"
        
        print(f"O {self.tipo} atacou usando {ataque}")

heroi1 = Heroi("Aragorn", 87, "guerreiro")
heroi2 = Heroi("Gandalf", 2019, "mago")

heroi1.atacar()
heroi2.atacar()