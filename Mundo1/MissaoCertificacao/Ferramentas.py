import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
import os
from pathlib import Path
import uuid
from collections import Counter
from Atualizafrmt import *
from tktooltip import ToolTip
import Principal

# -------------------------------------------
# widgets


class Ferramentas(Frame):
    """
    Classe para cadastro de Ferramentas
    """

    def __init__(self, parent):
        super().__init__()
        self._getterVar()
        self.app = None
        self.num = None
        self.image = Image.open('.\Layout\imagens\_back3.png')
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
        self.center_frame = Frame(self, relief='raised', background='#3E6676')
        self.center_frame.place(relx=0.35, rely=0.5, anchor='e')
        self.lbl_id = ttk.Label(self.center_frame,
                                text='Id: ',
                                font=('verdana', 10, 'bold'),
                                background='#3E6676',
                                foreground='White')

        self.lbl_desc = ttk.Label(self.center_frame,
                                  text='Descrição: ',
                                  font=('verdana', 10, 'bold'),
                                  background='#3E6676',
                                  foreground='White')

        self.lbl_fab = ttk.Label(self.center_frame,
                                 text='Fabricante: ',
                                 font=('verdana', 10, 'bold'),
                                 background='#3E6676',
                                 foreground='White')

        self.lbl_volt = ttk.Label(self.center_frame,
                                  text='Voltagem: ',
                                  font=('verdana', 10, 'bold'),
                                  background='#3E6676',
                                  foreground='White')

        self.lbl_prtnum = ttk.Label(self.center_frame,
                                    text='Part Number: ',
                                    font=('verdana', 10, 'bold'),
                                    background='#3E6676',
                                    foreground='White')

        self.lbl_tamanho = ttk.Label(self.center_frame,
                                     text='Tamanho: ',
                                     font=('verdana', 10, 'bold'),
                                     background='#3E6676',
                                     foreground='White')

        self.lbl_undMed = ttk.Label(self.center_frame,
                                    text='Unidade de medida: ',
                                    font=('verdana', 10, 'bold'),
                                    background='#3E6676',
                                    foreground='White')

        self.lbl_tipoFrmt = ttk.Label(self.center_frame,
                                      text='Tipo de ferramenta: ',
                                      font=('verdana', 10, 'bold'),
                                      background='#3E6676',
                                      foreground='White')

        self.lbl_material = ttk.Label(self.center_frame,
                                      text='Material: ',
                                      font=('verdana', 10, 'bold'),
                                      background='#3E6676',
                                      foreground='White')

        self.lbl_tempo = ttk.Label(self.center_frame,
                                   text='Tempo máximo de reserva: ',
                                   font=('verdana', 10, 'bold'),
                                   background='#3E6676',
                                   foreground='White')

        self.spaceLin = ttk.Label(self.center_frame, background='#3E6676')

        self.inp_id = ttk.Entry(
            self.center_frame, textvariable=self.inptId, width=20, state='disabled')

        self.inp_desc = ttk.Entry(
            self.center_frame, textvariable=self.inptDesc, width=20, name='descricao')

        self.inp_fab = ttk.Entry(
            self.center_frame, textvariable=self.inptFab, width=20, name='fabricante')

        self.inp_volt = ttk.Entry(
            self.center_frame, textvariable=self.inptVolt, width=20, name='voltagem')

        self.inp_prtnum = ttk.Entry(
            self.center_frame, textvariable=self.inptPrtnum, width=20, name='partnumber')

        self.inp_tamanho = ttk.Entry(
            self.center_frame, textvariable=self.inptTamanho, width=20, name='tamanho')

        self.inp_undMed = ttk.Entry(
            self.center_frame, textvariable=self.inptUndMed, width=20, name='uni_medida')

        self.inp_tipoFrmt = ttk.Entry(
            self.center_frame, textvariable=self.inptTipoFrmt, width=20, name='tipo')

        self.inp_material = ttk.Entry(
            self.center_frame, textvariable=self.inptMaterial, width=20, name='material')

        self.inp_tempo = ttk.Entry(
            self.center_frame, textvariable=self.inptTempo, width=20, name='tempo')

        self.btn_cadastrar = tk.Button(self.center_frame,
                                       font=('verdana', 10, 'bold'),
                                       background='#052335',
                                       foreground='white',
                                       textvariable=self.btncad,
                                       width=12,
                                       command=self.concluirCad)

        self.btn_atualizar = tk.Button(self.center_frame,
                                       font=('verdana', 10, 'bold'),
                                       background='#052335',
                                       foreground='white',
                                       textvariable=self.btnatualiza,
                                       width=12,
                                       command=self._atualizar_frmt)

