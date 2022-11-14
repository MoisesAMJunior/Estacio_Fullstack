from tkinter import Toplevel
from PIL import Image, ImageTk
from numpy import insert
import pandas as pd
from Tecnicos import *
import os


class Atualizatec:
    """
    TopLevel com treeview para seleção dos registros dos técnicos
    """

    def __init__(self, master, mainwin):
        super().__init__()
        self.master = master
        self.mainwin = mainwin
        self.master.title("Atualização de técnicos")
        self.master.geometry("960x540")
        self.master.resizable(False, False)
        self.master.configure(bg='#B98D6B')
        self.master.pack_propagate(False)
        style = ttk.Style()
        style.theme_use('clam')
        self.center_frame = Frame(
            self.master, relief='raised', background='#B98D6B')
        self.center_frame.winfo_height()
        self.center_frame.winfo_width()
        self.center_frame.place(relx=0.50, rely=0.02, anchor='n')
        self.btn_atualizar = tk.Button(self.center_frame,
                                       text='Editar',
                                       font=('verdana', 10, 'bold'),
                                       background='#533227',
                                       foreground='white',
                                       command=self.edit_item).pack(side=LEFT)

        self.btn_excluir = tk.Button(self.center_frame,
                                     text='Excluir',
                                     font=('verdana', 10, 'bold'),
                                     background='#533227',
                                     foreground='white',
                                     command=self.del_item).pack(side=LEFT)

        self.my_tree = ttk.Treeview(self.master, selectmode="browse")
        self.treescrolly = ttk.Scrollbar(self.my_tree, orient='vertical',
                                         command=self.my_tree.yview)

        self.treescrollx = ttk.Scrollbar(self.my_tree, orient='horizontal',
                                         command=self.my_tree.xview)

        user_profile = os.environ['USERPROFILE'] + '\Documents\\tecnicos.csv'
        user_documents = r'{}'.format(user_profile)

        self.df = pd.read_csv(user_documents, sep=';',
                              dtype=str, encoding='utf-8-sig')
        self.df.fillna('', inplace=True)

        self.my_tree['columns'] = list(self.df.columns)
        self.my_tree['show'] = 'headings'

        for column in self.my_tree['columns']:
            self.my_tree.column(column, anchor=CENTER)
            self.my_tree.heading(column, text=column)

        df_rows = self.df.to_numpy().tolist()

        for row in df_rows:
            self.my_tree.insert('', 'end', values=row)
            self.my_tree.pack(
                anchor='n', pady=100, ipadx=400, ipady=300)

        self.treescrollx.pack(side='bottom', fill='x')
        self.treescrolly.pack(side='right', fill='y')
        self.my_tree.configure(
            xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set)

    def del_item(self):
        """
        Função para deletar um registro da lista.
        """
        # Deleta o ítem selecionado
        user_profile = os.environ['USERPROFILE'] + '\Documents\\tecnicos.csv'
        user_documents = r'{}'.format(user_profile)

        selected_item = self.my_tree.selection()[0]
        item_index = self.my_tree.index(selected_item)
        self.my_tree.delete(selected_item)

        newdf = self.df.drop(axis=0, index=item_index, inplace=True)
        newdf = self.df.update(newdf)
        self.df.to_csv(user_documents, index=None, sep=';',
                       header=True, encoding='utf-8-sig', mode='w')

    def edit_item(self):
        """
        Função para editar um registro
        """
        messagebox.showinfo(
            message='Efetue as alterações necessárias e clique em "SALVAR"')

        selected = self.my_tree.focus()
        self._item = self.my_tree.item(selected, 'values')
        self.num = self.my_tree.index(selected)
        Tecnicos.treeview_to_input(
            self.mainwin, treeItem=self._item, num=self.num)
