import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 4
LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED, DOWN_PRESSED = False, False, False, False
PAGE = 1
FONT_SIZE = 15

class Menu:
    def __init__(self):
        # Ruins image from Reddit user u/Minoz99
        self.texture = arcade.load_texture("images/ruins.png")

    def draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(40, 80, self.texture.width,
                                      self.texture.height, self.texture, 0)

        arcade.draw_text("Press space to play", 225, 200, arcade.color.WHITE, 2*FONT_SIZE)
        arcade.draw_text("Press I to instructions", 200, 125, arcade.color.WHITE, 2*FONT_SIZE)

        arcade.finish_render()


class Instructions:
    def __init__(self):
        self.texture = arcade.load_texture("images/ruins.png")

        # Heart image from Undertale Wiki.  Purple heart colour pallet change done by Calvin.
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

class Bone:
    pass

class Attacks:
    pass
class Heart:
    def __init__(self, position_x, position_y, change_x, change_y):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

        self.texture1 = arcade.load_texture("images/heart.png")
        self.scale = 0.025

    def draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.position_x, self.position_y, self.scale * self.texture1.width,
                                      self.scale * self.texture1.height, self.texture1, 0)
        arcade.finish_render()

    def update(self):
        # Move the heart
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the heart hit the edge of the screen. If so, change direction
        if self.position_x < 40:
            self.position_x = 40

        if self.position_x > SCREEN_WIDTH - 40:
            self.position_x = SCREEN_WIDTH - 40

        if self.position_y < 40:
            self.position_y = 40

        if self.position_y > SCREEN_HEIGHT - 40:
            self.position_y = SCREEN_HEIGHT - 40


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

        self.heart_x = 250
        self.heart_y = 250

        # Create Menu Screen
        self.menu = Menu()

        # Create Instructions Screen
        self.instuctions = Instructions()

        # Create heart
        self.heart = Heart(self.heart_x, self.heart_y, 0, 0)

    def on_draw(self):
        arcade.start_render()
        if PAGE == 1:
            self.menu.draw()
        elif PAGE == 2:
            self.instuctions.draw()
        elif PAGE == 3:
            self.heart.draw()

    def update(self, delta_time):
        self.heart.update()

        # Check if the heart is supposed to move
        if LEFT_PRESSED is True:
            self.heart.change_x = -MOVEMENT_SPEED
        elif RIGHT_PRESSED is True:
            self.heart.change_x = MOVEMENT_SPEED
        else:
            self.heart.change_x = 0
        if UP_PRESSED is True:
            self.heart.change_y = MOVEMENT_SPEED
        elif DOWN_PRESSED is True:
            self.heart.change_y = -MOVEMENT_SPEED
        else:
            self.heart.change_y = 0

    def on_key_press(self, key, modifiers):
        """ Called whenever a user presses a key """
        global LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED, DOWN_PRESSED, PAGE
        if key == arcade.key.SPACE:
            PAGE = 3
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
    arcade.run()


main()
