import pygame as pg

class Node:
    def __init__(self, rect, visited, weight, coordinates, target):
        self.rect = rect
        self.visited = visited
        self.weight = weight
        self.coordinates = coordinates
        self.target = target

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255,0,0)
blocksize = 30
cols = rows = 600 // blocksize

def main():
    pg.init()
    global screen, clock, nodeList
    screen = pg.display.set_mode((600, 600))
    clock = pg.time.Clock()
    
    nodeList = gridlist()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                clickedRect(pos)

        screen.fill(BLACK)
        draw()
        pg.display.update()
        clock.tick(60)

    pg.quit()

def clickedRect(pos):
    cord = posToNode(pos)
    x, y = int(cord.x), int(cord.y)
    if 0 <= x < cols and 0 <= y < rows:
        nodeList[x][y].target = True

def gridlist():
    grid = [[None for _ in range(rows)] for _ in range(cols)]
    for x in range(cols):
        for y in range(rows):
            px, py = x * blocksize, y * blocksize
            rect = pg.Rect(px, py, blocksize, blocksize)
            coord = pg.math.Vector2(x, y)
            grid[x][y] = Node(rect, False, -1, coord, False)
    return grid

def draw():
    for row in nodeList:
        for node in row:
            color = RED if node.target else WHITE
            pg.draw.rect(screen, color, node.rect, 1)

def posToNode(pos):
    x, y = pos
    return pg.math.Vector2(x // blocksize, y // blocksize)




if __name__ == "__main__":
    main()
