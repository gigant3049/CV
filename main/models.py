from django.db import models


class AboutMe(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
    birthday = models.DateField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    complete_projects = models.CharField(max_length=50)
    cvv = models.FileField(upload_to='media/')

    class Meta:
        verbose_name_plural = 'About Me'


class Partners(models.Model):
    image = models.ImageField(upload_to='media/')

    class Meta:
        verbose_name_plural = 'Partners'


class Education(models.Model):
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Education'


class Experience(models.Model):
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    description = models.TextField()


class Awards(models.Model):
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Awards'


class Skills(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    current = models.CharField(max_length=100)
    last_week = models.CharField(max_length=100)
    last_month = models.CharField(max_length=100)
    is_top_3 = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Skills'


# class Categories(models.Model):
#     education = models.ForeignKey(Education, on_delete=models.CASCADE)
#     experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
#     awards = models.ForeignKey(Awards, on_delete=models.CASCADE)
#     skills = models.ForeignKey(Skills, on_delete=models.CASCADE)

class Services(models.Model):
    icon = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Services'


class Projects(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Projects'


class Achievements(models.Model):
    title = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Achievements'


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
