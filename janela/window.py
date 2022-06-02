from tkinter import *
from game import jogo

class window:

    janela = Tk()
    janela.title("Snake Game - Inicio")
    janela.geometry("640x480")
    janela.resizable(width=0, height=0)

class buttons:

    def fecharJogo():

        window.janela.destroy()

    def abrirJogo():

        window.janela.destroy()
        jogo.play.iniciar()

    startButton = Button(window.janela, text="Começar o jogo", command=abrirJogo)
    startButton.place(x=250, y=200)

    exitButton = Button(window.janela, text="Sair do jogo", command=fecharJogo)
    exitButton.place(x=270, y=250)
