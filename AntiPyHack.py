import requests

R='\033[1;31m'
W='\033[1;37m'


def GetLibrary (full) :
    AllLibrary=[]
    for ThisLine in full.splitlines() :
        if ThisLine.strip().startswith('#'):continue
        if 'import ' in ThisLine :
            if 'from ' in ThisLine :
                NoneLine=ThisLine[0:ThisLine.find(' import')]
                NoneLine=NoneLine.replace('from','')
                NoneLine=NoneLine.strip()
                NoneLine=NoneLine.replace(',','\n')
                for LineItem in NoneLine.splitlines() :
                    GGG=LineItem.strip()
                    if '.' in GGG :
                        CutLibrary=GGG[0:GGG.find('.')]
                        AllLibrary.append(CutLibrary)
                    else:
                        AllLibrary.append(GGG)
            else:
                NoneLine=ThisLine.replace('import','')
                NoneLine=NoneLine.strip()
                NoneLine=NoneLine.replace(',','\n')
                for LineItem in NoneLine.splitlines() :
                    GGG=LineItem.strip()
                    if '.' in GGG :
                        CutLibrary=GGG[0:GGG.find('.')]
                        AllLibrary.append(CutLibrary)
                    else:
                        AllLibrary.append(GGG)
    return AllLibrary

class TelegramScanner () :
    def T1 (library) :
        if 'telebot' in library :
            print(f'{W}[{R}-{W}] {R}Telegram Bot With Telebot Library')
        ###################################################
        if 'telepot' in library :
            print(f'{W}[{R}-{W}] {R}Telegram Bot With Telepot Library')
        ###################################################
        if 'telegram' in library :
            print(f'{W}[{R}-{W}] {R}Telegram Bot With Telegram.ext Library')
    def T2 (line,library,Num) :
        if 'https://api.telegram.org/bot' in line :
            if 'requests' in library :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Telegram Api Bot With Requests Library')
                return
            if 'http' in library :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Telegram Api Bot With Http.client Library')
                return
            #######################################################
            else:
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Telegram Api Bot')
    
class DiscordScanner () :
    def T1 (library) :
        if 'discord' in library :
                print(f'{W}[{R}-{W}] {R}Discord Bot With Discord Library')
        ###################################################################
        if 'discordwebhook' in library :
                print(f'{W}[{R}-{W}] {R}Discord WebHook With Discordwebhook Library')
        ###################################################################
        if 'discord_webhooks' in library :
                print(f'{W}[{R}-{W}] {R}Discord WebHook With Discord_webhooks Library')
    def T2 (line,library,Num) :
        if 'https://discordapp.com/api/webhooks/' in line :
            if 'requests' in library :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Discord Api WebHook With Requests Library')
                return
            if 'http' in library :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Discord Api WebHook With Http.client Library')
                return
            #######################################################
            else:
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Discord Api WebHook')

def SocketScanner (line,library,Num,Port) :
    if 'connect(' in line :
        if 'socket' in library :
            if '. connect(' in line :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Hack Connetion ({Port}) With Socket Library')
                return
            if '.connect (' in line :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Hack Connetion ({Port}) With Socket Library')
                return
            #######################
            if '.connect(' in line :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Hack Connetion ({Port}) With Socket Library')
                return
            if '. connect (' in line :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Hack Connetion ({Port}) With Socket Library')
                return
    ###########################################################
    if 'connect (' in line :
        if 'socket' in library :
            if '. connect(' in line :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Hack Connetion ({Port}) With Socket Library')
                return
            if '.connect (' in line :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Hack Connetion ({Port}) With Socket Library')
                return
            #######################
            if '.connect(' in line :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Hack Connetion ({Port}) With Socket Library')
                return
            if '. connect (' in line :
                print(f'{W}[{R}-{W}] {W}[{R}Line {Num}{W}] {R}Hack Connetion ({Port}) With Socket Library')
                return

def GetSocketPort (full) :
    if 'SOCK_STREAM' in full :
        return 'TCP-Normal_Connect'
    if 'SOCK_DGRAM' in full :
        return 'UDP-Botnet_Connect'
    else:
        return 'Unknown_Connect'
    
