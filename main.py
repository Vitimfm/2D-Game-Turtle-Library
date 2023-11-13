'''
Fisrt Game
- Vitor Freitas de Meneses  
Sprite 'Link' by 'xander@tsgk.capitainn.net' 
Sprite 'inimigo' by 'zeldapunkgrrl' on Zelda Fan Game Central
Background Sprites: OOT 2D by CheerfulSage & GodsTurf

'''
import turtle
import random

# Screen 
main = turtle.Screen()                  
main.tracer(0)                          # Screen Update
main.title('Zeldinha')                  
main.setup(800, 600)                   
main.bgpic('res/background.gif')            
main.bgcolor('lightgreen')              

# Adding Sprites
main.addshape('res/LinkUp.gif')             
main.addshape('res/LinkLeft.gif')           
main.addshape('res/LinkRight.gif')          
main.addshape('res/LinkDown.gif')           
main.addshape('res/inimigo.gif')            
main.addshape('res/Rupee.gif')              
main.addshape('res/coracao.gif')            

x = 310          
y = 215          
vidas = 3        
placar = 0       
recorde = 0
FPS = 30     #Variável para os frames na função ontimer

# Desenhar Arena Retangular

arena = turtle.Turtle()          # Define turtle
def desenhaArena():              
    arena.penup()                # Para não riscar na trajetória feita
    arena.speed(0)               # Define velocidade do turtle 'arena'    
    arena.pensize(width=4)       # Define largura da caneta
    arena.goto(-340, -250)       # Começa desenhando na parte inferior esquerda da arena
    arena.pendown()              # Para riscar na trajetória feita
    arena.color('black')         # Cor da caneta
desenhaArena()            

for i in range(2):               
    arena.forward(680)           # Anda para frente até o ponto definido
    arena.left(90)               # Vira para esquerda em 90 graus
    arena.forward(500)           # Anda para frente até o ponto definido
    arena.left(90)               # Vira para esquerda em 90 graus
arena.hideturtle()               # Esconde o turtle 'arena'

# Definir Vida, Pessonagem, Inimigo, Rupee e Pontuação e Recorde  

def criaPersonagem(nome, speed, x, y, shape):
    nome.penup()
    nome.speed(speed)
    nome.goto(x, y)
    nome.shape(shape)

def criaPlacar(nome, color, x, y, write, font, Align):
    nome.color(color)
    nome.hideturtle()
    nome.penup()
    nome.goto(x, y)
    nome.write(write, font=(font, 14, 'bold'), align = Align)

coracao1 = turtle.Turtle()
coracao2 = turtle.Turtle()
coracao3 = turtle.Turtle()
persona_1 = turtle.Turtle()
inimigo = turtle.Turtle()
rupee_placar = turtle.Turtle()
rupee = turtle.Turtle()
pontuacao = turtle.Turtle()
recor = turtle.Turtle()

persona_1.veloc = 15
inimigo.veloc = 5 
rupee.veloc = 4 

criaPersonagem(coracao1, 0, -325, 270, 'res/coracao.gif')
criaPersonagem(coracao2, 0, -300, 270, 'res/coracao.gif')
criaPersonagem(coracao3, 0, -275, 270, 'res/coracao.gif')
criaPersonagem(persona_1, 0, 0, 0, 'res/LinkDown.gif') 
criaPersonagem(inimigo, 0, random.randint(-340, 340), random.randint(-250, 250), 'res/inimigo.gif')     
criaPersonagem(rupee, 0, random.randint(-340, 340), random.randint(-250, 250), 'res/Rupee.gif')      
criaPersonagem(rupee_placar, 0, 290, 275, 'res/Rupee.gif')

criaPlacar(pontuacao, 'black', 315, 260, '0', 'Verdana', 'center')
criaPlacar(recor, 'black', 0, 260, 'recorde: 0', 'Verdana', 'center')

# Funções limites do Personagem na arena definindo movimentação 

def persona_1_up():
    persona_1.shape('res/LinkUp.gif')              
    persona_1.setheading(90)                  # setheading define para onde o 'persona_1' está virado
    if persona_1.ycor() < y:                  # Checa ponto y do persona_1
        persona_1.forward(persona_1.veloc)    # condição de andar para frente na velocidade definida
persona_1_up()
def persona_1_right():
    persona_1.shape('res/LinkRight.gif')
    persona_1.setheading(0)
    if persona_1.xcor() < x:
        persona_1.forward(persona_1.veloc)
