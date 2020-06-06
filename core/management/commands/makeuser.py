from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(phone_number="63588213").exists():
            User.objects.create_superuser(
                phone_number="63588213",
                first_name="Tobi",
                last_name="DEGNON",
                email="tobidegnon@protonmail.com",
                password="**blumen**"
            )
            self.stdout.write(self.style.SUCCESS('Admin user has created'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists'))
