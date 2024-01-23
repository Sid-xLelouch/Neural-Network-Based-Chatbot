#Function
import datetime
from Speak import Say
import webbrowser as web
#2 Types

#1 - Non Input
#eg. Time , Date , Speedtest

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day) 


def NonInputExecution(query):

    query = str(query)

    if "time" in query:
         Time()

    elif "date" in query:
         Date()

    elif "day" in query:
         Day()    
               
#2 - Input
# eg - Google Search , Wikipedia 
    
def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("","")
        import wikipedia 
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
         query = str(query).replace("google","")
         query = query.replace("search","")
         import pywhatkit
         pywhatkit.search(query)

    elif "youtube" in tag:
         query = str(query).replace("youtube","")
         query = query.replace("search","")
         result= "https://www.youtube.com/results?search_query=" + query
         web.open(result)
         pywhatkit.playonyt(query)
               
    elif "gmail" in tag:
         query = str(query).replace("gmail","")
         query = query.replace("","")
         import pywhatkit
         pywhatkit.search(query)   

           