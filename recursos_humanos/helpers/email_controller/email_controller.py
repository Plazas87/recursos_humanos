import ezgmail


class EmailController:

    INBOX_SEARCH = 'label:inbox '

    def __init__(self):
        ezgmail.init()

    def send_email(self, recipients, subject='Test subject', body='Probando'):
        for recipient in recipients:
            ezgmail.send(recipient=recipient, subject=subject, body=body)

    def _search_emails(self, subject):
        search_query = self.INBOX_SEARCH + subject
        res_threat = ezgmail.search(search_query)
        # print(ezgmail.summary(res_threat, printInfo=False))
        return res_threat

    def download_all_attachments_by_subject(self, subject):
        emails = self._search_emails(subject)
        for email_index, email_threat in enumerate(emails):
            for reply_index, email_message in enumerate(email_threat.messages):
                print(f'Threat: {email_index} - reply: {reply_index}')
                print(f'   Adjuntos: {email_message.attachments}')
                email_message.downloadAllAttachments(downloadFolder=f'cv/{subject}_selection_process')

    def download_all_attachments_by_subject_and_format(self, subject, file_format='.pdf'):
        emails = self._search_emails(subject)
        for email_index, email_threat in enumerate(emails):
            for reply_index, email_message in enumerate(email_threat.messages):
                print(f'Threat: {email_index} - reply: {reply_index}')
                print(f'   Adjuntos: {email_message.attachments}')

                attachments = email_message.attachments
                directory_name = file_format.replace('.', '')
                for attachment in self.filter_by_extension(files=attachments, extension=file_format):
                    email_message.downloadAttachment(filename=attachment,
                                                     downloadFolder=f'cv/{subject}_selection_process_{directory_name}')

    def filter_by_extension(self, files, extension):
        tmp_file_list = [file for file in files if extension in file]
        return tmp_file_list

    # TODO: Hacer que el parámetro subject sea una lista de strings


if __name__ == '__main__':
    reader = EmailController()
    int()