from django.core.management.base import BaseCommand
from book import settings
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for user in settings.ADMINS:
                username = user.replace(' ', '')
                email = user[1]
                password = settings.DOCKER_ADMIN_PASSWORD
                print('Creating account for %s (%s)' % (username, email))
                admin = User.objects.create_superuser(email=email,
                                                      username=username,
                                                      password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
