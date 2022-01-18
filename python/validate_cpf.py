import re
from termcolor import colored

num = input('Digite seu cpf: ').strip()
regexp = re.compile(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})')
cpf = regexp.match(num)

if cpf != None and len(cpf[0]) == 14 and cpf[0] == num:
    print(colored('CPF Valido! ', 'green'))
else:
    print(colored('----------------------- ATENÇÃO -----------------------\n', 'red'))
    print(colored('O CPF que foi digitado é Inválido...', 'yellow'))
    print(colored('Exemplo de CPF Valido: 123.456.789-10\n', 'blue'))