import pytz
from .models import FileData
from connect.dropbox import make_connection


# NB It would be a better option to use a scheduled celery task.
# TODO add a function thats check for files within subfolders...
def update_filedata():
    """ Retrieve data from dropbox root folder

    Query the database and check if the entry exists.
    Update the last modification date and occurence.
    If the entry does not exist, create a new one.

    Returns:
        list -- return a list of updated files
    """

    # we save our filedata objects in a list
    query_file_data = [file for file in FileData.objects.all()]

    # we create a dict with k = file_id and v = modification_date
    data_dict = {}
    for file in query_file_data:
        data_dict[file.file_id] = file.modification_date

    # we create a connection to our dropbox folder
    dbx = make_connection()

    # we set a timezone (we will use it while file.client_modified is naive datetime)
    utc = pytz.timezone('utc')

    # we create a list for our updated file
    updated_file = []

    # we create a list for new file
    created_file = []

    # we loop on our files in the root folder
    for file in dbx.files_list_folder('').entries:

        # If the file exists
        if file.id in data_dict:

            # If the file has not the same modification date
            if file.client_modified.astimezone(utc) != data_dict[file.id]:
                # We update the current file
                entry = FileData.objects.get(file_id=file.id)
                entry.modification_date = file.client_modified
                entry.occurence += 1
                entry.save()
                updated_file.append(entry.name)

        else:
            # Create an entry within the database
            new_entry = FileData.objects.create(
                            file_id=file.id,
                            name=file.name,
                            modification_date=file.client_modified,
                        )
            created_file.append(file.name)

    # we return our list that will be displayed after executing the command
    return updated_file, created_file
