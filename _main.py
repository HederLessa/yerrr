from _categoria import Categoria
from _transacao import Transacao

c = Categoria(nome="Receita")

t1 = Transacao(
    descricao= "Salario jan/2024",
    valor= 1000.9,
    categoria= c
    )
t1.exibir()