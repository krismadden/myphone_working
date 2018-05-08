#from espeak import espeak

#espeak.set_voice("en")

#espeak.synth("hello")


import sys
import pyttsx

voiceEngine = pyttsx.init()
voiceEngine.setProperty('rate', 125)

def speak(str):
	if len(sys.argv) > 1:
		str = sys.argv[1]
	voiceEngine.say(str + "       ")
	voiceEngine.runAndWait()

def main():

	rate = voiceEngine.getProperty('rate')
	volume = voiceEngine.getProperty('volume')
	voice = voiceEngine.getProperty('voice')

	print rate
	print volume
	print voice
	
	
	speak("Type something to say or type EXIT to exit.")
	while True:
		input = raw_input("Type something to say or type EXIT to exit.\n")
		if input == "EXIT" or input == "exit" or input == "Exit":
			break
		else:
			speak(input)

if __name__ == '__main__':
	main()
