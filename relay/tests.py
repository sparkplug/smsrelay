"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from rapidsms.models import Contact, Connection, Backend
from rapidsms.messages.incoming import IncomingMessage
from rapidsms_httprouter.models import Message
from rapidsms_httprouter.router import get_router


class TestParsing(TestCase):
    def setup(self):
        self.backend=Backend.objects.create(name="gateway")
        self.connection=Connection.objects.create(identity="11235",backend=self.backend)

    def fakeIncoming(self, message, connection):
        self.router.handle_incoming(connection.backend.name, connection.identity, message)
    def test_parsing(self):
        self.fakeIncoming('You Have Received UGX1000,000 from 0777801652. Reason:-. Your balance is UGX102,000.',self.connection)

