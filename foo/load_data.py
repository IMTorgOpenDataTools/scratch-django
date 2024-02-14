"""
Load test data into the database
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foo.settings")
django.setup()

from api.models import Examiner


def run():
    for idx in range(1, 3):
        e = Examiner(name=f'User-{idx}')
        e.save()


if __name__ == '__main__': 
    run()