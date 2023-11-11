
import supervisor
import time
import board
import touchio

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

name_is_main = __name__ == '__main__'

while name_is_main:
    print('Running code.py')
    print('TOUCH1 for spacebar')
    print('TOUCH2 for midi')
    time.sleep(5)
    if touch1.value or touch2.value:
        supervisor.set_next_code_file('spacebar.py' if touch1.value else 'midi.py')
        supervisor.reload()
