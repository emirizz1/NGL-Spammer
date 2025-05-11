import requests
import random
import time
import os
import getpass
import random
import re
import sys
from colorama import init, Fore, Style
init(autoreset=True)

renkler = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE
]
sifirla = Style.RESET_ALL



key = [
    "ariva",
    "ARİVA"
]

sifre = getpass.getpass("Lütfen Satın Aldığınız Anahtarı Giriniz!\n Anahtar: ").strip()  

if sifre in key:
    print(Fore.GREEN + "Başarılı! Yükleniyor..." + sifirla)
    time.sleep(1)

    asci = [
        " █████╗ ██████╗ ██╗██╗   ██╗ █████╗ ",
        "██╔══██╗██╔══██╗██║██║   ██║██╔══██╗",
        "███████║██████╔╝██║██║   ██║███████║",
        "██╔══██║██╔══██╗██║╚██╗ ██╔╝██╔══██║",
        "██║  ██║██║  ██║██║ ╚████╔╝ ██║  ██║",
        "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝"
    ]

    for i in range(1, len(asci) + 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        for j, line in enumerate(asci[:i]):
            if j % 2 == 0:
                renk = random.choice(renkler)
            print(renk + line + sifirla)
        time.sleep(0.3)

    print(Style.BRIGHT + Fore.GREEN + "\nMerhaba NGL Spam Tooluna Hoşgeldiniz, Lütfen Seçenekleri Numaralarıyla Cevaplandırınız." + sifirla)
    print(Fore.BLUE + "1 / NGL Spam Tool'unu Çalıştır." + sifirla)
    print(Fore.RED + "2 / Çıkış" + sifirla)

    secim = input("Seçiminiz: ")

    if secim == "1":
        os.system('cls') 
        print("🔧 Tool başlatılıyor... ")
        username = input("Lütfen NGL Spam Mesajları Atılacak NGL Hesabını Yazınız: ")
        message = input("Spam Atılacak Mesajı Giriniz: ")

        # API URL
        url = "https://ngl.link/api/submit"

        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 11; SM-G991B)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3)",
            "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL)",
            "Mozilla/5.0 (Windows NT 10.0; ARM64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 12; SM-A525F)",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)",
            "Mozilla/5.0 (iPod touch; CPU iPhone OS 13_3_1 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 9; Redmi Note 7)",
            "Mozilla/5.0 (Windows NT 10.0; WOW64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P)",
            "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)",
            "Mozilla/5.0 (iPad; CPU OS 13_6 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 7.1.1; Moto G5 Plus)",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 7 Build/LMY48P)",
            "Mozilla/5.0 (Windows NT 6.2; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3)",
            "Mozilla/5.0 (iPad; CPU OS 16_0 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 13; Pixel 7)",
            "Mozilla/5.0 (Windows NT 10.0; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 12; OnePlus 9)",
            "Mozilla/5.0 (Windows NT 5.1; rv:40.0)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)",
            "Mozilla/5.0 (iPad; CPU OS 12_5 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 4)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; rv:79.0)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 10; Galaxy S20)",
            "Mozilla/5.0 (Windows NT 6.0; WOW64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)"
        ]


        i = 1 

        while True:
            headers = {
                'User-Agent': random.choice(user_agents),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://ngl.link',
                'Referer': f'https://ngl.link/{username}',
            }
            
            data = {
                'username': username,
                'question': message,
                'deviceId': '', 
                'gameSlug': '',
                'referrer': '',
            }
            
            response = requests.post(url, headers=headers, data=data)

            if i == 20:
                time.sleep(20)
                i = 1
            
            if response.status_code == 200:
                print(Fore.GREEN + f"[{i}] Mesaj gönderildi." + sifirla)
            else:
                print(Fore.RED + f"[{i}] Hata oluştu! Status Code: {response.status_code}" + sifirla)
            
            i += 1

    elif secim == "2":
        print("👋 Çıkılıyor...")
    else:
        print("⚠️ Geçersiz seçim.")
else:
    print("❌ Giriş reddedildi. Kullanıcı adı veya şifre yanlış.")
