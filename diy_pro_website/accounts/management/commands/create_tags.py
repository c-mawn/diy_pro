from django.core.management.base import BaseCommand
from accounts.models import Tag


class Command(BaseCommand):
    help = "Create default tech repair tags"

    def handle(self, *args, **kwargs):
        tags = [
            "Smartphone Repair",
            "Laptop Repair",
            "PC Repair",
            "Tablet Repair",
            "Console Repair",
            "Camera Repair",
            "Small Electronics",
            "Battery Replacement",
            "Screen Replacement",
            "Electrical",
            "Fast Repair Tools",
            "Precision Tools",
            "iPhone Repair",
            "Screwdriver Tools",
            "Replacement Parts",
            "Ratcheting Tools",
            "Flat Head Screwdriver",
            "Phillips Head Screwdriver",
            "Single Tip Screwdriver",
            "Replaceable Tip Screwdriver",
        ]
        created_count = 0
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"{created_count} repair tags created successfully!")
        )
