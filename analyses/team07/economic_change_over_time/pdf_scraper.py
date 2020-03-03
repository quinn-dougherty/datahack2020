from PyPDF2 import PdfFileReader

path_to_pdf = r"C:\Users\tbnnu\projects\datahack2020\analyses\team07\economic_change_over_time\Philly-Neighborhood-Rankings_7_31_19.pdf"
text_file = r"C:\Users\tbnnu\projects\datahack2020\analyses\team07\economic_change_over_time\Philly-Neighborhood-Rankings_7_31_19.txt"

with open(path_to_pdf, 'rb') as f:
    reader = PdfFileReader(f)
    for i in range(9,12):
        text = reader.getPage(i).extractText()

        try:
            txt = open(text_file, 'a+')
            txt.write(text)
            txt.close()
        except Exception as e:
            pass