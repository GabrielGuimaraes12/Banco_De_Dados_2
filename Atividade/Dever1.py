class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor


class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self):
        print(self.som)

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho


# Programa principal
nome = input("Digite o nome do elefante: ")
idade = int(input("Digite a idade do elefante: "))
especie = input("Digite a espécie do elefante: ")
cor = input("Digite a cor do elefante: ")
tamanho = input("Digite o tamanho do elefante: ")

if especie == "Africano":
    if idade < 10:
        som = "Paaah"
        tamanho = "pequeno"
    else:
        som = "PAHHHHHH"
        tamanho = "grande"
else:
    som = "Algum som aleatório"

elefante = Elefante(nome, idade, especie, cor, som, tamanho)

print("O som do elefante é:", end=" ")
elefante.trombar()
print("O tamanho do elefante é:", elefante.tamanho)
elefante.emitir_som()
elefante.mudar_cor("verde")
elefante.mudar_tamanho("médio")
print("Novo tamanho:", elefante.tamanho)
