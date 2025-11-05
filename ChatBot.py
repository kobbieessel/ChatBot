import ollama
import speech_recognition as sr
import pyttsx3

def setup():
    Client = ollama.Client()
    recognizer = sr.Recognizer()
    tSpeech = pyttsx3.init()
    return (Client, recognizer, tSpeech)

def chat_bot():
    model = "llama2"
    Client, recognizer, tSpeech = setup()

    while True:
        with sr.Microphone() as source:
            print('Say something (or say "exit" to quit): ')
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.pause_threshold = 1

            try:
                audio = recognizer.listen(source, timeout=5)
                prompt = recognizer.recognize_google(audio, language='en-US')
                if "exit" in prompt.lower():
                    tSpeech.say("Goodbye!")
                    tSpeech.runAndWait()
                    break

            except sr.WaitTimeoutError:
                print("Listening timed out. Please try again.")
                continue

            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                continue

        block = ["fool","crazy","idiot",'stupid'] 

        if any(word in prompt.lower() for word in block):
            tSpeech.say("Please respect yourself. Inappropriate words are not allowed.")
            tSpeech.runAndWait()
            continue

        try:
            response = Client.generate(model=model, prompt=prompt)
            
        except Exception as e:
            print(f"Error generating response: {e}")
            tSpeech.say("Sorry, I ran into an issue.")
            tSpeech.runAndWait()
            continue
   
        voices = tSpeech.getProperty('voices')
        tSpeech.setProperty('voice', voices[1].id)
        tSpeech.setProperty('rate', 180)

        tSpeech.say(response.response)
        print(f"You said: {prompt}\n")
        print(f"Bot:\n{response.response}")
        tSpeech.runAndWait()

if __name__ == "__main__":
    chat_bot()