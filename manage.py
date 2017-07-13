#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("appByDoc.settings")#"DJANGO_SETTINGS_MODULE",原来在括号里的环境变量
                                        #作用是终端中输入命令是不用再输入python+manage.py ...
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
