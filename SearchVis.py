import pygame as pg

class Node:
    def __init__(self, rect, visited, weight, coordinates, target):
        self.rect = rect
        self.visited = visited
        self.weight = weight
        self.coordinates = coordinates
        self.target = target
        self.parent = None

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

blocksize = 30
cols = rows = 600 // blocksize

def main():
    pg.init()
    global screen, clock, nodeList, targetNodes
    screen = pg.display.set_mode((600, 600))
    clock = pg.time.Clock()
    
    nodeList = gridlist()
    targetNodes = []
    running = True
   
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                clickedRect(pos)
            elif event.type == pg.KEYUP:
                if event.key == pg.K_RETURN:
                   BFS() 

        
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
        targetNodes.append(nodeList[x][y])


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
            if node.target:
             color = RED
            elif node.weight == -2:  
               color = GREEN
            elif node.visited:
              color = BLUE
            
            else:
              color = WHITE
            pg.draw.rect(screen, color, node.rect, 1)

def posToNode(pos):
    x, y = pos
    return pg.math.Vector2(x // blocksize, y // blocksize)


def BFS():
    if (len(targetNodes) < 2):
        print("need atleast a starting and target node in order to use a pathfinding algorithm")
        return
    
    start = targetNodes[0]
    end = targetNodes[1]
    #reset nodes to not visited
    for row in nodeList:
        for node in row:
            node.visited = False
            node.parent = None 
    
    queue = [start]
    start.visited = True

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue:  
        current = queue.pop(0)
        x, y = int(current.coordinates.x), int(current.coordinates.y)  

        if current == end:
            print("target reached")
            trace_path(end)
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows:
                neighbor = nodeList[nx][ny]
                if not neighbor.visited:
                    neighbor.visited = True
                    neighbor.parent = current
                    queue.append(neighbor)

def trace_path(end_node):
    current = end_node.parent 
    while current and not current.target:
        current.weight = -2  
        current = current.parent

if __name__ == "__main__":
    main()
