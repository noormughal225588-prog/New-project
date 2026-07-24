import os
import time

def speak(text):
    print(f"Jarvis: {text}")
    os.system(f"termux-tts-speak '{text}'")

def main():
    speak("Hello Sir, I am your assistant. How can I help you today?")
    
    while True:
        command = input("Aap kya kehna chahte hain? (exit likhein band karne ke liye): ")
        
        if 'exit' in command.lower():
            speak("Goodbye Sir!")
            break
        elif 'time' in command.lower():
            current_time = time.strftime("%H:%M:%S")
            speak(f"Current time is {current_time}")
        elif 'naam kya hai' in command.lower() or 'who are you' in command.lower():
            speak("Mera naam Jarvis hai, aur main aapka personal assistant hoon.")
        else:
            speak("Maine yeh command abhi seekhi nahi hai.")

if __name__ == "__main__":
    main()

