import pyautogui
import os
import time
import speech_recognition as sr
import schedule
import requests

'''
def capture_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ola tudo bem, Sou PX estou aqui para te ajudar, escolha uma das funções")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta o nível de ruído do ambiente
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        return text
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio.")
        return None
    except sr.RequestError:
        print("Não foi possível acessar o serviço de reconhecimento de fala.")
        return None

if __name__ == "__main__":
    while True:
        command = capture_audio()
        if command and "parar" in command.lower():
            print("Assistente encerrado.")
            break
'''

def abrir_valorant():
    def is_valorant_installed_windows():
        valorant_install_dir = "C:\\Riot Games\\VALORANT"
        return os.path.exists(valorant_install_dir)

    if is_valorant_installed_windows():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('valorant', interval=0.25)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        print("Valorant não está instalado no Windows.")

def abrir_Steam():
    def is_steam_installed_windows():
        steam_install_dir = "C:\\Program Files (x86)\\Steam\\steam"
        return os.path.exists(steam_install_dir)

    if is_steam_installed_windows():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('steam', interval=0.25)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        print("Valorant não está instalado no Windows.")

def abrir_Epic():
    def is_epic_installed_windows():
        epic_install_dir = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32" 
        return os.path.exists(epic_install_dir)

    if is_epic_installed_windows():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('epic', interval=0.25)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        print("Valorant não está instalado no Windows.")

def abrir_Lol():
    def is_lol_installed_windows():
        lol_install_dir = "C:\\Riot Games\\League of Legends\\LeagueClient.exe"
        return os.path.exists(lol_install_dir)

    if is_lol_installed_windows():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('League of Legends', interval=0.25)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        print("League of Legends não está instalado no Windows.")

def abrir_Vscode():
    def is_Vscode_installed_windows():
        vscode_install_dir ="C:\\Users\\Imperios\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        return os.path.exists(vscode_install_dir)
    
    if is_Vscode_installed_windows():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('Visual Studio Code', interval=0.25)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        print("Vs Studio Code não está instalado no Windows.")

def abrir_Obsidian():
    def is_obsidian_installed_windows():
        obsidian_install_dir = "C:\\Users\\Imperios\\AppData\\Local\\Obsidian\\Obsidian.exe"
        return os.path.exists(obsidian_install_dir)
    
    if is_obsidian_installed_windows():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('Obsidian', interval=0.25)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        print("Obsidian não está instalado no Windows.")

def abrir_Chrome():
    def is_chrome_installed_windows():
        chrome_install_dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        return os.path.exists(chrome_install_dir)
    
    if is_chrome_installed_windows():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('Chrome', interval=0.25)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        print("Chrome não está instalado no Windows.")

def abrir_Firefox():
    def is_Firefox_installed_windows():
        firefox_install_dir = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        return os.path.exists(firefox_install_dir)
    
    if is_Firefox_installed_windows():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('Firefox', interval=0.25)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
    else:
        print("FireFox não está instalado no Windows.")

def obter_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        print("Erro ao obter as cotações.")
        return None
    
def cotacoes():
    cotacoes = obter_cotacoes()
    if cotacoes:
        usd_brl = float(cotacoes['USDBRL']['bid'])
        eur_brl = float(cotacoes['EURBRL']['bid'])
        btc_brl = float(cotacoes['BTCBRL']['bid'])

        print(f"Cotação USD-BRL: {usd_brl:.2f}")
        print(f"Cotação EUR-BRL: {eur_brl:.2f}")
        print(f"Cotação BTC-BRL: {btc_brl:.2f}")
        time.sleep(5)

