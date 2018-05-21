from django.core.management.base import BaseCommand, CommandError
from checker.cron import update_filedata
from checker.models import FileData

class Command(BaseCommand):
    """ Update filedata in db """
    help = 'Update'

    def handle(self, *args, **options):
            try:
                import pdb; pdb.set_trace()
                update = update_filedata()
            except FileData.DoesNotExist:
                raise CommandError('An error occured with {}'.format(update))

            for lists in update:
                if lists:
                    self.stdout.write(self.style.SUCCESS('Successfully updated filedata "%s"' % update))
            else:
                self.stdout.write(self.style.SUCCESS('Command successfully launched but no files were updated'))