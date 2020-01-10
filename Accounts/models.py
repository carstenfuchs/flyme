from hashlib import md5
from improved_user.model_mixins import AbstractUser


class User(AbstractUser):
    """
    A custom user model based on package `django-improved-user`.
    See https://django-improved-user.readthedocs.io/ for details.
    """
    def get_gravatar_url(self):
        """Returns the URL of this user's Gravatar image."""
        hash_ = md5(self.email.lower().encode("utf-8")).hexdigest()
        return f"https://www.gravatar.com/avatar/{hash_}"

    def __str__(self):
        return self.full_name
