from botcity.document_processing import *
import pathlib

def lerPDF(arquivo):
    reader = PDFReader()
    parser = reader.read_file(r'./docs/Contoso_INVOICE_Fabrikam_UK.pdf')

    _date = parser.get_first_entry("Date:")
    value = parser.read(_date, 1.4, -1.25, 3.15, 2.416667)
    print('Date:' + value)

    _bill_to = parser.get_first_entry("Bill to:")
    value = parser.read(_bill_to, 1.240741, -1.416667, 3.555556, 2.833333)
    print('Bill to:' + value)

    _contact = parser.get_first_entry("Contact:")
    value = parser.read(_contact, 1.065789, -1.333333, 4, 3.166667)
    print('Contact:' + value)

    _balance_due = parser.get_first_entry("Balance due:")
    value = parser.read(_balance_due, 1.14, -1.071429, 1.266667, 2.214286)
    print('Balance Due:' + value)
   

arquivos = pathlib.Path(r"C:\Users\dessa\projetos\botcity-teste\lerPDF\docs").glob("*.pdf")

lerPDF()


