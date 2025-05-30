
import json
import os

class funcionarios():
    def __init__(self):
        self.arquivo2 = "funcionarios.json"
        self.funcionarios = self.carregar_dados2()

    #para carregar os dados dos funcionários
    def carregar_dados2(self):
        if os.path.exists(self.arquivo2):
            with open(self.arquivo2, "r") as f:
                return json.load(f)
        return {}

    #para salvar os dados dos funcionários
    def salvar_dados2(self):
        with open(self.arquivo2, "w") as f:
            json.dump(self.funcionarios, f, indent=4)

    def adicionar_func(self):
        nome = input("Qual o nome do funcionário que deseja adicionar?\n")
        codigo = input("Qual a credencial desse funcionário?\n")
        quantidade = input("Qual o salário do funcionário?\n")

        if codigo in self.funcionarios.keys():
            print("\nEsse funcionário já está cadastrado.")
        else:
            self.funcionarios[codigo] = {
                'nome': nome,
                'quantidade': quantidade
            }
            print("\nProduto adicionado ao estoque.")
        self.salvar_dados2()

    def listar_func(self):
        if not self.funcionarios:
            print("Nenhum funcionário está cadastrado.")
            return
        print("\nFuncionários cadastrados:\n")
        for codigo, info in self.funcionarios.items():
            print(f"Nome: {info['nome']} || Credencial: {codigo} || Salário: {info['quantidade']}")


    def remover_func(self):
        codigo = input("Qual a  credencial do funcionário que deseja remover?\n")
        if codigo in self.funcionarios:
            del self.funcionarios[codigo]
            self.salvar_dados2()
            print("\nFuncionário retirado do sistema!")