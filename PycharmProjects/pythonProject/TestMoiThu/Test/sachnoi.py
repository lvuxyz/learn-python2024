import pyttsx3
from PyPDF2 import PdfReader

sach = open("121.pdf", "rb")
pdfReader = PdfReader(sach)
so_trang = len(pdfReader.pages)
print(so_trang)

bot = pyttsx3.init()
voices = bot.getProperty('voices')
bot.setProperty('voice', voices[0].id)
page_number = 0
page = pdfReader.pages[page_number]
text = page.extract_text()

bot.say(text)
bot.runAndWait()
