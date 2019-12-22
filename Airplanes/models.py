from django.db import models
from Organizations.models import Organization, User


class Airfield(models.Model):
    name = models.CharField(max_length=80)
    icao = models.CharField(max_length=4)

    def __str__(self):
        if self.icao:
            return f"{self.name} ({self.icao})"
        return self.name


class Airplane(models.Model):
    callsign = models.CharField(max_length=20)
    mf_type  = models.CharField(max_length=40, blank=True, verbose_name="type")
    owner    = models.ForeignKey(Organization, models.CASCADE)
    # Lärmschutz

    def __str__(self):
        # if self.mf_type:
        #     return f"{self.callsign} ({self.mf_type})"
        return self.callsign


class Flight(models.Model):
    """
    The model that is representing a flight is the most difficult datastructure
    that we have, as flight records widely vary in their purpose and nature.

    The free-style `text_input` field is needed in order to implement our
        "Saving always succeeds!"
    guarantee. We still need the model/database fields (especially foreign
    keys) to run database queries over them.

    All ForeignKey fields can be left empty/null in order to make it possible
    to give values that are not in the related table. Such values can instead
    be given in our `text_input` field, where our interpreter makes them look
    like native values. Note that this is a very flexible and powerful feature:
    It lets us deal with airplanes that are not in `Airplanes` (e.g. a one-time
    chartered airplane for your personal flight log) or pilots that are not in
    `Users` (e.g. for airfield logbooks).
    """
    ROLE_CHOICES = [
        ("PIC", "Pilot"),
        ("CO", "Copilot"),
        ("Gast", "Gast"),
        ("FI", "Fluglehrer"),
        ("FE", "Flugprüfer"),
        ("OTH", "other"),
    ]

    airplane   = models.ForeignKey(Airplane, models.PROTECT, null=True, blank=True)
    pic        = models.ForeignKey(User, models.PROTECT, null=True, blank=True, verbose_name="pilot", related_name="pilots")
    pic_role   = models.CharField(max_length=4, choices=ROLE_CHOICES, blank=True, verbose_name="pilot's role")
    co         = models.ForeignKey(User, models.PROTECT, null=True, blank=True, verbose_name="copilot", related_name="copilots")
    co_role    = models.CharField(max_length=4, choices=ROLE_CHOICES, blank=True, verbose_name="copilot's role")
    attendants = models.SmallIntegerField(null=True, blank=True)

    dt_offbl   = models.DateTimeField(null=True, blank=True, verbose_name="off-block time")
    dt_takeoff = models.DateTimeField(null=True, blank=True, verbose_name="take-off time")
    dt_landing = models.DateTimeField(null=True, blank=True, verbose_name="landing time")
    dt_onbl    = models.DateTimeField(null=True, blank=True, verbose_name="on-block time")
    pause      = models.SmallIntegerField(null=True, blank=True, help_text="Time in minutes that is subtracted from the total flight time. Used when several flights are summarized in a single record.")

    from_af    = models.ForeignKey(Airfield, models.PROTECT, null=True, blank=True, verbose_name="from", related_name="from_airfields")
    to_af      = models.ForeignKey(Airfield, models.PROTECT, null=True, blank=True, verbose_name="to", related_name="to_airfields")
    landings   = models.SmallIntegerField(null=True, blank=True, verbose_name="number of landings")
    op_time    = models.IntegerField(null=True, blank=True, help_text="The airplane's operation time, used for computing flight fees. E.g. flight time in minutes, hobbs meter, tach meter, etc.")
    remark     = models.CharField(max_length= 120, blank=True)
    text_input = models.CharField(max_length=1000, blank=True)  # This field is needed to implement our "Saving always succeeds!" guarantee.

    def __str__(self):
        s = ""

        if self.dt_offbl:
            s += str(self.dt_offbl.date())
        elif self.dt_takeoff:
            s += str(self.dt_takeoff.date())
        elif self.dt_landing:
            s += str(self.dt_landing.date())
        elif self.dt_onbl:
            s += str(self.dt_onbl.date())

        s += f", {self.airplane}, {self.pic} ({self.pic_role}), {self.co} ({self.co_role}), "

        if self.from_af:
            s += f"from {self.from_af} "
        if self.to_af:
            s += f"to {self.to_af} "

        s += f", „{self.remark}“"

        s = s.replace("()", "")
        s = s.replace(" ,", ",")
        s = s.replace(",,", ",")
        s = s.replace("  ", " ")

        return s.strip(", \t\n")


class Reservation(models.Model):
    """
    The implementation must make sure that a user can only reserve airplanes
    of organizations whose member he is.
    """
    user     = models.ForeignKey(User, models.PROTECT)
    airplane = models.ForeignKey(Airplane, models.PROTECT)
    begin    = models.DateTimeField()
    end      = models.DateTimeField()
    remark   = models.CharField(max_length=120, blank=True)

    def __str__(self):
        s = f"Reservation of {self.airplane} by {self.user} from {self.begin} to {self.end}"
        if self.remark:
            s += ", " + self.remark
        return s
