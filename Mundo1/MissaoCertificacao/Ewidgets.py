import tkinter as tk
from tkinter import Checkbutton, ttk, messagebox, TRUE, END
from validate_docbr import CPF


class Texto(ttk.Entry):
    def __init__(self, master=None, max_len=40, **kwargs):
        self.var = tk.StringVar()
        self.max_len = max_len
        ttk.Entry.__init__(
            self, master, textvariable=self.var, **kwargs, width=20)
        self.old_value = ''
        self.var.trace('w', self.check)

    def getvar(self):
        return self.get()

    def check(self, *args):
        if len(self.get()) <= self.max_len:
            self.old_value = self.get()  # accept change
        else:
            self.var.set(self.old_value)  # reject change

    # Função da validação do CPF
    def validacaocpf(self, docbr):
        docbr = CPF()
        if docbr.validate(self.cpf_entrada.get()) == True:
            return True
        else:
            messagebox.showerror(
                'Ops, algo deu errado :(', 'CPF Inválido \n\n Por favor, digite um CPF válido')
            self.cpf_entrada.delete(0, END)
            self.cpf_entrada.insert(0, '')


class Numerico(ttk.Entry):
    def __init__(self, master=None, max_len=8, **kwargs):
        self.var = tk.StringVar()
        self.max_len = max_len
        ttk.Entry.__init__(
            self, master, textvariable=self.var, **kwargs, width=20)
        self.old_value = ''
        self.var.trace('w', self.check)

    def check(self, *args):
        if len(self.get()) <= self.max_len and self.get().isnumeric() == True:
            self.old_value = self.get()  # accept change
        elif self.get() == '':
            self.old_value = self.get()
        else:
            self.var.set(self.old_value)  # reject change
            

