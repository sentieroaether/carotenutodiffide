import os
import subprocess

from utilities import find_executable_by_partial_path


#search_directory = "C:\\"  # Root directory (use with caution)
#partial_path = "soffice.exe"
#libreoffice_path = find_executable_by_partial_path(search_directory, partial_path)
libreoffice_path = "/opt/homebrew/bin/soffice"


def convert_docx_to_pdf(input_path, output_path):
    """
    Convert a DOCX file to PDF using LibreOffice.

    Parameters:
    - input_path: Path to the input DOCX file.
    - output_path: Path to the output PDF file.
    """
    # Define the command to run LibreOffice in headless mode for conversion
    command = [
        libreoffice_path, #"C:\\Program Files\\LibreOffice\\program\\soffice.exe",  # LibreOffice executable
        "--headless",  # Run without GUI
        "--convert-to", "pdf",  # Conversion format
        "--outdir", os.path.dirname(output_path),  # Output directory
        input_path  # Input file
    ]

    try:
        # Run the command
        subprocess.run(command, check=True)
        print(f"Conversion successful: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during conversion: {e}")

# Example usage:
#convert_docx_to_pdf("C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\angelo_guarracino_projects\\UseCase1\\input_data\\TemplateLetteraDiffida.docx", "C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\angelo_guarracino_projects\\UseCase1\\output_data\\output.pdf")

