from colorama import Fore
import subprocess
print(Fore.CYAN + "do 'google-search' for google!")

running = True

while running:
    url = input(Fore.BLUE +"https://")
    if url.lower() == "google-search":
        subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'http://www.google.com/'])
    else:
        subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', url])
        print("Opened", url)



    
