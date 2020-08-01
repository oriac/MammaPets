from django.db import models


# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Client(Person):
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address


class Pet(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MammaPet(Person):
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.phone


class Contract(models.Model):
    start_date = models.DateTimeField('date started')
    end_date = models.DateTimeField('date started')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    mamma_pet = models.ForeignKey(MammaPet, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    # TODO: CHANGE TO ENUM
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status
