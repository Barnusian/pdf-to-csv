
import pdfplumber
import csv

def pdf_into_csv(pdf_file, csv_file):
    with pdfplumber.open(pdf_file) as pdf:
        page = pdf.pages[0]
        tables = page.extract_tables()

        all_rows = []
        for table in tables:
            all_rows.extend(table)

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(all_rows)

# Example usage
pdf_file = 'path/to/your/pdf_file.pdf'
csv_file = 'path/to/your/output.csv'
pdf_into_csv(pdf_file, csv_file)
