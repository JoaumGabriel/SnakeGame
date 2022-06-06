from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from janela import helper

from game import jogo

class window:

    janela = Tk()
    janela.title("Snake Game - Inicio")
    janela.geometry("640x480")
    janela.resizable(width=0, height=0)
    janela.config(bg="gray")

class buttons:

    def fecharJogo():

        window.janela.destroy()

    def abrirJogo():

        window.janela.destroy()
        jogo.play.iniciar()

    def openHelper():

        window.janela.destroy()
        helper.windowHelp.openTutorial()

    style = Style()

    style.configure('GameTitle.TLabel', font=('arial', 18, 'bold'), background='gray')

    style.configure('EnterGame.TButton', font=('arial', 11, 'bold'), background='gray')
    style.configure('Tutorial.TButton', font=('arial', 11, 'bold'), background='gray')
    style.configure('Exit.TButton', font=('arial', 11, 'bold'), background='gray')

    gameTitle = ttk.Label(window.janela, text="SnakeGame - v1", style='GameTitle.TLabel')
    gameTitle.place(x=230, y=50)

    startButton = ttk.Button(window.janela, text="Começar o jogo", command=abrirJogo, style='EnterGame.TButton')
    startButton.place(x=250, y=200)

    helpButton = ttk.Button(window.janela, text="Como jogar", command=openHelper, style='Tutorial.TButton')
    helpButton.place(x=260, y=250)

    exitButton = ttk.Button(window.janela, text="Sair do jogo", command=fecharJogo, style='Exit.TButton')
    exitButton.place(x=260, y=300)

