from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

command = "whoami"
shell = "cmd.exe"

def start_shell (shell):
	keyboard.press(Key.cmd_l)
	keyboard.press('r')
	keyboard.release(Key.cmd_l)
	keyboard.release('r')
	time.sleep(0.5)
	for c in shell:
		keyboard.press(c)
		time.sleep(0.1)
		keyboard.release(c)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(0.5)
	

def run_command (command):
	for c in command:
		keyboard.press(c)
		time.sleep(0.1)
		keyboard.release(c)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

def main():
    start_shell(shell)
    run_command(command)

if __name__ == "__main__":
    main()