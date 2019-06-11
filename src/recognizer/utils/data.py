import glob
from os.path import normpath, basename


def get_data_filenames(path_to_data):
    """Get filenames of default dataset.
    Parameters
    ----------
    directory : directory with data

    Returns
    -------
    List[str]
            Filenames
    """
    return [basename(normpath(f)) for f in glob.glob(path_to_data + "*.png")]
