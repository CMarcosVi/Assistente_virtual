from reportlab.pdfgen import canvas
import tkinter as tk
import os
import subprocess
import time
from threading import Thread
import speech_recognition as sr
import requests
import pyttsx3
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


user_profile = os.environ['USERPROFILE']

def iniciacao():
    try :
        menu()
    except:
        InterfaceCenter()










class AnimatedCircles:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Circles")
        self.root.geometry("350x550")
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(root, width=350, height=550, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.outer_circle = self.create_outer_circle(175, 275)
        self.animate()

    def create_outer_circle(self, x, y):
        outer_circle = self.canvas.create_oval(x - 25, y - 25, x + 25, y + 25, outline="white", width=2)
        return outer_circle

    def animate(self):
        # Animação para criar um círculo transparente
        self.animate_transparent_circle()

    def animate_transparent_circle(self):
        inner_circle = self.canvas.create_oval(175 - 15, 275 - 15, 175 + 15, 275 + 15, outline="white", width=2, stipple="gray50")

        # Agendamento da próxima etapa da animação (deletar o círculo transparente)
        self.root.after(250, self.canvas.delete, inner_circle)

        # Agendamento da próxima etapa da animação
        self.root.after(1000, self.animate)  # 2000ms (2 segundos) para a próxima animação

    def fechar(self):
        self.root.destroy()

def InterfaceCenter():
    root = tk.Tk()
    app = AnimatedCircles(root)
    root.mainloop()
















    def capture_audio():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Ajusta o nível de ruído do ambiente
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
            return None
        except sr.RequestError:
            print("Não foi possível acessar o serviço de reconhecimento de fala.")
            return None


# funções do aplicativo
def hora_local_data():
    url = "http://worldtimeapi.org/api/ip"
    response= requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['datetime']
        
    else:
        return "Erro não conseguimos estabelecer sua localização"

def abrir_valorant():
    def is_valorant_installed_windows():
        valorant_exe = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
        return os.path.exists(valorant_exe)

    if is_valorant_installed_windows():
        valorant_exe = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
        subprocess.run([valorant_exe], check=True)
        time.sleep(1)
    else:
        print("Valorant não está instalado no Windows.")


def abrir_Steam():
    def is_steam_installed_windows():
        steam_install_dir = r'C:\Program Files (x86)\Steam\Steam.exe'
        return os.path.exists(steam_install_dir)

    if is_steam_installed_windows():
        steam_install_dir = r'C:\Program Files (x86)\Steam\Steam.exe'
        subprocess.run([steam_install_dir], check=True)
        time.sleep(1)
    else:
        print("Steam não está instalado no Windows.")

def abrir_Epic():
    def is_epic_installed_windows():
        epic_install_dir = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32" 
        return os.path.exists(epic_install_dir)

    if is_epic_installed_windows():
        epic_install_dir = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe" 
        subprocess.run(epic_install_dir, check=True)
        time.sleep(1)
    else:
        print("Epic Games não está instalado no Windows.")

def abrir_Lol():
    def is_lol_installed_windows():
        lol_install_dir = "C:\\Riot Games\\League of Legends\\LeagueClient.exe"
        return os.path.exists(lol_install_dir)

    if is_lol_installed_windows():
        lol_install_dir = "C:\\Riot Games\\League of Legends\\LeagueClient.exe"
        subprocess.run(lol_install_dir, check=True)
        time.sleep(1)
    else:
        print("League of Legends não está instalado no Windows.")

def abrir_Vscode():
    def is_Vscode_installed_windows():
        vscode_install_dir ="{}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe".format(user_profile)
        return os.path.exists(vscode_install_dir)
    
    if is_Vscode_installed_windows():
        vscode_install_dir ="{}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe".format(user_profile)
        subprocess.run(vscode_install_dir, check=True)
        time.sleep(1)
    else:
        print("Vs Studio Code não está instalado no Windows.")

def abrir_Obsidian():
    def is_obsidian_installed_windows():
        obsidian_install_dir = "{}\\AppData\\Local\\Obsidian\\Obsidian.exe".format(user_profile)
        return os.path.exists(obsidian_install_dir)
    
    if is_obsidian_installed_windows():
        obsidian_install_dir = "{}\\AppData\\Local\\Obsidian\\Obsidian.exe".format(user_profile)
        subprocess.run(obsidian_install_dir, check=True)
        time.sleep(1)
    else:
        print("Obsidian não está instalado no Windows.")

def abrir_Chrome():
    def is_chrome_installed_windows():
        chrome_install_dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        return os.path.exists(chrome_install_dir)
    
    if is_chrome_installed_windows():
        chrome_install_dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        subprocess.run(chrome_install_dir, check=True)
        time.sleep(1)
    else:
        print("Chrome não está instalado no Windows.")

def abrir_Firefox():
    def is_Firefox_installed_windows():
        firefox_install_dir = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        return os.path.exists(firefox_install_dir)
    
    if is_Firefox_installed_windows():
        firefox_install_dir = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        subprocess.run(firefox_install_dir, check=True)
        time.sleep(1)
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
    
def procurar_cep():
    valor_cep = input("Digite o CEP desejado: ")
    url = f"https://viacep.com.br/ws/{valor_cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            print("Informações do CEP:")
            print(f"CEP: {data['cep']}")
            print(f"Logradouro: {data['logradouro']}")
            print(f"Complemento: {data['complemento']}")
            print(f"Bairro: {data['bairro']}")
            print(f"Localidade: {data['localidade']}")
            print(f"UF: {data['uf']}")
            print(f"Ibge: {data['ibge']}")
            print(f"Gia: {data['gia']}")
            print(f"DDD: {data['ddd']}")
            print(f"Siafi: {data['siafi']}")
            time.sleep(5)
        else:
            print("CEP não encontrado")
    else:
        print("Erro na requisição")

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

def calorias():
    class PesoInputApp(QWidget):
        def __init__(self):
            super().__init__()

            self.init_ui()

        def init_ui(self):
            self.setWindowTitle('Informe seu peso')
            self.setGeometry(300, 300, 300, 150)

            layout = QVBoxLayout()

            label = QLabel('Digite seu peso em Kg:')
            self.peso_input = QLineEdit()
            self.peso_input.setPlaceholderText('Peso em Kg')
            button = QPushButton('Gerar PDF')

            layout.addWidget(label)
            layout.addWidget(self.peso_input)
            layout.addWidget(button)

            button.clicked.connect(self.gerar_pdf)

            self.setLayout(layout)

        def gerar_pdf(self):
            peso = float(self.peso_input.text())
            nome_do_arquivo_pdf = "informacoes_consumo_diario.pdf"
            caminho_completo = os.path.join("C:/Users/Public/Documents", nome_do_arquivo_pdf)

            pdf = canvas.Canvas(caminho_completo)
            pdf.drawString(100, 800, "Informações de Consumo Diário:")

            y = 780  # Posição vertical inicial
            informacoes = consumoDiario(peso)
            for info in informacoes:
                y -= 20  # Move para baixo a cada linha
                pdf.drawString(100, y, info)

            pdf.save()
            self.close()

    def consumoDiario(peso):
        informacoes = [
            "Kcal:",
            "-----",
            f"Kcal perder peso: {peso * 25:.2f} Kcal",
            f"Kcal manter peso: {peso * 35:.2f} Kcal",
            f"Kcal ganhar peso: {peso * 45:.2f} Kcal",
            "-----",
            "M A C R O S:",
            "-----",
            f"Quantidade de Proteínas Diárias: {peso * 1.5:.2f} g",
            f"Quantidade de Carboidratos Diários: {peso * 9:.2f} g",
            f"Quantidade de Água Diária: {peso * 45:.2f} ml",
            f"Quantidade de Gordura Diária: {peso * 0.25:.2f} g",
            "-----",
            "MICROS:",
            "-----",
            f"Vitamina A mínima Diária: {peso * 12:.2f} mcg",
            f"Vitamina B1 mínima Diária: {peso * 17.15:.2f} mcg",
            f"Vitamina B2 mínima Diária: {peso * 18.60:.2f} mcg",
            f"Vitamina B3 minima Diaria: {peso * 230:.2f} mcg",
            f"Vitamina B5 minima Diaria: {peso * 72:.2f} mcg",
            f"Vitamina B6 minima Diaria: {peso * 25:.2f} mcg",
            f"Vitamina B7 minima Diaria: {peso * 1.5:.2f} mcg",
            f"Vitamina B9 minima Diaria: {peso * 9:.2f} mcg",
            f"Vitamina B12 minima Diaria: {peso * 0.035:.2f} mcg",
            f"Vitamina C minima Diaria: {peso * 1.75:.2f} mg",
            f"Vitamina D minima Diaria: {peso * 12:.2f} UI",
            f"Vitamina E minima Diaria: {peso * 0.22:.2f} mg",
            f"Vitamina K minima Diaria: {peso * 1.75:.2f} mcg",
            f"Ferro minima Diaria: {peso * 145:.2f} mg",
            f"Zinco minima Diaria: {peso * 175:.2f} mg",
            f"Iodo minima Diaria: {peso * 2.15:.2f} mcg",
            f"Selênio minima Diaria: {peso * 0.80:.2f} mcg",
            f"Cobre minima Diaria: {peso * 13.50:.2f} mcg",
            f"Manganês minima Diaria: {peso * 0.04:.2f} mg",
            f"Molibdênio minima Diaria: {peso * 0.65:.2f} mg",
            f"Molibdênio minima Diaria: {peso * 0.65:.2f} mcg",
            f"Cromo minima Diaria: {peso * 0.5:.2f} mcg",
            f"Flúor minima Diaria: {peso * 0.06:.2f} mg",
        ]

        return informacoes

    app = QApplication([])
    app.setStyle('Fusion')  # Escolha um estilo de GUI, como 'Fusion'
    janela = PesoInputApp()
    janela.show()
    app.exec_()

def calculo_do_IMC():
    peso = float(input("diga seu peso em Kg:"))
    altura = float(input("Diga sua altura em Metros:"))
    imc = peso / (altura ** 2)
    print("seu imc é de {0:.2f}".format(imc))
    time.sleep(5)


# menu de exibição das alternativas
def menu(root):
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
        print("12. Procurar CEP")
        print("13. Pegar Hora e Data")
        print("14. Sair do programa")
        
        engine = pyttsx3.init()
        engine.say("Ola tudo bem, Sou PX estou aqui para te ajudar, escolha uma das funções")
        engine.runAndWait()
        engine.stop()
    
        opcao = input("Escolha uma opção: ")
        engine = pyttsx3.init()

        if opcao == "1" or opcao.lower() == "abrir valorant":
            engine.say("Abrindo valorant,aguarde por favor")
            engine.runAndWait()
            engine.stop()
            abrir_valorant()
        elif opcao == "2" or opcao.lower() == "abrir Lol": # arrumar mensagem de inexistencia não esta aparecendo
            engine.say("Abrindo League of legends,aguarde Por favor")
            engine.runAndWait()
            engine.stop()
            abrir_Lol()
        elif opcao == "3" or opcao.lower() == "abrir steam":
            engine.say("Abrindo steam,aguarde Por favor")
            engine.runAndWait()
            engine.stop()
            abrir_Steam() 
        elif opcao == "4" or opcao.lower() == "abrir epic":
            engine.say("Abrindo Epic,aguarde Por favor")
            engine.runAndWait()
            engine.stop()
            abrir_Epic()
        elif opcao == "5" or opcao.lower() == "abrir vscode":
            engine.say("Abrindo Visual Studio Code,aguarde Por favor")
            engine.runAndWait()
            engine.stop()
            abrir_Vscode()
        elif opcao == "6" or opcao.lower() == "abrir obsidian":
            engine.say("Abrindo Obsidian,aguarde Por favor")
            engine.runAndWait()
            engine.stop()
            abrir_Obsidian()
        elif opcao == "7" or opcao.lower() == "abrir chrome":
            engine.say("Abrindo Chrome,aguarde Por favor")
            engine.runAndWait()
            engine.stop()
            abrir_Chrome()
        elif opcao == "8" or opcao.lower() == "abrir firefox":
            engine.say("Abrindo Firefox,aguarde Por favor")
            engine.runAndWait()
            engine.stop()
            abrir_Firefox()
        elif opcao == "9" or opcao.lower() == "cotação":
            engine.say("Pesquisando cotações Do Dolar,Euro e Bitcoin")
            engine.runAndWait()
            engine.stop()
            cotacoes()
        elif opcao == "10" or opcao.lower() == "bioconsumo":
            engine.say("Informaremos o seu consumo diario de MacroNutrientes e MicroNutrientes, Insira seu peso em Kilos")
            engine.runAndWait()
            engine.stop()
            calorias()
        elif opcao == "11" or opcao.lower() == "imc":
            engine.say("Insira as informações para que possamos calcular seu IMC")
            engine.runAndWait()
            engine.stop()
            calculo_do_IMC()
        elif opcao == "12" or opcao.lower() == "procurar cep":
            engine.say("Insira o CEP que deseja buscar")
            engine.runAndWait()
            engine.stop()
            procurar_cep()
        elif opcao == "13" or opcao.lower() == "data e hora":
            current_time = hora_local_data()
            date_part, time_part = current_time.split("T")
            time_part = time_part.split(".")[0]
            print("Data atual:", date_part)
            print("Hora atual:", time_part)
            time.sleep(5)
        elif opcao == "14" or opcao.lower() == "Desligar":
            engine.say("Até Logo")
            engine.runAndWait()
            engine.stop()
            print("Programa encerrado.")
            app = AnimatedCircles(root)
            app.fechar()
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    root = tk.Tk()
    interface_thread = Thread(target=InterfaceCenter)
    interface_thread.start()
    menu(root)
    interface_thread.join()

if __name__ == "__main__":
    main()
