import random
import curses

snake1 = curses.initscr()
curses.curs_set(0)
snakeHeight, snakeWidth = snake1.getmaxyx()
w = curses.newwin(snakeHeight, snakeWidth, 0, 0)
w.keypad(1)
w.timeout(100)

snakeWidth1 = snakeWidth/4
snakeHeight1 = snakeHeight/2

snake = [
    [snakeHeight1, snakeWidth1],
    [snakeHeight1, snakeWidth1-1],
    [snakeHeight1, snakeWidth1-2]
]

food = [snakeHeight/2, snakeWidth/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

# Continue loop

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, snakeHeight] or snake[0][1] in [0,snakeWidth] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1

    if key == curses.KEY_UP:
        new_head[0] -= 1
    
    if key == curses.KEY_LEFT:
        new_head[1] -= 1 
    
    if key == curses.KEY_RIGHT:
        new_head[1] += 1   

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None 
        while food is None:
            nf = [
                random.randint(1, snakeHeight-1),
                random.randint(1, snakeWidth-1)
            ]

            food = nf if nf not in snake else None 
        w.addch(food[0], food[1], curses.ACS_PI)

    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)