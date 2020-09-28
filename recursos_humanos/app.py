import ezgmail


class EmailReader:

    def start_app(self):
        self.read()

    def read(self):
        ezgmail.init()
        for index, x in enumerate(ezgmail.unread()):
            var = index
            print(var)
            x.messages[0].downloadAllAttachments(downloadFolder='cv')

    def read_by_subject(self, value):
        # TODO:
        pass

    def read_cv_pdf(self, value, format='pdf'):
        # TODO
        pass

    def read_docx(self, value, format='docx'):
        # TODO
        pass


if __name__ == '__main__':
    reader = EmailReader()
    reader.start_app()
