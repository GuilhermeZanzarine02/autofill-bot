import PyPDF2 as pdf
import pandas as pd
import re

def read_file():
    # 'rb' significa: r = read, b = binary
    with open(r"Files\testePdf.pdf", "rb") as file:
        content = pdf.PdfReader(file)
        text = ''
        for page in content.pages:
            text += page.extract_text()
        return text

def filter_name():
    # Regex para capturar o nome após "Aluno"
    name = r"Aluno:\s+([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)"

    text = read_file()

    responce = re.search(name, text) 
    
    if responce:
        formated_name = responce.group(1)
        return formated_name

def get_data_fromCSV():
    df_city = pd.read_csv(r"Files\capitais_do_mundo.csv", header=None)
    city = df_city.iloc[1:, 1].reset_index(drop=True).to_list()

    df_email = pd.read_csv(r"Files\random_emails.csv", header=None)
    emails = df_email.iloc[:, 0].to_list()

    return city, emails
