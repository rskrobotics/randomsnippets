from dispatcher import Dispatcher
from pynput import keyboard
qwerty = ('q', 'w', 'e', 'r', 't', 'y')
asdfg = ('a', 's', 'd', 'f', 'g')
import time

def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
        if key.char in qwerty:
            print(f"we got a match! {key.char}")
        elif key.char == 'z':
            dispatcher.dink()
        elif key.char == 'j':
            print('Should Trigger')
            dispatcher.enable_next_cycle()
            time.sleep(1)

    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

def on_release(key):
    # print('Key released: {0}'.format(
    #     key))

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released



if __name__ == '__main__':
    dispatcher = Dispatcher(trigger_register='R9',
                            enable_next_register='R10')
    dispatcher.go_to_numeric_registers()
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()