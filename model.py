import datetime
from enum import Enum

from mongoengine import *

connect('99lb')


class NotificationTarget(Enum):
    TELEGRAM = 'telegram'
    EMAIL = 'email'


class User(Document):
    user_id = StringField(required=True)  # to be used in the configuration
    email = EmailField()  # username at the same time
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    telegram_username = StringField(
        unique=True, required=False, sparse=True, default=None
    )
    telegram_chat_id = LongField(unique=True, required=False, sparse=True, default=None)
    # password fields
    hash = StringField()
    salt = BinaryField()
    rounds = IntField()
    hashed = BinaryField()
    # misc
    notification_targets = ListField()  # values from NotificationTarget enum


class Status(Enum):
    DRAFT = 'draft'
    ACTIVE = 'active'
    ARCHIVED = 'archived'


class ProcessTemplateVersion(EmbeddedDocument):
    version = IntField(required=True)
    version_publication_date = DateTimeField()
    status = EnumField(Status, default=Status.DRAFT)
    template = StringField(required=True)


class ProcessTemplate(Document):
    name = StringField(required=True)
    description = StringField()
    versions = EmbeddedDocumentListField(ProcessTemplateVersion)


class Process(Document):
    start_time = DateTimeField(default=datetime.datetime.utcnow, required=True)
    process_template = ReferenceField(ProcessTemplate, required=True)
    process_content = StringField()
