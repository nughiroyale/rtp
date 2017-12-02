# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

satpam = LINETCR.LINE() # Koplaxs # Login Pake Akun Utama Kalian(Gunanya Supaya Akun Utama Ke Kick bisa Terima Undangan dari Bot Otomatis)
satpam.login(qr=True)
satpam.loginResult()

cl = LINETCR.LINE() #Aphrodite
cl.login(qr=True)
cl.loginResult()

ki = LINETCR.LINE() #Athena
ki.login(qr=True)
ki.loginResult()

kk = LINETCR.LINE() #Hera
kk.login(qr=True)
kk.loginResult()

kc = LINETCR.LINE() #Hestia
kc.login(qr=True)
kc.loginResult()

ks = LINETCR.LINE() #Artemis
ks.login(qr=True)
ks.loginResult()

ka = LINETCR.LINE() #Dione
ka.login(qr=True)
ka.loginResult()

kb = LINETCR.LINE() #Demeter
kb.login(qr=True)
kb.loginResult()

ko = LINETCR.LINE() #Nyx
ko.login(qr=True)
ko.loginResult()

ke = LINETCR.LINE() #Hemera
ke.login(qr=True)
ke.loginResult()

ku = LINETCR.LINE() # Ananke
ku.login(qr=True)
ku.loginResult()

k1 = LINETCR.LINE() #Backup (Gunanya Kalo Akun Utama Ke Kick, Dy masuk ke Group dan Ngekick yang Kick Akun Utama Dan Akun Utama Di undang sama dia,lalu dy leave lagi :D)
k1.login(qr=True)
k1.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" ^[ⓡ҉ⓞ҉ⓨ҉ⓐ҉ⓛ҉ⓔ҉ ⓣ҉ⓔ҉ⓐ҉ⓜ҉ ⓑ҉ⓞ҉ⓣ҉]^
OWNER •ⓃⓊⒼⒽⒾ•
♪♫•*¨*•.¸¸¸¸.•*¨*•♫♪
[̲̲̅̅ⓜ̲̅ⓔ̲̅ⓜ̲̅ⓑ̲̅ⓔ̲̅ⓡ̲ ̅ⓒ̲̅ⓞ̲̅ⓜ̲̅ⓜ̲̅ⓐ̲̅ⓝ̲̅ⓓ̲̅]
.help
.adminlist
.gid
.gurl
.creator

[̲̲̅̅ⓐ̲̅ⓓ̲̅ⓜ̲̅ⓘ̲̅ⓝ̲ ̅ⓒ̲̅ⓞ̲̅ⓜ̲̅ⓜ̲̅ⓐ̲̅ⓝ̲̅ⓓ̲̅]
.gn
.kick
.invite
.spam:
.bot?
.me
.gift
.allgift
.cancel
.openqr
.closeqr
.jointicket
.ginfo
.mymid
.midbot
.tl:
.banlist
.cekban
.killban
.clear
.random:
.respon
.mc
.cancelon/off
.qron/off
.contacton/off
.joinon/off
.leaveon/off
.shareon/off
.addon/off
.commenton/off
.jamon/off
.status
.cancelall
.setread => .cctv
.keluar
.tagall
.kill
.nk
.blacklist @
.banned @
.up
.lg
.speed

♪♫•*¨*•.¸¸¸¸.•*¨*•♫♪
ŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ
♪♫•*¨*•.¸¸¸¸.•*¨*•♫♪
"""

Setgroup =""" 
[̲̲̅̅ⓟ̲̅ⓡ̲̅ⓘ̲̅ⓥ̲̅ⓐ̲̅ⓣ̲̅ⓔ̲ ̅ⓒ̲̅ⓞ̲̅ⓜ̲̅ⓜ̲̅ⓐ̲̅ⓝ̲̅ⓓ̲̅]
.addadmin @
.remadmin @
.addbot @
.ban
.unban
.allbio:
.myname:
.invitemeto:
.masukgaes
.comein
.botlike
.likefr
.speed
.bc
.lg2
.allout
.vaccum
.mid @
.unban @
♪♫•*¨*•.¸¸¸¸.•*¨*•♫♪
   ⓡ҉ⓞ҉ⓨ҉ⓐ҉ⓛ҉ⓔ҉ ⓣ҉ⓔ҉ⓐ҉ⓜ҉ ⓑ҉ⓞ҉ⓣ҉
