import speech_recognition as sr
import webbrowser

# Function to listen for the command
def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"Command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand command")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

# Main loop
while True:
    command = listen_for_command()
    if command is not None and "whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        print("WhatsApp Web opened!")
