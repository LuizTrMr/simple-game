import pygame as pg

def main():
    WINDOW_WIDTH  = 800 # Comprimento da janela
    WINDOW_HEIGHT = 600 # Altura

    pg.init()

    window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    clock = pg.time.Clock()

    player = pg.Rect(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, 120, 70)
    player_dx = 0
    player_dy = 0
    PLAYER_SPEED = 3 # Rapidez do player

    run = True
    while run:
        # Input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

            keys = pg.key.get_pressed()
            # X
            player_dx = 0
            if keys[pg.K_RIGHT]:
               player_dx = PLAYER_SPEED
            if keys[pg.K_LEFT]:
               player_dx = -PLAYER_SPEED

            # Y
            player_dy = 0
            if keys[pg.K_UP]:
               player_dy = -PLAYER_SPEED
            if keys[pg.K_DOWN]:
               player_dy = PLAYER_SPEED

        # Update
        new_player_x = player.x + player_dx
        if new_player_x > 0 and new_player_x < WINDOW_WIDTH-player.width:
            player.x = new_player_x

        new_player_y = player.y + player_dy
        if new_player_y > 0 and new_player_y < WINDOW_HEIGHT-player.height:
            player.y = new_player_y

        # Render
        window.fill((255,0,0,255)) # Limpar a tela

        pg.draw.rect(window, (0,255,0,255), player) # Desenhar nosso retângulo

        pg.display.flip() # Atualizar a tela

        # Computa quantos milissegundos passaram desde a última chamada da função.
        # Se passar do framerate selecionado(rodar em menos tempo), a função espera.
        # Isso seta um framerate máximo pro jogo.
        # Nesse caso, o jogo NÃO vai rodar a mais que 60 fps
        clock.tick(60)

main()
