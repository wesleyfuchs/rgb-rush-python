from tkinter import *
import tkinter.messagebox
import random

# Cores
cor0 = "#444466" 
cor1 = "#feffff"
cor2 = "#503c44"
cor3 = "#000000"

pontuacao = 0

# Função para iniciar o jogo principal
def iniciar_jogo():
    
    # Destrua a tela de entrada
    tela_entrada.destroy()

    # Crie a janela do jogo principal
    janela = Tk()
    janela.geometry("650x300")
    janela.configure(bg=cor2)
    janela.title("RGB Hour")

    # configurando a janela
    sliders = Label(janela, bg=cor2)
    sliders.grid(row=0, column=0, padx=10)

    tela = Label(janela, bg=cor3, width=20, height=10, bd=1)
    tela.grid(row=0, column=1, pady=10)

    tela_objetivo = Label(janela, bg=cor3, width=20, height=10, bd=1)
    tela_objetivo.grid(row=0, column=3, pady=10)

    codigo_hex = Frame(janela, bg=cor1)
    codigo_hex.grid(row=1, column=0)

    # funcao scale
    def escala(valor):
        r=s_red.get()
        g=s_green.get()
        b=s_blue.get()

        rgb = f'{r}, {g}, {b}'

        hexadecimal = "#%02x%02x%02x" % (r, g, b)

        #alterando a cor do fundo da tela
        tela['bg'] = hexadecimal

        # alterando a entry
        e_cor.delete(0,END)
        e_cor.insert(0,hexadecimal)

    def gerar_cor_aleatoria():
        '''Gera uma cor aleatoria usando valores RGB e aplica valores hexadecimais'''
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        hexadecimal = "#%02x%02x%02x" % (r, g, b)

        tela_objetivo['bg'] = hexadecimal
    
    gerar_cor_aleatoria()

    # Sliders RGB
    largura = 300

    l_red = Label(sliders,text='R', width=2, bg=cor2, fg='black', anchor='nw', font=("Time New Roman", 12, "bold"))
    l_red.grid(row=0, column=0)
    s_red=Scale(sliders, command=escala, from_=0, to=255, length=largura, bg=cor2, fg="red", orient=HORIZONTAL)
    s_red.grid(row=0, column=1)

    l_green = Label(sliders,text='G', width=2, bg=cor2, fg='black', anchor='nw', font=("Time New Roman", 12, "bold"))
    l_green.grid(row=1, column=0)
    s_green=Scale(sliders, command=escala, from_=0, to=255, length=largura, bg=cor2, fg="green", orient=HORIZONTAL)
    s_green.grid(row=1, column=1)

    l_blue = Label(sliders,text='B', width=2, bg=cor2, fg='black', anchor='nw', font=("Time New Roman", 12, "bold"))
    l_blue.grid(row=2, column=0)
    s_blue=Scale(sliders, command=escala, from_=0, to=255, length=largura, bg=cor2, fg="blue", orient=HORIZONTAL)
    s_blue.grid(row=2, column=1)


    #entry
    e_cor = Entry(codigo_hex, width=12, font=("Ivy", 10, "bold"), justify=CENTER)
    e_cor.grid(row=1, column=0, padx=5, pady=10)


    # Função para calcular a porcentagem de similaridade entre duas cores RGB
    def calcula_porcentagem_similaridade(cor1, cor2):
        '''Calcula a porcentagem de similaridade entre duas cores'''
        r1, g1, b1 = cor1
        r2, g2, b2 = cor2

        diferenca = ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5
        max_diferenca = (255 ** 2 * 3) ** 0.5
        similaridade = ((max_diferenca - diferenca) / max_diferenca) * 100

        return similaridade

    # Função para atualizar a pontuação na interface
    def atualizar_pontuacao():
        pontuacao_label.config(text=f"Pontuação: {pontuacao}")

    # Função para verificar a cor e calcular a porcentagem de similaridade
    def verificar_cor():
        global pontuacao  # Declarando a variável pontuacao como global
        
        cor_tela = tela['bg']
        cor_tela_objetivo = tela_objetivo['bg']

        cor_rgb_tela = tuple(int(cor_tela[i:i+2], 16) for i in (1, 3, 5))
        cor_rgb_tela_objetivo = tuple(int(cor_tela_objetivo[i:i+2], 16) for i in (1, 3, 5))

        similaridade = calcula_porcentagem_similaridade(cor_rgb_tela, cor_rgb_tela_objetivo)

        resultado_label.config(text=f"{similaridade:.2f}%")
        
        if similaridade > 90:
            pontuacao += 1
            atualizar_pontuacao()
            
        gerar_cor_aleatoria()  # Chamando a função para gerar uma nova cor aleatória
        

    # Botões
    # gerar_cor_button = Button(codigo_hex, text="Gerar Cor Aleatória", command=gerar_cor_aleatoria)
    # gerar_cor_button.grid(row=0, column=0, padx=5, pady=10)

    verificar_button = Button(codigo_hex, text="Verificar Cor", command=verificar_cor)
    verificar_button.grid(row=0, column=0, padx=5, pady=10)

    resultado_label = Label(codigo_hex, text="", font=("Ivy", 10, "bold"), fg="black")
    resultado_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
    
    # Label para exibir a pontuação
    pontuacao_label = Label(janela, text=f"Score: {pontuacao}", font=("Ivy", 12, "bold"), fg="black")
    pontuacao_label.grid(row=1, column=1, columnspan=2, padx=5, pady=10)


    janela.mainloop()
    
    
# Criando a tela de entrada
tela_entrada = Tk()
tela_entrada.geometry("400x200")
tela_entrada.configure(bg=cor1)
tela_entrada.title("Bem-Vindo ao RGB Hour")

# botão "Entrar"
titulo_label = Label(tela_entrada, text="Bem-Vindo ao RGB Hour", font=("Arial", 16))
titulo_label.pack(pady=20)

instrucao_label = Label(tela_entrada, text="Clique em 'Entrar' para começar o jogo.", font=("Arial", 12))
instrucao_label.pack()

entrar_button = Button(tela_entrada, text="Entrar", command=iniciar_jogo)
entrar_button.pack(pady=20)


tela_entrada.mainloop()