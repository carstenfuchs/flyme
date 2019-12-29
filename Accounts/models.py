from improved_user.model_mixins import AbstractUser


class User(AbstractUser):
    """
    A custom user model based on package `django-improved-user`.
    See https://django-improved-user.readthedocs.io/ for details.
    """
    def __str__(self):
        return self.full_name
