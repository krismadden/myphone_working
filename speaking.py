#from espeak import espeak

#espeak.set_voice("en")

#espeak.synth("hello")


import sys
import pyttsx

def speak(str speakThis):
	engine = pyttsx.init()
	str = "how are you doing? c'est une belle maison."
	if len(sys.argv) > 1:
		str = sys.argv[1]
	engine.say(str)
	engine.runAndWait()

def main():
# 	print 'running speaking.py'
# 	engine = pyttsx.init()
# 	str = "how are you doing? c'est une belle maison."
# 	if len(sys.argv) > 1:
# 		str = sys.argv[1]
# 	engine.say(str)
# 	engine.runAndWait()
	speak("how are you doing?")
	while True:
		input = raw_input("Enter Something to Say or type EXIT to exit.\n")
		if input == "EXIT" or input == "exit" or input == "Exit":
			break
		else:
			str = input
			if  len(sys.argv) > 1:
				str = sys.argv[1]
			engine.say(str)
			engine.runAndWait()

if __name__ == '__main__':
	main()
