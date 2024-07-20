import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk

def display():
    nome = input('Olá, qual seu nome?:')
    print('Seja bem vindo(a)',nome,'Vamos descobrir se você passou de ano!!! ')

j = tk.Tk()

entry_nome = tk.Entry(j)
entry_nome.pack(padx=20)

mostrar = tk.label(j, text = Vamos descobrir se você passou de ano!!! )

def carregar():
    caminho = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    df = pd.read_excel(caminho)
    plt.bar(['Disciplinas'], ['Notas'], ['Modo de Avaliação'], ['Presença'])
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')
    plt.show()

janela = tk.Tk()
btn = tk.Button(janela, text="Carregar Dados e Gerar Gráfico", command=carregar)
btn.pack()
janela.mainloop()