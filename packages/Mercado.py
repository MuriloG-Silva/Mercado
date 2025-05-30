class mercado():
    def __init__(self, nome, codigo, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        
    def __str__(self):
        return print(f"Nome: {self.nome} || Código: {self.codigo} || Quantidade: {self.quantidade}")
    