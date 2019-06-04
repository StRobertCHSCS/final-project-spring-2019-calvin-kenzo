import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 2.5
LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED, DOWN_PRESSED = False, False, False, False
PAGE = 1
FONT_SIZE = 15
RECT_CENTER_X = 400
RECT_CENTER_Y = 200
RECT_DISTANCE_FROM_CENTER = 250
PLAYER_MOVEMENT_BORDERS = 20
SPEAR_COUNT1 = 7
SPEAR_COUNT2 = 5


class Menu:
    def __init__(self):
        # Ruins image from Reddit user u/Minoz99
        self.texture = arcade.load_texture("images/ruins.png")

    def draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(40, 80, self.texture.width,
                                      self.texture.height, self.texture, 0)

        arcade.draw_text("Press space to play", 225, 200, arcade.color.WHITE, 2*FONT_SIZE)
        arcade.draw_text("Press I for instructions", 200, 125, arcade.color.WHITE, 2*FONT_SIZE)

        arcade.finish_render()


class Instructions:
    def __init__(self):
        self.texture = arcade.load_texture("images/ruins.png")

        # Heart image from Undertale Wiki.  Purple heart pallet change done by Calvin.
        self.texture_heart = arcade.load_texture("images/heart.png")
        self.texture_heart_purple = arcade.load_texture("images/heart_purple.png")
        self.scale = 0.025

    def draw(self):
        arcade.start_render()

        # Draws background
        arcade.draw_texture_rectangle(40, 80, self.texture.width,
                                      self.texture.height, self.texture, 0)

        # Draws hearts
        arcade.draw_texture_rectangle(475, 280, self.scale * self.texture_heart.width,
                                      self.scale * self.texture_heart.height, self.texture_heart, 0)
        arcade.draw_texture_rectangle(475, 230, self.scale * self.texture_heart_purple.width,
                                      self.scale * self.texture_heart_purple.height, self.texture_heart_purple, 0)

        arcade.draw_text("INSTRUCTIONS", 150, 525, arcade.color.WHITE, 50)
        arcade.draw_text("In this game, you play as a heart.  Use the arrow keys to move", 50, 470, arcade.color.WHITE, FONT_SIZE)
        arcade.draw_text("Avoid attacks at all costs! Keep dodging until time runs out", 50, 425, arcade.color.WHITE, FONT_SIZE)
        arcade.draw_text("If your HP hits 0, you lose!", 50, 375, arcade.color.WHITE, FONT_SIZE)
        arcade.draw_text("Be careful! The enemy can change your controls!", 50, 325, arcade.color.WHITE, FONT_SIZE)
        arcade.draw_text("The red heart can move freely but...", 50, 275, arcade.color.WHITE, FONT_SIZE)
        arcade.draw_text("The purple heart is affected by gravity.", 50, 225, arcade.color.WHITE, FONT_SIZE)
        arcade.draw_text("Press the UP key to jump when you're purple", 50, 175, arcade.color.WHITE, FONT_SIZE)
        arcade.draw_text("Press space to start the game", 175, 100, arcade.color.WHITE, FONT_SIZE + 10)
        arcade.finish_render()


class GameOver:
    def __init__(self):
        # Broken heart image from Redbubble.com
        self.texture = arcade.load_texture("images/broken_heart.jpg")
        self.texture_heart = arcade.load_texture("images/heart.png")
        self.scale = 0.1
        self.counter = 0

    def draw(self):
        self.counter += 1
        if self.counter <= 45:
            arcade.draw_texture_rectangle(400, 300, self.scale * self.texture_heart.width,
                                          self.scale * self.texture_heart.height, self.texture_heart, 0)
        elif self.counter > 46:
            arcade.draw_texture_rectangle(400, 300, self.texture.width,
                                          self.texture.height, self.texture, 0)
            if self.counter >= 80:
                arcade.draw_text("GAME OVER", 210, 525, arcade.color.WHITE, 50)


class Spears1(arcade.Sprite):
    def update(self):
        self.center_x -= 4


