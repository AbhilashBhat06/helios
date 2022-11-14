from django.db import models

# Create your models here.
class buildings(models.Model):
    LOCATION_CHOICES = (
        ("Electronic City", "Electronic City"),
        ("Whitefield", "Whitefield"),
        ("Jayanagar", "Jayanagar"),
        ("Marathalli", "Marathalli"),
    )
    DATES_CHOICES = (
        ("12-11-22", "12-11-22"),
        ("13-11-22", "13-11-22"),
        ("14-11-22", "14-11-22"),
    )

    SUBJECT_CHOICES = (
        ("Government", "Government"),
        ("Corporate", "Corporate"),
        ("Hobbyist", "Hobbyist"),
        ("Student", "Student"),
    )

    location = models.CharField(
        max_length=50, default="Electronic City", choices=LOCATION_CHOICES
    )
    date = models.DateTimeField(default="14-11-22", choices=DATES_CHOICES)
    subject = models.CharField(
        max_length=25, default="Government", choices=SUBJECT_CHOICES
    )
    # image = models.ImageField(
    # upload_to=None, height_field=100, width_field=100, max_length=100
    # )
