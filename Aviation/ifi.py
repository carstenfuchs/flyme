class Token(object):
    """A token in the input string."""
#    TYPE_UNKNOWN = 1
#    TYPE_MODEL_FIELD = 2
#    TYPE_PREFIX = 3
#    TYPE_COMMENT = 4

    def __init__(self, string):
        super(Token, self).__init__()
        self.string = string
        self.probs = {}
#        self.token_type = TYPE_UNKNOWN
#        self.model_field = None
#        self.value = None       # use  get_value()  instead?


def get_probability_is_time():
    return 0.0, time(0, 0)


def get_probability_is_date():
    return 0.0, date(2020, 1, 1)


class ExplicitPrefix(object):
    def __init__(self, arg):
        super(ExplicitPrefix, self).__init__()
        self.arg = arg


class ModelFieldAirplane(object):
    """Represents the probability that the input string addresses the model field `airplane`."""
    model_field_name = 'airplane'

    def _get_force_prob(force_prefix):
        if not force_prefix:
            return 0.0
        if force_prefix != self.model_field_name:
            raise ValueError(f"Prefix {force_prefix} cannot enforce model field `{self.model_field_name}`")
        return 1.0

    def _set(self, prob, value):
        self.prob = prob
        self.value = value

    def __init__(self, token_string, force_prefix=None):
        force_prob = 0.0
        if force_prefix:
            if force_prefix != self.model_field_name:
                return _set(0.0, None)
            force_prob = 1.0

        if ist in datenbank:
            return _set(force_prob or 1.0, airplane)

        if ist mit eingefügtem "-" in Datenbank:
            return _set(force_prob or 0.9, airplane)

        if len(token_string) > 8:
            return _set(force_prob or 0.0, None)

        if letzte vier Stellen matchen:
            return _set(force_prob or 0.8, airplane)

        # TODO: Falls das vorherige Token ein explizites Prefix war, also "airplane",
        # dann müssen wir hier ebenfalls das `airplane` Objekt zurückgeben, aber nicht mit
        # prob == 0.4, sondern 1.0.
        # D.h. get_probablity() --> __init__(prev_token, this_token) setzt self.prob = 0.x, self.value = y
        if letzte zwei Stellen matchen:
            return _set(0.4, airplane)

        # Kein Treffer in der DB gefunden, aber wegen Prefix "airplane" trotzdem ein Flugzeug?
        return _set(force_prob, token_string)


class ModelFieldPic(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        if ist in datenbank:
            return 1.0, user

        return 0.0, None


class ModelFieldPicRole(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return 0.0, None


class ModelFieldCo(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return 0.0, None


class ModelFieldCoRole(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return 0.0, None


class ModelFieldAttendants(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return 0.0, None


class ModelFieldDtOffblock(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return get_probability_is_time(token_string)


class ModelFieldDtTakeoff(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return get_probability_is_time(token_string)


class ModelFieldDtLanding(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return get_probability_is_time(token_string)


class ModelFieldDtOnblock(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return get_probability_is_time(token_string)


class ModelFieldPause(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        try:
            i = int(token_string)
            if -240 <= i < 0:
                return (0.8, i)
        except ValueError:
            pass
        return 0.0, None


class ModelFieldFromAirfield(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return 0.0, None


class ModelFieldToAirfield(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return 0.0, None


class ModelFieldLandings(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        try:
            i = int(token_string)
            if 1 <= i < 20:
                return (0.8, i)
        except ValueError:
            pass
        return 0.0, None


class ModelFieldOpTime(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        try:
            f = float(token_string.replace(",", ".", 1))
            if 0.0 < f < 100000.0:
                return (0.8, f)
        except ValueError:
            pass
        return 0.0, None


class ModelFieldRemark(object):
    def get_probability(token_string):
        """Returns the probability that the input string addresses this model field."""
        return 0.1, token_string


def parse(user, informal_input):
    tokens = [Token(s) for s in informal_input.replace(",", " ").split()]

    # Resolve explicit assignments to model fields that are given via prefixes,
    # for example "to" and "PIC" in "... PIC Fuchs ... to EDRH ...".
    i = 0
    while i < len(tokens)-1:
        prefix = tokens[i].string.lower()

        if prefix in ("pic", "pilot"):
            tokens[i].probs["__prefix__"] = 1.0
            i += 1
            tokens[i].probs["pic"] = 1.0

        elif prefix in ("co", "copilot"):
            tokens[i].probs["__prefix__"] = 1.0
            i += 1
            tokens[i].probs["co"] = 1.0

        i += 1

    # Assign initial probabilities on the basis of simple rules.
    for t in tokens:
        if t.
        pass


    # Strategie:
    # Ordne jedem Token eine Liste von Wahrscheinlichkeiten zu, z.B. dem Token "EDRT":  80% airplane, 15% from_af, 5% to_af
    # Dann versuche immer mehr Tokens zu 100% aufzulösen, wobei sich der Rest durch Normalisierung immer weiter klärt.



    # Try guesses from data formats
    # content (z.B. d-eien) or format (hh:mm).

    # Need UNPROCESSED (vs. processed but unknown?)
    # Need pool of unassigned model fields that are still "wanted".

    # Need "history": "FI" found -- did we previouly see PIC or CO?   Time found -- did we see other times beforehand?

    # Pilot names can have multiple tokens, e.g. "Carsten Fuchs"

    # Need ambiguitiy: is 1209 == 12:09 or 12.09.2020 or 2020-12-09 or D-1209 ?
    #    ---> Plain numbers can be times, dates or callsigns, even op hours

    # date of flight might be missing -- "today" is the default

    result = {}

    return result
