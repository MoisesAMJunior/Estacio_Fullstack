from logging import root
from msilib.schema import ComboBox
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
import os
from pathlib import Path
from tktooltip import ToolTip
from tkcalendar import *
from datetime import datetime
import Principal

# -------------------------------------------
# widgets


class Reserva(Frame):
    """
    Classe para reserva de Ferramentas
    """

    def __init__(self, parent):
        super().__init__()
        self._getterVar()
        self.app = None
        self.num = None
        self.image = Image.open('.\Layout\imagens\_back4.png')
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
        self.center_frame = Frame(self, relief='raised', background='#548235')
        self.center_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.lbl_id = ttk.Label(self.center_frame,
                                text='Id: ',
                                font=('verdana', 10, 'bold'),
                                background='#548235',
                                foreground='White')

        self.lbl_desc = ttk.Label(self.center_frame,
                                  text='Descrição da solicitação: ',
                                  font=('verdana', 10, 'bold'),
                                  background='#548235',
                                  foreground='White')

        self.lbl_retirada = ttk.Label(self.center_frame,
                                      text='Data e hora da retirada: ',
                                      font=('verdana', 10, 'bold'),
                                      background='#548235',
                                      foreground='White')

        self.lbl_devolucao = ttk.Label(self.center_frame,
                                       text='Data e hora prevista de devolução: ',
                                       font=('verdana', 10, 'bold'),
                                       background='#548235',
                                       foreground='White')

        self.lbl_tecnico = ttk.Label(self.center_frame,
                                     text='Técnico responsável pela retirada: ',
                                     font=('verdana', 10, 'bold'),
                                     background='#548235',
                                     foreground='White')

        self.spaceLin = ttk.Label(self.center_frame, background='#548235')

        self.inp_id = ttk.Entry(
            self.center_frame, textvariable=self.inptId, width=40, name='id')

        self.inp_desc = ttk.Entry(
            self.center_frame, textvariable=self.inptDesc, width=40, name='descricao')

        self.inp_retirada = DateEntry(
            self.center_frame, textvariable=self.inptRetirada, width=12, name='retirada')

        self.inp_devolucao = DateEntry(
            self.center_frame, textvariable=self.inptDevolucao, width=12, name='devolucao')

        self.hourR = tk.Spinbox(self.center_frame, from_=0, to=23, wrap=True,
                                textvariable=self.hourstrR, width=2, name='hora_retirada')

        self.minR = tk.Spinbox(self.center_frame, from_=0, to=59, wrap=True,
                               textvariable=self.minstrR, width=2, name='minutos_retirada')

        self.hourD = tk.Spinbox(self.center_frame, from_=0, to=23, wrap=True,
                                textvariable=self.hourstrD, width=2, name='hora_devolucao')

        self.minD = tk.Spinbox(self.center_frame, from_=0, to=59, wrap=True,
                               textvariable=self.minstrD, width=2, name='minutos_devolucao')

        user_profile = os.environ['USERPROFILE'] + \
            '\Documents\\tecnicos.csv'
        user_documents = r'{}'.format(user_profile)
        df = pd.read_csv(user_documents, sep=';',
                         dtype=str, encoding='utf-8-sig')

        tecs = list(df['Nome'].unique())
        self.inp_tecnico = ttk.Combobox(
            self.center_frame, textvariable=self.inptTecnico, width=37, values=tecs, state='readonly')

        self.btn_reservar = tk.Button(self.center_frame,
                                      font=('verdana', 10, 'bold'),
                                      text='RESERVAR',
                                      background='#273C18',
                                      foreground='white',
                                      width=12,
                                      command=self.concluirCad)


