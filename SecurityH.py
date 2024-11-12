import requests as r
import warnings as w
from urllib3.exceptions import InsecureRequestWarning as I
from termcolor import colored as c

w.filterwarnings("ignore", category=I)

H = {
    "Strict-Transport-Security": "HSTS",
    "Content-Security-Policy": "CSP",
    "X-Content-Type-Options": "XCTO",
    "X-Frame-Options": "XFO",
    "X-XSS-Protection": "XXP",
    "Referrer-Policy": "RP",
    "Feature-Policy": "FP",
    "Permissions-Policy": "PP"
}

def b():
    a = r"""
                 |--------------------------------|                                     
                 | Security Headers Scanner       |
                 | Created by: Abhishek Joshi     |
                 | Version: 1.0                   |
                 |--------------------------------|
    """
    print(c(a, 'cyan'))

def s(u):
    try:
        x = r.get(u, verify=False)
        h = x.headers

        print("\nRaw Headers Returned:")
        for k, v in h.items():
            print(f"{k}: {v}")

        f = {}
        n = []

        for k, _ in H.items():
            if k in h:
                f[k] = h[k]
            else:
                n.append(k)

        print("\nSecurity Headers Scan Results:")
        for k in H.keys():
            if k in f:
                print(c(f"• {k}: Found - {f[k]}", 'green'))
            else:
                print(c(f"• {k}: Not Found", 'red'))

        tf = len(f)
        tn = len(n)

        print("\nTotal Security Headers Scan:")
        print(f"Total Security Headers Found: {tf}")
        print(f"Total Security Headers Not Found: {tn}")

    except r.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    print("\nWARNING: This tool may give false positives. Please verify using Burp Suite or visit https://securityheaders.com/.")

if __name__ == "__main__":
    b()
    url = input("Enter the URL of the website to scan (including http:// or https://): ")
    s(url)