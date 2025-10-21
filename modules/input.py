import speech_recognition as sr


def take_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Optional duration
        print("Listening...")

        # Adjust pause and energy thresholds
        recognizer.pause_threshold = 1.5  # or experiment with 2.0 to 2.5
        recognizer.energy_threshold = 400  # Set this based on testing in your environment

        try:
            audio = recognizer.listen(source, timeout=2)  # 5 seconds of silence will stop listening
        except sr.WaitTimeoutError:
            print("Listening timed out, please try again.")
            return "None"

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Say that again please...")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"

