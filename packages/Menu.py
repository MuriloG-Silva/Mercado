from packages.Funcionarios import funcionarios
from packages.Estoque import estoque

class menu():
    def __init__(self):
        self.estoque = estoque()
        self.funcionarios = funcionarios()

    def menu(self):
        while True:
            print("\nVocê deseja o menu de Produtos, menu de Funcionários ou sair do sistema?")
            print("1. para Produtos")
            print("2. para Funcionários")
            print("3. para abrir uma janela com a interface gráfica")
            menu_op = input()
            
            # Menu de Produtos (usa métodos polimórficos de 'estoque')
            if menu_op == "1":
                print("\n--------| Menu de Produtos |-------\n")
                print("1. Adicionar um produto")
                print("2. Listar produtos no estoque")
                print("3. Remover um produto de estoque")
                print("4. Editar produto")
                print("5. Limpar todo o estoque")
                print("6. Sair do sistema")
                opcao = input("\nEscolha uma das opções: ")

                if opcao == "1":
                    self.estoque.adicionar() 
                elif opcao == "2":
                    self.estoque.listar()    
                elif opcao == "3":
                    self.estoque.remover()   
                elif opcao == "4":
                    self.estoque.edit_prod()    
                elif opcao == "5":
                    self.estoque.limpar_tudo()
                elif opcao == "6":
                    print("\nSistema fechado.\n")
                    break
                else:
                    print("Opção inválida!")

            # Menu de Funcionários (usa métodos polimórficos de 'funcionarios')
            elif menu_op == "2":
                print("\n--------| Menu de Funcionários |-------\n")
                print("1. Adicionar um funcionário")
                print("2. Listar os funcionários")
                print("3. Remover um funcionário")
                print("4. Sair do sistema")
                opcao = input("\nEscolha uma das opções: ")

                if opcao == "1":
                    self.funcionarios.adicionar()  
                elif opcao == "2":
                    self.funcionarios.listar()    
                elif opcao == "3":
                    self.funcionarios.remover()  
                elif opcao == "4":
                    print("\nSistema fechado.\n")
                    break
                else:
                    print("Opção inválida!")

            elif menu_op == "3":
                print("\nSistema fechado\n")
                break
            else:
                print("Opção inválida!")