
import json
import os

class estoque():
    def __init__(self):
        self.arquivo = "estoque.json"
        self.produtos = self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                return json.load(f)
        return {}

    def salvar_dados(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.produtos, f, indent=4)

    def adicionar_produto(self):
        nome = input("Nome do produto: ")
        codigo = input("Código de barras: ")
        quantidade = int(input("Quantidade do produto: "))

        if codigo in self.produtos.keys():
            self.produtos[codigo]['quantidade'] += quantidade
            print("\njá temos esse produto em estoque, a quantidade dele foi atualizada.")
        else:
            self.produtos[codigo] = {
                'nome': nome,
                'quantidade': quantidade
            }
            print("\nProduto adicionado ao estoque.")
        self.salvar_dados()

    def listar_prod(self):
        if not self.produtos:
            print("Nenhum produto esta cadastrado no estoque.")
            return
        print("\nProdutos no estoque:\n")
        for codigo, info in self.produtos.items():
            print(f"Nome: {info['nome']} || Código: {codigo} || Quantidade: {info['quantidade']}")

    def remover_prod(self):
        codigo = input("Qual produto deseja retirar do estoque?\n")
        if codigo in self.produtos:
            del self.produtos[codigo]
            self.salvar_dados()
            print("\nProduto retirado do estoque!")

    def edit_prod(self):
        codigo  = input("Qual o codigo do produto que deseja editar?\n")
        if codigo in self.produtos:
            produto = self.produtos[codigo]
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
            self.produtos = {}
            self.salvar_dados()
            print("\nEstoque completamente limpo!\n")
        else:
            return
