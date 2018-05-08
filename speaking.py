import sys
import pyttsx

voiceEngine = pyttsx.init()
voiceEngine.setProperty('rate', 150)
voiceEngine.setProperty('voice', 25)

def speak(str):
	if len(sys.argv) > 1:
		str = sys.argv[1]
	voiceEngine.say(str)
	voiceEngine.runAndWait()

def main():

	rate = voiceEngine.getProperty('rate')
	volume = voiceEngine.getProperty('volume')
	voice = voiceEngine.getProperty('voice')
	voice = voiceEngine.getProperty('voices')

	print rate
	print volume
	print voice
	
	
	speak("Type something to say!")
	while True:
		input = raw_input("Enter something to say or type EXIT to exit.\n")
		if input == "EXIT" or input == "exit" or input == "Exit":
			break
		else:
			speak(input)

if __name__ == '__main__':
	main()
