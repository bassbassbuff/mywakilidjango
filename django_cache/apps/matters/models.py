from django.contrib.auth.models import User
from django.db import models

from apps.client.models import Client



class Matter(models.Model):

    name = models.CharField(null=False, blank=False, max_length=255)
    description = models.CharField(null=False, blank=False, max_length=255)
    # client_id = models.IntegerField()
    created_by = models.ForeignKey(User, related_name='created_matters', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # team = models.ForeignKey(Team, related_name='invoices', on_delete=models.CASCADE)
    client_name = models.CharField(null=False, blank=False, max_length=255, default='testname')
    client_email = models.EmailField(default='a@test.com')
    client_org_number = models.CharField(max_length=255, blank=True, null=True)
    client_address1 = models.CharField(max_length=255, blank=True, null=True)
    client_address2 = models.CharField(max_length=255, blank=True, null=True)
    client_zipcode = models.CharField(max_length=255, blank=True, null=True)
    client_place = models.CharField(max_length=255, blank=True, null=True)
    client_county = models.CharField(max_length=255, blank=True, null=True)
    client_contact_person = models.CharField(max_length=255, blank=True, null=True)
    client_contact_reference = models.CharField(max_length=255, blank=True, null=True)
    client = models.ForeignKey(Client, related_name='matters', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    file = models.FileField(upload_to='uploads/', max_length=100)
    matter = models.ForeignKey(Matter, related_name='files', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name