# -------------------------------------------
# Dicas de navegação

        self.tips = ToolTip(self.inp_tempo,
                            msg='O formato digitado deve ser HH:MM:SS (horas, minutos e segundos)',
                            delay=0,
                            parent_kwargs={"bg": "black",
                                           "padx": 5, "pady": 5},
                            fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

        self.tips = ToolTip(self.inp_material,
                            msg='Se refere ao material da ferramenta. Ex.: Aço, madeira e etc.',
                            delay=0,
                            parent_kwargs={"bg": "black",
                                           "padx": 5, "pady": 5},
                            fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

        self.tips = ToolTip(self.inp_tipoFrmt,
                            msg='Ex.: Mecânica, elétrica, segurança e etc.',
                            delay=0,
                            parent_kwargs={"bg": "black",
                                           "padx": 5, "pady": 5},
                            fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)


# -------------------------------------------
# layout
        self.lbl_id.grid(row=0, column=0, sticky='W', pady=2)
        self.lbl_desc.grid(row=1, column=0, sticky='W', pady=2)
        self.lbl_fab.grid(row=2, column=0, sticky='W', pady=2)
        self.lbl_volt.grid(row=3, column=0, sticky='W', pady=2)
        self.lbl_prtnum.grid(row=4, column=0, sticky='W', pady=2)
        self.lbl_tamanho.grid(row=5, column=0, sticky='W', pady=2)
        self.lbl_undMed.grid(row=6, column=0, sticky='W', pady=2)
        self.lbl_tipoFrmt.grid(row=7, column=0, sticky='W', pady=2)
        self.lbl_material.grid(row=8, column=0, sticky='W', pady=2)
        self.lbl_tempo.grid(row=9, column=0, sticky='W', pady=2)

        self.inp_id.grid(row=0, column=1, sticky='W', pady=2)
        self.inp_desc.grid(row=1, column=1, sticky='W', pady=2)
        self.inp_fab.grid(row=2, column=1, sticky='W', pady=2)
        self.inp_volt.grid(row=3, column=1, sticky='W', pady=2)
        self.inp_prtnum.grid(row=4, column=1, sticky='W', pady=2)
        self.inp_tamanho.grid(row=5, column=1, sticky='W', pady=2)
        self.inp_undMed.grid(row=6, column=1, sticky='W', pady=2)
        self.inp_tipoFrmt.grid(row=7, column=1, sticky='W', pady=2)
        self.inp_material.grid(row=8, column=1, sticky='W', pady=2)
        self.inp_tempo.grid(row=9, column=1, sticky='W', pady=2)

        self.spaceLin.grid(row=10, column=0, sticky='W', pady=2)
        self.btn_cadastrar.grid(row=11, column=1, sticky='W', pady=2)
        self.btn_atualizar.grid(row=12, column=1, sticky='W', pady=2)

# -------------------------------------------
# bind

        self.inp_desc.bind('<Any-KeyPress>', self.onValidate)
        self.inp_desc.bind('<Any-KeyPress>', self.onValidate)
        self.inp_fab.bind('<Any-KeyPress>', self.onValidate)
        self.inp_volt.bind('<Any-KeyPress>', self.onValidate)
        self.inp_prtnum.bind('<Any-KeyPress>', self.onValidate)
        self.inp_tamanho.bind('<Any-KeyPress>', self.onValidate)
        self.inp_undMed.bind('<Any-KeyPress>', self.onValidate)
        self.inp_tipoFrmt.bind('<Any-KeyPress>', self.onValidate)
        self.inp_material.bind('<Any-KeyPress>', self.onValidate)
        self.inp_tempo.bind('<Any-KeyPress>', self.onValidate)


# -------------------------------------------
# Funcoes


    def _getterVar(self):
        """
        Função para definir variáveis para os principais widgets (Entry's)
        e para o botão de cadastro.
        """

        self.inptId = StringVar()
        self.inptDesc = StringVar()
        self.inptFab = StringVar()
        self.inptVolt = StringVar()
        self.inptPrtnum = StringVar()
        self.inptTamanho = StringVar()
        self.inptUndMed = StringVar()
        self.inptTipoFrmt = StringVar()
        self.inptMaterial = StringVar()
        self.inptTempo = StringVar()
        self.btncad = StringVar()
        self.btnatualiza = StringVar()
        self.btncad.set('CADASTRAR')
        self.btnatualiza.set('ATUALIZAR')
        self.inptId.set(int(uuid.uuid4()))

    # Função para validação dos Ttk.Entry
    def onValidate(self, event):
        """
        Função que valida o texto ao digitar no tk.entry
        """
        wgtName = str(event.widget).split(".")[-1]

        if wgtName == 'descricao':
            self.old_value = self.inptDesc.get()
            self.max_len = 60
            self.var = self.inptDesc

        elif wgtName == 'fabricante':
            self.old_value = self.inptFab.get()
            self.max_len = 30
            self.var = self.inptFab

        elif wgtName == 'voltagem':
            self.old_value = self.inptVolt.get()
            self.max_len = 15
            self.var = self.inptVolt

        elif wgtName == 'partnumber':
            self.old_value = self.inptPrtnum.get()
            self.max_len = 25
            self.var = self.inptPrtnum

        elif wgtName == 'tamanho':
            self.old_value = self.inptTamanho.get()
            self.max_len = 20
            self.var = self.inptTamanho

        elif wgtName == 'uni_medida':
            self.old_value = self.inptUndMed.get()
            self.max_len = 15
            self.var = self.inptUndMed

        elif wgtName == 'tipo':
            self.old_value = self.inptTipoFrmt.get()
            self.max_len = 15
            self.var = self.inptTipoFrmt

        elif wgtName == 'material':
            self.old_value = self.inptMaterial.get()
            self.max_len = 15
            self.var = self.inptMaterial

        elif wgtName == 'tempo':
            self.old_value = self.inptTempo.get()
            self.max_len = 8
            self.var = self.inptTempo

        self.var.trace('w', self.check)

    def check(self, *args):
        """
        Verificação para saber se as entradas atendem aos critérios
        necessários.
        """
        if self.var == self.inptPrtnum or self.var == self.inptTamanho:
            if len(str(self.var.get())) <= self.max_len and str(self.var.get()).isnumeric() == True:
                self.old_value = self.var.get()
            else:
                self.var.set(self.old_value)

        elif self.var == self.inptTempo:

            if self.var.get() != '':
                counter = Counter(str(self.var.get()))
                tam = len(str(self.var.get()))
                valtext = str(self.var.get()).replace(':', '')

                try:
                    int(valtext)
                    if tam <= self.max_len:
                        self.old_value = self.var.get()

                        if tam == 3 and counter[':'] == 0:
                            self.inp_tempo.insert(tam - 1, ':')

                        elif tam == 6 and counter[':'] == 1:
                            self.inp_tempo.insert(5, ':')
                    else:
                        self.var.set(self.old_value)
                except:
                    self.var.set(self.old_value)
            else:
                pass

        else:
            if len(self.var.get()) <= self.max_len:
                self.old_value = self.var.get()
            else:
                self.var.set(self.old_value)

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

        resposta = messagebox.askokcancel(message='Deseja enviar o cadastro?')

        if resposta == True:
            if self.verifEntrada() == "Ok":
                user_profile = os.environ['USERPROFILE'] + \
                    '\Documents\\ferramentas.csv'
                user_documents = r'{}'.format(user_profile)
                path = Path(user_documents)

                if path.is_file():
                    A = False
                else:
                    A = True

                Id = self.inptId.get()
                Descricao = self.inptDesc.get()
                Fabricante = self.inptFab.get()
                Voltagem = self.inptVolt.get()
                Partnumber = self.inptPrtnum.get()
                Tamanho = self.inptTamanho.get()
                Unidade_Medida = self.inptUndMed.get()
                Tipo_Ferramenta = self.inptTipoFrmt.get()
                Material = self.inptMaterial.get()
                Tempo = self.inptTempo.get()

                data = [{'Id': Id, 'Descricao': Descricao,
                        'Fabricante': Fabricante,
                         'Voltagem': Voltagem,
                         'Partnumber': Partnumber,
                         'Tamanho': Tamanho,
                         'Unidade_Medida': Unidade_Medida,
                         'Tipo_Ferramenta': Tipo_Ferramenta,
                         'Material': Material,
                         'Tempo': Tempo
                         }]

                df = pd.DataFrame(
                    data, columns=['Id', 'Descricao', 'Fabricante', 'Voltagem', 'Partnumber', 'Tamanho',
                                   'Unidade_Medida', 'Tipo_Ferramenta', 'Material', 'Tempo'])

                df.to_csv(user_documents, index=None, sep=';',
                          header=A, encoding='utf-8-sig', mode='a')

                messagebox.showinfo(
                    message='Cadastro efetuado com sucesso!')

                self.refresh()

        else:
            messagebox.showinfo(message='Tente novamente')

    def _atualizar_frmt(self):
        """
        Funções do botão 'Atualizar'
        """
        if self.btn_atualizar['text'] == 'ATUALIZAR':
            openwin2 = Toplevel(self.master)
            self.app = Atualizafrmt(openwin2, self)
        else:
            if self.verifEntrada() == "Ok":
                Id = self.inptId.get()
                Descricao = self.inptDesc.get()
                Fabricante = self.inptFab.get()
                Voltagem = self.inptVolt.get()
                Partnumber = self.inptPrtnum.get()
                Tamanho = self.inptTamanho.get()
                Unidade_Medida = self.inptUndMed.get()
                Tipo_Ferramenta = self.inptTipoFrmt.get()
                Material = self.inptMaterial.get()
                Tempo = self.inptTempo.get()

                data = {'Id': Id, 'Descricao': Descricao,
                        'Fabricante': Fabricante,
                        'Voltagem': Voltagem,
                        'Partnumber': Partnumber,
                        'Tamanho': Tamanho,
                        'Unidade_Medida': Unidade_Medida,
                        'Tipo_Ferramenta': Tipo_Ferramenta,
                        'Material': Material,
                        'Tempo': Tempo
                        }

                user_profile = os.environ['USERPROFILE'] + \
                    '\Documents\\ferramentas.csv'
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

    def verifEntrada(self):
        """
        Verifica os campos de entrada de dados

        """
        if self.inptDesc.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Preencha a descrição da ferramenta')

        elif self.inptFab.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Preencha o Fabricante')

        elif self.inptVolt.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Digite a voltagem')

        elif self.inptPrtnum.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Necessário preencher o partnumber')

        elif self.inptTamanho.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Faltou descrever o tamanho da ferramenta')

        elif self.inptUndMed.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Necessário colocar a unidade de medida')

        elif self.inptTipoFrmt.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', f'Faltou o tipo da ferramenta\nEx.: Elétrica, mecânica, segurança e etc.')

        elif self.inptMaterial.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Descreva o material da ferramenta')

        elif self.inptTempo.get() == '':
            messagebox.showerror(
                'Ops, algo deu errado :(', 'Necessário inserir o tempo máximo de uso')

        else:
            return 'Ok'

    def treeview_to_input(self, treeItem, num):
        """
        Recebe os valores do treeview da tela de atualização
        de técnicos (classe 'Atualizatec')
        """
        self.btnatualiza.set('SALVAR')
        self.btn_cadastrar['state'] = 'disabled'
        self.inp_id.insert(0, treeItem[0])
        self.inp_desc.insert(0, treeItem[1])
        self.inp_fab.insert(0, treeItem[2])
        self.inp_volt.insert(0, treeItem[3])
        self.inp_prtnum.insert(0, treeItem[4])
        self.inp_tamanho.insert(0, treeItem[5])
        self.inp_undMed.insert(0, treeItem[6])
        self.inp_tipoFrmt.insert(0, treeItem[7])
        self.inp_material.insert(0, treeItem[8])
        self.inp_tempo.insert(0, treeItem[9])
        self.num = num


# -------------------------------------------
# GUI
def Main():
    """
    Chamada da classe 'Ferramentas'
    """
    global raiz
    raiz = Tk()
    raiz.title('Cadastro de Ferramentas')
    raiz.minsize(960, 540)
    raiz.pack_propagate(False)
    raiz.foto_icone = ImageTk.PhotoImage(Image.open(
        '.\Layout\imagens\cadtool.bmp'))
    raiz.iconphoto(True, raiz.foto_icone)
    frm = Ferramentas(raiz).pack(fill=BOTH, expand=YES)
    raiz.protocol("WM_DELETE_WINDOW", on_closing)
    raiz.mainloop()


def on_closing():
    if messagebox.askokcancel("Sair", "Deseja sair do módulo de Ferramentas"):
        raiz.destroy()
        raiz.quit()


# -------------------------------------------
# Chamada Main
if __name__ == "__main__":
    Main()
