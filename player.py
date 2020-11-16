global P1
global P2
global P3 
global P4

class Player():
    def __init__(self, health, attack, defense, speed, points=0):
        self.max_health = health
        self.current_health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.points = points


def init_players():
    global P1, P2, P3, P4
    P1 = Player(health = 3, attack = 1, defense = 0, speed = 0)
    P2 = Player(health = 3, attack = 1, defense = 0, speed = 0)
    P3 = Player(health = 3, attack = 1, defense = 0, speed = 0)
    P4 = Player(health = 3, attack = 1, defense = 0, speed = 0)

def render_player_labels(font, screen, screen_size):
    global P1, P2, P3, P4

    P1_text = 'P1: ' + str(P1.points) + " coins"
    text_surface = font.render(P1_text, True, (255, 255, 255), (0, 0, 0))
    screen.blit(text_surface, (screen_size[0]//2.5, screen_size[1]-6*text_surface.get_rect().height))

    P2_text = 'P2: ' + str(P2.points) + " coins"
    text_surface = font.render(P2_text, True, (255, 255, 255), (0, 0, 0))
    screen.blit(text_surface, (text_surface.get_rect().width, screen_size[1]//2))

    P3_text = 'P3: ' + str(P3.points) + " coins"
    text_surface = font.render(P3_text, True, (255, 255, 255), (0, 0, 0))
    screen.blit(text_surface, (screen_size[0]//2.5, 5*text_surface.get_rect().height))
    
    P4_text = 'P4: ' + str(P4.points) + " coins"
    text_surface = font.render(P4_text, True, (255, 255, 255), (0, 0, 0))
    screen.blit(text_surface, (screen_size[0]-2*text_surface.get_rect().width, screen_size[1]//2))
