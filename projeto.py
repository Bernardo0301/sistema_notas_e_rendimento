#Programa para calcular média de notas dos alunos, média total da turma e outras
#análises de desempenho da turma

#Exemplo para 5 alunos-Pode ser feito com quantos alunos quiser

#Declaração de matrizes usadas para armazenar as notas e nome
media = []
notas = []
aluno = []

#inicializando variáveis
aprovados = 0
recuperacao = 0
reprovados = 0
contador = 0
soma_medias = 0.0


#Trecho Para receber informações:
n = int(input("Quantos alunos? "))

#nome dos alunos
for i in range(n):
    aluno.append(input(f"\nNome do aluno {i+1}: "))

    notas_alunos = []
    soma = 0.0

    for j in range(3): #laço para atribuir as 3 notas aquele aluno
        nota = float(input(f"Nota {j+1}: "))
        notas_alunos.append(nota)
        soma = soma + nota

    notas.append(notas_alunos)
    media.append(soma/3.0)
    soma_medias = soma_medias + soma

media_geral = soma_medias / (n * 3)

#Mostra a maior e menor média
maior_media = media[0]
menor_media = media[0]

for i in range(1, n):
    if media[i] > maior_media:
        maior_media = media[i]

    if media[i] < menor_media:
        menor_media = media[i]

#Resultados:

for i in range(n):
    notas_string = f"{notas[i][0]:.1f}, {notas[i][1]:.1f}, {notas[i][2]:.1f}"

    if media[i] >= 7.0:
        situacao = "Aprovado"
        aprovados += 1
    elif media[i] >= 4.0:
        situacao = "Recuperacao"
        recuperacao += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    print(f"{aluno[i]} - Notas: {notas_string} - Media: {media[i]:.2f} - {situacao}")

#Resume o desempenho da turma:

print(f"\nAprovados:   {aprovados}")
print(f"Recuperacao: {recuperacao}")
print(f"Reprovados:  {reprovados}")
print(f"Maior media: {maior_media:.2f}")
print(f"Menor media: {menor_media:.2f}")
print(f"Media geral: {media_geral:.2f}")