from .email_controller import EmailController


if __name__ == '__main__':
    email_controller = EmailController()
    # email_controller.send_email(recipients=['pedromtz93@gmail.com'])
    email_controller.download_all_attachments_by_subject_and_format('cv', '.docx')
    email_controller.download_all_attachments_by_subject_and_format('cv', '.pdf')
    # email_controller.download_all_attachments_by_subject('cv')
    # email_controller.send_email()
