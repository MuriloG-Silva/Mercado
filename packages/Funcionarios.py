from packages.BaseDados import BaseDados

class funcionarios(BaseDados):
    def __init__(self):
        super().__init__("funcionarios.json")

    def adicionar(self, nome, codigo, salario):
        if codigo in self.dados:
            return "Esse funcionário já está cadastrado."
        else:
            self.dados[codigo] = {'nome': nome, 'quantidade': salario}
            self.salvar_dados()
            return "Funcionário adicionado ao sistema."

    def listar(self):
        if not self.dados:
            return "Nenhum funcionário está cadastrado."
        
        funcionarios = []
        for codigo, info in self.dados.items():
            funcionarios.append(f"Nome: {info['nome']} || Credencial: {codigo} || Salário: {info['quantidade']}")
        return "\n".join(funcionarios)

    def remover(self, codigo):
        if codigo in self.dados:
            del self.dados[codigo]
            self.salvar_dados()
            return "Funcionário removido do sistema!"
        return "Funcionário não encontrado."