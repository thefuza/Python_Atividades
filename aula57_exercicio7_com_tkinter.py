"""
Faça uma lista de compras com linhas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na lista
"""

# lista_de_compras = ['Arroz', 'Feijão', 'Macarrão']

# for lista in enumerate(lista_de_compras):
#     print(lista)

import tkinter as tk
from tkinter import messagebox


# --- FUNÇÕES DE LÓGICA ---
def inserir_item():
    item = entry_item.get().strip()

    if not item:
        messagebox.showwarning("Aviso", "Por favor, digite um item!")
        return

    # Evita duplicados (como na sua lógica original)
    # Pegamos todos os itens atuais da Listbox para comparar
    itens_atuais = lista_visual.get(0, tk.END)
    if item in itens_atuais:
        messagebox.showerror("Erro", "Já existe um item com esse nome!")
        entry_item.delete(0, tk.END)
        return

    lista_visual.insert(tk.END, item)
    entry_item.delete(0, tk.END)  # Limpa o campo de texto


def apagar_item():
    try:
        # Pega o índice do item selecionado pelo usuário na tela
        indice_selecionado = lista_visual.curselection()

        if not indice_selecionado:
            messagebox.showwarning("Aviso", "Selecione um item da lista para apagar!")
            return

        # Remove o item usando o índice (Tratado contra erros de índice)
        item_removido = lista_visual.get(indice_selecionado)
        lista_visual.delete(indice_selecionado)
        messagebox.showinfo("Sucesso", f'"{item_removido}" foi removido!')

    except IndexError:
        messagebox.showerror("Erro", "Erro ao tentar apagar o item.")


# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---
janela = tk.Tk()
janela.title("Lista de Compras")
janela.geometry("400x450")
janela.resizable(False, False)

# --- ELEMENTOS DA INTERFACE (WIDGETS) ---

# Título
lbl_titulo = tk.Label(
    janela, text="Sua Lista de Compras", font=("Arial", 14, "bold")
)
lbl_titulo.pack(pady=10)

# Campo para digitar o item
frame_entrada = tk.Frame(janela)
frame_entrada.pack(pady=10)

lbl_item = tk.Label(frame_entrada, text="Item:", font=("Arial", 10))
lbl_item.pack(side=tk.LEFT, padx=5)

entry_item = tk.Entry(frame_entrada, width=25, font=("Arial", 10))
entry_item.pack(side=tk.LEFT, padx=5)

# Botão Inserir
btn_inserir = tk.Button(
    frame_entrada, text="Inserir", command=inserir_item, bg="green", fg="white"
)
btn_inserir.pack(side=tk.LEFT, padx=5)

# Lista Visual (Equivalente ao seu 'listar' com enumerate, já mostra os itens em linhas)
lista_visual = tk.Listbox(janela, width=40, height=12, font=("Arial", 10))
lista_visual.pack(pady=10)

# Botão Apagar
btn_apagar = tk.Button(
    janela,
    text="Apagar Item Selecionado",
    command=apagar_item,
    bg="red",
    fg="white",
    width=25,
)
btn_apagar.pack(pady=10)

# Botão Sair
btn_sair = tk.Button(janela, text="Sair", command=janela.quit, width=10)
btn_sair.pack(side=tk.BOTTOM, pady=15)

# Executa o aplicativo
janela.mainloop()