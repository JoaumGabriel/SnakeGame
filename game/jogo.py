import pygame as pg
from random import randrange

class play:

    def iniciar():

        try:
            pg.init()
            print("Iniciou com sucesso")
        except:
            print("Módulo do pygame não foi iniciado com sucesso")

        largura = 640 # largura da tela
        altura = 480 # altura da tela
        tamanho = 10 # ajustar no grid

        black = (0, 0, 0) # cor preta
        white = (255, 255, 255) # cor branca
        red = (255, 0, 0)

        Speed = 5

        fps = pg.time.Clock() # funçao para o fps
        scene = pg.display.set_mode((largura, altura)) # funcao para montar a tela
        pg.display.set_caption("SnakeGame - 0.5 | Velocidade: " + str(Speed)) # titulo da tela na pagina do jogo

        def makeCobra(CobraXY): # desenha a cobra com base no vetor dela
            for xy in CobraXY:
                pg.draw.rect(scene, white, [xy[0], xy[1], tamanho, tamanho])

        def maca(x, y):
            pg.draw.rect(scene, red, [x, y, tamanho, tamanho])

        sair = True
        fimdejogo = False

        pos_x = randrange(0, largura-tamanho, 10) # declara aonde a cobra vai nascer
        pos_y = randrange(0, altura-tamanho, 10) # declara aonde a cobra vai nascer
        maca_x = randrange(0, largura-tamanho, 10) # declara aonde a maca vai nascer
        maca_y = randrange(0, altura-tamanho, 10) # declara aonde a maca vai nascer

        velocidade_x = 0 # determina se ela vai para esquerda ou direita
        velocidade_y = 0 # determina se ela vai para cima ou para baixo

        Cobra = [] # vetor que guarda o tamanho da cobra
        Comp = 1 # comprimento da cobra
        Speed = 5

        while sair == True: # while responsavel pela execucao do jogo

            while fimdejogo == True:

                scene.fill(white)

                pg.display.update()

                for event in pg.event.get():

                    if event.type == pg.QUIT:

                        sair = False
                        fimdejogo = False

                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_c:

                            sair = True
                            fimdejogo = False

                            pos_x = randrange(0, largura - tamanho, 10)
                            pos_y = randrange(0, altura - tamanho, 10)
                            maca_x = randrange(0, largura - tamanho, 10)
                            maca_y = randrange(0, altura - tamanho, 10)

                            velocidade_x = 0
                            velocidade_y = 0

                            Cobra = []
                            Comp = 1
                            Speed = 5

                        if event.key == pg.K_s:

                            sair = False
                            fimdejogo = False

            for event in pg.event.get(): # analisa se acontece algum evento do pygame e armazena seu tipo

                if event.type == pg.QUIT: # se o jogador apertar no botao de fechar
                    sair = False
                    fimdejogo = False
                if event.type == pg.KEYDOWN: # verifica se alguma tecla foi pressionada
                    if event.key == pg.K_w and velocidade_y != tamanho: # tecla W
                        print("indo para cima")
                        velocidade_x = 0
                        velocidade_y = -tamanho
                    if event.key == pg.K_s and velocidade_y != -tamanho: # tecla S
                        print("indo para baixo")
                        velocidade_y = tamanho
                        velocidade_x = 0
                    if event.key == pg.K_a and velocidade_x != tamanho: # tecla A
                        print("indo para a esquerda")
                        velocidade_y = 0
                        velocidade_x = -tamanho
                    if event.key == pg.K_d and velocidade_x != -tamanho: # tecla D
                        print("indo para a direita")
                        velocidade_y = 0
                        velocidade_x = tamanho

            scene.fill(black) # define o fundo da tela
            pos_x += velocidade_x # orienta a movimentacao da cobra no eixo x
            pos_y += velocidade_y # orienta a movimentacao da cobra no eixo y

            if pos_x == maca_x and pos_y == maca_y:

                maca_x = randrange(0, largura - tamanho, 10)
                maca_y = randrange(0, altura - tamanho, 10)
                Comp += 1
                Speed += 2

            if pos_x >= largura:
                fimdejogo = True
            if pos_x < 0:
                fimdejogo = True
            if pos_y >= altura:
                fimdejogo = True
            if pos_y < 0:
                fimdejogo = True

            CobraCabeca = []
            CobraCabeca.append(pos_x) # armazena a cabeca da cobra quando for no eixo x
            CobraCabeca.append(pos_y) # armazena a cabeca da cobra quando for no eixo y
            Cobra.append(CobraCabeca) # armazena a cobra como um todo

            if len(Cobra) > Comp:
                del Cobra[0]

            if any(Bloco == CobraCabeca for Bloco in Cobra[:-1]):
                fimdejogo = True


            makeCobra(Cobra) # gera a cobra
            maca(maca_x, maca_y) # gera a maca

            fps.tick(Speed)
            pg.display.set_caption("SnakeGame - 0.5 | Velocidade: " + str(Speed))
            pg.display.update()
