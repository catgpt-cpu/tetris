import pygame, random

pygame.init()

info = pygame.display.Info()
W, H = info.current_w, info.current_h
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("tetris")

COLS, ROWS = 10, 20
BLOCK = W // 12
PLAY_W = COLS * BLOCK
PLAY_H = ROWS * BLOCK

offset_x = (W - PLAY_W) // 2
offset_y = 100

font = pygame.font.SysFont("Arial", int(BLOCK*0.8))

SHAPES = [
[[1,1,1,1]],
[[1,1],[1,1]],
[[0,1,0],[1,1,1]],
[[1,0,0],[1,1,1]],
[[0,0,1],[1,1,1]],
[[1,1,0],[0,1,1]],
[[0,1,1],[1,1,0]]
]

def rotate(s):
    return [list(r) for r in zip(*s[::-1])]

def try_rotate(p, g):
    old_shape = p["s"]
    old_x = p["x"]
    new_shape = rotate(old_shape)
    kicks = [0,-1,1,-2,2,-3,3,-4,4]
    for k in kicks:
        p["s"] = new_shape
        p["x"] = old_x + k
        if valid(p,g):
            return True
    p["s"] = old_shape
    p["x"] = old_x
    return False

def random_color():
    return random.choice([
        (0,255,255),(0,200,255),(0,150,255),
        (0,0,255),(255,165,0),(255,255,0),
        (0,255,0),(255,0,0),(255,255,255)
    ])

