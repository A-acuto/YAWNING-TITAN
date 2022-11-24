import shutil

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Command for setting up directories necessary for yawning titan operation with front end.

    Usage:
    python manage.py setup
    """

    help = "sets up yawning titan dependencies"

    def handle(self, *args, **kwargs):
        """Method that is fired on execution of the command in the terminal."""
        print("Running setup...")
        from setup import (
            _copy_package_data_notebooks_to_notebooks_dir,
            _create_app_dirs,
        )
        from yawning_titan import DATA_DIR
        from yawning_titan_gui import _YT_GUI_ROOT_DIR

        _create_app_dirs()
        _copy_package_data_notebooks_to_notebooks_dir()
        # Creates the static ui files copy in the data directory
        shutil.copytree(
            (_YT_GUI_ROOT_DIR / "static").as_posix(),
            DATA_DIR.as_posix(),
            dirs_exist_ok=True,
        )