class main () :
    def __init__ (self) :
        print(f'''{R}
                 _   _ _____       _    _            _    
     /\         | | (_)  __ \     | |  | |          | |   
    /  \   _ __ | |_ _| |__) |   _| |__| | __ _  ___| | __
   / /\ \ | '_ \| __| |  ___/ | | |  __  |/ _` |/ __| |/ /
  / ____ \| | | | |_| | |   | |_| | |  | | (_| | (__|   < 
 /_/    \_\_| |_|\__|_|_|    \__, |_|  |_|\__,_|\___|_|\_\\
 @Zaky                        __/ |                       
                             |___/                      
        ''')
        ScanTybe=input(f'{R}[ {W}*{R} ] {W}A Sample Python Scripts Scanner\n\n{R}[{W}1{R}] {W}Scan By Raw Link\n{R}[{W}2{R}] {W}Scan By File\n{R}[{W}3{R}] {W}Scan By Command Line\n\n{R}[ {W}?{R} ] {W} Select : ').strip()
        if ScanTybe in ['1','2','3'] :Nothing=0
        else:
            input(f'{R}[ {W}+{R} ] {W}Please Select With Number\n{R}[ {W}+{R} ] {W}Click Enter To Back :')
            main()
            exit()
        if ScanTybe == '1' :
            RawLink=input(f'\n\n{R}[ {W}?{R} ] {W}Enter Raw Link : ')
            print('\n')
            try:
                Raw=str(requests.get(RawLink).text)
            except:
                input(f'''{R}[ {W}-{R} ] {W}This Link is Wrong !!
{R}[ {W}Note{R} ]{W}--------------------

{R}[ {W}Wrong{R} ] {W}www.RawLink.com
{R}[ {W}Right{R} ] {W}https://www.RawLink.com

---------------------------''')
                exit()
            librarys=GetLibrary(Raw)
            TelegramScanner.T1(librarys)
            DiscordScanner.T1(librarys)
            LineNum=0
            for LineLoop in Raw.splitlines() :
                LineNum+=1
                if LineLoop.strip().startswith('#'):continue
                TelegramScanner.T2(LineLoop,librarys,LineNum)
                DiscordScanner.T2(LineLoop,librarys,LineNum)
                SocketScanner(LineLoop,librarys,LineNum,GetSocketPort(Raw))
            print(f'\n\n{R}[ {W}*{R} ] {W}Sacnning is Done !!')
            return
        if ScanTybe == '2' :
            FileName=input(f'\n{R}[ {W}?{R} ] {W}Enter File Name : ')
            print('\n')
            try:
                FileSrc=open(FileName,'r').read()
            except:
                input(f'''{R}[ {W}-{R} ] {W}File is Not Found
{R}[ {W}Note{R} ]{W}--------------------

{R}[ {W}Wrong{R} ] {W}File
{R}[ {W}Right{R} ] {W}File.py

---------------------------''')
                exit()
            librarys=GetLibrary(FileSrc)
            TelegramScanner.T1(librarys)
            DiscordScanner.T1(librarys)
            LineNum=0
            for LineLoop in FileSrc.splitlines() :
                LineNum+=1
                if LineLoop.strip().startswith('#'):continue
                TelegramScanner.T2(LineLoop,librarys,LineNum)
                DiscordScanner.T2(LineLoop,librarys,LineNum)
                SocketScanner(LineLoop,librarys,LineNum,GetSocketPort(FileSrc))
            print(f'\n{R}[ {W}*{R} ] {W}Sacnning is Done !!')
            return
        else:
            print(f'\n\n{R}[{W}Note{R}] {W}Write "out" To Stop Loop')
            AllSrc=''
            LineNum=0
            while True:
                Command=input(f'{W}#-Enter Command :')
                if Command.strip() == 'out' :
                    break
                LineNum+=1
                if Command.strip().startswith('#'):continue
                AllSrc+=Command+'\n'
                librarys=GetLibrary(AllSrc)
                TelegramScanner.T1(librarys)
                DiscordScanner.T1(librarys)
                TelegramScanner.T2(Command,librarys,LineNum)
                DiscordScanner.T2(Command,librarys,LineNum)
                SocketScanner(Command,librarys,LineNum,GetSocketPort(AllSrc))



if __name__ == '__main__' :
    main()
