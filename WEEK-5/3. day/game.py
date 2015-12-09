class Character():
    def __init__(self,health=20,armor=10):
        self._health = health
        self._armor = armor
        self._isAlive = True

    def sufferDamage(self,damage):
        sufferDamage = self._health + self._armor - damage

        if sufferDamage < 1:
            self._isAlive = False

    def heal(self, heal):
        self._health += heal

    def isAlive(self):
        return self._isAlive

    def getHealth(self):
        return self._health

def handleEvents(eventList):
    list(map(handleEvent,eventList))

def handleEvent(event):
    eventHandlers[event['type']](event)

def applyHeal(event):
    event['character'].heal(event['size'])

def applyDamage(event):
    event['character'].sufferDamage(event['size'])

eventHandlers = {
    'damage':applyDamage,
    'heal':applyHeal
}
