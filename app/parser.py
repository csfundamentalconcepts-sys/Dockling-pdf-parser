from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.pipeline_options import RapidOcrOptions
import pikepdf
import tempfile
import re
import json
import os

pipeline_options = PdfPipelineOptions()
pipeline_options.ocr_options = RapidOcrOptions()
pipeline_options.images_scale = 2.0

converter = DocumentConverter(
    format_options={
        "pdf": PdfFormatOption(pipeline_options=pipeline_options)
    }
)

def unlock_pdf(pdf_path: str, password: str):
    """
    Unlocks a password-protected PDF and returns path of unlocked PDF.
    """
    with pikepdf.open(pdf_path, password=password) as pdf:
        pdf.save("unlocked.pdf")
    print("PDF unlocked and saved in the /app directory")

def parse_page_using_docling(pdf_path : str) :
   
    result = converter.convert(pdf_path)
    with open('conversion_results1.txt', 'w', encoding='utf-8') as f:
        f.write("\n\nMarkdown Conversion:\n")
        f.write(result.document.export_to_markdown())
        

    
def formatter(vulnerability : list) :
    data = {}

    with open("conversion_results1.txt", "r", encoding="utf-8") as f:
        text = f.read()

    for line in text.splitlines():
        match = re.match(r"\|\s*(.*?)\s*\|\s*(.*?)\s*\|", line)
        if match:
            key, value = match.groups()

            # skip separator rows (-----)
            if set(key.strip()) == {"-"}:
                continue

            # handle duplicate keys
            if key in data:
                if isinstance(data[key], list):
                    data[key].append(value)
                else:
                    data[key] = [data[key], value]
            else:
                data[key] = value

    print(len(data))
    
    if(len(data) == 13 or len(data) == 14) :
        vulnerability.append(data)

# parse_page_using_docling()


def parse_document(pdf_path : str, password : str) -> list:
    vulnerabilities = []
    unlocked_pdf_path_name = "unlocked.pdf"
    unlock_pdf(pdf_path=pdf_path, password=password)
    total_pages = 0
    with pikepdf.open(unlocked_pdf_path_name) as pdf:
        total_pages = len(pdf.pages)
        print(f"Total pages: {total_pages}")
    
    for page_num in range(0, total_pages):

        with pikepdf.open(unlocked_pdf_path_name) as pdf1:
            single_page_pdf = pikepdf.Pdf.new()
            single_page_pdf.pages.append(pdf1.pages[page_num])

            temp_path = f"temp_page_{page_num + 1}.pdf"
            single_page_pdf.save(temp_path)

        print(f"Processing page num {page_num + 1}....")
        parse_page_using_docling(temp_path)
        formatter(vulnerability=vulnerabilities)
        
        single_page_pdf.close()
        os.remove(temp_path)

    
    
    print(vulnerabilities)
    return vulnerabilities

# parse_document("VAPT1.pdf", "Bpcl#111225")
    


