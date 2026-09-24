import pyttsx3
import PyPDF2

book = open('book.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(book)

total_pages = len(pdf_reader.pages)
print(f"Playing audiobook... Total pages: {total_pages}")

speaker = pyttsx3.init()

for num in range(0, total_pages):
    page = pdf_reader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

book.close()
