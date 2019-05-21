import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 4
LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED, DOWN_PRESSED = False, False, False, False


class Heart:
    def __init__(self, position_x, position_y, change_x, change_y):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        # Heart image from UndertaleWiki
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


class MyGame(arcade.Window   ):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

        self.heart_x = 250
        self.heart_y = 250

        # Create heart
        self.heart = Heart(self.heart_x, self.heart_y, 0, 0)

    def on_draw(self):
        arcade.start_render()
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
        global LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED, DOWN_PRESSED
        if key == arcade.key.RIGHT:
            RIGHT_PRESSED = True
        elif key == arcade.key.LEFT:
            LEFT_PRESSED = True
        if key == arcade.key.UP:
            UP_PRESSED = True
        elif key == arcade.key.DOWN:
            DOWN_PRESSED = True

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