class Spears2(arcade.Sprite):
    def update(self):
        self.center_x += 3


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

        # Create Menu Screen
        self.menu = Menu()

        # Create Instructions Screen
        self.instructions = Instructions()

        # Create Game Over screen
        self.game_over = GameOver()

        # Initialize variables used in the setup function
        self.player_list = None
        self.spear_list1 = None
        self.spear_list2 = None
        self.player_sprite = None
        self.size = None
        self.center_x = None
        self.center_y = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.spear_list1 = arcade.SpriteList()
        self.spear_list2 = arcade.SpriteList()

        # Set up the player
        # Heart image from Undertale Wiki
        self.player_sprite = arcade.Sprite("images/heart.png", 0.025)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)

        # Set up variables for spear_list1
        self.size = 0.3
        self.center_x = 700
        self.center_y = 75

        for i in range(SPEAR_COUNT1):
            # Set up the spear
            # Image self made
            spear = Spears1("images/spear_up.png", self.size)
            # Center the spear
            spear.center_x = self.center_x
            spear.center_y = self.center_y
            # Add spear to the list of spears
            self.spear_list1.append(spear)
            # Change size and position of spear
            self.size += 0.05
            self.center_x += 30 + 5*i
            spear.center_y += 25 + 5*i

        # Set up variables for spear_list2
        self.size = 0.3
        self.center_x = 50
        self.center_y = 330

        for i in range(SPEAR_COUNT2):
            # Set up the spear
            # Image self made
            spear = Spears2("images/spear_down.png", self.size)
            # Center the spear
            spear.center_x = self.center_x
            spear.center_y = self.center_y
            # Add spear to the list of spears
            self.spear_list1.append(spear)
            # Change size and position of spear
            self.size += 0.05
            self.center_x += 30 + 5*i
            spear.center_y -= 25 + 5*i

    def on_draw(self):
        arcade.start_render()
        if PAGE == 1:
            self.menu.draw()
        elif PAGE == 2:
            self.instructions.draw()
        elif PAGE == 3:
            self.player_list.draw()
            self.spear_list1.draw()
            arcade.draw_rectangle_outline(RECT_CENTER_X, RECT_CENTER_Y, RECT_DISTANCE_FROM_CENTER,
                                          RECT_DISTANCE_FROM_CENTER, arcade.color.WHITE, 1)
        elif PAGE == 4:
            self.game_over.draw()

    def update(self, delta_time):
        global PAGE
        # Check if the heart is supposed to move
        if (LEFT_PRESSED is True and self.player_sprite.center_x
                > RECT_CENTER_X - RECT_DISTANCE_FROM_CENTER/2 + PLAYER_MOVEMENT_BORDERS):
            self.player_sprite.center_x -= MOVEMENT_SPEED
        if (RIGHT_PRESSED is True and self.player_sprite.center_x
                < RECT_CENTER_X + RECT_DISTANCE_FROM_CENTER/2 - PLAYER_MOVEMENT_BORDERS):
            self.player_sprite.center_x += MOVEMENT_SPEED
        if (UP_PRESSED is True and self.player_sprite.center_y
                < RECT_CENTER_Y + RECT_DISTANCE_FROM_CENTER/2 - PLAYER_MOVEMENT_BORDERS):
            self.player_sprite.center_y += MOVEMENT_SPEED
        if (DOWN_PRESSED is True and self.player_sprite.center_y
                > RECT_CENTER_Y - RECT_DISTANCE_FROM_CENTER/2 + PLAYER_MOVEMENT_BORDERS):
            self.player_sprite.center_y -= MOVEMENT_SPEED

        self.spear_list1.update()
        self.spear_list2.update()

        # Generate a list of all sprites that collided with the player.
        player_hit_list1 = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.spear_list1)
        player_hit_list2 = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.spear_list1)

        if len(player_hit_list1) > 0 or len(player_hit_list2) > 0:
            PAGE = 4
    def on_key_press(self, key, modifiers):
        """ Called whenever a user presses a key """
        global LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED, DOWN_PRESSED, PAGE

        if key == arcade.key.RIGHT:
            RIGHT_PRESSED = True
        elif key == arcade.key.LEFT:
            LEFT_PRESSED = True
        if key == arcade.key.UP:
            UP_PRESSED = True
        elif key == arcade.key.DOWN:
            DOWN_PRESSED = True

        if PAGE == 1 and key == arcade.key.SPACE:
            PAGE = 3
        if PAGE == 1 and key == 105:
            PAGE = 2
        if PAGE == 2 and key == arcade.key.SPACE:
            PAGE = 3

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        global LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED, DOWN_PRESSED

        if key == arcade.key.RIGHT:
            RIGHT_PRESSED = False
        elif key == arcade.key.LEFT:
            LEFT_PRESSED = False
        if key == arcade.key.UP:
            UP_PRESSED = False
        elif key == arcade.key.DOWN:
            DOWN_PRESSED = False


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "CPT FINAL")
    window.setup()
    arcade.run()


main()
