from packages.Estoque import estoque
from packages.Mercado import mercado
from packages.Menu import menu
from packages.Funcionarios import funcionarios
from packages.BaseDados import BaseDados
from packages.TkinterInterface import TkinterInterface
import tkinter as tk


def main():
    root = tk.Tk()
    app = TkinterInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()