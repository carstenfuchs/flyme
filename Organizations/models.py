from datetime import date
from django.db import models
from django.utils import timezone
from Accounts.models import User


class Organization(models.Model):
    name    = models.CharField(max_length=80)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    """
    A membership expresses how a user relates to an organization:
      - a user can be a member in several organizations
      - an organization can have several members
    """
    FAR_FUTURE = date(2999, 12, 31)

    STATUS_ACTIVE = "a"         # active, full, ordinary, regular (aktiv)
    STATUS_SUPPORTING = "s"     # passive, supporting, sponsoring, sustaining, promoting (passiv, fördernd)
    STATUS_HONORARY = "h"
    STATUS_OTHER = "o"
    STATUS_FORMER = "x"         # former, past (ehemalig)

    STATUS_CHOICES = [
        (STATUS_ACTIVE,     "active"),
        (STATUS_SUPPORTING, "supporting"),
        (STATUS_HONORARY,   "honorary"),
        (STATUS_OTHER,      "other"),
        (STATUS_FORMER,     "former"),
    ]

    user   = models.ForeignKey(User, models.PROTECT)
    orga   = models.ForeignKey(Organization, models.PROTECT, verbose_name="organization")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    begin  = models.DateField()
    end    = models.DateField(editable=False, default=FAR_FUTURE)   # The day before the *next* status or `FAR_FUTURE`.
    is_mgr = models.BooleanField(default=False, help_text="Is the member given management access to the organization?")
    remark = models.CharField(max_length=120, blank=True)

    def __str__(self):
        rem = f" ({self.remark})" if self.remark else ""
        return f"{self.user} is \"{self.get_status_display()}\" member in {self.orga} since {self.begin}{rem}"

    class Meta:
        get_latest_by = "begin"


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

    def days_valid(self):
        if self.expires is None:
            return 999999
        return (self.expires - timezone.localdate()).days

    def __str__(self):
        num = f" ({self.number})" if self.number else ""
        exp = f" until {self.expires}" if self.expires else ""
        rem = f" ({self.remark})" if self.remark else ""
        return f"{self.kind}{num}{exp} of {self.user}{rem}"

    class Meta:
        get_latest_by = "expires"
        verbose_name_plural = "abilities"
