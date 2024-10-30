import tkinter as tk

janela = tk.Tk()

botao_classeeconomica = tk.Radiobutton(text="Classe Econômica")
botao_classeexecutiva = tk.Radiobutton(text="Classe Executiva")
botao_primeiraclasse = tk.Radiobutton(text="Primeira Classe")
botao_classeeconomica.grid(row=0, column=0)
botao_classeexecutiva.grid(row=0, column=1)
botao_primeiraclasse.grid(row=0, column=2)

janela.mainloop()