# pyrefly: ignore [missing-import]
from pypdf import PdfWriter

# List out the PDFs you want to merge in order
pdf_files = ["File1.pdf", "File2.pdf"]

# Initialise the writer
merger = PdfWriter()

# Loop through and append each PDF
for pdf in pdf_files:
    merger.append(pdf)

# Save the combined file
merger.write("merged_file.pdf")
merger.close()

print("PDFs merged successfully")
