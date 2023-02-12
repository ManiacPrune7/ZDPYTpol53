"""
    Modul niespelniajacy zasady odwrotnej zaleznosci.
    Klasa nie zalezy od abstrakcji!
"""


class Task:
    def process(self) -> None:
        # some processing things...
        email_sender = EmailSender()
        email_sender.send('some nice message')


class EmailSender:
    def send(self, message: str) -> None:
        # send email
        print(f'Sending email with message: {message}')
