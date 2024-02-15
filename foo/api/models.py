from django.db import models

import uuid
import json


# Create your models here.
class DocumentGroup(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.TextField()
    end_active_date = models.DateTimeField()

class Examiner(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.TextField()
    active = models.BooleanField(default=True)
    docgrp = models.ManyToManyField(DocumentGroup)          #creates join table
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
'''
# Many-to-Many (Join table)
class UserDocGroup(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(Examiner.uuid)
    docgrp = models.ForeignKey(DocumentGroup.uuid)    
'''
# One-to-One
class Note(models.Model):
    uuid = models.UUIDField()
    user_docgrp = models.OneToOneField(to=Examiner.docgrp, on_delete=models.CASCADE)        #join table: api_examiner_docgrp
    note = models.TextField()

class Document(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.TextField()
    docgrp = models.ForeignKey(to=DocumentGroup, on_delete=models.CASCADE)
    metadata = models.TextField()
    uintarray = models.TextField()

    def set_metadata(self, data):
        self.metadata = json.dumps(data)

    def get_metadata(self):
        return json.loads(self.metadata)

    def set_array(self, arr):
        self.uintarray = json.dumps(arr)

    def get_array(self):
        return json.loads(self.uintarray)
