import pathlib


def create_not_existing_directory(
        directory: str
):
    """Create not existing directory. If directory exists, do nothing.
    Parameters
    ----------
    directory : directory to create

    """
    p = pathlib.Path(directory)
    if not p.is_dir():
        print(f'Creating directory: {directory} as it does not exist')
        p.mkdir(parents=True, exist_ok=True)
