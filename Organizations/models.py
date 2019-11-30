from datetime import date
from django.db import models
from improved_user.model_mixins import AbstractUser


class User(AbstractUser):
    """
    A custom user model based on package `django-improved-user`.
    See https://django-improved-user.readthedocs.io/ for details.
    """
    def __str__(self):
        return self.full_name


class Ability(models.Model):
    """
    The licenses, ratings, certificates and abilities that a user may have.
    """
    KIND_OF_ABILITY_CHOICES = [
        (
            "Pilot Licenses",
            (
                ("SPL", "Sailplane License"),
                ("PPL(A)", "Private Pilot License (A)"),
                ("CPL(A)", "Commercial Pilot License (A)"),
                ("ATPL", "Air Transport Pilot License"),
                ("LAPL", "Light Airplain Pilot License"),
                ("US-PPL", "United States PPL"),
                ("UL", "Ultralight License"),
            )
        ),
        (
            "Ratings",
            (
                ("SEP (land)", "CR SEP (land)"),
                ("SEP (sea)", "CR SEP (sea)"),
                ("TMG", "CR TMG"),
                ("NVFR", "Night VFR"),
                ("FI SPL", "Flight Instructor (SPL)"),
                ("FI TMG/SEP", "Flight Instructor (SE, SP)"),
                ("winch", "Winch"),
                ("tow", "Aerotow"),
            )
        ),
        (
            "Radio",
            (
                ("BZF1", "BZF I"),
                ("BZF2", "BZF II"),
                ("AZF", "AZF"),
                ("L4", "Language Proficiency L4"),
                ("L5", "Language Proficiency L5"),
                ("L6", "Language Proficiency L6"),
            )
        ),
        ("MED1", "Medical Class 1"),
        ("MED2", "Medical Class 2"),
        ("ZÜP", "ZÜP"),
        (
            "Documents",
            (
                ("ID", "ID card"),
                ("passport", "Passport"),
            )
        ),
        ("reminder", "Reminder"),
        ("other", "other"),
    ]

    user    = models.ForeignKey(User, models.CASCADE)
    kind    = models.CharField(max_length=20, choices=KIND_OF_ABILITY_CHOICES)
    number  = models.CharField(max_length=40, blank=True)
    expires = models.DateField(null=True, blank=True)
    remark  = models.CharField(max_length=80, blank=True)

    class Meta:
        get_latest_by = "expires"
        verbose_name_plural = "abilities"


class Organization(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Member(models.Model):
    """
    Each member refers to exactly one User and to exactly one Organization.
    As such, the Member model acts as an intermediate table:
      - A user can be a member of several organizations.
      - An organization can, as members, have several users.
    """
    user = models.ForeignKey(User, models.PROTECT)
    orga = models.ForeignKey(Organization, models.PROTECT, verbose_name="organization")


class Status(models.Model):
    """
    The membership status that a member can have.
    """
    FAR_FUTURE = date(2999, 12, 31)
    KIND_OF_STATUS_CHOICES = [
        ("a", "aktiv"),
        ("p", "passiv (fördernd)"),
        ("e", "Ehrenmitglied"),
        ("o", "other"),
        ("x", "ausgeschieden"),
    ]

    member = models.ForeignKey(Member, models.CASCADE)
    status = models.CharField(max_length=20, choices=KIND_OF_STATUS_CHOICES)
    begin  = models.DateField()
    end    = models.DateField(editable=False, default=FAR_FUTURE)   # The day before the *next* status or `FAR_FUTURE`.
    remark = models.CharField(max_length=120, blank=True)

    class Meta:
        get_latest_by = "begin"
        verbose_name_plural = "statuses"
