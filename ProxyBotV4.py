import telebot
from telebot import types
import threading
import requests
import time
import os
import re

token = "-----" #ur token
dev = "t.me/susiraq" #the dev url
chat_id = "@defproxy" #ur channel's username
channelname = "404" #ur channel's name
channelurl = "t.me/teamon404" #ur channel's url
filename = "proxy.txt" # don't change it
timeProxy = 60 # every minute send one proxy to channel
timeFile = 3600 # every hour send file (1000 proxy) to channel 
url_1 = "https://gimmeproxy.com/api/getProxy"
url_2 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
urls = '''
http://globalproxies.blogspot.com/
http://www.cybersyndrome.net/plz.html
http://www.cybersyndrome.net/plr5.html
http://biskutliat.blogspot.com/
http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html
http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html
http://www.cybersyndrome.net/pla5.html
http://vipprox.blogspot.com/2013_06_01_archive.html
http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html
http://vipprox.blogspot.com/p/blog-page_7.html
http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html
http://vipprox.blogspot.com/2013_02_01_archive.html
http://alexa.lr2b.com/proxylist.txt
http://vipprox.blogspot.com/2013_03_01_archive.html
http://browse.feedreader.com/c/Proxy_Server_List-1/449196260
http://browse.feedreader.com/c/Proxy_Server_List-1/449196258
http://sock5us.blogspot.com/2013/06/01-07-13-free-proxy-server-list.html#comment-form
http://browse.feedreader.com/c/Proxy_Server_List-1/449196251
http://free-ssh.blogspot.com/feeds/posts/default
http://browse.feedreader.com/c/Proxy_Server_List-1/449196259
http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html
http://proxyfirenet.blogspot.com/
https://www.javatpoint.com/proxy-server-list
https://openproxy.space/list/http
http://proxydb.net/
http://olaf4snow.com/public/proxy.txt
http://westdollar.narod.ru/proxy.htm
https://openproxy.space/list/socks4
https://openproxy.space/list/socks5
http://tomoney.narod.ru/help/proxi.htm
http://sergei-m.narod.ru/proxy.htm
http://rammstein.narod.ru/proxy.html
http://greenrain.bos.ru/R_Stuff/Proxy.htm
http://inav.chat.ru/ftp/proxy.txt
http://johnstudio0.tripod.com/index1.htm
http://atomintersoft.com/transparent_proxy_list
http://atomintersoft.com/anonymous_proxy_list
http://atomintersoft.com/high_anonymity_elite_proxy_list
http://atomintersoft.com/products/alive-proxy/proxy-list/3128
http://atomintersoft.com/products/alive-proxy/proxy-list/com
http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/
http://atomintersoft.com/products/alive-proxy/socks5-list
http://atomintersoft.com/proxy_list_domain_com
http://atomintersoft.com/proxy_list_domain_edu
http://atomintersoft.com/proxy_list_domain_net
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt
http://atomintersoft.com/proxy_list_domain_org
http://atomintersoft.com/proxy_list_port_3128
http://atomintersoft.com/proxy_list_port_80
http://atomintersoft.com/proxy_list_port_8000
http://atomintersoft.com/proxy_list_port_81
http://hack-hack.chat.ru/proxy/allproxy.txt
https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt
http://hack-hack.chat.ru/proxy/anon.txt
http://hack-hack.chat.ru/proxy/p1.txt
http://hack-hack.chat.ru/proxy/p2.txt
http://hack-hack.chat.ru/proxy/p3.txt
http://hack-hack.chat.ru/proxy/p4.txt
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt
https://free-proxy-list.net/
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt
https://www.us-proxy.org/
https://free-proxy-list.com/
https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt
https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all
https://spys.one/
https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt
https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all
'''
bot = telebot.TeleBot(token, num_threads=100, skip_pending=True, parse_mode="markdown", disable_web_page_preview=True)

keyboard = types.InlineKeyboardMarkup(row_width=1)
devurl = types.InlineKeyboardButton("The Owner", url=dev)
channellurl = types.InlineKeyboardButton("Our Channel", url=channelurl)
keyboard.row(devurl, channellurl)

def proxyGay():
    while False: #if u want to send to the channel make it True
        try:
            rq = requests.get(url_1)
            data = rq.json()
            protocol = data["protocol"]
            ipport = data["ipPort"]
            country = data["country"]
            speed = data["speed"]
            messageProxy = f"*- New Proxy*\n*Ip-Port:* `{ipport}`.\n*Type:* {protocol}.\n*Speed:* {speed}.\n*Country:* {country}.\n----- ------- ------- ----\n-=> [{channelname}]({channelurl})"
            bot.send_message(chat_id, messageProxy)
            print("done send proxy")
        except Exception as e:
            print(f"an error when send proxy:\n{e}")
        time.sleep(timeProxy)

