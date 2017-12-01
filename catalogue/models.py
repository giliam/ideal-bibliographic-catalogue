from django.db import models


class Function(models.Model):
    """
        Job
    """

    name = models.CharField(max_length=150, blank=False)

    comments = models.TextField(blank=True, default="")

    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"Function {0}".format(self.name)



class Person(models.Model):
    """
        Actor
    """
    firstname = models.CharField(max_length=150, default="", blank=True)
    lastname = models.CharField(max_length=150, blank=False)

    comments = models.TextField(blank=True, default="")

    function = models.ManyToManyField(Function)

    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['lastname', 'firstname']

    def __str__(self):
        return u"{0} {1}".format(self.firstname, self.lastname.upper())

