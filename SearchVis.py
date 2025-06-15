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
nodeList = {}

def main():
    pg.init()
    global screen, clock
    screen = pg.display.set_mode((600, 600))
    clock = pg.time.Clock()
    
    global nodeList
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
    key = (cord.x, cord.y)
    if key in nodeList:
        nodeList[key].target = True

def gridlist():
    nodelist = {}
    for x in range(0, 600, blocksize):
        for y in range(0, 600, blocksize):
            rect = pg.Rect(x, y, blocksize, blocksize)
            cord = posToNode((x, y))
            n1 = Node(rect, False, -1, cord, False)
            nodelist[(cord.x, cord.y)] = n1
    return nodelist

def draw():
    for node in nodeList.values():
        color = RED if node.target else WHITE
        pg.draw.rect(screen, color, node.rect, 1)

def posToNode(pos):
    x, y = pos
    x = x // blocksize
    y = y // blocksize
    return pg.math.Vector2(x, y)

if __name__ == "__main__":
    main()
