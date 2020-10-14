from .helpers import EmailController, PDFReader


class RecursosHumanos:

    @staticmethod
    def run():
        email_controller = EmailController()
        # email_controller.send_email(recipients=['pedromtz93@gmail.com'])
        # email_controller.download_all_attachments_by_subject_and_format('cv', '.docx')
        email_controller.download_all_attachments_by_subject_and_format('text', '.pdf')
        pdf_reader = PDFReader('CV Juan Carlos Aguirre 2020 ingles.pdf')
        pdf_reader.extract_information()
        pdf_reader.extract_text()
        # email_controller.download_all_attachments_by_subject('cv')
        # email_controller.send_email()
