import random
import copy
import pygame

WIDTH = 1500
HEIGHT = 1000
FPS =30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test GoL")

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

def add_cell(x,y,cells,click, right_click):
    if click:
        cells[x//10][y//10] = 1
    elif right_click:
        cells[x // 10][y // 10] = 0
    return cells

def count_alive(cells, x, y):
    return cells[x-1][y+1] + cells[x][y+1] + cells[x+1][y+1] + cells[x-1][y] + cells[x+1][y] + cells[x-1][y-1] + cells[x][y-1] + cells[x+1][y-1]

def update_cells(cells):
    new_cells = copy.deepcopy(cells)

    for i in range(1,len(cells)-2):
        for j in range(1,len(cells[0])-2):
            alive = count_alive(cells,i,j)
            if alive > 0:
                print("im at: " +str(i)+" "+str(j))
                print(str(i+1)+" "+str(j+1))
                print(alive)
            if alive <= 1 or alive >= 4:
                new_cells[i][j] = 0
            elif alive == 3:
                new_cells[i][j] = 1

    return new_cells

def update(x,y,cells,paused,click,right_click):
    if paused:
        WIN.fill((0, 0, 0))
    else:
        WIN.fill((255, 255, 255))
    if click or right_click:
        cells = add_cell(x,y, cells,click,right_click)
    if not paused:
        tempcells = copy.deepcopy((cells))
        cells =copy.deepcopy(tempcells)
    draw_grid(paused)
    draw_cells(cells,paused)

def main():
    clock = pygame.time.Clock()
    run = True
    x,y = 0,0
    paused = False
    #random.randint(0,1)
    cells = [[0] * (HEIGHT//10) for i in range(WIDTH//10)]
    click = False
    right_click = False
    while run:
        x, y = pygame.mouse.get_pos()
        clock.tick(FPS)
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and event.button ==3:
                if right_click == True:
                    right_click = False
                else:
                    right_click = True
            if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and event.button == 1:
                if click == True:
                    click = False
                else:
                    click = True
            if event.type == pygame.KEYUP:
                if pressed[pygame.K_SPACE]:
                    if paused == False:
                        paused = True
                    else:
                        paused = False
            if right_click and click:
                right_click = False
                click = False
        update(x,y,cells,paused,click, right_click)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
