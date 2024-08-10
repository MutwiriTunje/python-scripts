from spire.doc import *
from spire.doc.common import *

# Create a Document object
document = Document()
# Load a Word DOCX file
document.LoadFromFile("incoming.docx")
# Or load a Word DOC file
#document.LoadFromFile("Sample.doc")

# Convert the document to a list of image streams
image_streams = document.SaveImageToStreams(ImageType.Bitmap)

# Incremental counter
i = 1

# Save each image stream to a PNG file
for image in image_streams:
    image_name = str(i) + ".png"
    with open(image_name,'wb') as image_file:
        image_file.write(image.ToArray())
    i += 1

# Close the document
document.Close()