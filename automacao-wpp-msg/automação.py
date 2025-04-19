import pyautogui as pa
import pyperclip
import time
import csv

# Pergunta qual mensagem o usuário deseja enviar
mensagem_base = input("Digite a mensagem (use {nome} para personalizar): ")

# Lê os dados dos clientes
clientes = []
with open('clientes.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nome = linha['nome'].strip()
        numero = linha['numero'].strip()
        clientes.append({'nome': nome, 'numero': numero})

# Abre o navegador só uma vez
pa.press('win')
time.sleep(0.5)
pa.write('chrome') //coloque o navegador de preferência OBS: é necessário baixar o whatsapp em seu pc
time.sleep(0.5)
pa.press('enter')
time.sleep(3)

for cliente in clientes:
    nome = cliente['nome']
    numero = cliente['numero']

    # Gera o link e copia pro clipboard
    link = f'https://wa.me/{numero}'
    pyperclip.copy(link)

    # Vai para o link do número na mesma aba
    pa.hotkey('ctrl', 'l')  # Seleciona a barra de endereços
    time.sleep(0.3)
    pa.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pa.press('enter')
    time.sleep(8)

    # Clica na caixa de mensagem (ajuste x e y conforme seu monitor)
    pa.click(x=600, y=700)
    time.sleep(1)

    # Agora sim, copia a MENSAGEM personalizada
    mensagem = mensagem_base.replace('{nome}', nome)
    pyperclip.copy(mensagem)

    # Cola e envia a mensagem
    pa.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pa.press('enter')
    time.sleep(2)

    # Troca de janela (se necessário)
    pa.hotkey('alt', 'tab')
    time.sleep(1)
