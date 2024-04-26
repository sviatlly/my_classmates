from pygame import *
mixer.init()
font.init()
shrift = font.SysFont('Comic Sans MS',60)
pep_win = shrift.render('Пепа выигруля ',True,(250, 10, 226))
pep_lose = shrift.render('Пепа не крутая ',True,(250, 10, 226))
shrep_win = shrift.render('Шрепа выигруля ',True,(13, 235, 9))
shrep_lose = shrift.render('Шрепа не крутая ',True,(13, 235, 9))
W = 700
H = 700
window = display.set_mode((W, H))
backround = transform.scale(image.load('background.jpg'),(W, H)) 
lose_backround =transform.scale(image.load('наташа.jpeg'),(W, H)) 
window.blit(backround,(0,0))
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')

class Peppahead(sprite.Sprite):
    def __init__ (self,x,y,file_name,w,h):
        super().__init__()
        self.peppa = transform.scale(image.load(file_name),(w,h))
        self.x_speed = 0
        self.y_speed = 0
        self.rect= Rect(x,y,w,h)
        self.x_finish = None
        self.y_finish = None

    def pep_move(self): 
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x <= 0:
            self.rect.x = 0
            kick.play()
        if self.rect.right >= W:
            self.rect.right = W
            kick.play()
        if self.rect.bottom >= H: 
            self.rect.bottom = H
            kick.play()
        if self.rect.y <= 0: 
            self.rect.y = 0
            kick.play()
        if self.x_finish is not None:    #проверка мыши
            if self.x_speed > 0 and self.rect.centerx > self.x_finish:
                self.x_finish = None
                self.x_speed = 0
            if self.x_speed < 0 and self.rect.centerx < self.x_finish:
                self.x_finish = None
                self.x_speed = 0
        if self.y_finish is not None:     
            if self.y_speed > 0 and self.rect.centery > self.y_finish:
                self.y_finish = None
                self.y_speed = 0
            if self.y_speed < 0 and self.rect.centery < self.y_finish:
                self.y_finish = None
                self.y_speed = 0
        for wall in walls:   #проверка стен
            if sprite.collide_rect(self,wall):
               global game_mode 
               game_mode = 'walls touch'
                              
    def pep_draw(self):
        window.blit(self.peppa,(self.rect.x,self.rect.y))

    def memory_finish(self,x,y):
        self.x_finish,self.y_finish = x,y

class Wall(sprite.Sprite):
    def __init__(self,x,y,w,h,color):
        super().__init__()
        self.rect = Rect(x,y,w,h)
        self.color = color
        walls.append(self)
    def draw(self):
        draw.rect(window,self.color,self.rect)

class Finish(sprite.Sprite):
    def __init__ (self,x,y,file_name,w,h):
        super().__init__()
        self.image = transform.scale(image.load(file_name),(w,h))
        self.rect= Rect(x,y,w,h)
    def finish_draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

peppa = Peppahead(x = 350,y =300,w= 50,h =50,file_name = 'Peppa pig.jpeg')
shreppa =Peppahead(x = 325,y =300,w= 50,h =50,file_name = 'Shreppa.jpeg')
finish = Finish(x = 10,y =10,w= 30,h =30,file_name = 'treasure.png')
walls = []
wall_1 = Wall(x=200,y=0,w=30,h=400,color=(225,0,250))
wall_2 = Wall(x=200,y=400,w=300,h=30,color=(225,0,250))
wall_3 = Wall(x=470,y=177,w=30,h=250,color=(225,0,250))
wall_4 = Wall(x=330,y=150,w=170,h=30,color=(225,0,250))
wall_5 = Wall(x=330,y=90,w=30,h=90,color=(225,0,250))
wall_6 = Wall(x=200,y=260,w=100,h=30,color=(225,0,250))
wall_7 = Wall(x=580,y=0,w=30,h=300,color=(225,0,250))
wall_8 = Wall(x=580,y=300,w=70,h=30,color=(225,0,250))
wall_9 = Wall(x=580,y=150,w=70,h=30,color=(225,0,250))
wall_10 = Wall(x=630,y=300,w=30,h=300,color=(225,0,250))
wall_11 = Wall(x=430,y=570,w=200,h=30,color=(225,0,250))
wall_12 = Wall(x=500,y=510,w=30,h=60,color=(225,0,250))
wall_13 = Wall(x=500,y=510,w=60,h=30,color=(225,0,250))
wall_14 = Wall(x=330,y=400,w=30,h=100,color=(225,0,250))
wall_15 = Wall(x=115,y=570,w=200,h=30,color=(225,0,250))
wall_16 = Wall(x=100,y=140,w=30,h=460,color=(225,0,250))
wall_17 = Wall(x=115,y=500,w=125,h=30,color=(225,0,250))
wall_18 = Wall(x=115,y=140,w=100,h=30,color=(225,0,250))
wall_19 = Wall(x=0,y=80,w=120,h=30,color=(225,0,250))
#wall_20 = Wall(x=90,y=50,w=30,h=30,color=(225,0,250))

game_mode = 'game'

while True:
    window.blit(backround,(0,0))
    if game_mode == 'game':
        for wall in walls:
            wall.draw()
        peppa.pep_move()
        peppa.pep_draw()
        shreppa.pep_draw()
        shreppa.pep_move()
        finish.finish_draw()
        if sprite.collide_rect(peppa,finish):
            game_mode = 'pep_finish'
        if sprite.collide_rect(shreppa,finish):
            game_mode = 'shrep_finish'
    if game_mode == 'pep_finish':
        window.blit(pep_win,(100,100))
        window.blit(shrep_lose,(100,300))
    if game_mode == 'shrep_finish':
        window.blit(shrep_win,(100,100))
        window.blit(pep_lose,(100,300))
    if game_mode == 'walls touch':
        window.blit(lose_backround,(0,0))
    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.key == K_w:
                peppa.y_speed -= 0.5
            if e.key == K_UP:
                shreppa.y_speed -= 0.5
            
            if e.key == K_s:
                peppa.y_speed += 0.5
            if e.key == K_DOWN:
                shreppa.y_speed += 0.5
            
            if e.key == K_a:
                peppa.x_speed -= 0.5
            if e.key == K_LEFT:
                shreppa.x_speed -= 0.5
            
            if e.key == K_d:
                peppa.x_speed += 0.5
            if e.key == K_RIGHT:
                shreppa.x_speed += 0.5
        
        if peppa.x_speed >= 5:
            peppa.x_speed = peppa.x_speed - 1.5
        if peppa.y_speed >= 5:
            peppa.y_speed = peppa.y_speed - 1.5
        if e.type == MOUSEBUTTONDOWN:
            click_x,click_y= e.pos
            peppa.memory_finish(click_x, click_y)
            if peppa.rect.x > click_x:
                peppa.x_speed -= 1
            if peppa.rect.x < click_x:
                peppa.x_speed += 1
            if peppa.rect.y < click_y:
                peppa.y_speed += 1
            if  peppa.rect.y > click_y:
                peppa.y_speed -= 1    
            #peppa.rect.x, peppa.rect.y = e.pos
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)
    
    display.update()