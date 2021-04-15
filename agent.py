import json
from bcolors import bcolors
from tp import delai
from time import sleep
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


def scanCarte(ts, idBadgeuse, typeBadgeuse):
    idCarte = ts.IN(("cartePosee", idBadgeuse, -1), [2])[0]
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
    etatColor = Color.GREEN
    print(bcolors.OK + "Accès autorisée" + bcolors.RESET)
    sec = delai
    while (sec > 0):
        sleep(1)
        print(bcolors.WARNING + str(sec - 1) + " temps restant pour passer la porte " + bcolors.RESET)
        sec -= 1
    etatColor = Color.OFF
    print(bcolors.FAIL + "Porte fermée" + bcolors.RESET)


def lumiereRouge(ts, idBadgeuse):
    ts.IN(("lumiereRouge", idBadgeuse), [])
    etatColor = Color.RED
    print(bcolors.FAIL + "Accès non-autorisée" + bcolors.RESET)
    sleep(3)
    etatColor = Color.OFF


def detectionPassage(ts, tsPersonne, idBadgeuse):
    res = ts.IN(("detectionPassage", idBadgeuse, -1, ""), [2, 3])
    idCarte = res[0]
    typeBadgeuse = res[1]
    sec = delai
    nbPersonne = 0
    while (sec > 0):
        sleep(1)
        passage = ts.INUNBLOCKED(("capteurPassage", idBadgeuse), [])
        if passage is None:
            nbPersonnes = ts.RD(("nbPersonnesPassees", idBadgeuse, -1), [2])[0]
            ts.ADD(("nbPersonnesPassees", idBadgeuse, nbPersonnes + 1), [2])
        sec -= 1
    nbPersonnesPassees = ts.RD(("nbPersonnesPassees", idBadgeuse, -1), [2])[0]
    if nbPersonnesPassees > 1:
        print("if")
        print(nbPersonnesPassees)
        ts.OUT(("declencheAlarme", idBadgeuse, typeBadgeuse))
        ts.ADD(("nbPersonnesPassees", idBadgeuse, 0), [2])
        detectionPassage(ts, tsPersonne, idBadgeuse)
    elif nbPersonnesPassees == 1:
        if (idBadgeuse % 2) == 0:
            print("badgeuse entrée")
            tsPersonne.OUT(("personnePresente", idCarte, idBadgeuse, typeBadgeuse))
        else:
            print("badgeuse sortie")
            tsPersonne.IN(("personnePresente", idCarte, idBadgeuse, typeBadgeuse))
        print("elif")
        print(nbPersonnesPassees)
        ts.ADD(("nbPersonnesPassees", idBadgeuse, 0), [2])
        detectionPassage(ts, tsPersonne, idBadgeuse)
    else:
        print("else")
        print(nbPersonnesPassees)
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
                            print(bcolors.FAIL + "alerte déclenchée à la sortie du batiment : " + batiment[
                                "name"] + ", porte : " + badgeuse["name"] + bcolors.RESET)
                        else:
                            print(bcolors.FAIL + "alerte déclenchée à l'entree du batiment : " + batiment[
                                "name"] + ", porte : " + badgeuse["name"] + bcolors.RESET)
    else:
        for batiment in data["batiments"]:
            for badgeuse in batiment["informations"]["badgeuses"]:
                if not badgeuse["batiment"]:
                    if idBadgeuse == badgeuse["sortie"] or idBadgeuse == badgeuse["entree"]:
                        if badgeuse["sortie"] == idBadgeuse:
                            print(bcolors.FAIL + "alerte déclenchée à la sortie de la salle : " + badgeuse[
                                "name"] + bcolors.RESET)
                        else:
                            print(bcolors.FAIL + "alerte déclenchée à l'entree de la salle : " + badgeuse[
                                "name"] + bcolors.RESET)
    sleep(5)
    etatColor = Color.OFF
