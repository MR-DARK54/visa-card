o
    a?b	  ?                   @   s?  d dl Z d dlZd dlZd dlmZ d dlmZ d dlZd dlZd dl	Z	d dl
Z
dd? ZejjZejjZejjZejjZejjZejjZejjZejjZe
?d? dd? Zee? ? eed	 ? eed
 ? eed ? e ed ?Z!dd? Z"dd? Z#dd? Z$e!dkr?eed ? e?%d? ee"? ? dS e!dkr?eed ? ee#? ? dS e!dkr?eed ? e ed ?Z&e? dkr?e
?'de& ??(? Z'eee' e ? dS e
?'de& ??(? Z'eee' e ? dS dS )?    N)?BeautifulSoup)?Figletc                   C   s   dt jv rdS dS )N?win?windowsZlinux)?sys?platform? r   r   ?/sdcard/card.py?	detect_os   s   
r
   ?clearc                  C   s   t dd??d?} t|  S )NZstandard)Zfontz  D A R K - C A R D )r   Z
renderText?gn)Zfigletr   r   r	   ?logo   s   r   z'[-] telegram >> https://t.me/name_dark z[+] Made By M R - D A R Kz#[=] my is hacker i from egypt : 1.1z?
[x] 1) Generate single valid cc
[x] 2) Generate multi valid cc (generate cc list)
[x] 3) CC validator

[^] Please Enter an option :  c                  C   s?   ddddddd?} dd	d
dd?}ddddddddddd
d?}d}t j||| |d?}t?|j?}|d d }td|d |d |d |d |d |d  |d! |d" |d# |d$ f
  t S )%N?@8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i?GA1.2.1579916434.1654760883?GA1.2.1410860416.1654760883?dID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw?TUID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw??[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]?Z	csrftokenZ_gaZ_gidZ_gadsZ_gpiZFCNEC?oMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36?!application/x-www-form-urlencoded?@xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj?XMLHttpRequest?z
User-Agentzcontent-typezx-csrftokenzx-requested-with?VISA?UNITED STATES?121 FINANCIAL C.U.? ?
500 - 1000?10?TEXT?on?ZbrandZcountryZbankZcvv?date?year?rangeZamountZ
dataformatZpinZctoken?Ahttps://www.vccgenerator.org/fetchdata/generate-home-credit-card/??headers?cookies?data?
creditCard?   z?[-] Brand : %s
[-] Card Number : %s
[-] Bank : %s
[-] Name : %s
[-] Address : %s
[-] Country : %s
[-] Money Range : %s
[-] CVV : %s
[-] Expiry : %s
[-] Pin : %s
============================
[*] Telegram Channel : https://t.me/name_dark?IssuingNetwork?
CardNumber?Bank?Name?Address?Country?
MoneyRange?CVV?Expiry?Pin)?requests?post?json?loads?textr   ?cv)r)   r(   ?payload?sitex?rsr*   ?cardr   r   r	   ?genscard)   s   LrA   c            	      C   s?   ddddddd?} dd	d
dd?}ddddddddddd
d?}d}t j||| |d?}t?|j?}tdd??d? tdd?D ]2}|d | }tdd?}|?d|d |d  |d! |d" |d# |d$ |d% |d& |d' |d( f
 ? q<td) t	 S )*Nr   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r    r!   r"   r&   r'   zdark_card.txt?wr,   ?
   r+   ?az?[-] Brand : %s
[-] Card Number : %s
[-] Bank : %s
[-] Name : %s
[-] Address : %s
[-] Country : %s
[-] Money Range : %s
[-] CVV : %s
[-] Expiry : %s
[-] Pin : %s
===================================
r-   r.   r/   r0   r1   r2   r3   r4   r5   r6   zB[$] The operation has been success
[+] Saved File as dark_card.txt)
r7   r8   r9   r:   r;   ?open?writer%   r   r<   )	r)   r(   r=   r>   r?   r*   ?ir@   ?fr   r   r	   ?genmcard3   s   
LrI   c                 C   s8   d}d| |d?}t j||d?}t|jd?}t|j t S )Nzhttps://www.tools4noobs.com/Zajax_credit_card_validate)?actionr;   Zcc)r*   zhtml.parser)r7   r8   r   r;   ?blr<   )?number?typeZsiter=   ?resultZsoupr   r   r	   ?ccvalidatorA   s
   rO   ?1z"[&] You selected first option ! 

r,   ?2z#[&] You selected second option ! 

?3z#[&] You selected third option !! 

z$[$] Please Enter your card number : r   znode core\val.js znode core/val.js ))r   r7   r9   Zbs4r   Zpyfigletr   Zcolorama?timeZasyncio?osr
   ZForeZREDZrdZWHITEr<   ZMAGENTAZmagZBLUErK   ZGREENr   ZYELLOWZylZCYANZcyZLIGHTCYAN_EXZgg?systemr   ?print?inputZoprrA   rI   rO   ?sleeprL   ?popen?readr   r   r   r	   ?<module>   sX   




?