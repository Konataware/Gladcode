from functionsglad import *
is_targetDead = False
alvo_x = None
alvo_y = None
angulo_hit = None
start = True
meu_x = None
meu_y = None
meu_agi = 15 
in_unsafezone = False
distancia_do_alvo = None
my_hp = None

def Ataque():
    def ChooseEnemy():
        if getLowHp() or getCloseEnemy():
            speak("Um inseto caminhando para o matadouro.")
            moveToTarget()
    def AtaqueCharge():
            speak("VENHA AQUI!")
            charge()
    def ArenaCombatMovement():
        stepLeft()
        turnTo(alvo_x, alvo_y)
    def BlockEffect():
        speak("Sobrevivência favorece o mais forte.")
        block()

def MovementAlgorithm():
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
            turnTo(angulo_hit)
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
    if minha_agi <= 20:
        upgradeAGI(5)
        minha_agi = getAGI()
        
    else:
        upgradeSTR(5)

def LowHP():
    speak("Essa é a dor... Eu esqueci da sensação...")
    charge()
    moveTo(12.5, 12,5)

def loop():
    global Ataque, MovementAlgorithm, VariableUpdate, UpgradeStats, LowHP, my_hp, is_targetDead, alvo_esta_morto, alvo_x, alvo_y, angulo_hit, start, meu_x, meu_y, meu_agi, in_unsafezone, distancia_do_alvo

    VariableUpdate
    UpgradeStats
