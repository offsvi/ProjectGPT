import tkinter as tk


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Verificar se o nome de usuário e a senha são válidos
    if username == "admin" and password == "123":
        message_label.config(text="Login bem-sucedido!")
    else:
        message_label.config(text="Nome de usuário ou senha incorretos.")


# Criar janela principal
root = tk.Tk()
root.title("Login")

# Criar campos de entrada e rótulos para o nome de usuário e senha
username_label = tk.Label(root, text="Nome de usuário:")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Senha:")
password_entry = tk.Entry(root, show="*")

# Criar botão de login e mensagem de status
login_button = tk.Button(root, text="Login", command=login)
message_label = tk.Label(root, text="Insira suas credenciais e clique em Login.")

# Organizar widgets na janela
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()
message_label.pack()

# Iniciar loop principal do tkinter
root.mainloop(
