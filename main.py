import threading
import pygame
eb = []
uib = []
mem = map([{'type': 'null'}] * 20000,lambda i: i.copy())
def p_eval(item,vector):
    pass
def pg_main():
    global uib, eb
    pygame.init()
    display = pygame.display.set_mode((600,600))
    done = False
    while not done:
        for ui in uib:
            ui(display)
        uib = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True
                break
            else:
                eb.append(event)
def vm_main():
    vector = []
    def boot():
        for i in vector:
            try:
                i.eval(vector)
            except Exception:
                p_eval(i,vector)
    boot()