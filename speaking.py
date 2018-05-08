#from espeak import espeak

#espeak.set_voice("en")

#espeak.synth("hello")


import sys
import pyttsx

voiceEngine = pyttsx.init()

def speak(str):
	if len(sys.argv) > 1:
		str = sys.argv[1]
	voiceEngine.say(str)
	voiceEngine.runAndWait()

def main():

	rate = voiceEngine.getProperty('rate')
	volume = voiceEngine.getProperty('volume')
	voice = voiceEngine.getProperty('voice')

	print rate
	print volume
	print voice
	
	
	speak("how are you doing?")
	while True:
		input = raw_input("Enter Something to Say or type EXIT to exit.\n")
		if input == "EXIT" or input == "exit" or input == "Exit":
			break
		else:
			speak(input)

if __name__ == '__main__':
	main()
