import tkinter as tk

janela = tk.Tk()

janela.title("Conotação de Moedas")

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='#7E40C8')
mensagem.pack()

mensagem2 = tk.Label(text = " Selecione a moeda desejada")
mensagem2.pack()

janela.mainloop()