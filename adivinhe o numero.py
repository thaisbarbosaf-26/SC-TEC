i = 1
while i <=30:

  i = int(input("Adivinhe o número Secreto!!! "))

  if i <18:
    print ("TENTE OUTRA VEZ!!! **Dica: O número é maior que este!!!\n")
  elif i >18:
    print ("TENTE OUTRA VEZ!!! **Dica: O número é Menor que este!!!\n")
  else:
    print("PARABÉNS, VOCÊ ACERTOU !!!!\n")
