class Pessoa:
    olhos = 2
    boca = 1
    pernas = 2
    bracos = 2
    dedos_das_maos = 10
    dedos_dos_pes = 10
    nariz = 1
    orelhas = 2

    def __init__(self, nome, sobrenome, sexo, idade, comendo=False, falando=False):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.falando == True:
            print(f'{self.nome} está falando e por isso não pode comer.')
            return
        if self.comendo == False:
            print(f'{self.nome} começou a comer {alimento}')
            self.comendo = True
            return
        else:
            print(f'{self.nome} já esta comendo')
            return

    def falar(self, assunto):
        if self.comendo == True:
            print(f'{self.nome} está comendo e por isso não pode falar.')
            return
        if self.falando == False:
            print(f'{self.nome} começou a falar sobre {assunto}')
            self.falando = True
            return

        else:
            print(f'{self.nome} já esta falando.')
            return

    def parar_comer(self):
        if self.falando == True:
            print(f'{self.nome} já não está comendo porque esta falando.')
            return
        if self.comendo == False:
            print(f'{self.nome} não esta comendo')
            return
        else:
            print(f'{self.nome} parou de comer.')
            self.comendo = False
            return

    def parar_falar(self):
        if self.comendo == True:
            print(f'{self.nome} já não está falando porque esta comendo')
            return
        if self.falando == False:
            print(f'{self.nome} não esta falando')
            return
        else:
            print(f'{self.nome} parou de falar.')
            self.falando = False
            return


p1 = Pessoa('Djonatas', 'Borges', 'Masculino', 30)
print(p1.nome, p1.sobrenome, p1.sexo, p1.idade)
p1.comer('Maça')
p1.comer('Macarrão')
p1.falar('Python')
p1.parar_falar()
p1.parar_comer()
p1.falar('Python 3')
p1.falar('Django')
p1.comer('Maça')
p1.parar_comer()
p1.parar_falar()
print(f'{p1.nome} {p1.sobrenome} tem os {p1.olhos} olhos')
print(f'{p1.nome} {p1.sobrenome} tem as {p1.orelhas} orelhas')
print(f'{p1.nome} {p1.sobrenome} tem os {p1.bracos} braços')
print(f'{p1.nome} {p1.sobrenome} tem as {p1.pernas} pernas')
p1.dedos_das_maos = 8
print(f'{p1.nome} {p1.sobrenome} tem {p1.dedos_das_maos} dedos nas mãos.')


