import pandas as pd
import numpy as np
import tkinter as tk
import openpyxl
from tkinter import filedialog

def carregar():

    caminho = filedialog.askopenfilename(filetype=[("Arquivos Excel","*.xlsx"),("Todos os arquivos", "*.*")])
    
    if caminho:
        file  =  openpyxl.load_workbook(caminho)
        planilha = file.active

        lista  =  []

        for linhas in planilha.iter_rows(values_only=True):
            n_linhas = "\t".join(str(celula) for celula in linhas)
            lista.append(n_linhas)
        texto =  "\n".join(lista)
        text.delete('1.0', tk.END)
        text.insert(tk.END, texto)


janela  =  tk.Tk()

btn = tk.Button(janela, text='Carregar', command = carregar)
btn.grid(pady=30)

text = tk.Text(janela, width =60, height=50)
text.grid(pady=20)

janela.mainloop()
