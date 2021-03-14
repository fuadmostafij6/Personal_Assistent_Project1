import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as dt
import wikipedia
import pyjokes
import cv2
import googletrans
import requests


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
translator = googletrans.Translator()

IBM_USERNAME = 'Fuad Mostafij'
IBM_PASSWORD = 'fuad58585'


def talk(text):
    engine.say(text)
    engine.runAndWait()


def NewsFromBBC():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "360e7029a4494556a2b0f57fc10863c6"
    }
    main_url = "https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    article = open_bbc_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

    talk(results)


def take_command():
    with sr.Microphone() as source:
        print('listening...')
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'assist' in command:
            command = command.replace('assist', '')
            print(command)
    try:
        print("IBM Speech to Text thinks you said " + listener.recognize_ibm(command, username=IBM_USERNAME, password=IBM_PASSWORD))


    except:
        pass
    return command


def start():
    hour = int(dt.datetime.now().hour)

    if hour >= 0 and hour <= 12:

        print('Good Morning')
        talk('Good Morning')
    elif hour>12 and hour<18:
        talk('Good Afternoon')
        print('Good Afternoon')
    else: talk('Good evening')

    print('I am psycho, Can i help you?')
    talk('I am psycho, Can i help you?')


if __name__ == '__main__':
    start()

    while True:

        command = take_command()
        print(command)
        if 'can you play any song for me' in command:
            talk('Yes I can')
            talk('which song are you want for play')
            song = take_command()
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:

            t = dt.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + t)
            print(t)
        elif 'tell me about' in command:
            person = command.replace('tell me about', ' ')
            talk('wait I will telling you')
            info = wikipedia.summary(person, 5)
            print(info)
            talk(info)
        elif 'search' in command:
            talk('searching')
            site = command.replace('search', ' ')
            pywhatkit.search(site)
            talk(site)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            print(joke)
        elif 'translate' in command:
            talk('translating')
            trans = command.replace('translate', ' ')
            translated = translator.translate(trans, dest='bn')
            print(translated.text)
            talk(translated.text)
        elif 'news' in command:
            talk('here your news. I am reading now')
            NewsFromBBC()
        elif 'thank you' in command:
            talk('you are welcome')
        elif 'i love you' in command:
            talk('i love you too so much')
        elif 'camera' in command:
            talk('opening')
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    talk('closing')
                    break

            # After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()
        elif 'no thanks' in command:
            talk('ok Take care sir')
            break

        elif 'bongobondhu' in command:
            talk('Mujib was born in Tungipara, a village in Gopalganj District in the province of Bengal in British India, to Sheikh Lutfur Rahman, a serestadar (court clerk) of Gopalganj civil court, and his wife Sheikh Sayera Khatun. He was born into a Bengali Muslim family as the third child in a family of four daughters and two sons. His parents used to adoringly call him "Khoka".In 1929, Mujib entered into class three at Gopalganj Public School, and two years later, class four at Madaripur Islamia High School.[5] From very early age Mujib showed a potential of leadership. His parents noted in an interview that at a young age, he organized a student protest in his school for the removal of an inept principal.[citation needed] Mujib withdrew from school in 1934 to undergo eye surgery, and returned to school only after four years, owing to the severity of the surgery and slow recovery.')
        else:
            talk('Please say the command again.')

        talk('Have you any job for me')


