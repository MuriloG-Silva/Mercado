import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from packages.Estoque import estoque
from packages.Funcionarios import funcionarios

class TkinterInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento")
        self.root.geometry("800x600")
        
        self.estoque = estoque()
        self.funcionarios = funcionarios()
        
        self.create_main_menu()

    def clear_window(self):
        """Limpa todos os widgets da janela"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_main_menu(self):
        """Cria o menu principal"""
        self.clear_window()
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(main_frame, text="Sistema de Gerenciamento", font=('Helvetica', 16)).pack(pady=10)
        
        ttk.Button(main_frame, text="Menu de Produtos", 
                  command=self.create_product_menu).pack(fill=tk.X, pady=5)
        ttk.Button(main_frame, text="Menu de Funcionários", 
                  command=self.create_employee_menu).pack(fill=tk.X, pady=5)
        ttk.Button(main_frame, text="Sair", 
                  command=self.root.quit).pack(fill=tk.X, pady=5)

    # ========== PRODUTOS ==========
    def create_product_menu(self):
        """Cria o menu de produtos"""
        self.clear_window()
        
        product_frame = ttk.Frame(self.root, padding="20")
        product_frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(product_frame, text="Menu de Produtos", font=('Helvetica', 14)).pack(pady=10)
        
        buttons = [
            ("Adicionar Produto", self.add_product_window),
            ("Listar Produtos", self.list_products_window),
            ("Remover Produto", self.remove_product_window),
            ("Editar Produto", self.edit_product_window),
            ("Limpar Estoque", self.clear_stock_window),
            ("Voltar", self.create_main_menu)
        ]
        
        for text, command in buttons:
            ttk.Button(product_frame, text=text, command=command).pack(fill=tk.X, pady=5)

    def add_product_window(self):
        """Janela para adicionar produto"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(frame, text="Adicionar Produto", font=('Helvetica', 14)).pack(pady=10)
        
        # Campos de entrada
        ttk.Label(frame, text="Nome do produto:").pack()
        self.nome_produto = ttk.Entry(frame)
        self.nome_produto.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text="Código de barras:").pack()
        self.codigo_produto = ttk.Entry(frame)
        self.codigo_produto.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text="Quantidade:").pack()
        self.quantidade_produto = ttk.Entry(frame)
        self.quantidade_produto.pack(fill=tk.X, pady=5)
        
        # Botões
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="Adicionar", command=self.execute_add_product).pack(side=tk.LEFT, expand=True)
        ttk.Button(btn_frame, text="Cancelar", command=self.create_product_menu).pack(side=tk.LEFT, expand=True)

    def execute_add_product(self):
        """Executa a adição de produto"""
        nome = self.nome_produto.get()
        codigo = self.codigo_produto.get()
        quantidade = self.quantidade_produto.get()
        
        if not nome or not codigo or not quantidade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
            
        try:
            quantidade = int(quantidade)
            resultado = self.estoque.adicionar(nome, codigo, quantidade)
            messagebox.showinfo("Sucesso", resultado)
            self.create_product_menu()
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro!")

    def list_products_window(self):
        """Janela para listar produtos"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(frame, text="Lista de Produtos", font=('Helvetica', 14)).pack(pady=10)
        
        # Área de texto com scroll
        text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=20)
        text_area.pack(expand=True, fill=tk.BOTH)
        
        produtos = self.estoque.listar()
        text_area.insert(tk.END, produtos)
        text_area.config(state=tk.DISABLED)
        
        ttk.Button(frame, text="Voltar", command=self.create_product_menu).pack(pady=10)

    def remove_product_window(self):
        """Janela para remover produto"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(frame, text="Remover Produto", font=('Helvetica', 14)).pack(pady=10)
        
        ttk.Label(frame, text="Código do produto:").pack()
        self.codigo_remover = ttk.Entry(frame)
        self.codigo_remover.pack(fill=tk.X, pady=5)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="Remover", command=self.execute_remove_product).pack(side=tk.LEFT, expand=True)
        ttk.Button(btn_frame, text="Cancelar", command=self.create_product_menu).pack(side=tk.LEFT, expand=True)

    def execute_remove_product(self):
        """Executa a remoção de produto"""
        codigo = self.codigo_remover.get()
        
        if not codigo:
            messagebox.showerror("Erro", "Código do produto é obrigatório!")
            return
            
        resultado = self.estoque.remover(codigo)
        messagebox.showinfo("Informação", resultado)
        self.create_product_menu()

    def edit_product_window(self):
        """Janela para editar produto (primeira etapa - buscar produto)"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(frame, text="Editar Produto", font=('Helvetica', 14)).pack(pady=10)
        
        ttk.Label(frame, text="Código do produto:").pack()
        self.codigo_editar = ttk.Entry(frame)
        self.codigo_editar.pack(fill=tk.X, pady=5)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="Buscar", command=self.execute_edit_product_search).pack(side=tk.LEFT, expand=True)
        ttk.Button(btn_frame, text="Cancelar", command=self.create_product_menu).pack(side=tk.LEFT, expand=True)

    def execute_edit_product_search(self):
        """Busca produto para edição"""
        codigo = self.codigo_editar.get()
        
        if not codigo:
            messagebox.showerror("Erro", "Código do produto é obrigatório!")
            return
            
        if codigo in self.estoque.dados:
            self.show_edit_product_details(codigo)
        else:
            messagebox.showinfo("Informação", "Produto não encontrado!")

    def show_edit_product_details(self, codigo):
        """Mostra detalhes do produto para edição"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(frame, text="Editar Produto", font=('Helvetica', 14)).pack(pady=10)
        
        # Obter detalhes do produto
        produto = self.estoque.dados[codigo]
        
        ttk.Label(frame, text="Novo nome:").pack()
        self.novo_nome = ttk.Entry(frame)
        self.novo_nome.insert(0, produto['nome'])
        self.novo_nome.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text="Nova quantidade:").pack()
        self.nova_quantidade = ttk.Entry(frame)
        self.nova_quantidade.insert(0, str(produto['quantidade']))
        self.nova_quantidade.pack(fill=tk.X, pady=5)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="Salvar", 
                  command=lambda: self.execute_save_product(codigo)).pack(side=tk.LEFT, expand=True)
        ttk.Button(btn_frame, text="Cancelar", 
                  command=self.create_product_menu).pack(side=tk.LEFT, expand=True)

    def execute_save_product(self, codigo):
        """Salva as alterações do produto"""
        novo_nome = self.novo_nome.get()
        nova_quantidade = self.nova_quantidade.get()
        
        if not novo_nome or not nova_quantidade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
            
        try:
            nova_quantidade = int(nova_quantidade)
            resultado = self.estoque.edit_prod(codigo, novo_nome, nova_quantidade)
            messagebox.showinfo("Sucesso", resultado)
            self.create_product_menu()
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro!")

    def clear_stock_window(self):
        """Janela de confirmação para limpar estoque"""
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja limpar todo o estoque?"):
            resultado = self.estoque.limpar_tudo('s')
            messagebox.showinfo("Informação", resultado)
            self.create_product_menu()

    # ========== FUNCIONÁRIOS ==========
    def create_employee_menu(self):
        """Cria o menu de funcionários"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(frame, text="Menu de Funcionários", font=('Helvetica', 14)).pack(pady=10)
        
        buttons = [
            ("Adicionar Funcionário", self.add_employee_window),
            ("Listar Funcionários", self.list_employees_window),
            ("Remover Funcionário", self.remove_employee_window),
            ("Voltar", self.create_main_menu)
        ]
        
        for text, command in buttons:
            ttk.Button(frame, text=text, command=command).pack(fill=tk.X, pady=5)

    def add_employee_window(self):
        """Janela para adicionar funcionário"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(frame, text="Adicionar Funcionário", font=('Helvetica', 14)).pack(pady=10)
        
        ttk.Label(frame, text="Nome do funcionário:").pack()
        self.nome_funcionario = ttk.Entry(frame)
        self.nome_funcionario.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text="Credencial:").pack()
        self.credencial_funcionario = ttk.Entry(frame)
        self.credencial_funcionario.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text="Salário:").pack()
        self.salario_funcionario = ttk.Entry(frame)
        self.salario_funcionario.pack(fill=tk.X, pady=5)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="Adicionar", command=self.execute_add_employee).pack(side=tk.LEFT, expand=True)
        ttk.Button(btn_frame, text="Cancelar", command=self.create_employee_menu).pack(side=tk.LEFT, expand=True)

    def execute_add_employee(self):
        """Executa a adição de funcionário"""
        nome = self.nome_funcionario.get()
        credencial = self.credencial_funcionario.get()
        salario = self.salario_funcionario.get()
        
        if not nome or not credencial or not salario:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
            
        resultado = self.funcionarios.adicionar(nome, credencial, salario)
        messagebox.showinfo("Informação", resultado)
        self.create_employee_menu()

    def list_employees_window(self):
        """Janela para listar funcionários"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(frame, text="Lista de Funcionários", font=('Helvetica', 14)).pack(pady=10)
        
        text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=20)
        text_area.pack(expand=True, fill=tk.BOTH)
        
        funcionarios = self.funcionarios.listar()
        text_area.insert(tk.END, funcionarios)
        text_area.config(state=tk.DISABLED)
        
        ttk.Button(frame, text="Voltar", command=self.create_employee_menu).pack(pady=10)

    def remove_employee_window(self):
        """Janela para remover funcionário"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(frame, text="Remover Funcionário", font=('Helvetica', 14)).pack(pady=10)
        
        ttk.Label(frame, text="Credencial do funcionário:").pack()
        self.credencial_remover = ttk.Entry(frame)
        self.credencial_remover.pack(fill=tk.X, pady=5)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="Remover", command=self.execute_remove_employee).pack(side=tk.LEFT, expand=True)
        ttk.Button(btn_frame, text="Cancelar", command=self.create_employee_menu).pack(side=tk.LEFT, expand=True)

    def execute_remove_employee(self):
        """Executa a remoção de funcionário"""
        credencial = self.credencial_remover.get()
        
        if not credencial:
            messagebox.showerror("Erro", "Credencial do funcionário é obrigatória!")
            return
            
        resultado = self.funcionarios.remover(credencial)
        messagebox.showinfo("Informação", resultado)
        self.create_employee_menu()