import os
import subprocess
import shutil

def convert_docx_to_pdf(input_path, output_path):
    """
    Converts a DOCX file to PDF using LibreOffice in headless mode.

    Parameters:
    - input_path: Path to the input DOCX file.
    - output_path: Path to the output PDF file.
    """
    libreoffice_path = shutil.which("libreoffice")
    if not libreoffice_path:
        raise RuntimeError("LibreOffice non trovato. Assicurati che sia installato correttamente.")

    command = [
        libreoffice_path,  # Path to LibreOffice executable
        "--headless",     # Run in headless mode
        "--convert-to", "pdf",  # Convert to PDF
        "--outdir", os.path.dirname(output_path),  # Specify output directory
        input_path  # Input DOCX file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Conversion successful: {output_path}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"An error occurred during PDF conversion: {e}")
