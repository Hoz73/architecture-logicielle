import json
from bcolors import bcolors
from tp import delai
from time import sleep
from datetime import datetime
from enum import Enum


class Color(Enum):
    RED = 1
    ORANGE = 2
    GREEN = 3
    OFF = 4

etatColor = Color.OFF

with open('config.json') as json_file:
    global data
    data = json.load(json_file)


def lecteurCarte(ts, idBadgeuse, idCarte):
    ts.OUT(("cartePosee", idBadgeuse, idCarte))

def verifCarte(tsBatiment, tsAutorisation, idBadgeuse):
    idCarte = tsBatiment.IN(("verifCarte", idBadgeuse, -1), [2])[0]
    res = tsAutorisation.RD(("autorisationCarte", idBadgeuse, idCarte, True), [3])[0]
    tsBatiment.OUT(("porteDebloquee", idBadgeuse, res))
    verifCarte(tsBatiment, tsAutorisation, idBadgeuse)

def scanCarte(ts, idBadgeuse, typeBadgeuse):
    res = ts.IN(("cartePosee", idBadgeuse, -1), [2])
    idCarte = res[0]
    batiment = trouverBatiment(idBadgeuse,typeBadgeuse)
    ts.OUT(("verifCarte", idBadgeuse, idCarte))
    res = ts.IN(("porteDebloquee", idBadgeuse, True), [2])[0]
    if res:
        ts.OUT(("lumiereVerte", idBadgeuse))
        ts.OUT(("detectionPassage", idBadgeuse, idCarte, typeBadgeuse))
        scanCarte(ts, idBadgeuse, typeBadgeuse)
    else:
        ts.OUT(("lumiereRouge", idBadgeuse))
        scanCarte(ts, idBadgeuse, typeBadgeuse)

def lumiereVerte(ts, idBadgeuse):
    ts.IN(("lumiereVerte", idBadgeuse), [])
    ts.OUT(("turnOnLightGreen",0))
    etatColor = Color.GREEN
    print(bcolors.OK + "Accès autorisee" + bcolors.RESET)
    sec = delai
    while (sec > 0):
        sleep(1)
        print(bcolors.WARNING + str(sec - 1) + " temps restant pour passer la porte " + bcolors.RESET)
        sec -= 1
    etatColor = Color.OFF
    ts.OUT(("turnOffLightGreen",0))
    print(bcolors.FAIL + "Porte fermee" + bcolors.RESET)
    lumiereVerte(ts, idBadgeuse)

def lumiereRouge(ts, idBadgeuse):
    ts.IN(("lumiereRouge", idBadgeuse), [])
    ts.OUT(("turnOnLightRed",0))

    etatColor = Color.RED
    print(bcolors.FAIL + "Accès non-autorisee" + bcolors.RESET)
    sleep(3)
    etatColor = Color.OFF
    ts.OUT(("turnOffLightRed",0))
    lumiereRouge(ts, idBadgeuse)


def detectionPassage(ts, tsPersonne, idBadgeuse):
    res = ts.IN(("detectionPassage", idBadgeuse, -1, ""), [2, 3])
    idCarte = res[0]
    typeBadgeuse = res[1]
    batiment = trouverBatiment(idBadgeuse, typeBadgeuse)
    resType = typeBadgeuse == "batiment"
    
    ts.OUT(("actionPorte", batiment, idBadgeuse, resType))
    sec = delai
    nbPersonne = 0
    while (sec > 0):
        sleep(1)
        passage = ts.INUNBLOCKED(("capteurPassage", idBadgeuse), [])
        if  passage is not None:
            nbPersonnes = ts.RD(("nbPersonnesPassees", idBadgeuse, -1), [2])[0]
            ts.ADD(("nbPersonnesPassees", idBadgeuse, nbPersonnes + 1), [2])
        sec -= 1
    ts.OUT(("actionPorte", batiment, idBadgeuse, resType))
    nbPersonnesPassees = ts.RD(("nbPersonnesPassees", idBadgeuse, -1), [2])[0]
    if nbPersonnesPassees > 1:
        msg = data["cartes"][str(idCarte)] + " a declenche l'alarme a la badgeuse " + str(idBadgeuse)
        logAgent(msg)
        ts.OUT(("declencheAlarme", idBadgeuse, typeBadgeuse))
        ts.ADD(("nbPersonnesPassees", idBadgeuse, 0), [2])
        detectionPassage(ts, tsPersonne, idBadgeuse)
    elif nbPersonnesPassees == 1:
        if (idBadgeuse % 2) != 0:
            msg = data["cartes"][str(idCarte)] + " est entre via la badgeuse " + str(idBadgeuse) 
            logAgent(msg)
            tsPersonne.OUT(("personnePresente", idCarte, idBadgeuse, typeBadgeuse))
        else:
            msg = data["cartes"][str(idCarte)] + " est sortie via la badgeuse " + str(idBadgeuse)
            logAgent(msg)
            tsPersonne.IN(("personnePresente", idCarte, idBadgeuse, typeBadgeuse),[])
        ts.ADD(("nbPersonnesPassees", idBadgeuse, 0), [2])
        detectionPassage(ts, tsPersonne, idBadgeuse)
    else:
        msg = data["cartes"][str(idCarte)] + " a active la badgeuse " + str(idBadgeuse) + " mais personne n'est entree"
        logAgent(msg)
        ts.ADD(("nbPersonnesPassees", idBadgeuse, 0), [2])
        detectionPassage(ts, tsPersonne, idBadgeuse)

