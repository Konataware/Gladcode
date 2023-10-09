from functionsglad import *

is_targetDead = False
alvo_x = 12.5
alvo_y = 12.5
angulo_hit = 0
start = True
meu_x = 12.5
meu_y = 12.5
meu_agi = 15
in_unsafezone = False
distancia_do_alvo = 12.5
my_hp = 12.5

def VariablesScopeToGlobal():
    global my_hp, is_targetDead, alvo_x, alvo_y, angulo_hit, start, meu_x, meu_y, meu_agi, in_unsafezone, distancia_do_alvo
VariablesScopeToGlobal()
def ChooseEnemy():
    if getLowHp() or getCloseEnemy():
        speak("Um inseto caminhando para o matadouro.")
        moveToTarget()
def AtaqueCharge():
    speak("VENHA AQUI!")
    charge()              
def ArenaCombatMovement():
    while getTargetHealth() > 0:
        turnTo(alvo_x, alvo_y)        
        stepLeft()
        attackMelee()

def BlockEffect():
    if getBlockTimeLeft() <= 0:
        speak("Sobrevivência favorece o mais forte.")
        block()

def GoToSafezone():
    if not isSafeThere(meu_x-1, meu_y-1) or not isSafeThere(meu_x+1, meu_y+1):
        speak("VOCÊ TÁ BRINCANDO COMIGO?")
        turnTo(12.5, 12.5)
        while(in_unsafezone):
            moveForward(2)
            if isSafeHere() or not isSafeThere(12.5,12.5):
                in_unsafezone = True
def ArenaIdleMovement():
    stepLeft()
    turnTo(12.5, 12.5)
    
def TurnToHit():
    angulo_hit = getLastHitAngle()
    turnToAngle(angulo_hit)
    if not getCloseEnemy:
        stepLeft()
        charge()
        moveForward(9)

def VariableUpdate():
    meu_y = getY()
    meu_x = getX()
    angulo_hit = getLastHitAngle()
    alvo_x = getTargetX()
    alvo_y = getTargetY()
    distancia_do_alvo = getDistToTarget()
    my_hp = getHp()
def UpgradeStats():
    if meu_agi < 20:
        upgradeAGI(5)
        minha_agi = getAGI()
    else:
        upgradeSTR(5)

def LowHP():
    speak("Essa é a dor... Eu esqueci da sensação...")
    charge()
    moveTo(12.5, 12.5)

def loop():
    VariablesScopeToGlobal()
    global MeleeAttack, ChooseEnemy, AtaqueChargem, ArenaCombatMovement, BlockEffect, GoToSafezone, ArenaIdleMovement, TurnToHit, VariableUpdate, UpgradeStats, LowHP, MovementAlgorithm, VariableUpdate, UpgradeStats, LowHP
    
    VariableUpdate()
    UpgradeStats()
    LowHP()
    GoToSafezone()

    if getLowHp() or getCloseEnemy():
        speak("Um inseto caminhando para o matadouro.")
        moveToTarget()
        if getBlockTimeLeft() <= 0:
            BlockEffect()
        if distancia_do_alvo >= 3:
            AtaqueCharge()
        elif distancia_do_alvo <= 2:
            ArenaCombatMovement()
        
    

    elif getHit():
        TurnToHit()
    
    else:
        ArenaIdleMovement()