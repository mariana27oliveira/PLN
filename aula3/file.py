import re

#apagar new pages

file = open ('dicionario_medico.txt', encoding='utf8')
text = file.read()
#text = re.sub(r'\f', '', text) -- anterior, não apanhava as descrições que estavam na outra página
text = re.sub(r'\f', '\n', text)
text = re.sub(r'(\n\n.+)\n\n', 'r\1', text)



#print (re.sub(r'\n\f', '', text))

entries = re.findall(r'\n\n(.+)((?:\n.+)+)', text)

print(entries)

#print(entries)

#remover o \n
new_entries = [(designation, description.strip()) for designation, description in entries]



'''
new_entries = []
for designation, description in entries:
    description = description.strip()
    new_entries.append((designation, description))

print(new_entries [10])

'''


file.close()

html = open('dicionario_medico.html', 'w', encoding = 'utf8')

header = '''<html>
<head>
<meta charset = 'utf-8' />
'<h1 style="font-size:60px; font-family: Arial, sans-serif;color: green;text-align: center">Dicionário Médico</h1>'
</head>
<body>

''' 
body = '<table style="border-collapse: collapse; border: 1px solid gray; margin: auto; width: 80%">'


# Cabeçalho da tabela
body += '<tr>'
body += '<th style="border: 1px solid gray; font-size: 20px; color: green; font-family: Arial, sans-serif; text-align: center;background-color: lightgray; padding-top: 5px; padding-bottom: 5px; padding-left: 5px;padding-right: 5px;">Designação</th>'
body += '<th style="border: 1px solid gray; font-size: 20px; color: green; font-family: Arial, sans-serif; text-align: center;background-color: lightgray; padding-top: 5px; padding-bottom: 5px; padding-left: 5px;padding-right: 5px;">Descrição</th>' 
body += '</tr>'

# Linhas da tabela
for designation, description in new_entries:
    body += '<tr>'
    body += '<td style="border: 1px solid gray; font-size: 14px; font-family: Arial, sans-serif; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px;padding-right: 5px;"><b>' + designation + '</b></td>'
    body += '<td style="border: 1px solid gray; font-size: 14px; font-family: Arial, sans-serif; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px;padding-right: 5px;">' + description + '</td>'
    body += '</tr>'



body += '</table>'


"""
body = ''
for designation, description in new_entries:
    body += '<b>' + designation + '</b>'
    body += '<p>' + description + '</p>' + '<hr>'

#hr cria uma linha de espaço

"""

footer = '''</body>
</html>'''

html.write(header + body + footer)



html.close()



