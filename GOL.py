import pygame

WIDTH = 1500
HEIGHT = 1000
FPS = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test orbit")

def draw_cells(cells,paused):
    if paused:
        color = (255, 255, 255)
    else:
        color = (0, 0, 0)
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j] == 1:
                x = i*10
                y = j*10
                pygame.draw.rect(WIN, color,(x,y,10,10))

def draw_grid(paused):
    if paused:
        color = (255, 255, 255)
    else:
        color = (0, 0, 0)
    for i in range(HEIGHT//10):
        pygame.draw.line(WIN, color, (0, i*10), (WIDTH, i*10))
    for i in range(WIDTH//10):
        pygame.draw.line(WIN, color, (i*10, 0), (i*10, HEIGHT))

def add_cell(x,y,cells):
    cells[x//10][y//10] = 1
    return cells

def update_cells(cells):
    new_cells = cells
    for i in range(len(cells)-1):
        for j in range(len(cells[0])-1):
            alive = 0
            for k in range(i-1,i+2):
                #print(k)
                for l in range(j-1,j+2):
                    #print(l)
                    #print("i: " + str(i) + " j: " + str(j) + " k: " + str(k) + " l: " + str(l))
                    if k != i or l != j:
                        #pygame.draw.rect(WIN, (100,0,100), (i*10, j*10, 10, 10))
                        #print("i: "+str(i)+" j: "+ str(j)+ " k: "+str(k)+" l: " + str(l))
                        if cells[k][l] == 1:
                            alive +=1
                    #print("")
            if alive >= 1:
                print(alive)
            if alive <= 1 or alive >= 4:
                new_cells[i][j] = 0
            elif alive == 3:
                new_cells[i][j] = 1
    return new_cells

def update(x,y,cells,paused,click):
    if paused:
        WIN.fill((0, 0, 0))
    else:
        WIN.fill((255, 255, 255))
    if click:
        cells = add_cell(x,y, cells)
    if not paused:
        cells = update_cells(cells)
    draw_grid(paused)
    draw_cells(cells,paused)

def main():
    clock = pygame.time.Clock()
    run = True
    x,y = 0,0
    paused = False
    cells = [[0] * (HEIGHT//10) for i in range(WIDTH//10)]
    while run:
        clock.tick(FPS)
        pressed = pygame.key.get_pressed()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                click = True
            if pressed[pygame.K_SPACE]:
                if paused == False:
                    paused = True
                else:
                    paused = False
        update(x,y,cells,paused,click)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
