#import pyttsx3
#engine = pyttsx3.init()
#engine.say("I will speak this text")
#engine.runAndWait()

#import pyttsx3

#speaker = pyttsx3.init()
#speaker.save_to_file("This is a test.", 'test.mp3')
#speaker.runAndWait()
#speaker.stop()

import pyttsx3
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.5)
engine.save_to_file('Hello World' , 'test.mp3')
print("klar")
engine.runAndWait()