from Aviation.ifi import parse
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Analyzes the informal input for a flight and outputs the resulting data."

    def add_arguments(self, parser):
        parser.add_argument(
            "ifi",
            help="The informal flight input that is to be analyzed."
        )

    def handle(self, *args, **options):
        ifi = options["ifi"]
        self.stdout.write(self.style.HTTP_NOT_MODIFIED(ifi))
        out = str(parse(None, ifi))
        self.stdout.write(out)