♪♫•*¨*•.¸¸¸¸.•*¨*•♫♪"""
KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]

mid = cl.getProfile().mid #Aphrodite
Amid = ki.getProfile().mid #Athena
Bmid = kk.getProfile().mid #Hera
Cmid = kc.getProfile().mid #Hestia
Dmid = ks.getProfile().mid #Artemis
Emid = ka.getProfile().mid #Dione
Fmid = kb.getProfile().mid #Demeter
Gmid = ko.getProfile().mid #Nyx
Hmid = ke.getProfile().mid #Hemera
Imid = ku.getProfile().mid #Ananke
Smid = satpam.getProfile().mid #Akun Utama
mid1 = k1.getProfile().mid #Backup

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Smid,mid1,"u08810e0d9afa004ff8d0de22fdb49b69"]
admin=["u08810e0d9afa004ff8d0de22fdb49b69","u356f48bf4857b500313d613f113d1d67"] 
owner=["u08810e0d9afa004ff8d0de22fdb49b69"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""Thanks for add me as friend
≫ ŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ ≪

Ready:

≫ Protect Bot ≪
≫ Self Bot ≪

Minat? Silahkan PM!
Idline: http://line.me/ti/p/~nughiroyale""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"[ⓡ҉ⓣ҉ⓑ҉]Aphrodite ",
    "cName2":"[ⓡ҉ⓣ҉ⓑ҉]Athena ",
    "cName3":"[ⓡ҉ⓣ҉ⓑ҉]Hera ",
    "cName4":"[ⓡ҉ⓣ҉ⓑ҉]Hestia ",
    "cName5":"[ⓡ҉ⓣ҉ⓑ҉]Artemis ",
    "cName6":"[ⓡ҉ⓣ҉ⓑ҉]Dione ",
    "cName7":"[ⓡ҉ⓣ҉ⓑ҉]Demeter ",
    "cName8":"[ⓡ҉ⓣ҉ⓑ҉]Nyx ",
    "cName9":"[ⓡ҉ⓣ҉ⓑ҉]Hemera ",
    "cName10":"[ⓡ҉ⓣ҉ⓑ҉]Ananke ",
    "cName11":"",
    "cName12":"ⓡ҉ⓞ҉ⓨ҉ⓐ҉ⓛ҉ⓔ҉ ⓣ҉ⓔ҉ⓐ҉ⓜ҉ ⓑ҉ⓞ҉ⓣ҉ ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    #"Protectjoin":True, # Ga Kepake(Yang Gabung langsung di kick :D) Udah  Udah ada Protect Cancell
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

#def NOTIFIED_READ_MESSAGE(op):
    #try:
        #if op.param1 in wait2['readPoint']:
            #Name = cl.getContact(op.param2).displayName
            #if Name in wait2['readMember'][op.param1]:
                #pass
            #else:
                #wait2['readMember'][op.param1] += "\n・" + Name
                #wait2['ROM'][op.param1][op.param2] = "・" + Name
        #else:
            #pass
    #except:
        #pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if op.param2 not in Bots:
              G = random.choice(KAC).getGroup(op.param1)
              G.preventJoinByTicket = True
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).updateGroup(G)
              random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        #------Joined User Kick start------#
        #if op.type == 17: #awal 17 ubah 13
           #if wait["Protectjoin"] == True:
               #if op.param2 not in admin and Bots : # Awalnya admin doang
                   #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#
        if op.type == 19: #Member Ke Kick
          if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            cl.inviteIntoGroup(op.param1,[op.param3])
        
        if op.type == 19: 
          if op.param3 in admin: #Kalo Admin ke Kick
            if op.param2 in Bots:
              pass
            if op.param2 in owner:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
              
        if op.type == 19:
          try:
            if op.param3 in Smid: #Akun Utama Ke Kick
              G = random.choice(KAC).getGroup(op.param1)
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              G.preventJoinByTicket = False
              random.choice(KAC).updateGroup(G)
              Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
              satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              G.preventJoinByTicket = True
              random.choice(KAC).updateGroup(G)
              satpam.updateGroup(G)
              wait["blacklist"][op.param2] = True
                                
            if op.param3 in mid:
              if op.param2 in Amid:
                G = ki.getGroup(op.param1)
                G.preventJoinByTicket = False
                ki.updateGroup(G)
                Ticket = ki.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ki.updateGroup(G)
              else:
                G = ki.getGroup(op.param1)
                ki.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ki.updateGroup(G)
                Ticket = ki.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                ki.updateGroup(G)
                wait["blacklist"][op.param2] = True
                
            if op.param3 in Amid:
              if op.param2 in Bmid:
                G = kk.getGroup(op.param1)
                G.preventJoinByTicket = False
                kk.updateGroup(G)
                Ticket = kk.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                kk.updateGroup(G)
              else:
                G = kk.getGroup(op.param1)
                kk.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kk.updateGroup(G)
                Ticket = kk.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kk.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Bmid:
              if op.param2 in Cmid:
                G = kc.getGroup(op.param1)
                G.preventJoinByTicket = False
                kc.updateGroup(G)
                Ticket = kc.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                kc.updateGroup(G)
              else:
                G = kc.getGroup(op.param1)
                kc.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kc.updateGroup(G)
                Ticket = kc.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kc.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Cmid:
              if op.param2 in Dmid:
                G = ks.getGroup(op.param1)
                G.preventJoinByTicket = False
                ks.updateGroup(G)
                Ticket = ks.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ks.updateGroup(G)
              else:
                G = ks.getGroup(op.param1)
                ks.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ks.updateGroup(G)
                Ticket = ks.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                ks.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Dmid:
              if op.param2 in Emid:
                G = ka.getGroup(op.param1)
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = ka.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ka.updateGroup(G)
              else:
                G = ka.getGroup(op.param1)
                ka.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = ka.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                ka.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Emid:
              if op.param2 in Fmid:
                G = kb.getGroup(op.param1)
                G.preventJoinByTicket = False
                kb.updateGroup(G)
                Ticket = kb.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                kb.updateGroup(G)
              else:
                G = kb.getGroup(op.param1)
                kb.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kb.updateGroup(G)
                Ticket = kb.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kb.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Gmid:
              if op.param2 in Hmid:
                G = ku.getGroup(op.param1)
                G.preventJoinByTicket = False
                ku.updateGroup(G)
                Ticket = ku.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ku.updateGroup(G)
              else:
                G = ku.getGroup(op.param1)
                ku.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ku.updateGroup(G)
                Ticket = ku.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                ku.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Hmid:
              if op.param2 in Imid:
                G = ko.getGroup(op.param1)
                G.preventJoinByTicket = False
                ko.updateGroup(G)
                Ticket = ko.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ko.updateGroup(G)
              else:
                G = ko.getGroup(op.param1)
                ko.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ko.updateGroup(G)
                Ticket = ko.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                #cl.updateGroup(G)
                ko.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Imid:
              if op.param2 in mid:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
              else:
                G = cl.getGroup(op.param1)
                cl.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                #ke.updateGroup(G)
                #wait["blacklist"][op.param2] = True
          except:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            cl.inviteIntoGroup(op.param1,[op.param3])
#--------------------------------
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                              
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in [".help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in [".menu"]:
              if msg.from_ in owner:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif (".gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Aphrodite gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Aphrodite gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Athena gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Athena gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Hera gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Hera gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif ".kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "Aphrodite kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Athena kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Hera kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif ".invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Aphrodite invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Athena invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Athena invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("finvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif ".addadmin @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif ".remadmin @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif msg.text in [".adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Admin ⓡ҉ⓞ҉ⓨ҉ⓐ҉ⓛ҉ⓔ҉ ⓣ҉ⓔ҉ⓐ҉ⓜ҉ ⓑ҉ⓞ҉ⓣ҉||\n=====================\n"
                  for mi_d in admin:
                      mc += "♪♫" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------
    #-------------- Add Friends ------------
            elif ".addbot @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  gs = ka.getGroup(msg.to)
                  gs = kb.getGroup(msg.to)
                  gs = ke.getGroup(msg.to)
                  gs = ko.getGroup(msg.to)
                  gs = ku.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                        ka.findAndAddContactsByMid(target)
                        kb.findAndAddContactsByMid(target)
                        ko.findAndAddContactsByMid(target)
                        ke.findAndAddContactsByMid(target)
                        ku.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                  
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif ".allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.statusMessage = string
                    kb.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ku.getProfile()
                    profile.statusMessage = string
                    ku.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif ".myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
            elif ".spam: " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas :v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
    #-----------------=Selesai=------------------
            elif msg.text in [".bot?"]: #Ngirim Semua Kontak Bot
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kb.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ko.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ke.sendMessage(msg)
            elif msg.text in [".me"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ",".gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ",".allgift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in [".cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in [".botcancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in [".openqr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Terbuka ")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Aphrodite buka qr","Aphrodite open qr"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done ")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Athena buka qr","Athena open qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done ")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Hera open qr","Hera buka qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done ")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in [".closeqr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup ")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Aphrodite close qr","Aphrodite tutup qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done ")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Athena tutup qr","Athena close qr"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done ")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Hera tutup qr","Hera close qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done ")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif ".jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif ".ginfo" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif ".mymid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif ".midbot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                ka.sendText(msg.to,Emid)
                kb.sendText(msg.to,Fmid)
                ko.sendText(msg.to,Gmid)
                ke.sendText(msg.to,Hmid)
                ku.sendText(msg.to,Imid)

            elif msg.text in [".tl: "]:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            
            elif msg.text in [".mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            
            elif msg.text in [".cancelon"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in [".canceloff"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in [".qron"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in [".qroff"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in [".contacton"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in [".contactoff"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³",".joinon","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•",".joinoff","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in [".gcanc:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³",".leaveon","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•",".leaveoff","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³",".shareon"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•",".shareoff"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in [".status",".set"]:
              if msg.from_ in admin:
                md = "⭐Status Proteksi⭐\n*============*\n"
                if wait["Protectgr"] == True: md+="[•]Protect QR [On]\n"
                else: md+="[•]Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="[•]Protect Invite [On]\n"
                else: md+="[•]Protect Invite [Off]\n"
                if wait["contact"] == True: md+="[•]Contact [On]\n"
                else: md+="[•]Contact [Off]\n"
                if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
                else: md +="[•]Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="[•]Auto Leave [On]\n"
                else: md+=" Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="[•]Share [On]\n"
                else:md+="[•]Share [Off]\n"
                if wait["autoAdd"] == True: md+="[•]Auto Add [On]\n"
                else:md+="[•]Auto Add [Off]\n"
                if wait["commentOn"] == True: md+="[•]Comment [On]\n"
                else:md+="[•]Comment [Off]\n*============*\n⭐ⓡ҉ⓞ҉ⓨ҉ⓐ҉ⓛ҉ⓔ҉ ⓣ҉ⓔ҉ⓐ҉ⓜ҉ ⓑ҉ⓞ҉ⓣ҉⭐\n*============*"
                cl.sendText(msg.to,md)
            elif ".album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif ".album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif ".album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in [".gid"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in [".cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif ".album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³",".addon","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•",".addoff","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            
#---------------------Sc invite owner ke group------
            elif ".invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace(".invitemeto: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalam grup itu")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³",".commenton","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•",".commentoff","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in [".comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in [".gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
            
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in [".jamon"]:
              if msg.from_ in admin:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in [".jamoff"]:
              if msg.from_ in admin:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in [".cclock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in [".jamupdate"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == ".setread":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Cek CCTV")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == ".cctv":
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "||Readers||%s\n||ROYALE TEAM PROTECTOR||\n\n>♪♫•*¨*•.¸¸ ⓒⓒⓣⓥ ¸¸.•*¨*•♫♪<\n%s۰۪۫ⓒ۪۫۰۰۪۫ⓒ۪۫۰۰۪۫ⓣ۪۫۰۰۪۫ⓥ۪۫۰\nKamu Termasuk yang mana?\n•Ga ngerti yang diobrolin\n•Ga kenal\n•Sombong\n•Cemburu\n•Sakit Hati\n\n[̲̲̅̅ⓗ̲̅ⓐ̲̅ⓗ̲̅ⓐ̲̅ⓗ̲̅ⓐ̲̅]\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik .setread dulu\nBaru Ketik .cctv\n۪ⓡ۫۰۪ⓞ۫۰۪ⓨ۫۰۪ⓐ۫۰۪ⓛ۫۰۪ⓔ۫۰ ۪ⓣ۫۰۪ⓔ۫۰۪ⓐ۫۰۪ⓜ۫۰ ۪ⓑ۫۰۪ⓞ۫۰۪ⓣ۫۰")
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in [".masukgaes"]:
              if msg.from_ in owner:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Semua Sudah Lengkap"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
  
            elif msg.text in [".comein"]:
              if msg.from_ in owner:
                        G = satpam.getGroup(msg.to)
                        ginfo = satpam.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        satpam.updateGroup(G)
                        invsend = 0
                        Ticket = satpam.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = satpam.getGroup(msg.to)
                        ginfo = satpam.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        satpam.updateGroup(G)
                        print "Semua Sudah Lengkap"
                        G.preventJoinByTicket(G)
                        satpam.updateGroup(G)

            
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in [".comeout"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in [".keluar"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        #cl.leaveGroup(msg.to)
                    except:
                        pass
                      
            
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in [".tagall"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
            elif msg.text in [".botlike"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in [".likefr"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in [".kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks,ka,kb,ku,ke,ko]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif ".vaccum" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    random.choice(KAC).sendText(msg.to,"maaf kalo gak sopan")
                    random.choice(KAC).sendText(msg.to,"makasih semuanya..")
                    random.choice(KAC).sendText(msg.to,"Group Cleaner")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    random.choice(KAC).sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KAC).sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in admin and Bots:
                            try:
                                klist=[cl,ki,kk,kc,ks,ka,kb,ku,ke,ko]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                random.choice(KAC).sendText(msg.to,"Sorry Bro")
                                random.choice(KAC).sendText(msg.to,"Sorry Sis")
                                random.choice(KAC).sendText(msg.to,"No Baper")

        #----------------Fungsi Kick User Target Start----------------------#
            elif ".nk " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace(".nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                satpam.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                   sendMessage(msg.to,"user does not exist")
                   pass
                else:
                   for target in targets:
                      try:
                        satpam.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        satpam.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif ".blacklist @ " in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes ")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif ".banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif ".mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif ".unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in [".up"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
		cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
		cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
		cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
		cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
		cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
		cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
		cl.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ko.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
                ku.sendText(msg.to,"SPAM 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif ".bc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in owner:
                 bctxt = msg.text.replace("Bc ","")
                 a = cl.getGroupIdsJoined()
                 a = ki.getGroupIdsJoined()
                 a = kk.getGroupIdsJoined()
                 a = kc.getGroupIdsJoined()
                 a = ks.getGroupIdsJoined()
                 a = ka.getGroupIdsJoined()
                 a = ku.getGroupIdsJoined()
                 a = ke.getGroupIdsJoined()
                 a = ko.getGroupIdsJoined()
                 a = kb.getGroupIdsJoined()
                 for taf in a:
                     cl.sendText(taf, (bctxt))
                     ki.sendText(taf, (bctxt))
                     kk.sendText(taf, (bctxt))
                     kc.sendText(taf, (bctxt))
                     ks.sendText(taf, (bctxt))
                     ka.sendText(taf, (bctxt))
                     kb.sendText(taf, (bctxt))
                     ke.sendText(taf, (bctxt))
                     ku.sendText(taf, (bctxt))
                     ko.sendText(taf, (bctxt))
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in [".lg"]: #Melihat List Group
              if msg.from_ in admin:
                 gids = cl.getGroupIdsJoined()
                 h = ""
                 for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                 cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in [".lg2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in [".allout"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in owner:
                 gid = cl.getGroupIdsJoined()
                 gid = ki.getGroupIdsJoined()
                 gid = kk.getGroupIdsJoined()
                 gid = kc.getGroupIdsJoined()
                 gid = ks.getGroupIdsJoined()
                 gid = ka.getGroupIdsJoined()
                 gid = kb.getGroupIdsJoined()
                 gid = ko.getGroupIdsJoined()
                 gid = ke.getGroupIdsJoined()
                 gid = ku.getGroupIdsJoined()
                 for i in gid:
                   ku.leaveGroup(i)
                   ke.leaveGroup(i)
                   ko.leaveGroup(i)
                   kb.leaveGroup(i)
                   ka.leaveGroup(i)
                   ks.leaveGroup(i)
                   kc.leaveGroup(i)
                   ki.leaveGroup(i)
                   kk.leaveGroup(i)
                   cl.leaveGroup(i)
                 if wait["lang"] == "JP":
                   cl.sendText(msg.to,"Sayonara")
                 else:
                   cl.sendText(msg.to,"He declined all invitations")
 #------------------------End---------------------

            
       #-------------Fungsi Respon Start---------------------#
            elif msg.text in [".respon"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"⭐⭐⭐")
                ki.sendText(msg.to,"⭐⭐⭐⭐")
                kk.sendText(msg.to,"⭐⭐⭐⭐⭐")
                kc.sendText(msg.to,"⭐⭐⭐⭐⭐⭐")
                ks.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐")
                ka.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐⭐")
                kb.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                ko.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                ke.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                ku.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                cl.sendText(msg.to,"Completed 100%\nSiap Protect Group\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
      #-------------Fungsi Respon Finish---------------------#
                            

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in [".sp",".speed"]:
              if msg.from_ in admin and owner:
                start = time.time()
                cl.sendText(msg.to, "Sabar ...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in [".ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
            elif msg.text in [".unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in [".creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'u08810e0d9afa004ff8d0de22fdb49b69'}
              cl.sendText(msg.to,"======================")
              cl.sendMessage(msg)
              cl.sendText(msg.to,"======================")
              cl.sendText(msg.to,"ஜ۩۞۩ஜ [̲̅ⓞ̲][̲̅ⓤ̲][̲̅ⓡ̲] [̲̅ⓑ̲][̲̅ⓞ̲][̲̅ⓢ̲][̲̅ⓢ̲] ஜ۩۞۩ஜ")
                
      #-------------Fungsi Chat ----------------
            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Kupret Lu','Muka Lu Kaya Jamban','Ada Orang kah disini?','Sange Euy','Ada Perawan Nganggur ga Coy?']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in [".banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in [".cekban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in [".killban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in [".clear"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif ".random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif ".albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif ".fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n♦" + Name
                wait2['ROM'][op.param1][op.param2] = "♦" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
        if op.type == 17:
           if op.param2 in Bots:
              return
           ginfo = cl.getGroup(op.param1)
           random.choice(KAC).sendText(op.param1, "Welcome to " + str(ginfo.name))
           random.choice(KAC).sendText(op.param1, "Founder " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
           random.choice(KAC).sendText(op.param1,"Budayakan Baca Note !!! 😊\nSemoga Betah 😘")
           print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
           if op.param2 in Bots:
              return
           random.choice(KAC).sendText(op.param1, "Kasihan ga dapat tikungan disini hahaha ")
           print "MEMBER HAS LEFT THE GROUP"
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          satpam.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          satpam.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"[̲̅ⓐ̲][̲̅ⓤ̲][̲̅ⓣ̲][̲̅ⓞ̲][̲̅ⓛ̲][̲̅ⓘ̲][̲̅ⓚ̲][̲̅ⓔ̲] \n\n[̲̅ⓑ̲][̲̅ⓨ̲] [̲̅ⓡ̲][̲̅ⓞ̲][̲̅ⓨ̲][̲̅ⓐ̲][̲̅ⓛ̲][̲̅ⓔ̲] [̲̅ⓣ̲][̲̅ⓔ̲][̲̅ⓐ̲][̲̅ⓜ̲] [̲̅ⓟ̲][̲̅ⓡ̲][̲̅ⓞ̲][̲̅ⓣ̲][̲̅ⓔ̲][̲̅ⓒ̲][̲̅ⓣ̲][̲̅ⓞ̲][̲̅ⓡ̲]")
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kb.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ku.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ke.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ko.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\n\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"¸¸♬·¯·♩¸¸♪·¯·♫¸¸ ⓐ҉ⓤ҉ⓣ҉ⓞ҉ⓛ҉ⓘ҉ⓚ҉ⓔ҉ ¸¸♫·¯·♪¸¸♩·¯·♬¸¸\nŘØ¥ΔŁ€ Ŧ€ΔΜ ƤŘØŦ€ĆŦØŘ")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like "
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
                
                profile11 = satpam.getProfile()
                profile11.displayName = wait["cName11"]
                satpam.updateProfile(profile11)
                
                profile12 = k1.getProfile()
                profile12.displayName = wait["cName12"]
                k1.updateProfile(profile12)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
