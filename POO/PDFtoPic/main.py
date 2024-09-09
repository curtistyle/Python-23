
popper_path = r"D:\popper\poppler-24.07.0\Library\bin"
pdf_path = r"D:\Progarmacion\Python-23\POO\PDFtoPic\Eric_Matthes_Python_Crash_Course_A_Hands.pdf"

from pdf2image import convert_from_path
page = convert_from_path(pdf_path=pdf_path, poppler_path=popper_path, first_page=1, last_page=1,use_cropbox=True, dpi=100)[0]

print(page)

saving_folder = r"D:\Progarmacion\Python-23\POO\PDFtoPic"

import os
c=1
img_name = f"img-{c}.jpeg"
page.save(os.path.join(saving_folder, img_name), "JPEG")

    
