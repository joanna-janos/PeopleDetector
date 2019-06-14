import glob
import typing
from os.path import normpath, basename


def get_filenames(
        path_to_data
) -> typing.List[str]:
    """Get filenames
    Parameters
    ----------
    path_to_data : directory with data

    Returns
    -------
    List[str]
            Filenames
    """
    paths_to_data = []
    for extension in ["png", "jpg"]:
        paths_to_data += [basename(normpath(f)) for f in glob.glob(path_to_data + "*." + extension)]

    return paths_to_data