def declencheAlarme(ts):
    res = ts.IN(("declencheAlarme", -1, ""), [1, 2])

    idBadgeuse = res[0]
    typeBadgeuse = res[1]

    etatColor = Color.ORANGE
    if typeBadgeuse == "batiment":
        for batiment in data["batiments"]:
            for badgeuse in batiment["informations"]["badgeuses"]:
                if badgeuse["batiment"]:
                    if idBadgeuse == badgeuse["sortie"] or idBadgeuse == badgeuse["entree"]:
                        if badgeuse["sortie"] == idBadgeuse:
                            print(bcolors.FAIL + "alerte declenchee a la sortie du batiment : " + batiment[
                                "name"] + ", porte : " + badgeuse["name"] + bcolors.RESET)
                        else:
                            print(bcolors.FAIL + "alerte declenchee a l'entree du batiment : " + batiment[
                                "name"] + ", porte : " + badgeuse["name"] + bcolors.RESET)
    else:
        for batiment in data["batiments"]:
            for badgeuse in batiment["informations"]["badgeuses"]:
                if not badgeuse["batiment"]:
                    if idBadgeuse == badgeuse["sortie"] or idBadgeuse == badgeuse["entree"]:
                        if badgeuse["sortie"] == idBadgeuse:
                            print(bcolors.FAIL + "alerte declenchee a la sortie de la salle : " + badgeuse[
                                "name"] + bcolors.RESET)
                        else:
                            print(bcolors.FAIL + "alerte declenchee a l'entree de la salle : " + badgeuse[
                                "name"] + bcolors.RESET)
    sleep(5)
    etatColor = Color.OFF

def logAgent(msg):
    f = open("logPassage.txt", "a")
    f.write("< " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " > : " + msg + "\n")
    f.close()

    
def etatPorte(ts,batiment,etat):
    res = ts.IN(("actionPorte", batiment, -1, False),[1,2,3])
    for i in range(len(data["batiments"])) :
        if data["batiments"][i]["name"] == res[0]:
            for j in range(len((data["batiments"][i]["informations"]["badgeuses"]))):
                if (data["batiments"][i]["informations"]["badgeuses"][j]["entree"] == res[1] or data["batiments"][i]["informations"]["badgeuses"][j]["sortie"] == res[1]) and data["batiments"][i]["informations"]["badgeuses"][j]["batiment"] == res[2]:
                    data["batiments"][i]["informations"]["badgeuses"][j]["ouvert"] =  etat
                    etat = not etat
    etatPorte(ts,batiment, etat)

def incendie(ts,batiment, ):
    batiment = ts.IN(("incendie", batiment),[1])[0]
    for i in range(len(data["batiments"][batiment]["informations"]["badgeuses"])):
        data["batiments"][batiment]["informations"]["badgeuses"][i]["ouvert"] = True
    ts.OUT(("turnOnLightFire",0))
    print(data)


def trouverBatiment(idBadgeuse, typeBadgeuse):
    for bat in data["batiments"]:
        for badgeuse in bat["informations"]["badgeuses"]:
            if (badgeuse["batiment"] == typeBadgeuse or typeBadgeuse == "batiment") and (badgeuse["entree"] == idBadgeuse or badgeuse["sortie"] == idBadgeuse):
                return bat["name"]
    return None
            