import threading
pygame = None
try:
    import pygame as pygame_
    pygame = pygame_
except Exception: pass
browser = None
try: 
    import browser as browser_
    browser = browser_
except Exception: pass
eb = []
uib = []
mem = map([{'type': 'null'}] * 20000,lambda i: i.copy())
async def p_eval(item,vector):
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
    async def boot():
        for i in vector:
            try:
                await i.eval(vector)
            except Exception:
                await p_eval(i,vector)
    boot()