def consumoDiario():
    peso = float(input("Digite seu peso em Kg:"))
    print("KCAL")
    print("Kcal perder peso: {0:.2f}Kcal".format(peso*25))
    print("Kcal manter peso: {0:.2f}Kcal".format(peso*35))
    print("Kcal manter peso: {0:.2f}Kcal".format(peso*45))
    print("M A C R O S:")
    print("Quantidade de Proteinas Diaria: {0:.2f}g".format(peso*1.5))
    print("Quantidade de Carboidrato Diaria: {0:.2f}g".format(peso*9))
    print("Quantidade de Agua Diaria: {0:.2f}ml".format(peso*45))
    print("Quantidade de Gordura Diaria: {0:.2f}g".format(peso*0.25))
    print("MICROS")
    print("Vitamina A minima Diaria: {0:.2f} mcg".format(peso*12))
    print("Vitamina B1 minima Diaria: {0:.2f} mcg".format(peso*17.15))
    print("Vitamina B2 minima Diaria: {0:.2f} mcg".format(peso*18.60))
    print("Vitamina B3 minima Diaria: {0:.2f} mcg".format(peso*230))
    print("Vitamina B5 minima Diaria: {0:.2f} mcg".format(peso*72))  
    print("Vitamina B6 minima Diaria: {0:.2f} mcg".format(peso*25))
    print("Vitamina B7 minima Diaria: {0:.2f} mcg".format(peso*1.5))
    print("Vitamina B9 minima Diaria: {0:.2f} mcg".format(peso*9))
    print("Vitamina B12 minima Diaria: {0:.2f} mcg".format(peso*0.035))
    print("Vitamina C minima Diaria: {0:.2f} mg".format(peso*1.75))
    print("Vitamina D minima Diaria: {0:.2f} UI".format(peso*12))
    print("Vitamina E minima Diaria: {0:.2f} mg".format(peso*0.22))
    print("Vitamina K minima Diaria: {0:.2f} mcg".format(peso*1.75))
    print("Ferro minima Diaria: {0:.2f} mg".format(peso*145))
    print("Zinco minima Diaria: {0:.2f} mg".format(peso*175))
    print("Iodo minima Diaria: {0:.2f} mcg".format(peso*2.15))
    print("Selênio minima Diaria: {0:.2f} mcg".format(peso*0.80))
    print("Cobre minima Diaria: {0:.2f} mcg".format(peso*13.50))
    print("Manganês minima Diaria: {0:.2f} mg".format(peso*0.04))
    print("Molibdênio minima Diaria: {0:.2f} mg".format(peso*0.65))
    print("Molibdênio minima Diaria: {0:.2f} mcg".format(peso*0.65))
    print("Cromo minima Diaria: {0:.2f} mcg".format(peso*0.5))
    print("Flúor minima Diaria: {0:.2f} mg".format(peso*0.06))
    time.sleep(20)


def calculo_do_IMC():
    peso = float(input("diga seu peso em Kg:"))
    altura = float(input("Diga sua altura em Metros:"))
    imc = peso / (altura ** 2)
    print("seu imc é de {0:.2f}".format(imc))
    time.sleep(5)



def menu():
    while True:
        print("\n-- Menu --")
        print("1. Abrir/Verificar se o Valorant está instalado")
        print("2  Abrir/Verificar League of Legends")
        print("3. Abrir/Verificar se o Steam está instalado")
        print("4. Abrir/Verificar se o Epic está instalado")
        print("5. Abrir/Verificar se o Vs Code está instalado")
        print("6. Abrir/Verificar se o Obsidian está instalado")
        print("7. Abrir/Verificar se o Chrome está instalado")
        print("8. Abrir/Verificar se o FireFox está instalado")
        print("9. Verificar cotação de moedas")
        print("10. Consumo diario de Nutrientes e vitaminas")
        print("11. IMC")
        print("12. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            abrir_valorant()
        elif opcao == "2":
            abrir_Lol()
        elif opcao == "3":
            abrir_Steam()
        elif opcao == "4":
            abrir_Epic()
        elif opcao == "5":
            abrir_Vscode()
        elif opcao == "6":
            abrir_Obsidian()
        elif opcao == "7":
            abrir_Chrome()
        elif opcao == "8":
            abrir_Firefox()
        elif opcao == "9":
            cotacoes()
        elif opcao == "10":
            consumoDiario()
        elif opcao == "11":
            calculo_do_IMC()
        elif opcao == "12":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    while True:
        menu()
    