import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import webbrowser

# Text to Speech
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Voice Input
def take_command():
    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")

            listener.adjust_for_ambient_noise(source, duration=1)

            audio = listener.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            command = listener.recognize_google(audio)
            command = command.lower()

            print("You Said:", command)

            return command

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""

    except sr.RequestError:
        print("No internet connection.")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""

# Main Assistant
def run_assistant():

    speak("Hello, I am your Voice Assistant")

    while True:

        command = take_command()

        if not command:
            continue

        # Time
        if "time" in command:

            current_time = datetime.datetime.now().strftime("%I:%M %p")

            speak(f"Current time is {current_time}")

        # Date
        elif "date" in command:

            today = datetime.datetime.now().strftime("%d %B %Y")

            speak(f"Today's date is {today}")

        # Search Person
        elif "who is" in command:

            person = command.replace("who is", "").strip()

            speak(f"Searching information about {person}")

            webbrowser.open(
                f"https://www.google.com/search?q={person}"
            )

        # Open Google
        elif "open google" in command:

            speak("Opening Google")

            webbrowser.open("https://www.google.com")

        # Open YouTube
        elif "open youtube" in command:

            speak("Opening YouTube")

            webbrowser.open("https://www.youtube.com")

        # Play Song
        elif "play" in command:

            song = command.replace("play", "").strip()

            speak(f"Playing {song}")

            pywhatkit.playonyt(song)

        # Exit
        elif "stop" in command or "exit" in command:

            speak("Goodbye. Have a nice day.")

            break

        else:

            speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    run_assistant()