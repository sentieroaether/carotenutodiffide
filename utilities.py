import os
from pathlib import Path
import datetime


def find_executable_by_partial_path(start_directory, partial_path):
    """
    Recursively search for an executable in a given directory using pathlib
    by matching a partial path.

    Parameters:
    - start_directory: Directory to start the search from.
    - partial_path: Partial path to match the executable.

    Returns:
    - The path to the executable if found, otherwise None.
    """
    start_path = Path(start_directory)
    for path in start_path.rglob('*'):
        print(path)
        if partial_path in str(path) and path.is_file() and os.access(path, os.X_OK):
            print(f"Executable matching '{partial_path}' found at: {path}")
            return str(path)
    print(f"No executable matching '{partial_path}' found in {start_directory}.")
    return None


# Example usage
#search_directory = "C:\\"  # Root directory (use with caution)
#partial_path = "soffice.exe"
#find_executable_by_partial_path(search_directory, partial_path)


def get_data():
    # Mappatura per i giorni della settimana e i mesi in italiano
    giorni_settimana = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
    mesi_anno = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre',
                 'Ottobre', 'Novembre', 'Dicembre']

    # Genera la data attuale
    current_date = datetime.datetime.now()

    # Estrai i componenti della data
    giorno_settimana = giorni_settimana[current_date.weekday()]
    giorno = current_date.day
    mese = mesi_anno[current_date.month - 1]
    anno = current_date.year

    # Formatta la data manualmente
    # formatted_date_full = f'{giorno_settimana}, {giorno} {mese} {anno}'
    # formatted_date_short = f'{giorno:02d}/{current_date.month:02d}/{anno}'

    formatted_date_full = f'{giorno} {mese} {anno}'
    formatted_date_short = f'{giorno:02d}/{current_date.month:02d}/{anno}'

    return {"alfanumerico": formatted_date_full, "numerico": formatted_date_short}


