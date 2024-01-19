import time, pyperclip
import pyautogui as py

local_img = r'C:\Pasta\Imagens' # Caminho da pasta de imagens (.png) do projeto
nome_certificado = 'CERTIFICADO EMPRESA' # Nome do certificado digital (ou CNPJ) exibido na janela do navegador


def localiza_img(arquivos, tempo_img, confidence= 0.7, grayscale= False):
        espera_img = 0
        if isinstance(arquivos, str):
            arquivos = [arquivos]
        while espera_img <= tempo_img:
            try:
                for arquivo in arquivos:
                    img_localizada = py.locateCenterOnScreen(local_img+ f'\{arquivo}', grayscale= grayscale, confidence= confidence)
                    if img_localizada:
                        return img_localizada
                espera_img +=1
                time.sleep(1)
            except Exception as e:
                print (e)
                pass
        return False

def select_certificado_browser(certificado):
    # Selecionar Certificado Digital
    img_btn_info_cert, select_cert = 0, 0
    while True:
        while True: # Tratativas para o botão 'Informações do Certificado' (Chrome)
            try:
                btn_info_certif = localiza_img('info_cert.png', 1, 0.7, True) #arquivo.png, tempo, confidence, grayscale
                break
            except:
                img_btn_info_cert +=1
                if img_btn_info_cert == 10:
                    btn_info_certif_chrome = False
                    break
                time.sleep(1)
                pass
        if btn_info_certif:
            py.click(btn_info_certif) # Clicar no botão 'Informações do Certificado' 
            
            time.sleep(2)
            py.hotkey('ctrl', 'tab')
            time.sleep(0.2)
            py.press('tab')
            time.sleep(0.2)
            py.press('down', presses=7)
            time.sleep(0.2)
            py.press('tab')
            time.sleep(0.5)
            py.hotkey('ctrl', 'c')
            time.sleep(0.2)
            py.press('tab')

            if certificado and certificado in pyperclip.paste():
                py.press('esc')
                time.sleep(1)
                py.press('enter')
                break
            else:
                py.press('esc')
                time.sleep(1)
                py.press('down')
                
                if select_cert == 30:
                    driver.quit() #Fecha o navegador.
                    print('ERRO GERAL')
                    continue
                
                select_cert +=1
                pass
        else:
            return False



# Executa função para selecionar o certificado digital na páginca navegador
select_certificado_browser(nome_certificado)
