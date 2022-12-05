import aspose.words as aw

# Load DOC
doc = aw.Document("calibre.docx")

# Create save options and set image compression
saveOptions = aw.saving.PdfSaveOptions()
saveOptions.image_compression = aw.saving.PdfImageCompression.JPEG
saveOptions.jpeg_quality = 50 # Sets JPEG compression at % quality. Lower percentages reduce file size

# Save as PDF
doc.save("PDF.pdf", saveOptions)