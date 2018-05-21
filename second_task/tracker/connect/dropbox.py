import dropbox

from decouple import config


def make_connection():
    """ Create a connection to dropbox API """
    return dropbox.Dropbox(config('DROPBOX_TOKEN'))