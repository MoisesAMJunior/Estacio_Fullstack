import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import tkinter
from PIL import Image, ImageTk
import pandas as pd
import os
from pathlib import Path
from tktooltip import ToolTip
import Tecnicos
import Ferramentas
import Reserva
import os

# -------------------------------------------
# widgets


class Principal(Frame):
    """
    Classe para cadastro de Ferramentas
    """

    def __init__(self, parent):
        super().__init__()
        self.app = None
        self.image = Image.open(
            '.\Layout\imagens\_gerencial.png')
        TooltConf = ttk.Style()
        TooltConf.configure(
            "custom.TButton", foreground="#ffffff", background="#1c1c1c")
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        self.background.winfo_height()
        self.background.winfo_width()
        self.center_frame = Frame(self, relief='raised', background='#7F7F7F')
        self.center_frame.place(relx=0.2, rely=0.3, anchor='n')
        self.btn_tecnicos = tk.Button(self.center_frame,
                                      font=('verdana', 10, 'bold'),
                                      background='#595959',
                                      foreground='white',
                                      text='CADASTRAR TÉCNICOS',
                                      width=30,
                                      command=self.chamaTecnicos)

        self.btn_ferramentas = tk.Button(self.center_frame,
                                         font=('verdana', 10, 'bold'),
                                         background='#595959',
                                         foreground='white',
                                         text='CADASTRAR FERRAMENTAS',
                                         width=30,
                                         command=self.chamaFerramentas)

        self.btn_reserva = tk.Button(self.center_frame,
                                     font=('verdana', 10, 'bold'),
                                     background='#595959',
                                     foreground='white',
                                     text='RESERVA DE FERRAMENTAS',
                                     width=30,
                                     command=self.chamaReserva)

        self.btn_expFerramentas = tk.Button(self.center_frame,
                                            font=('verdana', 10, 'bold'),
                                            background='#595959',
                                            foreground='white',
                                            text='EXPORTAR LISTA DE FERRAMENTAS',
                                            width=30,
                                            command=self.exportarFerramentas)

        self.btn_expReservas = tk.Button(self.center_frame,
                                         font=('verdana', 10, 'bold'),
                                         background='#595959',
                                         foreground='white',
                                         text='EXPORTAR RESERVAS',
                                         width=30,
                                         command=self.exportarReservas)

        user_profile = os.environ['USERPROFILE'] + \
            '\Documents\\ferramentas.csv'
        user_documents = r'{}'.format(user_profile)

        path = Path(user_documents)

        user_profile2 = os.environ['USERPROFILE'] + \
            '\Documents\\reserva.csv'
        user_documents2 = r'{}'.format(user_profile2)

        path2 = Path(user_documents2)

        if path.is_file():
            pass
        else:
            self.btn_expFerramentas.config(state='disable')
            self.btn_reserva.config(state='disable')
            self.btn_expReservas.config(state='disable')

        if path2.is_file():
            pass
        else:
            self.btn_expReservas.config(state='disable')

# -------------------------------------------
# Dicas de navegação

        self.tips = ToolTip(self.btn_tecnicos,
                            msg='Manutenção do cadastro de técnicos',
                            delay=0,
                            parent_kwargs={"bg": "black",
                                           "padx": 5, "pady": 5},
                            fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

        self.tips = ToolTip(self.btn_ferramentas,
                            msg='Manutenção do cadastro de ferramentas',
                            delay=0,
                            parent_kwargs={"bg": "black",
                                           "padx": 5, "pady": 5},
                            fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

        self.tips = ToolTip(self.btn_reserva,
                            msg='Reserva de ferramentas para execução de manutenções',
                            delay=0,
                            parent_kwargs={"bg": "black",
                                           "padx": 5, "pady": 5},
                            fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

        self.tips = ToolTip(self.btn_expFerramentas,
                            msg='Exporta a lista de ferramentas cadastradas no sistema',
                            delay=0,
                            parent_kwargs={"bg": "black",
                                           "padx": 5, "pady": 5},
                            fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

        self.tips = ToolTip(self.btn_expReservas,
                            msg='Exporta a lista de reservas de ferramentas',
                            delay=0,
                            parent_kwargs={"bg": "black",
                                           "padx": 5, "pady": 5},
                            fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)


# -------------------------------------------
# layout
        self.btn_tecnicos.grid(row=0, column=0, sticky='NW', pady=5)
        self.btn_ferramentas.grid(row=1, column=0, sticky='NW', pady=5)
        self.btn_reserva.grid(row=2, column=0, sticky='NW', pady=5)
        self.btn_expFerramentas.grid(row=3, column=0, sticky='NW', pady=5)
        self.btn_expReservas.grid(row=4, column=0, sticky='NW', pady=5)


# -------------------------------------------
# Funcoes


    def _resize_image(self, event):
        """
        redimensiona a imagem de fundo conforme a dimensão
        da tela.
        """

        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

    def chamaTecnicos(self):
        os.system('Tecnicos.py')

    def chamaFerramentas(self):
        os.system('Ferramentas.py')

    def chamaReserva(self):
        os.system('Reserva.py')

    def exportarFerramentas(self):
        user_profile = os.environ['USERPROFILE'] + \
            '\Documents\\ferramentas.csv'

        FileXlsx = os.environ['USERPROFILE'] + \
            '\Documents\\Ferramentas.xlsx'

        user_documents = r'{}'.format(user_profile)
        FileConv = r'{}'.format(FileXlsx)

        path = Path(user_documents)
        ExportFile = Path(FileConv)

        OldFile = pd.read_csv(path, sep=';')
        NewFile = pd.ExcelWriter(ExportFile)
        OldFile.to_excel(NewFile, sheet_name="Ferramentas", index=False)
        NewFile.save()

        messagebox.showinfo(
            message='Lista de ferramentas exportada com sucesso! \n Verifique em '
            + FileConv)

    def exportarReservas(self):
        user_profile = os.environ['USERPROFILE'] + \
            '\Documents\\reserva.csv'

        FileXlsx = os.environ['USERPROFILE'] + \
            '\Documents\\Reservas.xlsx'

        user_documents = r'{}'.format(user_profile)
        FileConv = r'{}'.format(FileXlsx)

        path = Path(user_documents)
        ExportFile = Path(FileConv)

        OldFile = pd.read_csv(path, sep=';')
        NewFile = pd.ExcelWriter(ExportFile)
        OldFile.to_excel(NewFile, sheet_name="Reservas", index=False)
        NewFile.save()
        messagebox.showinfo(
            message='Lista de reservas exportada com sucesso! \n Verifique em '
            + FileConv)


# -------------------------------------------
# GUI


def Main():
    """
    Chamada da classe 'Principal'
    """
    global raiz
    raiz = Tk()
    raiz.title('Painel Gerencial')
    raiz.minsize(960, 540)
    raiz.pack_propagate(False)
    raiz.foto_icone = ImageTk.PhotoImage(Image.open(
        '.\Layout\imagens\cadtool.bmp'))
    raiz.iconphoto(True, raiz.foto_icone)
    frm = Principal(raiz).pack(fill=BOTH, expand=YES)
    raiz.mainloop()


# -------------------------------------------
# Chamada Main
if __name__ == "__main__":
    Main()
