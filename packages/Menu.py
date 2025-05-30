from packages.Estoque import estoque

class menu():
    def __init__(self):
        self.estoque_atual = estoque()

    def menu(self):
        while True:
            menu_op = input("\nVocê deseja o menu de Produtos, menu de Funcionários ou sair do sistema?\n1. para Produtos\n2. para Funcionários\n3. para sair do sistema\n")
            if menu_op == "1":

                print("\n--------| Opções |-------\n")
                print("1. Adicionar um produto")
                print("2. Listar produtos no estoque")
                print("3. Remover um produto de estoque")
                print("4. Editar um produto")
                print("5. Limpar todo o estoque")
                print("6. Sair do sistema")
                opcao = input("\nEscolha uma das opções: ")

                if opcao == "1":
                    self.estoque_atual.adicionar_produto()
                elif opcao == "2":
                    self.estoque_atual.listar_prod()
                elif opcao =="3":
                    self.estoque_atual.remover_prod()
                elif opcao == "4":
                    self.estoque_atual.edit_prod()
                elif opcao == "5":
                    self.estoque_atual.limpar_tudo()
                elif opcao == "6":
                    print("\nSistema fechado.\n")
                    break
            
                else:
                    print("Número da operação incorreto, escolha uma opção listada acima!")

            elif menu_op == "2":

                print("\n--------| Opções |-------\n")
                print("1. Adicionar um funcionário")
                print("2. Listar os funcionários")
                print("3. Remover um funcionário")
                print("4. Sair do sistema")
                opcao = input("\nEscolha uma das opções: ")

                if opcao == "1":
                    self.estoque_atual.adicionar_func() 
                elif opcao == "2":
                    self.estoque_atual.listar_func()
                elif opcao == "3":
                    self.estoque_atual.remover_func()
                elif opcao == "4":
                    print("\nSistema fechado.\n")
                    break
                else:
                    print("Número da operação incorreto, escolha uma opção listada acima!")

            elif menu_op == "3":
                print("\nSistema fechado\n")
                break
            else:
                print("Número da operação incorreto, escolha uma opção listada acima!")

