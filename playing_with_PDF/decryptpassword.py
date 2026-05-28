import os
from PyPDF2 import PdfReader, PdfWriter

def remove_pdf_password(input_pdf_path, password, output_pdf_path):

    if not os.path.isfile(input_pdf_path):
        raise FileNotFoundError(f"File not found: {input_pdf_path}")

    if not input_pdf_path.lower().endswith(".pdf"):
        raise ValueError("Input file must be a PDF file.")

    try:
        reader = PdfReader(input_pdf_path)

        if reader.is_encrypted:
            result = reader.decrypt(password)

            if result == 0:
                raise ValueError("Incorrect password or empty password not allowed")

            print("✅ PDF decrypted successfully")

        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_pdf_path, "wb") as f:
            writer.write(f)

        print(f"✅ Password removed successfully: {output_pdf_path}")

    except Exception as e:
        print(f"❌ Error processing PDF: {e}")


if __name__ == "__main__":

    input_pdf = "path\input.pdf"
    pdf_password = ""     # keep empty if PDF opens without asking password
    output_pdf = "path\unlocked_output.pdf"

    remove_pdf_password(input_pdf, pdf_password, output_pdf)