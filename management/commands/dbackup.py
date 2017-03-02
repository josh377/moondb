import os
import time
import shutil
from django.conf import settings
from django.core.management.base import (BaseCommand, CommandError)

DATABASE_NAME = 'db.sqlite3' #eg: 'db.sqlite3'


class Command(BaseCommand):
    help = ('Command to deploy and backup the latest database.')

    def add_arguments(self, parser):
        parser.add_argument(
            '-b', '--backup', action='store_true',
            help='Just backup command confirmation.'
        )

    def success_info(self, info):
        return self.stdout.write(self.style.SUCCESS(info))

    def error_info(self, info):
        return self.stdout.write(self.style.ERROR(info))

    def handle(self, *args, **options):
        backup = options['backup']

        if backup == False:
            return self.print_help()

        if os.path.isfile(DATABASE_NAME):
            # backup the latest database, eg to: `db.2017-02-29.sqlite3`
            backup_database = 'db.%s.sqlite3' % time.strftime('%Y-%m-%d')
            shutil.copyfile(DATABASE_NAME, backup_database)
            self.success_info("[+] Backup the database `%s` to %s" % (DATABASE_NAME, backup_database))