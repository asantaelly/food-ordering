"""
    Command for testing
"""

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Showing the welcome home from commandline!'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Welcome to the boring site'))