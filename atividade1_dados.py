#MATRIZ E 3 FILIAIS
#Hora de entrada: das 7h às 12h, após não pode registrar ponto.
#intervalo de almoço: das 12h às 15h

matricula_alunos = (1,1001)
matriz = 4
filial1 = 1
filial2 = 2
filial3 = 3

matricula_alunos = int(input("Digite sua matrícula: "))
escolas = int(input("Digite o número correspondente a sua escola: (Matriz = 4, Filial 1 = 1, Filial 2 = 2, Filial 3 = 3): "))

hora_entrada = int(input("Digite a hora de entrada: "))
hora_inicio_almoco = int(input("Digite a hora de início do almoço: "))
hora_fim_almoco = int(input("Digite a hora de fim do almoço: "))
hora_saida = int(input("Digite a hora de saída: "))

if hora_entrada > 7 and hora_entrada <= 12:
    print("Tenha um bom dia início de turno!")
else:
    print("Dirija-se ao RH, por gentileza!")

if hora_inicio_almoco >= 12 and hora_inicio_almoco <= 15:
    print("Bom almoço!")    
else:
    print("Dirija-se ao RH, por gentileza!")

if hora_saida >= 7 and hora_saida < 18:
    print("Favor dirigir-se ao RH e justificar o motivo da saída antecipada, por gentileza!")
elif hora_saida == 18:
    print("Bom descanso!!!")
else:
    print("Dirija-se ao RH e justifique o motivo da hora extra")
