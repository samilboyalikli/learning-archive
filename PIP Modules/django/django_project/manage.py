#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
        # django.core.management modülünden execute_from_command_line fonksiyonunu içe aktarır.
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
            # djangonun içeri aktarılamaması halinde yukarıdaki hata metniyle birlikte bir ImportError fırlatır.

        ) from exc
    execute_from_command_line(sys.argv)
    # Komut satırından alınan argümanları kullanarak yönetim komutlarını çalıştırır.


if __name__ == '__main__':
    main()