# -------------------------------------------
# Dicas de navegação

        self.tips = ToolTip(self.inp_desc,
                            msg='Descreva a finalidade da solicitação',
                            delay=0,
                            parent_kwargs={"bg": "black",
                                           "padx": 5, "pady": 5},
                            fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

# -------------------------------------------
# bind

        self.hourR.bind('<Any-KeyPress>', self.onValidate)
        self.hourD.bind('<Any-KeyPress>', self.onValidate)
        self.minD.bind('<Any-KeyPress>', self.onValidate)
        self.minR.bind('<Any-KeyPress>', self.onValidate)


# -------------------------------------------
# layout
        self.lbl_id.grid(row=0, column=0, sticky='W', pady=2)
        self.lbl_desc.grid(row=1, column=0, sticky='W', pady=2)
        self.lbl_retirada.grid(row=2, column=0, sticky='W', pady=2)
        self.lbl_devolucao.grid(row=3, column=0, sticky='W', pady=2)
        self.lbl_tecnico.grid(row=4, column=0, sticky='W', pady=2)

        self.inp_id.grid(row=0, column=1, sticky='W', pady=2)
        self.inp_desc.grid(row=1, column=1, sticky='W', pady=2)
        self.inp_retirada.grid(row=2, column=1, sticky='W', pady=2)
        self.inp_devolucao.grid(row=3, column=1, sticky='W', pady=2)
        self.inp_tecnico.grid(row=4, column=1, sticky='W', pady=2)

        self.hourR.grid(row=2, column=1, sticky='W', padx=105)
        self.minR.grid(row=2, column=1, sticky='W', padx=135)
        self.hourD.grid(row=3, column=1, sticky='W', padx=105)
        self.minD.grid(row=3, column=1, sticky='W', padx=135)

        self.spaceLin.grid(row=10, column=0, sticky='W', pady=2)
        self.btn_reservar.grid(row=11, column=1, sticky='W', pady=2)

# -------------------------------------------
# Funcoes

    def onValidate(self, event):
        """
        Função que valida o texto ao digitar no tk.entry
        """
        wgtName = str(event.widget).split(".")[-1]

        if wgtName == 'hora_retirada':
            self.old_value = self.hourstrR.get()
            self.max_len = 2
            self.var = self.hourstrR

        elif wgtName == 'hora_devolucao':
            self.old_value = self.hourstrD.get()
            self.max_len = 2
            self.var = self.hourstrD

        elif wgtName == 'minutos_retirada':
            self.old_value = self.minstrR.get()
            self.max_len = 2
            self.var = self.minstrR

        elif wgtName == 'minutos_devolucao':
            self.old_value = self.minstrD.get()
            self.max_len = 2
            self.var = self.minstrD

        self.var.trace('w', self.check)

    def check(self, *args):
        """
        Verificação para saber se as entradas atendem aos critérios
        necessários.
        """
        if self.var == self.hourstrR or self.var == self.hourstrD:

            VarTime = str(self.var.get())
            Cond0 = VarTime.isnumeric() == True
            if Cond0 == True:
                Cond1 = len(VarTime) <= self.max_len
                Cond2 = int(VarTime) <= 23
                Cond3 = int(VarTime) >= 0

                if Cond1 == True and Cond2 == True and Cond3 == True:
                    self.old_value = self.var.get()
                else:
                    self.var.set(self.old_value)
            else:
                self.var.set(self.old_value)

        elif self.var == self.minstrR or self.var == self.minstrD:
            VarTime = str(self.var.get())
            Cond0 = VarTime.isnumeric() == True
            if Cond0 == True:
                Cond1 = len(VarTime) <= self.max_len
                Cond2 = int(VarTime) <= 59
                Cond3 = int(VarTime) >= 0

                if Cond1 == True and Cond2 == True and Cond3 == True:
                    self.old_value = self.var.get()
                else:
                    self.var.set(self.old_value)
            else:
                self.var.set(self.old_value)

    def _getterVar(self):
        """
        Função para definir variáveis para os principais widgets (Entry's)
        e para o botão de cadastro.
        """

        self.inptId = StringVar()
        self.inptDesc = StringVar()
        self.inptRetirada = StringVar()
        self.inptDevolucao = StringVar()
        self.inptTecnico = StringVar()
        self.hourstrR = StringVar()
        self.minstrR = StringVar()
        self.hourstrD = StringVar()
        self.minstrD = StringVar()

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

    def concluirCad(self):
        """
        Salva os dados digitados no arquivo '.csv'
        na pasta 'Documentos' do usuário.
        """

        resposta = messagebox.askokcancel(message='Deseja fazer a reserva?')

        if resposta == True:
            if self.verifEntrada() == "Ok":
                user_profile = os.environ['USERPROFILE'] + \
                    '\Documents\\reserva.csv'
                user_documents = r'{}'.format(user_profile)
                path = Path(user_documents)

                Id = self.inptId.get()
                Descricao = self.inptDesc.get()
                Retirada = str(self.inptRetirada.get()) + ' ' + \
                    str(self.hourstrR.get()) + ':' + str(self.minstrR.get())

                Devolucao = self.inptDevolucao.get() + ' ' + \
                    str(self.hourstrD.get()) + ':' + str(self.minstrD.get())

                Tecnico = self.inptTecnico.get()

                Formato = '%d/%m/%Y %H:%M'
                pdRetirada = datetime.strptime(Retirada, Formato)
                pdDevolucao = datetime.strptime(Devolucao, Formato)

                data = [{'Id': Id, 'Descricao': Descricao,
                        'Retirada': pdRetirada,
                         'Devolucao': pdDevolucao,
                         'Tecnico': Tecnico
                         }]

                df = pd.DataFrame(
                    data, columns=['Id', 'Descricao', 'Retirada', 'Devolucao', 'Tecnico'])

                if path.is_file():
                    A = False
                else:
                    A = True

                df.to_csv(user_documents, index=None, sep=';',
                          header=A, encoding='utf-8-sig', mode='a')

                messagebox.showinfo(
                    message='Reserva efetuada com sucesso!')

                self.refresh()

        else:
            messagebox.showinfo(message='Tente novamente')

    def verifEntrada(self):
        """
        Verifica os campos de entrada de dados

        """
        Id = self.inptId.get()
        Descricao = self.inptDesc.get()
        Retirada = str(self.inptRetirada.get()) + ' ' + \
            str(self.hourstrR.get()) + ':' + str(self.minstrR.get())

        Devolucao = self.inptDevolucao.get() + ' ' + \
            str(self.hourstrD.get()) + ':' + str(self.minstrD.get())

        Tecnico = self.inptTecnico.get()

        Formato = '%d/%m/%Y %H:%M'
        pdRetirada = datetime.strptime(Retirada, Formato)
        pdDevolucao = datetime.strptime(Devolucao, Formato)
        datetime_str = datetime.now().strftime('%Y-%m-%d %H:%M')
        datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

        # Ferramentas
        user_profile = os.environ['USERPROFILE'] + \
            '\Documents\\ferramentas.csv'
        user_documents = r'{}'.format(user_profile)

        df = pd.read_csv(user_documents, sep=';',
                         dtype=str, encoding='utf-8-sig')

        # Reserva
        user_profile2 = os.environ['USERPROFILE'] + \
            '\Documents\\reserva.csv'
        user_documents2 = r'{}'.format(user_profile2)

        path = Path(user_documents2)

        verif = Id in df['Id'].unique()

        if verif != True:

            messagebox.showerror(
                'Ops, algo deu errado :(', 'Por favor insira um ID de ferramenta válido')

        elif pdDevolucao <= pdRetirada:
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Data e hora da devolução'
                ' e data e hora de retirada não podem ser iguais \n \
                E a data de devolução não deve ser menor que a data de retirada.')

        elif Descricao == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'É necessário descrever o motivo da solicitação')

        elif Retirada == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Por favor, informe a data e a hora para retirada')

        elif Devolucao == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Por favor, informe a data e a hora de devolucao')

        elif Tecnico == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Informe qual é o técnico responsável pela retirada')

        elif path.is_file():
            df2 = pd.read_csv(user_documents2, sep=';',
                              dtype=str, encoding='utf-8-sig', header=0)

            if df2['Id'].str.contains(Id).any():
                DevolDatas = pd.DataFrame(
                    df2.set_index('Id').loc[Id, 'Devolucao'])
                DevolDatas['Devolucao'] = pd.to_datetime(
                    DevolDatas['Devolucao'], errors='coerce')

                if pdRetirada <= datetime_object:
                    messagebox.showerror(
                        'Ops, algo deu errado :(', 'Data de reserva inválida')

                elif DevolDatas['Devolucao'].max() >= pdRetirada:
                    messagebox.showerror(
                        'Ops, algo deu errado :(',
                        'Escolha outra data ou horário: \n A ferramenta estará uso nesse período')

                else:
                    return 'Ok'
            else:
                return 'Ok'

        else:
            return 'Ok'

    def refresh(self):
        raiz.destroy()
        Main()
        raiz.quit()


# -------------------------------------------
# GUI
def Main():
    """
    Chamada da classe 'Reserva'
    """
    global raiz
    raiz = Tk()
    raiz.title('Reserva de ferramentas')
    raiz.minsize(960, 540)
    raiz.pack_propagate(False)
    raiz.foto_icone = ImageTk.PhotoImage(Image.open(
        '.\Layout\imagens\cadtool.bmp'))
    raiz.iconphoto(True, raiz.foto_icone)
    frm = Reserva(raiz).pack(fill=BOTH, expand=YES)
    raiz.protocol("WM_DELETE_WINDOW", on_closing)
    raiz.mainloop()


def on_closing():
    if messagebox.askokcancel("Sair", "Deseja sair do módulo de Técnicos"):
        raiz.destroy()
        raiz.quit()


# -------------------------------------------
# Chamada Main
if __name__ == "__main__":
    Main()
