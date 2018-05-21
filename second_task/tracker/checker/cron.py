from .models import FileData
from connect.dropbox import make_connection


# NB It would be a better option to use a scheduled celery task.
def update_filedata():
    """ Retrieve data from dropbox root folder

    Query the database and check if the entry exists.
    Update the last modification date and occurence.
    If the entry does not exist, create a new one.

    Returns:
        list -- return a list of updated files
    """
    query_filedata = FileData.objects.all().values_list('file_id', flat=True)
    dbx = make_connection()

    updated_file = []
    for file in dbx.files_list_folder('').entries:

        if file.id in query_filedata:
            # Update the date field and the occurence
            entry = FileData.objects.get(file_id=file.id)
            entry.modification_date = file.client_modified
            entry.occurence += 1
            entry.save()
            updated_file.append(entry)

        else:
            # Create an entry within the database
            new_entry = FileData.objects.create(
                            file_id=file.id,
                            name=file.name,
                            date=file.client_modified,
                        )

        return update_file