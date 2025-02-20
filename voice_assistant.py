import speech_recognition as sr
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize the chatbot
chatbot = ChatBot('VoiceBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)  # Speed of speech

def listen():
    """ Listen to audio from the microphone and convert it to text. """
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "I didn't understand that."
        except sr.RequestError:
            return "Sorry, I am having trouble understanding right now."

def speak(text):
    """ Convert text to speech. """
    tts_engine.say(text)
    tts_engine.runAndWait()

def chat():
    """ Main function to handle the chatbot conversation. """
    print("Start talking with the bot (say 'quit' to stop)!")
    while True:
        try:
            # Listen for user input
            user_input = listen()
            print("You: " + user_input)

            # Check if the user wants to quit
            if user_input.lower() == 'quit':
                print("Chatbot: Goodbye!")
                break

            # Get the chatbot response
            response = chatbot.get_response(user_input)
            print("Chatbot:", response)
            
            # Speak out the chatbot response
            speak(response)
        except KeyboardInterrupt:
            print("\nChatbot: Goodbye!")
            break

# Start the chat
chat()
