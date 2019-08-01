from django.core.management.base import BaseCommand, CommandError
from invitation.views import update_publications_auto

class Command(BaseCommand):
    help = 'Update instagram publications'

    def handle(self, *args, **options):
        update_publications_auto()
        self.stdout.write(self.style.SUCCESS('Successfully updated"%s"'))
