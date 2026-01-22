import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    """
    Merge two PDF files into a single PDF.
    """
    # Validate file existence
    if not os.path.isfile(pdf1_path):
        raise FileNotFoundError(f"File not found: {pdf1_path}")
    if not os.path.isfile(pdf2_path):
        raise FileNotFoundError(f"File not found: {pdf2_path}")

    # Validate file extensions
    if not pdf1_path.lower().endswith(".pdf") or not pdf2_path.lower().endswith(".pdf"):
        raise ValueError("Both input files must be PDF files.")

    merger = PdfMerger()
    try:
        # Append PDFs in order
        merger.append(pdf1_path)
        merger.append(pdf2_path)

        # Write to output file
        merger.write(output_path)
        print(f"✅ PDFs merged successfully into: {output_path}")
    except Exception as e:
        print(f"❌ Error merging PDFs: {e}")
    finally:
        merger.close()

if __name__ == "__main__":
    # Example usage
    pdf1 = "C:\\Users\\atharv\\Downloads\\2. PF Withdrawal Form.pdf"   # Replace with your first PDF path
    pdf2 = "C:\\Users\\atharv\\Downloads\\OpTransactionHistory10-11-2025.pdf-20-43-26.pdf"   # Replace with your second PDF path
    output = "merged.pdf"

    try:
        merge_pdfs(pdf1, pdf2, output)
    except Exception as err:
        print(f"Error: {err}")
