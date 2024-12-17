import subprocess
import os

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
        subprocess.run(command, check=True)
        print(f"Conversione completata: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Errore nella conversione: {e}")
        raise