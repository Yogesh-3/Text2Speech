import pyttsx3     #converts txt to speech
import PyPDF2      #for reading pdf 
x = open('GIVE PDF NAME HERE', 'rb')
pdfReader = PyPDF2.PdfFileReader(x)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
