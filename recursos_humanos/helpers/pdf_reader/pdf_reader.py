from PyPDF2 import PdfFileReader
from pdfminer.high_level import extract_text


class PDFReader:
    def __init__(self, file_name='', pdf_path='./cv/text_selection_process_pdf/'):
        self._file_name = file_name
        self._pdf_path = pdf_path
        self.pdf_controller = ''

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if isinstance(value, str):
            self._file_name = value

    @property
    def pdf_path(self):
        return self._pdf_path

    @pdf_path.setter
    def pdf_path(self, value):
        if isinstance(value, str):
            self._pdf_path = value

    def extract_information(self):
        full_path = self.pdf_path + self.file_name
        with open(full_path, 'rb') as f:
            self.pdf_controller = PdfFileReader(f)
            information = self.pdf_controller.getDocumentInfo()
            number_of_pages = self.pdf_controller.getNumPages()

            txt = f"""
            Information about {full_path}: 
    
            Author: {information.author}
            Creator: {information.creator}
            Producer: {information.producer}
            Subject: {information.subject}
            Title: {information.title}
            Number of pages: {number_of_pages}
            """

        print(txt)
        return information

    def extract_text(self):
        full_path = self.pdf_path + self.file_name
        text = extract_text(full_path)
        with open('./cv/pdf_to_text.txt', 'w') as file:
            file.write(text)

        print(repr(text))
        print(text)
        print(type(text))


if __name__ == '__main__':
    pdf_reader = PDFReader('CV Juan Carlos Aguirre 2020 ingles.pdf')
    pdf_reader.extract_information()
    pdf_reader.extract_text()