persona_1_right()
def persona_1_left():
    persona_1.shape('res/LinkLeft.gif')
    persona_1.setheading(180)
    if persona_1.xcor() > -x:
        persona_1.forward(persona_1.veloc)
persona_1_left()
def persona_1_down():
    persona_1.shape('res/LinkDown.gif')
    persona_1.setheading(270)
    if persona_1.ycor() > -y:
        persona_1.forward(persona_1.veloc)
persona_1_down()


# Listen para Movimentação no teclado

main.listen()
main.onkeypress(persona_1_up,'Up')
main.onkeypress(persona_1_down,'Down')
main.onkeypress(persona_1_right,'Right')
main.onkeypress(persona_1_left,'Left')
                             
# Função updateScreen para atualização da tela

def updateScreen():
    
    # Movimento e Limite do inimigo

    inimigo.forward(inimigo.veloc)
    if inimigo.ycor() > 220:
        inimigo.sety(220)
        inimigo.setheading(random.randint(0, 360))
    if inimigo.ycor() < -220:
        inimigo.sety(-220)
        inimigo.setheading(random.randint(0, 360))
    if inimigo.xcor() > 310:
        inimigo.setx(310)
        inimigo.setheading(random.randint(0, 360))
    if inimigo.xcor() < -305:
        inimigo.setx(-305)
        inimigo.setheading(random.randint(0, 360))

    # Movimento e Limite do rupee

    rupee.forward(rupee.veloc)
    if rupee.ycor() > 230:
        rupee.sety(230)
        rupee.setheading(random.randint(0, 360))
    if rupee.ycor() < -230:
        rupee.sety(-230)
        rupee.setheading(random.randint(0, 360))
    if rupee.xcor() > 325:
        rupee.setx(325)
        rupee.setheading(random.randint(0, 360))
    if rupee.xcor() < -325:
        rupee.setx(-325)
        rupee.setheading(random.randint(0, 360))
        
    # Colisão Inimigo
        
    def colisaoInimigo():
        global vidas
        global placar 
        global recorde  
        if inimigo.xcor() + 20 >= persona_1.xcor() - 20 and inimigo.xcor() -20 <= persona_1.xcor() + 20 and inimigo.ycor() + 25 >= persona_1.ycor() -25 and inimigo.ycor() - 25 <= persona_1.ycor() + 25:
            inimigo.goto(random.randint(-340, 340),random.randint(-250, 250))   # Define um ponto random para ir após a colisão
            inimigo.setheading(random.randint(0, 360))                     # Define uma direção random após a colisão
            vidas -= 1                      # Perde uma vida após colisão
            if vidas == 2:
                coracao3.hideturtle()       # Some um coração
            elif vidas == 1:
                coracao2.hideturtle()       # Some mais um coração
            else:
                coracao1.hideturtle()       # Some o último coração 
                vidas = 3                   # Vida volta ter 3 corações que serão mostrados novamente
                coracao3.showturtle()
                coracao2.showturtle()
                coracao1.showturtle()
                persona_1.goto(0,0)         # Após perder todas as vidas e restaura-las, jogador vai para o centro do jogo
                if placar > recorde:
                    recorde = placar
                    recor.clear()
                    recor.write('recorde: {}'.format(recorde), font=('Verdana', 15, 'bold'), align='center')
                # Resetar Placar:
                pontuacao.clear()     
                placar = 0
                pontuacao.write('{}'.format(placar), font=('Verdana', 15, 'bold'))
    colisaoInimigo() 
    
    # Colisão Rupee
    
    def colisaoRupee():
        global placar
        global pontuacao
        if rupee.xcor() + 20 >= persona_1.xcor() - 20 and rupee.xcor() -20 <= persona_1.xcor() + 20 and rupee.ycor() + 25 >= persona_1.ycor() - 25 and rupee.ycor() -25 <= persona_1.ycor() + 25:
            rupee.goto(random.randint(-340, 340),random.randint(-250, 250))  # Define um ponto random para ir após a colisão
            rupee.setheading(random.randint(0, 360))                    # Define uma direção random após a colisão
            placar += 1           # Após colisão, placar soma 1
            pontuacao.clear()     # Limpa pontuação anterior
            pontuacao.write('{}'.format(placar), font=('Verdana', 14, 'bold'))   # Reescreve o placar 
    colisaoRupee()
    
    turtle.ontimer(updateScreen, 1000 // 50)        # Para atualização em tempo real da tela

updateScreen()

while True:
    main.update()