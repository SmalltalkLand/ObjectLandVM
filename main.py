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
mem = map(lambda i: i.copy(),[{'type': 'null'}] * 20000)
class BrowserDisplay:
    QUIT = 'quit'
    def attachShadow(self,o):
        return self
    def appendChild(self,o):
        self._elem.appendChild(o)
    def __init__(self,the_element):
        self._events = []
        def on_event(evt):
            self._events.append(evt)
        def init_html(elem = the_element):
            self._elem = elem
            elem.bind('mousedown',on_event)
            elem.bind('mouseup',on_event)
            elem.bind('keydown',on_event)
            elem.bind('keyup',on_event)
        if the_element is not None:
            init_html()
        elif hasattr(self,'bind') and hasattr(self,'attachShadow'):
            s = self.attachShadow({'mode': 'open'})
            c = browser.window.document.createElement('canvas')
            s.appendChild(c)
            init_html(c)
    def get_events(self):
        e = self._events
        self._events = []
        return e
async def p_eval(item,vector):
    pass
def pg_main():
    global uib, eb
    display = None
    if pygame is not None:
        pygame.init()
        display = pygame.display.set_mode((600,600))
        display.get_events = pygame.event.get
        display.QUIT = pygame.QUIT
    elif browser is not None:
        display = BrowserDisplay(None)
    done = False
    while not done:
        for ui in uib:
            yield {'type': 'uiexec','data': ui}
            ui(display)
        uib = []
        for event in display.get_events():
            if event.type == display.QUIT: 
                done = True
                break
            else:
                yield {'type': 'handled_event','data': event}
                eb.append(event)
def vm_main():
    vector = []
    async def boot():
        nonlocal vector
        while len(vector) != 0:
            i = vector[-1]
            vector = vector[:-1]
            try:
                await i.eval(vector)
            except Exception:
                await p_eval(i,vector)
    boot()