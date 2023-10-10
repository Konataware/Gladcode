start = True
import random
randomico = random.randint(1,20)
SegundoRandomico = random.randint(1,20)
MeuY = ''
SemInimigo = False
foiAtacado = ''
def loop():
    global start,randomico,SegundoRandomico, MeuY, SemInimigo, foiAtacado
    upgradeINT(5)
    
    if not isSafeHere():
        moveTo(12.5,12.5)
        teleport(12.5,12.5)
        speak("Fim? A jornada não acaba aqui.")
    elif getHit() :
        teleport(randomico,SegundoRandomico)
        stepLeft()
        MeuY =getY()
        turnToLastHit()
    elif getCloseEnemy(): 
        if getAp() >= 40:
            fireball(getTargetX(), getTargetY())
            if isBurning():
                stepBack()
            speak("Volte para o abismo!")
        else:
            attackRanged(getTargetX(), getTargetY())
    elif start:
        moveTo(12, 12)  
        if getX() == 12 and getY() == 12:
            start = False
            speak("Se falharmos, caímos.")
    else:
       if isSafeHere():
            turn(60)
                
                
        
