from packages.BaseDados import BaseDados

class estoque(BaseDados):
    def __init__(self):
        super().__init__("estoque.json")

    def adicionar(self, nome, codigo, quantidade):
        if codigo in self.dados:
            self.dados[codigo]['quantidade'] += quantidade
            return "Já temos esse produto em estoque. Quantidade atualizada."
        else:
            self.dados[codigo] = {'nome': nome, 'quantidade': quantidade}
            self.salvar_dados()
            return "Produto adicionado ao estoque."
        

    def listar(self):
        if not self.dados:
            return "Nenhum produto está cadastrado no estoque."
        
        produtos = []
        for codigo, info in self.dados.items():
            produtos.append(f"Nome: {info['nome']} || Código: {codigo} || Quantidade: {info['quantidade']}")
        return "\n".join(produtos)

    def remover(self, codigo):
        if codigo in self.dados:
            del self.dados[codigo]
            self.salvar_dados()
            return "Produto retirado do estoque!"
        return "Produto não encontrado."

    def edit_prod(self, codigo, novo_nome, nova_quantidade=None):
        if codigo in self.dados:
            produto = self.dados[codigo]
            produto["nome"] = novo_nome
            if nova_quantidade is not None:
                produto["quantidade"] = nova_quantidade
            self.salvar_dados()
            return "Produto atualizado com sucesso!"
        return "Produto não encontrado."

    def limpar_tudo(self, confirmacao):
        if confirmacao.lower() == 's':
            self.dados = {}
            self.salvar_dados()
            return "Estoque completamente limpo!"
        return "Operação cancelada."
