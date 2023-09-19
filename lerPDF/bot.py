from botcity.document_processing import *
import pathlib
import pandas as pd

def lerPDF(arquivo):
    reader = PDFReader()
    parser = reader.read_file(arquivo)
    page_data = {}

    _date = parser.get_first_entry("Date:")
    page_data["date"] = parser.read(_date, 1.4, -1.25, 3.15, 2.416667)

    _bill_to = parser.get_first_entry("Bill to:")
    page_data["bill_to"] = parser.read(_bill_to, 1.240741, -1.416667, 3.555556, 2.833333)

    _contact = parser.get_first_entry("Contact:")
    page_data["contact"] = parser.read(_contact, 1.065789, -1.333333, 4, 3.166667)

    _balance_due = parser.get_first_entry("Balance due:")
    page_data["balance_due"] = parser.read(_balance_due, 1.14, -1.071429, 1.266667, 2.214286)

    return page_data


arquivos = pathlib.Path(r"C:\Users\andre\PycharmProjects\botcity-testes\lerPDF\docs").glob("*.pdf")

pdf_data = []
for arquivo in arquivos:
    pdf_data.append(lerPDF(arquivo))


print(pdf_data)

df = pd.DataFrame(pdf_data)
df.to_excel(r"dados.xlsx", index=False)
