from pta.models import Teacher, ParentalUnit, Homework, WishlistItem, \
    Activity, TodoItem, Message

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "clear sample from database"

    def handle(self, *args, **options):
        Teacher.objects.all().delete()
        ParentalUnit.objects.all().delete()
        Homework.objects.all().delete()
        WishlistItem.objects.all().delete()
        Activity.objects.all().delete()
        TodoItem.objects.all().delete()
#        TodoItemAssignedTo.objects.all().delete()
        Message.objects.all().delete()
#        MessageTo.objects.all().delete()

        for u in User.objects.all():
            if not u.is_staff:
                u.delete()

