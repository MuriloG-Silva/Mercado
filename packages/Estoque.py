
from packages.BaseDados import BaseDados

class estoque(BaseDados):
    def __init__(self):
        super().__init__("estoque.json")

    # Sobrescreve o método adicionar
    def adicionar(self):
        nome = input("Nome do produto: ")
        codigo = input("Código de barras: ")
        quantidade = int(input("Quantidade do produto: "))

        if codigo in self.dados:
            self.dados[codigo]['quantidade'] += quantidade
            print("\nJá temos esse produto em estoque. Quantidade atualizada.")
        else:
            self.dados[codigo] = {'nome': nome, 'quantidade': quantidade}
            print("\nProduto adicionado ao estoque.")
        self.salvar_dados()

    # Sobrescreve o método listar
    def listar(self):
        if not self.dados:
            print("Nenhum produto está cadastrado no estoque.")
            return
        print("\nProdutos no estoque:\n")
        for codigo, info in self.dados.items():
            print(f"Nome: {info['nome']} || Código: {codigo} || Quantidade: {info['quantidade']}")

    # Sobrescreve o método remover
    def remover(self):
        codigo = input("Qual produto deseja retirar do estoque?\n")
        if codigo in self.dados:
            del self.dados[codigo]
            self.salvar_dados()
            print("\nProduto retirado do estoque!")
            
    def edit_prod(self):
        codigo  = input("Qual o codigo do produto que deseja editar?\n")
        if codigo in self.dados:
            produto = self.dados[codigo]
            novo_nome = input("Qual o novo nome do produto?\n")
            produto["nome"] = novo_nome
            print("\nNome alterado com sucesso!\n")

            print("Deseja alterar a quantidade do produto? (s/n)")
            alt = input()
            if alt == "s" or alt == "S":
                nova_quant = int(input("Qual a nova quantidade do produto?\n"))
                produto["quantidade"] = nova_quant
                print("\nQuantidade alterada com sucesso!")
            self.salvar_dados()

    def limpar_tudo(self):
        print("\ndeseja limpar completamente o estoque? (s/n)")
        confirma = input()
        if confirma == "S" or confirma == "s":
            self.dados = {}
            self.salvar_dados()
            print("\nEstoque completamente limpo!\n")
        else:
            return
