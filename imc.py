"""
Programa calcula o Índice de Massa Corporal (IMC), 
usada para avaliar se um pessoa está dentro de uma faixa
considerada saudável em termos de peso em relação à altura.

Vamos considerar as seguintes categorias:
Abaixo do peso: IMC abaixo de 18,5
Peso normal: IMC entre 18,5 e 24,9
Sobrepeso: IMC entre 25 e 29,9
Obesidade classe I: IMC entre 30 e 34,9
Obesidade classe II: IMC entre 35 e 39,9
Obesidade classe III: IMC igual ou acima de 40 

Para esse projeto utilizamos a biblioteca de interface gráfica 
de usuário (GUI) Tkinter.

"""
from tkinter import *

# Função que calcula e exibe o valor do IMC
def calcular_imc():
    # Solicitar entrada do usuário
    altura = float(entry_altura.get())
    peso = float(entry_peso.get())
    msg = ""

    # Calcular IMC
    imc = peso / altura ** 2

    if imc <= 18.4:
        msg = '*** Você está abaixo do peso ***' 
    elif imc <= 24.9:
        msg = '*** Você está com peso normal ***'
    elif imc <= 29.9:
        msg = '*** Você está acima do peso ***'
    elif imc <= 34.9:
        msg = '*** Você está com sobrepeso ***'
    elif imc <= 40:
        msg = '*** Você está com obesidade ***'
    else:
         msg = '*** Você esta com obesidade mórbida ***'
    
    # Exibir resultado
    label_resultado['text'] = f'Seu IMC é: {imc:.2f}'
    label_categoria['text'] = msg

# Criar a interface
root = Tk()

root.title("Calculador de IMC")
root.minsize(300, 150)

frame_entrada = Frame(root)
frame_entrada.pack()

label_altura = Label(frame_entrada, text="Altura (m):")
label_altura.grid(row=0, column=0)

entry_altura = Entry(frame_entrada)
entry_altura.grid(row=0, column=1)

label_peso = Label(frame_entrada, text="Peso (kg)")
label_peso.grid(row=1, column=0)

entry_peso = Entry(frame_entrada)
entry_peso.grid(row=1, column=1)

frame_saida = Frame(root)
frame_saida.pack()

label_resultado = Label(frame_saida, text="")
label_resultado.pack()

label_categoria = Label(frame_saida, text="")
label_categoria.pack()

botao_calcular = Button(root, text="Calcular", command=calcular_imc)
botao_calcular.pack()

root.mainloop()

