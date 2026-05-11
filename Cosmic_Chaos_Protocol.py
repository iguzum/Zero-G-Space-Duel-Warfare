import random

class CCP:
    def __init__(self, player1, player2, surface, border_rect):
        self.player1 = player1
        self.player2 = player2
        self.surface = surface
        self.border_rect = border_rect

        self.event = None
        self.effect_name = None
        self.selected_player = None

        # Store original values
        self.base_p1_speed = player1.bullet_speed
        self.base_p2_speed = player2.bullet_speed

        self.base_p1_ammo = player1.max_bullets
        self.base_p2_ammo = player2.max_bullets
        
        self.base_p1_damage = player1.damage
        self.base_p2_damage = player2.damage
        
    def random_event(self):
        self.event = random.randint(1,7)

    def pick_player(self):
        self.selected_player = random.randint(1, 2)

    # RESET EVERYTHING BEFORE NEW EFFECT
    def reset_effects(self):
        self.player1.bullet_speed = self.base_p1_speed
        self.player2.bullet_speed = self.base_p2_speed

        self.player1.max_bullets = self.base_p1_ammo
        self.player2.max_bullets = self.base_p2_ammo
        
        self.player1.damage = self.base_p1_damage
        self.player2.damage = self.base_p2_damage
        
        self.player1.inverted_controls = False
        self.player2.inverted_controls = False
        
    def apply(self):
        if self.event == 1:
            self.effect_name = "NORMAL"
            
        if self.event == 2:
            self.effect_name = "FAST BULLET"
            if self.selected_player == 1:
                self.player1.bullet_speed = self.base_p1_speed + 10
            else:
                self.player2.bullet_speed = self.base_p2_speed + 10

        elif self.event == 3:
            self.effect_name = "HEALTH RECOVERY"
            self.player1.health = 10
            self.player2.health = 10

        elif self.event == 4:
            self.effect_name = "UNLIMITED AMMO"

            if self.selected_player == 1:
                self.player1.max_bullets = 25
            else:
                self.player2.max_bullets = 25
                
        elif self.event == 5:
            self.effect_name = "DOUBLE DAMAGE"
            if self.selected_player == 1:
                self.player1.damage = 2
            else:
                self.player2.damage = 2
        
        elif self.event == 6:
            self.effect_name = "NO ESCAPE"
            
        elif self.event == 7:
            self.effect_name = "KEYBOARD MALFUNCTION" # Invert the key inputs
            if self.selected_player == 1 or self.selected_player == 2:
                self.player1.inverted_controls = True
                self.player2.inverted_controls = True

        print("NEW EVENT:", self.effect_name)
        
    # MAIN FUNCTION (called every 20 sec)
    def generate_event(self):
        self.reset_effects()   # remove old effect
        self.random_event()   # generate new number
        self.pick_player()    # choose player
        self.apply()          # apply effect

    # UPDATE BASED ON EVENT
    def update(self):
        if self.event == 6:
            # Move border LEFT
            if self.selected_player == 1:
                if self.border_rect.x > 200:
                    self.border_rect.x -= 5
                    
                # Push away
                if self.player1.rect.right >= self.border_rect.left:
                    self.player1.rect.right = self.border_rect.left

            # Move border RIGHT
            elif self.selected_player == 2:
                if self.border_rect.x < 1000:
                    self.border_rect.x += 5
                
                # Push away 
                if self.player2.rect.left <= self.border_rect.right:
                    self.player2.rect.left = self.border_rect.right

        else:
            # Animate back to center
            if self.border_rect.x < self.surface.get_width() //2:
                self.border_rect.x += 5

            elif self.border_rect.x >  self.surface.get_width() //2:
                self.border_rect.x -= 5

            # Keep players outside border
            if self.player1.rect.right > self.border_rect.left:
                self.player1.rect.right = self.border_rect.left

            if self.player2.rect.left < self.border_rect.right:
                self.player2.rect.left = self.border_rect.right