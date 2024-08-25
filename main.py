class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.idade = 20
    
    def exibir(self):
        print(self.nome, self.email, self.idade)

    def chamar_exibir(self):
        self.exibir()

guilherme = Cliente("Guilherme","guilherme@gmail.com")
print(guilherme.nome)
print(guilherme.email)

guilherme.exibir()
guilherme.chamar_exibir()

