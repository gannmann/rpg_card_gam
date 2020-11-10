class Player():
    def __init__(self, number, hand, health, attack, speed, points):
        self.number = number
        self.hand = hand
        self.health = health
        self.max_health = health
        self.attack = attack
        self.speed = speed
        self.points = points