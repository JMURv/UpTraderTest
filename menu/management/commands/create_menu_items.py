from django.core.management.base import BaseCommand
from menu.models import Menu


class Command(BaseCommand):
    help = 'Creates multiple menu items'

    def handle(self, *args, **options):
        catalog = Menu.objects.create(name="catalog")

        pc_components = Menu.objects.create(name="pc_components", parent=catalog)
        smartphones = Menu.objects.create(name="smartphones", parent=catalog)
        cameras = Menu.objects.create(name="cameras", parent=catalog)

        graphic_cards = Menu.objects.create(name="graphic_cards", parent=pc_components)
        mother_boards = Menu.objects.create(name="mother_boards", parent=pc_components)

        samsung = Menu.objects.create(name="samsung", parent=smartphones)
        apple = Menu.objects.create(name="apple", parent=smartphones)

        canon = Menu.objects.create(name="canon", parent=cameras)
        nikon = Menu.objects.create(name="nikon", parent=cameras)

        self.stdout.write(self.style.SUCCESS('Successfully created menu items'))
