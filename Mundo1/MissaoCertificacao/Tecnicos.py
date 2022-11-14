import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Ewidgets import Texto, Numerico
import pandas as pd
import os
from pathlib import Path
from Atualizatec import *
import Principal

# -------------------------------------------
# widgets


class Tecnicos(Frame):
    """
    Classe utilizada para cadastrar, editar ou excluir
    registros de técnicos.

    """

    def __init__(self, parent):
        super().__init__()
        self.app = None
        self.num = None
        self.image = Image.open('.\Layout\imagens\_back2.png')
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        self.background.winfo_height()
        self.background.winfo_width()
        self.center_frame = Frame(self, relief='raised', background='#B98D6B')
        self.center_frame.place(relx=0.35, rely=0.5, anchor='e')
        self.nome_label = ttk.Label(self.center_frame,
                                    text='NOME: ',
                                    font=('verdana', 10, 'bold'),
                                    background='#B98D6B',
                                    foreground='black')

        self.nome_entrada = Texto(self.center_frame,
                                  font=('verdana', 10, 'normal'),
                                  max_len=40)

        self.cpf_label = ttk.Label(self.center_frame,
                                   text='CPF: ',
                                   font=('verdana', 10, 'bold'),
                                   background='#B98D6B',
                                   foreground='black')
        self.cpf_entrada = Numerico(self.center_frame,
                                    font=('verdana', 10, 'normal'), max_len=11)

        self.telefone_label1 = ttk.Label(self.center_frame,
                                         text='RÁDIO: ',
                                         font=('verdana', 10, 'bold'),
                                         background='#B98D6B',
                                         foreground='black')

        self.telefone_entrada1 = Numerico(self.center_frame,
                                          font=('verdana', 10, 'normal'), max_len=8)

        self.telefone_label2 = ttk.Label(self.center_frame,
                                         text='CELULAR : ',
                                         font=('verdana', 10, 'bold'),
                                         background='#B98D6B',
                                         foreground='black')

        self.telefone_entrada2 = Numerico(self.center_frame,
                                          font=('verdana', 10, 'normal'), max_len=9)

        self.turno_label = ttk.Label(self.center_frame,
                                     text='TURNO: ',
                                     font=('verdana', 10, 'bold'),
                                     background='#B98D6B',
                                     foreground='black')

        self.combo_turno = ttk.Combobox(self.center_frame,
                                        values=['Manhã', 'Tarde', 'Noite'], takefocus=0, state='readonly')

        self.equipe_label = ttk.Label(self.center_frame,
                                      text='EQUIPE: ',
                                      font=('verdana', 10, 'bold'),
                                      background='#B98D6B',
                                      foreground='black')

        self.equipe_entrada = Texto(self.center_frame,
                                    font=('verdana', 10, 'normal'),
                                    max_len=30)

        self.cadastrar_btn = tk.Button(self.center_frame,
                                       text="CADASTRAR",
                                       font=('verdana', 10, 'bold'),
                                       background='#533227',
                                       foreground='white',
                                       command=self.concluirCad)

        self.atualizar_btn = tk.Button(self.center_frame,
                                       text="ATUALIZAR",
                                       font=('verdana', 10, 'bold'),
                                       background='#533227',
                                       foreground='white',
                                       command=self._atualizar_tec)

        self.spaceLin = ttk.Label(
            self.center_frame, background='#B98D6B', foreground='black')

# -------------------------------------------
# layout

        self.nome_label.grid(row=0, column=0, sticky='W', pady=2)
        self.nome_entrada.grid(row=0, column=1, sticky='W', pady=2, padx=5)
        self.cpf_label.grid(row=1, column=0, sticky='W', pady=2)
        self.cpf_entrada.grid(row=1, column=1, sticky='W', pady=2, padx=5)
        self.telefone_label1.grid(row=2, column=0, sticky='W', pady=2)

        self.telefone_entrada1.grid(
            row=2, column=1, sticky='W', pady=2, padx=5)

        self.telefone_label2.grid(row=3, column=0, sticky='W', pady=2)

        self.telefone_entrada2.grid(
            row=3, column=1, sticky='W', pady=2, padx=5)

        self.turno_label.grid(row=4, column=0, sticky='W', pady=2)
        self.combo_turno.grid(row=4, column=1, sticky='nsew', pady=2, padx=5)
        self.equipe_label.grid(row=5, column=0, sticky='W', pady=2)
        self.equipe_entrada.grid(row=5, column=1, sticky='W', pady=2, padx=5)
        self.spaceLin.grid(row=6, column=1, sticky='nsew', pady=2)
        self.cadastrar_btn.grid(row=7, column=1, sticky='nsew', pady=2)
        self.atualizar_btn.grid(row=8, column=1, sticky='nsew', pady=2)


