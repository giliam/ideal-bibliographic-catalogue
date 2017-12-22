from django.db import models


class Theme(models.Model):
    """
        Topic of interest
    """

    name = models.CharField(max_length=150, blank=False)

    comments = models.TextField(blank=True, default="")

    parent_theme = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE,
        related_name="children_themes",
        blank=True
    )
    level = models.PositiveIntegerField(blank=False)

    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"Theme {0}".format(self.name)


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
        Actor in the bibliographic research
    """
    firstname = models.CharField(max_length=150, default="", blank=True)
    lastname = models.CharField(max_length=150, blank=False)

    comments = models.TextField(blank=True, default="")

    functions = models.ManyToManyField(Function)
    themes = models.ManyToManyField(Theme)

    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['lastname', 'firstname']

    def __str__(self):
        return u"{0} {1}".format(self.firstname, self.lastname.upper())


class TypeRessource(models.Model):
    """
        Topic of interest
    """

    name = models.CharField(max_length=150, blank=False)

    comments = models.TextField(blank=True, default="")

    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"Type of ressource {0}".format(self.name)


class Ressource(models.Model):
    """
        Ressource
    """
    name = models.CharField(max_length=150, blank=False)
    link_url = models.CharField(max_length=300, blank=True)

    comments = models.TextField(blank=True, default="")

    themes = models.ManyToManyField(Theme)
    type_ressource = models.ForeignKey(TypeRessource)

    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"Ressource {0}".format(self.name)
