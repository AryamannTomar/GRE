import os
from fpdf import FPDF
from datetime import datetime
dto=datetime.now()

# dir_name=f'{dto.strftime("%d%h_%a")}_{str(dto)[11:-7].replace(':','')}'
dir_name=f'../../{dto.strftime("%d%h_%a")}'
if os.path.exists(dir_name):
    os.rmdir(dir_name)
os.mkdir(dir_name)

l=[i for i in os.listdir() if i[-4:]=='.txt']

def txts_to_pdf(file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=5.3)
    with open(file, "r") as f:
        text = f.read()
    pdf.multi_cell(0, 3, txt=text)
    out_file=f"{dir_name}/{file[:-4]}.pdf"
    pdf.output(out_file)
    print(f'Created {out_file}')

list(map(txts_to_pdf, l))
dto2 = datetime.now()
dur=dto2-dto

print(f"Took {dur.seconds%60}Sec {dur.microseconds//1000}millisec")