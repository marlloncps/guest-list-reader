import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

caminho_arquivo = 'lista.xlsx'
pdf_name = 'convidados.pdf'

df = pd.read_excel(caminho_arquivo)

nomes = df['Nomes'].tolist()
nomes.sort()

c = canvas.Canvas(pdf_name, pagesize=letter)

style = getSampleStyleSheet()["Title"]
style.fontName = "Helvetica-Bold"
style.fontSize = 18

y = 750  # Posição inicial para escrever
indice = 1

c.setFont(style.fontName, style.fontSize)
c.drawString(100, y, 'Lista de convidados para a festa:')
y -= 40

for nome in nomes:
    c.setFont("Helvetica", 12)
    c.drawString(100, y, f'{indice}. {nome}')
    indice += 1
    y -= 20  # Deslocamento para a próxima linha

# Salva e fecha o arquivo PDF
c.save()

print(f'Nomes salvos em {pdf_name}')
