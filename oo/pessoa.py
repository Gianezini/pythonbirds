class Pessoa:
    def __init__(self, nome=Non, idade=35):
        self.idade = idade
        self.nome = None

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Mauricio')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)
    print(p.idade)
