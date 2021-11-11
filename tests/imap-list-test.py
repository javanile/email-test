
import imaplib, ssl, os, unittest

imap_host = os.environ.get('IMAP_HOST')
imap_port = os.environ.get('IMAP_PORT')
imap_username = os.environ.get('IMAP_USERNAME')
imap_password = os.environ.get('IMAP_PASSWORD')

class ImapListTest(unittest.TestCase):
    def runTest(self):
        imap = imaplib.IMAP4(imap_host, imap_port)
        imap.login(imap_username, imap_password)
        expected = ('OK', [
           b'(\\HasNoChildren \\Drafts) "." Drafts',
           b'(\\HasNoChildren \\Sent) "." Sent',
           b'(\\HasNoChildren \\Junk) "." Junk',
           b'(\\HasNoChildren \\Trash) "." Trash',
           b'(\\HasNoChildren) "." INBOX'
        ])
        self.assertEqual(expected, imap.list())

unittest.TextTestRunner().run(ImapListTest())
