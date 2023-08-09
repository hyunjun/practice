import os


from PyPDF2 import PdfReader
#import fitz


PDF_DIR = 'pdfs'


def get_pdffilenames(dirname=PDF_DIR):
    filenames = []
    try:
        filenames = os.listdir(dirname)
    except FileNotFoundError as e:
        os.mkdir(dirname)
        filenames = os.listdir(dirname)
    return [f'{dirname}/{filename}' for filename in filenames]


if __name__ == '__main__':
    filenames = get_pdffilenames()

    for filename in filenames:

        reader = PdfReader(filename)

        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            print(text)

        '''
        doc = fitz.open('example.pdf')
        text = []
        for page in doc:
            text.append(page.get_text())
        print('\n'.join(text))
        '''
