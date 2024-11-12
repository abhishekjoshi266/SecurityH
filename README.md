# Security Headers Test Tool


![Screenshot_20241112_114843](https://github.com/user-attachments/assets/096b123e-3872-4577-9e59-f4a809cdf4bd)




## Introduction
Welcome to the Security Headers Test Tool! This powerful tool is designed to help you assess and improve the security of your web applications by testing the presence and configuration of essential security headers.

## Features
- **Comprehensive Header Testing**: Checks for the presence of over 20 essential security headers.
- **Detailed Reports**: Provides detailed reports on the status of each header, along with recommendations for improvement.
- **User-Friendly Interface**: Easy to use, even for those without extensive technical knowledge.
- **Real-Time Feedback**: Instant results and actionable insights to enhance your web security.

## How to Use
1. **Installation**:

      `git clone https://github.com/abhishekjoshi266/SecurityH`
      `cd SecurityH`
    `  chmod +x SecurityH.py`
    `  python3 SecurityH.py`
   

## Security Headers Checked
- `Content-Security-Policy`
- `X-Content-Type-Options`
- `X-Frame-Options`
- `X-XSS-Protection`
- `Strict-Transport-Security`
- `Referrer-Policy`
- `Feature-Policy`
- `Expect-CT`
- `Permissions-Policy`

## Example Report
```plaintext

Security Headers Scan Result
=======================================


Raw Headers Returned:
Content-Length: 173499
Content-Type: text/html; charset=UTF-8
Link: <https://static.parastorage.com/>; rel=preconnect; crossorigin;,<https://static.parastorage.com/>; rel=preconnect;,<https://static.wixstatic.com/>; rel=preconnect; crossorigin;,<https://static.wixstatic.com/>; rel=preconnect;,<https://siteassets.parastorage.com>; rel=preconnect; crossorigin;,
Html-Cacheable: true
ETag: W/"047155664de0a0097f04ce9a2dcbe7c6"
Content-Language: en
Strict-Transport-Security: max-age=86400
Cache-Control: public,max-age=0,must-revalidate
Server: Pepyaka
X-Content-Type-Options: nosniff
Content-Encoding: br
Accept-Ranges: bytes
Age: 1129
Date: Tue, 12 Nov 2024 06:19:50 GMT
X-Served-By: cache-del21745-DEL
X-Cache: HIT
Vary: Accept-Encoding
Server-Timing: cache;desc=miss, varnish;desc=miss_hit, dc;desc=fastly_g
Set-Cookie: ssr-caching=cache#desc=miss#varnish=miss_hit#dc#desc=fastly_g; max-age=20
X-Wix-Request-Id: 1731392390.677435097271216553
X-Seen-By: yvSunuo/8ld62ehjr5B7kA==,7U7NzZSqfMgd9YnjHLtUa7xkNjrXdwdgtu6E0yACibU=,m0j2EEknGIVUW/liY8BLLn3pJ6os+jMZl8eSiOUhV8zQYjEJxCMSl2Cb+N3EkeV+,2d58ifebGbosy5xc+FRalodEdweTeAxyigfUmH/roSDEzBYBwqosghu2e6LYqjBnY+O/ZVf9/UwpIGIMy4LuOQ==,2UNV7KOq4oGjA5+PKsX47NAyUNYijOXLVpL50aLzshK8ZDY613cHYLbuhNMgAom1,XkGKDeZOMUJUOewmjHKJGjSjyRsx2GW2fdktQPGHYLM=,GiE5c8Q213kn1NHwElo57Gf8g9WqJSzeXQeLOng4wNkZuTIvkn1aLWagJEQu7azjIhLmn6kXswbjua8x2kAVdQ==,dXCupDx7fKRgT5AI44ZMHYMRCEItGhKWu8ocNnZC/es=,LoUK8/saGAmOxZWtpubo2vBBTDl5MAg6RxTDlmd/m4cvOnJRh6yb7RG2E3rKg4V9o+him43c2lRtSBQ8+lQcXQ==,ernGPVlPeSAKSTGO/spWi0gNi2FB/A/VcOPV9Icx/DM=,/a5ccLSK1HEmwPNg/x6OurE73w+moFxtx2DmX82/4zlOECBh36m9HqoHGpbqHAQutfvd87/YTxmiWsSN8DkrmbdJAPzAI0nyqs4CT/m6tKk=
Via: 1.1 google
glb-x-seen-by: bS8wRlGzu0Hc+WrYuHB8QIg44yfcdCMJRkBoQ1h6Vjc=
Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000


Security Headers Scan Results:
• Strict-Transport-Security: Found - max-age=86400
• Content-Security-Policy: Not Found
• X-Content-Type-Options: Found - nosniff
• X-Frame-Options: Not Found
• X-XSS-Protection: Not Found
• Referrer-Policy: Not Found
• Feature-Policy: Not Found
• Permissions-Policy: Not Found

Total Security Headers Scan:
Total Security Headers Found: 2
Total Security Headers Not Found: 6