def new():
    s=random.choice(SHAPES)
    return {"s":s,"x":COLS//2-len(s[0])//2,"y":0,"c":random_color()}

def valid(p,g):
    for y,r in enumerate(p["s"]):
        for x,v in enumerate(r):
            if v:
                nx,ny=p["x"]+x,p["y"]+y
                if nx<0 or nx>=COLS or ny>=ROWS:
                    return False
                if ny>=0 and g[ny][nx]:
                    return False
    return True

def merge(p,g):
    for y,r in enumerate(p["s"]):
        for x,v in enumerate(r):
            if v:
                g[p["y"]+y][p["x"]+x]=p["c"]

def get_full_lines(g):
    return [i for i,row in enumerate(g) if all(v!=0 for v in row)]

def clear_lines(g, lines):
    for i in sorted(lines, reverse=True):
        del g[i]
    for _ in lines:
        g.insert(0,[0]*COLS)
    return g

grid=[[0]*COLS for _ in range(ROWS)]
p=new()
clock=pygame.time.Clock()

fall=0
move_timer=0
hold_time=0

score=0
game_over=False

clear_lines_anim=[]
clear_timer=0

btn_y=offset_y+PLAY_H+10
btn_w=W//4
btn_h=110

btn_left=pygame.Rect(0,btn_y,btn_w,btn_h)
btn_down=pygame.Rect(btn_w,btn_y,btn_w,btn_h)
btn_rot=pygame.Rect(btn_w*2,btn_y,btn_w,btn_h)
btn_right=pygame.Rect(btn_w*3,btn_y,btn_w,btn_h)

pause_btn=pygame.Rect(W//2-45,3,90,90)

holding={"left":False,"right":False,"down":False,"rot":False}
paused=False

menu_w=280
menu_h=100
resume_btn=pygame.Rect(W//2-menu_w//2,H//2-70,menu_w,menu_h)
reset_btn=pygame.Rect(W//2-menu_w//2,H//2+60,menu_w,menu_h)

def reset_game():
    global grid,p,score,game_over,fall,clear_lines_anim,clear_timer
    grid=[[0]*COLS for _ in range(ROWS)]
    p=new()
    score=0
    game_over=False
    fall=0
    clear_lines_anim=[]
    clear_timer=0

def clear_inputs():
    global holding,hold_time,move_timer
    holding={k:False for k in holding}
    hold_time=0
    move_timer=0

def draw_button(rect,pressed):
    offset=6 if pressed else 0
    color=(40,40,40) if pressed else (70,70,70)
    pygame.draw.rect(
        screen,color,
        (rect.x,rect.y+offset,rect.w,rect.h),
        border_radius=20
    )

def draw_menu_button(rect,text):
    pygame.draw.rect(screen,(70,70,70),rect,border_radius=20)
    pygame.draw.rect(screen,(255,255,255),rect,4,border_radius=20)
    t=font.render(text,True,(255,255,255))
    screen.blit(
        t,
        (rect.centerx-t.get_width()//2,
         rect.centery-t.get_height()//2)
    )

run=True
while run:
    dt=clock.tick(60)

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False

        if e.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()

            if (not paused) and pause_btn.collidepoint(mx,my):
                paused=True
                clear_inputs()

            if game_over:
                reset_game()
                continue

            if paused:
                if resume_btn.collidepoint(mx,my):
                    clear_inputs()
                    paused=False
                elif reset_btn.collidepoint(mx,my):
                    clear_inputs()
                    reset_game()
                    paused=False
                continue

            if btn_left.collidepoint(mx,my):
                holding["left"]=True # <--- UDAH GA PAKE clear_inputs()
                hold_time=0
                move_timer=0
                p["x"]-=1 # langsung jalan 1x pas di tap
                if not valid(p,grid):
                    p["x"]+=1

            if btn_down.collidepoint(mx,my):
                holding["down"]=True
                fall = 80

            if btn_rot.collidepoint(mx,my):
                holding["rot"]=True
                try_rotate(p,grid)

            if btn_right.collidepoint(mx,my):
                holding["right"]=True # <--- UDAH GA PAKE clear_inputs()
                hold_time=0
                move_timer=0
                p["x"]+=1 # langsung jalan 1x pas di tap
                if not valid(p,grid):
                    p["x"]-=1

        if e.type==pygame.MOUSEBUTTONUP:
            if btn_down.collidepoint(e.pos):
                holding["down"]=False
            elif btn_left.collidepoint(e.pos):
                holding["left"]=False
            elif btn_right.collidepoint(e.pos):
                holding["right"]=False
            elif btn_rot.collidepoint(e.pos):
                holding["rot"]=False
            hold_time=0
            move_timer=0

    if not game_over and not paused:
        speed=80 if holding["down"] else 800
        fall+=dt
        if fall>speed:
            p["y"]+=1
            if not valid(p,grid):
                p["y"]-=1
                merge(p,grid)
                lines=get_full_lines(grid)
                if lines:
                    clear_lines_anim=lines
                else:
                    p=new()
                    if not valid(p,grid):
                        game_over=True
            fall=0

        if holding["left"]:
            hold_time+=dt
            move_timer+=dt
            if hold_time>200 and move_timer>80: # delay awal 200ms, abis itu 80ms
                p["x"]-=1
                if not valid(p,grid):
                    p["x"]+=1
                move_timer=0

        if holding["right"]:
            hold_time+=dt
            move_timer+=dt
            if hold_time>200 and move_timer>80:
                p["x"]+=1
                if not valid(p,grid):
                    p["x"]-=1
                move_timer=0

        if clear_lines_anim:
            clear_timer+=dt
            if clear_timer>200:
                grid=clear_lines(grid,clear_lines_anim)
                score+=len(clear_lines_anim)*10
                clear_lines_anim=[]
                clear_timer=0
                p=new()

    screen.fill((0,0,0))
    screen.blit(font.render("Score: "+str(score),1,(255,255,255)),(20,20))
    pygame.draw.rect(screen,(255,255,255),(offset_x-4,offset_y-4,PLAY_W+8,PLAY_H+8),4)

    for y in range(ROWS):
        for x in range(COLS):
            rect=(offset_x+x*BLOCK,offset_y+y*BLOCK,BLOCK,BLOCK)
            color=grid[y][x] if grid[y][x] else (0,0,0)
            if y in clear_lines_anim:
                if (pygame.time.get_ticks()//120)%2==0:
                    color=(255,255,255)
            pygame.draw.rect(screen,color,rect)
            pygame.draw.rect(screen,(30,30,30),rect,1)

    for y,r in enumerate(p["s"]):
        for x,v in enumerate(r):
            if v:
                rect=(offset_x+(p["x"]+x)*BLOCK,offset_y+(p["y"]+y)*BLOCK,BLOCK,BLOCK)
                pygame.draw.rect(screen,p["c"],rect)
                pygame.draw.rect(screen,(255,255,255),rect,2)

    draw_button(btn_left,holding["left"])
    draw_button(btn_down,holding["down"])
    draw_button(btn_rot,holding["rot"])
    draw_button(btn_right,holding["right"])

    # ICON 1: KIRI <
    pygame.draw.polygon(screen,(255,255,255),[
        (btn_left.centerx-18,btn_left.centery),
        (btn_left.centerx+18,btn_left.centery-22),
        (btn_left.centerx+18,btn_left.centery+22)
    ])

    # ICON 2: BAWAH V
    pygame.draw.polygon(screen,(255,255,255),[
        (btn_down.centerx-20,btn_down.centery-15),
        (btn_down.centerx+20,btn_down.centery-15),
        (btn_down.centerx,btn_down.centery+22)
    ])

    # ICON 3: ROTATE ↻
    cx, cy = btn_rot.centerx, btn_rot.centery
    pygame.draw.circle(screen,(255,255,255),(cx,cy),22,4)
    pygame.draw.polygon(screen,(255,255,255),[
        (cx+22,cy-5),
        (cx+10,cy-15),
        (cx+22,cy+5)
    ])

    # ICON 4: KAN >
    pygame.draw.polygon(screen,(255,255,255),[
        (btn_right.centerx+18,btn_right.centery),
        (btn_right.centerx-18,btn_right.centery-22),
        (btn_right.centerx-18,btn_right.centery+22)
    ])

    pygame.draw.rect(screen,(70,70,70),pause_btn,border_radius=18)
    cx,cy=pause_btn.centerx,pause_btn.centery
    if not paused:
        pygame.draw.rect(screen,(255,255,255),(cx-20,cy-25,10,50))
        pygame.draw.rect(screen,(255,255,255),(cx+10,cy-25,10,50))
    else:
        pygame.draw.polygon(screen,(255,255,255),[(cx-15,cy-28),(cx-15,cy+28),(cx+30,cy)])

    if paused:
        overlay=pygame.Surface((W,H))
        overlay.set_alpha(180)
        overlay.fill((0,0,0))
        screen.blit(overlay,(0,0))
        t=font.render("PAUSED",True,(255,255,0))
        screen.blit(t,(W//2-t.get_width()//2,H//2-170))
        draw_menu_button(resume_btn,"RESUME")
        draw_menu_button(reset_btn,"RESET")

    if game_over:
        overlay=pygame.Surface((W,H))
        overlay.set_alpha(160)
        overlay.fill((0,0,0))
        screen.blit(overlay,(0,0))
        t1=font.render("GAME OVER",True,(255,0,0))
        t2=font.render("TAP UNTUK ULANG",True,(255,255,255))
        screen.blit(t1,(W//2-t1.get_width()//2,H//2-60))
        screen.blit(t2,(W//2-t2.get_width()//2,H//2))

    pygame.display.update()

pygame.quit()