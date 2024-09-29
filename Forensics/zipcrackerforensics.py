#!/usr/bin/python3

from tqdm import tqdm
import zipfile

zip_file_name = "Trybreakingme.zip" 


wordlist_file = "rockyou.txt"  


def crack_zip_with_wordlist(zip_file_name, wordlist_file):
    try:
       
        with zipfile.ZipFile(zip_file_name) as zip_file:
            
            with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as wordlist:
                
                total_passwords = sum(1 for _ in wordlist)
                wordlist.seek(0)  

                print(f"Total passwords to test: {total_passwords}")

                
                for password in tqdm(wordlist, total=total_passwords, desc="Checking passwords"):
                    password = password.strip()  
                    try:
                       
                        zip_file.extractall(pwd=password.encode('utf-8'))
                        print(f"\n[+] Password Found: {password}")
                        return password  
                    except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
                        continue  

        print("[!] Password not found in the wordlist.")
        return None

    except FileNotFoundError:
        print("[!] Wordlist or ZIP file not found. Please check the file paths.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    crack_zip_with_wordlist(zip_file_name, wordlist_file)

