import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

janela.rowconfigure(0,weight=1)
janela.columnconfigure(0,weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text = "Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)

def buscar_cotacao():
    print(moeda.get())

botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

dicionario_cotacoes = {
     'Dólar': 5.47,
     'Euro':6.68,
     'Bitcoin':20000
}

janela.mainloop()