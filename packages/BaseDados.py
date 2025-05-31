import json
import os

class BaseDados:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                return json.load(f)
        return {}

    def salvar_dados(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.dados, f, indent=4)

    def adicionar(self):
        raise NotImplementedError("Método 'adicionar' deve ser implementado pela subclasse.")

    def listar(self):
        raise NotImplementedError("Método 'listar' deve ser implementado pela subclasse.")

    def remover(self):
        raise NotImplementedError("Método 'remover' deve ser implementado pela subclasse.")
