import random
from string import digits
from string import ascii_letters
from string import punctuation

# inputs 
escolha = int(input("Qual tipo de senha vc deseja: "))
q_c = int(input("Qual a quantidade de caracteres vc deseja: "))

# tipos de senhas
if escolha == 1:
  senha = digits
elif escolha == 2:
  senha = digits + ascii_letters
elif escolha == 3:
  senha = digits + ascii_letters + punctuation

# gerador de senha 
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(senha)
                  for i in range(q_c))
print(password)