def send404():
    while False: #if u want to send to the channel make it True
        cap = "*New proxy File*"
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print("- Done remove the old file")
            except Exception as e:
                print(f"an error in remove old file:\n{e}")
            try:
                dataa = requests.get(url_2).content
                with open(filename, 'wb') as f:
                    f.write(dataa)
                print("- Done download file")
            except Exception as e:
                print(f"an error in downloading file:\n{e}")
            try:
                with open(filename, 'rb') as txt:
                    bot.send_document(chat_id, txt, caption=cap)
                print("- Done send proxy file To channel")
            except Exception as e:
                print(f"an error when send the file:\n{e}")
        os.system("clear")
        time.sleep(timeFile)

oneminute = threading.Thread(target=proxyGay)
onehour = threading.Thread(target=send404)

oneminute.start()
onehour.start()

@bot.message_handler(commands=["start"])
def welcomemsg(message):
	bot.reply_to(message,"*أهلا بك عزيزي في بوت بروكسي\nأرسل* /send *للحصول على بروكسي\nأو* /file *للحصول على ملف بروكسيات*\n*Welcome To Proxy Bot\nSend* /send * To Get One Proxy\nOr* /file *To Send a Proxy File*", reply_markup=keyboard)

def scrape(urls, output_file):
    print("- Processing...")
    output_file = "proxies.txt"
    file = open(output_file, 'w')
    file.write('Proxies:\n')
    file.close()
    file = open(output_file, 'a')
    good_proxies = list()
    def pattern_one(url):
        ip_port = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}:\d{2,5})', url)
        if not ip_port:
            pattern_two(url)
        else:
            for i in ip_port:
                file.write(str(i) + '\n')
                good_proxies.append(i)
    def pattern_two(url):
        ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
        port = re.findall('td>(\d{2,5})<', url)
        if not ip or not port:
            pattern_three(url)
        else:
            for i in range(len(ip)):
                file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
                good_proxies.append(str(ip[i]) + ':' + str(port[i]))
    def pattern_three(url):
        ip = re.findall('>\n[\s]+(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
        port = re.findall('>\n[\s]+(\d{2,5})\n', url)
        if not ip or not port:
            pattern_four(url)
        else:
            for i in range(len(ip)):
                file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
                good_proxies.append(str(ip[i]) + ':' + str(port[i]))
    def pattern_four(url):
        ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
        port = re.findall('>(\d{2,5})<', url)
        if not ip or not port:
            pattern_five(url)
        else:
            for i in range(len(ip)):
                file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
                good_proxies.append(str(ip[i]) + ':' + str(port[i]))
    def pattern_five(url):
        ip = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
        port = re.findall('(\d{2,5})', url)
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))
    def start(url):
        try:
            req = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}).text
            pattern_one(req)
        except:
            print(str(url) + ' [x] Random Error')
    threads = list()
    for url in urls.splitlines():
        if url:
            x = threading.Thread(target=start, args=(url,))
            x.start()
            threads.append(x)
        for th in threads:
            th.join()	    

@bot.message_handler(commands=["file"])
def sendfile(message):
    bot.reply_to(message, "*أنتظر قليلاً ، قد تتأخر العملية لبضع دقائق\nبسبب سحب البروكسيات من مواقع كثيرة\nPlease Wait, The Process Maybe Delayed For a Few Minutes*")
    if os.path.exists("proxies.txt"):
        try:
            os.remove("proxies.txt")
            print("- done remove the old file")
        except Exception as e:
            print(f"an error in remove old file:\n{e}")
    try:
        scrape(urls, "proxies.txt")
        with open('proxies.txt', 'rb') as f:
            bot.send_document(message.chat.id, f, caption=f"*Done send the proxies\nit's a 60,000 -- 70,000*\n[{channelname}]({channelurl})")
            os.system("clear")
            print("- done send proxy file To chat")
    except Exception as e:
        bot.send_message(message.chat.id, f"*حدث خطأ، حاول مجددًا\n An Error, Please try again later\n\nأرسل الخطأ للمطور ليقوم بحله بأسرع وقت*:\n{e}")
        print("an error:\n{e}")

@bot.message_handler(commands=["send"])
def send(message):
    bot.reply_to(message,"*أنتظر قليلاً*")
    try:
        rqq = requests.get(url_1)
        datat = rqq.json()
        protocoll = datat["protocol"]
        ipportt = datat["ipPort"]
        countryy = datat["country"]
        speedd = datat["speed"]
        messageProxy = f"*- New Proxy*\n*Ip-Port:* `{ipportt}`.\n*Type:* {protocoll}.\n*Speed:* {speedd}.\n*Country:* {countryy}.\n----- ------- ------- ----\n-=> [{channelname}]({channelurl})"
        bot.send_message(message.chat.id, messageProxy)
        print("- done send proxy To chat")
    except Exception as e:
        bot.send_message(message.chat.id, f"*حدث خطأ، حاول مجددًا\n An Error, Please try again later\n\nأرسل الخطأ للمطور ليقوم بحله بأسرع وقت*:\n{e}")
        print(f"an error when send proxy:\n{e}")
				
bot.infinity_polling()