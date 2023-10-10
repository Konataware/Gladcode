import random
start = True
Agilidade = 0
Força = 0
Inteligente = 0
randomico = random.randint(1, 12)
SegundoRandomico = random.randint(1, 12)

def loop():
    global start, Agilidade, Força, Inteligente, randomico, SegundoRandomico
    Agilidade = getAGI()
    Força = getSTR()
    Inteligente = getINT()
    if Agilidade < 25:
        upgradeAGI(5)
    elif Inteligente <= 20 and Agilidade >= 25:
        upgradeINT(5)
    if not isSafeHere():
        moveTo(12.5, 12.5)
    elif getHit() and doYouSeeMe():
        turnToLastHit()
        stepLeft()
    elif getCloseEnemy():
      if getDistToTarget() < 4:
        stepBack()
        attackRanged(getTargetX(), getTargetX())
      if getAmbushTimeLeft() <= 1:
            ambush()
            if isStunned() and not doYouSeeMe():
                attackRanged(getTargetX(), getTargetY())
      else:
            attackRanged(getTargetX(), getTargetY())
    elif start:
        moveTo(12, 12)
        if getX() == 12 and getY() == 12:
            start = False
    else:
        turn(60)