# -------------------------------------------
# Funcoes


    def concluirCad(self):
        """
        Salva os dados digitados no arquivo '.csv'
        na pasta 'Documentos' do usuário.
        """

        resposta = messagebox.askokcancel(
            message='Deseja enviar o cadastro?')

        if resposta == True:
            if self.verifEntrada() == "Ok":
                user_profile = os.environ['USERPROFILE'] + \
                    '\Documents\\tecnicos.csv'
                user_documents = r'{}'.format(user_profile)
                path = Path(user_documents)

                if path.is_file():
                    A = False
                else:
                    A = True

                nome = self.nome_entrada.get()
                cpf = self.cpf_entrada.get()
                telefone1 = self.telefone_entrada1.get()
                telefone2 = self.telefone_entrada2.get()
                turno = self.combo_turno.get()
                equipe = self.equipe_entrada.get()

                data = [{'Nome': nome, 'CPF': cpf,
                        'Telefone1': telefone1,
                         'Telefone2': telefone2,
                         'Turno': turno,
                         'Equipe': equipe}]

                df = pd.DataFrame(
                    data, columns=['Nome', 'CPF', 'Telefone1', 'Telefone2', 'Turno', 'Equipe'])

                df.to_csv(user_documents, index=None, sep=';',
                          header=A, encoding='utf-8-sig', mode='a')

                messagebox.showinfo(
                    message='Cadastro efetuado com sucesso!')

                self.nome_entrada.delete(0, END)
                self.cpf_entrada.delete(0, END)
                self.telefone_entrada1.delete(0, END)
                self.telefone_entrada2.delete(0, END)
                self.combo_turno.set('')
                self.equipe_entrada.delete(0, END)

            else:
                messagebox.showinfo(message='Tente novamente')

    def verifEntrada(self):
        """
        Verifica os campos de entrada de dados

        """
        if self.nome_entrada.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Preencha o Nome')

        elif Texto.validacaocpf(self, self.cpf_entrada.get()) != True:
            pass

        elif self.telefone_entrada1.get() == '' and self.telefone_entrada2.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Preencha pelo menos um telefone')

        elif self.combo_turno.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Selecione o turno')

        elif self.equipe_entrada.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Preencha a equipe')

        else:
            return 'Ok'

    # Função para redimensionar a imagem
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

    def _atualizar_tec(self):
        """
        Funções do botão 'Atualizar'
        """
        if self.atualizar_btn['text'] == 'ATUALIZAR':
            openwin2 = Toplevel(self.master)
            self.app = Atualizatec(openwin2, self)
        else:
            if self.verifEntrada() == "Ok":
                nome = self.nome_entrada.get()
                cpf = self.cpf_entrada.get()
                telefone1 = self.telefone_entrada1.get()
                telefone2 = self.telefone_entrada2.get()
                turno = self.combo_turno.get()
                equipe = self.equipe_entrada.get()

                data = {'Nome': nome, 'CPF': cpf,
                        'Telefone1': telefone1,
                        'Telefone2': telefone2,
                        'Turno': turno,
                        'Equipe': equipe}

                user_profile = os.environ['USERPROFILE'] + \
                    '\Documents\\tecnicos.csv'
                user_documents = r'{}'.format(user_profile)
                df = pd.read_csv(user_documents, sep=';',
                                 dtype=str, encoding='utf-8-sig')
                newdf = df.drop(axis=0, index=self.num, inplace=True)
                newdf = df.update(newdf)
                df.loc[self.num] = list(data.values())
                df.sort_index(ascending=True, inplace=True)
                df.to_csv(user_documents, index=None, sep=';',
                          header=True, encoding='utf-8-sig', mode='w')

                messagebox.showinfo(
                    message='Atualização realizada com sucesso :)')
                self.refresh()

            else:
                messagebox.showinfo(message='Tente novamente')

    def refresh(self):
        raiz.destroy()
        Main()
        raiz.quit()

    def treeview_to_input(self, treeItem, num):
        """
        Recebe os valores do treeview da tela de atualização
        de técnicos (classe 'Atualizatec')
        """
        self.atualizar_btn['text'] = 'SALVAR'
        self.cadastrar_btn['state'] = 'disabled'
        self.nome_entrada.insert(0, treeItem[0])
        self.cpf_entrada.insert(0, treeItem[1])
        self.telefone_entrada1.insert(0, treeItem[2])
        self.telefone_entrada2.insert(0, treeItem[3])
        self.combo_turno.insert(0, treeItem[4])
        self.equipe_entrada.insert(0, treeItem[5])
        self.num = num


def Main():
    global raiz
    """
    Chamada da classe 'Tecnicos'
    """
    raiz = Tk()
    raiz.title("Cadastro de técnicos")
    raiz.geometry("960x540")
    raiz.minsize(960, 540)
    raiz.pack_propagate(False)
    raiz.foto_icone = ImageTk.PhotoImage(Image.open(
        '.\Layout\imagens\cadtec.bmp'))
    raiz.iconphoto(True, raiz.foto_icone)
    Apptec = Tecnicos(raiz).pack(fill=BOTH, expand=YES)
    raiz.protocol("WM_DELETE_WINDOW", on_closing)
    raiz.mainloop()


def on_closing():
    if messagebox.askokcancel("Sair", "Deseja sair do módulo de Técnicos"):
        raiz.destroy()
        raiz.quit()


if __name__ == "__main__":
    Main()
