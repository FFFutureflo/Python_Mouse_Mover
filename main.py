import getopt
import pyautogui 
import sys
import time

class MouseMover:

    next_step_down_right = True
    x_offset = 100
    y_offset = 100
    sleep_timer = 1

    def switch_offset(self):
        self.x_offset = -1 * self.x_offset
        self.y_offset = -1 * self.y_offset

    def main(self, argv):
        
        try:
            opts, args = getopt.getopt(argv,"t:", ["sleeptimer="])
        except getopt.GetoptError:
            print('main.py -t <time_in_seconds>')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-t", "--sleeptimer"):
                self.sleep_timer = float(arg)
        while True:
            # Check for moving the mouse back to the original position
            if not self.next_step_down_right:
                self.switch_offset()
            pyautogui.move(self.x_offset,self.y_offset)
            time.sleep(self.sleep_timer)
            self.next_step_down_right = not self.next_step_down_right
            
if __name__ == "__main__":
    mouse_mover = MouseMover()
    mouse_mover.main(sys.argv[1:])
   