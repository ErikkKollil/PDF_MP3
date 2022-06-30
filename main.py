import pdfplumber
from art import tprint
from gtts import gTTS
from pathlib import Path


# Для проверки на наличие PDF файла
def pdf_to_mp3(path_pdf_file, lan='en'):

    if Path(path_pdf_file).is_file() and Path(path_pdf_file).suffix == '.pdf':
        print(f'[+] Original files:{Path(path_pdf_file).name}', '\n', 'Processing...')

        with pdfplumber.PDF(open(path_pdf_file, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        audio_tack = gTTS(text=text, lang=lan, slow=False)
        file_name = Path(path_pdf_file).stem  # Получим имя файла

        audio_tack.save(f'{file_name}.mp3')
        return f'[+] {file_name}.mp3 saved!'

    else:
        return "File not exists!"


def main():
    tprint('PDF to MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")  # D:/KZ/PyCharmProject/PDF_MP3/test_text.pdf
    language = input("Choose language 'en'/'ru': ")
    print(pdf_to_mp3(path_pdf_file=file_path, lan=language))


if __name__ == '__main__':
    main()
