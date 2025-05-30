
from packages.BaseDados import BaseDados

class funcionarios(BaseDados):
    def __init__(self):
        super().__init__("funcionarios.json")

    # Sobrescreve o método adicionar
    def adicionar(self):
        nome = input("Qual o nome do funcionário que deseja adicionar?\n")
        codigo = input("Qual a credencial desse funcionário?\n")
        quantidade = input("Qual o salário do funcionário?\n")

        if codigo in self.dados:
            print("\nEsse funcionário já está cadastrado.")
        else:
            self.dados[codigo] = {'nome': nome, 'quantidade': quantidade}
            print("\nFuncionário adicionado ao sistema.")
        self.salvar_dados()

    # Sobrescreve o método listar
    def listar(self):
        if not self.dados:
            print("Nenhum funcionário está cadastrado.")
            return
        print("\nFuncionários cadastrados:\n")
        for codigo, info in self.dados.items():
            print(f"Nome: {info['nome']} || Credencial: {codigo} || Salário: {info['quantidade']}")

    # Sobrescreve o método remover
    def remover(self):
        codigo = input("Qual a credencial do funcionário que deseja remover?\n")
        if codigo in self.dados:
            del self.dados[codigo]
            self.salvar_dados()
            print("\nFuncionário removido do sistema!")