import subprocess
import os
from utilities import find_executable_by_partial_path


libreoffice_path = "libreoffice"


def convert_docx_to_pdf(input_path, output_path):
    """
    Converte un file DOCX in PDF utilizzando LibreOffice.
    """
    # Percorso esplicito di LibreOffice
    libreoffice_path = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    
    # Comando per la conversione
    command = [
        libreoffice_path,
        "--headless",  # Esegue senza GUI
        "--convert-to", "pdf",
        "--outdir", os.path.dirname(output_path),  # Directory di output
        input_path
    ]
    
    # Esegui il comando
    try:
        # Run the command
        subprocess.run(command, check=True)
        print(f"Conversion successful: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during conversion: {e}")