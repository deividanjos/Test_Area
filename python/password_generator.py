import random
from string import digits
from string import ascii_letters
from string import punctuation
import PySimpleGUI as sg

# Tema
sg.theme("Black")

# Todas as coisas que vão aparecer na janela!
layout = [[sg.Text("-=-" * 20)],
          [sg.Text("1. Senha só com números.")],
          [sg.Text("2. Senha com números e letras.")],
          [sg.Text("3. Senha com números, letras e caracteres especiais.")],
          [sg.Text("4. Senha só com letras.")],
          [sg.Text("5. Senha com letras é caracteres especiais.")],
          [sg.Text("-=-" * 20)],
          [sg.Text("\n")],
          [sg.Text("Escolha o que você deseja: "), sg.Input()],
          [sg.Text("Qual a Quantidade de caracteres: "), sg.Input()],
          [sg.Button("Ok"), sg.Button("Cancel")]]

# Criando a Janela
window = sg.Window("Gerador de Senhas", layout)

# Event Loop para processar "eventos" e obter os "valores" das entradas.
senha = ''
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break

    if int(values[0]) == 1:
        senha = digits
    elif int(values[0]) == 2:
        senha = digits + ascii_letters
    elif int(values[0]) == 3:
        senha = digits + ascii_letters + punctuation
    elif int(values[0]) == 4:
        senha = ascii_letters
    elif int(values[0]) == 5:
        senha = ascii_letters + punctuation

    # gerador de senha 
    secure_random = random.SystemRandom()
    password = "".join(secure_random.choice(senha)
                       for i in range(int(values[1])))

    sg.Print("Sua Senha é: ", password, size=[50, 10])

window.close()
