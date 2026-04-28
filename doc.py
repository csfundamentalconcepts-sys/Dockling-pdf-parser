# from docling.document_converter import DocumentConverter, PdfFormatOption
# from docling.datamodel.pipeline_options import PdfPipelineOptions
# from docling.datamodel.pipeline_options import RapidOcrOptions



# import pikepdf

# with pikepdf.open("VAPT1.pdf", password="Bpcl#111225") as pdf:
#     pdf.save("unlocked.pdf")
# source = "page_14.pdf"

# pipeline_options = PdfPipelineOptions()
# # pipeline_options.do_ocr = True
# pipeline_options.ocr_options = RapidOcrOptions()
# pipeline_options.images_scale = 2.0

# converter = DocumentConverter(
#     format_options={
#         "pdf": PdfFormatOption(pipeline_options=pipeline_options)
#     }
# )

# result = converter.convert(source)

# with open('conversion_results1.txt', 'w', encoding='utf-8') as f:
#     f.write("\n\nMarkdown Conversion:\n")
#     f.write(result.document.export_to_markdown())

