"""This is the main module"""
from pynput import keyboard
from board import Board

BOARD = Board()

def main():
    """
    This is the main function.
    """
    BOARD.shuffle()
    BOARD.refresh()
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def on_press(key):
    """
    It handled what happens when a key is pressed.
    :param key: package installed value.
    """
    BOARD.refresh()

def on_release(key):
    """
    It is responsible for What happens when a key is pressed.
    :param key: Listener parameter
    :return: Boolean
    """
    #TODO:: need to add actual behaviour.
    if key == keyboard.Key.up:
        BOARD.board, BOARD.empty_location = BOARD.move_up(BOARD.board, BOARD.empty_location)
    elif key == keyboard.Key.down:
        BOARD.board, BOARD.empty_location = BOARD.move_down(BOARD.board, BOARD.empty_location)
    elif key == keyboard.Key.left:
        BOARD.board, BOARD.empty_location = BOARD.move_left(BOARD.board, BOARD.empty_location)
    elif key == keyboard.Key.right:
        BOARD.board, BOARD.empty_location = BOARD.move_right(BOARD.board, BOARD.empty_location)
    elif key == keyboard.Key.shift:
        BOARD.solve()
    elif key == keyboard.Key.esc:
        # Stop listener
        return False
    BOARD.refresh()

if __name__ == '__main__':
    main()
