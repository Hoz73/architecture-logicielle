from multiprocessing import Process, Value, Array
from threading import Thread, Event
from time import sleep
import math
import json

from espaceDeTuples import espaceDeTuples
from bcolors import bcolors
from agent import *

delai = 15

tabAgent = list()

cartes = [1, 2, 3, 4, 5, 6]


def initialisationAutorisationTuple(ts):
    for batiment in data["batiments"]:
        for badgeuse in batiment['informations']['badgeuses']:
            for carte in badgeuse["cartes"]:
                ts.OUT(("autorisationCarte", badgeuse["entree"], carte['id'], carte["autorise"]))
                ts.OUT(("autorisationCarte", badgeuse["sortie"], carte['id'], carte["autorise"]))


def lancementAgents(tab):
    for agent in tab:
        agent.start()


def initialisationAgentBadgeuse(tsBatiment, tsAutorisation, tsPersonne, tabBadgeuse):
    res = []

    for badgeuse in tabBadgeuse:
        agentVerifCarte = Thread(target=verifCarte, args=(tsBatiment, tsAutorisation, badgeuse["id"]), daemon=True)
        agentScanCarte = Thread(target=scanCarte,
                                args=(tsBatiment, badgeuse["id"], "batiment" if badgeuse["batiment"] else "salle"),
                                daemon=True)
        agentLumiereVerte = Thread(target=lumiereVerte, args=(tsBatiment, badgeuse["id"]), daemon=True)
        agentLumiereRouge = Thread(target=lumiereRouge, args=(tsBatiment, badgeuse["id"]), daemon=True)
        agentDetectionPassage = Thread(target=detectionPassage, args=(tsBatiment, tsPersonne, badgeuse["id"]),daemon=True)
        agentAlarme = Thread(target=declencheAlarme, args=[tsBatiment], daemon=True)

        tsBatiment.OUT(("nbPersonnesPassees", badgeuse["id"], 0))

        res.append(agentVerifCarte)
        res.append(agentScanCarte)
        res.append(agentLumiereVerte)
        res.append(agentLumiereRouge)
        res.append(agentDetectionPassage)
        res.append(agentAlarme)

    return res
    # agents =    [agentVerifCarte,agentScanCarte,
    #             agentLumiereVerte,agentLumiereRouge,agentDetectionPassage,
    #             ]  


def start(tsBatiment, idBadgeuse, carte):
    agentLecteurCarte = Thread(target=lecteurCarte, args=(tsBatiment, idBadgeuse, carte), daemon=True)
    agentLecteurCarte.start()


def test():
    tupleSpaces = list()

    badgeuseTest = data['batiments'][0]['informations']['badgeuses'][0]['entree']
    badgeuseTest2 = data['batiments'][1]['informations']['badgeuses'][0]['entree']
    badgeuseTest3 = data['batiments'][2]['informations']['badgeuses'][0]['entree']
    carteTest1 = cartes[0]
    carteTest2 = cartes[1]


    initialisationAutorisationTuple(tsAutorisation)

    # agentLecteurCarte = Thread(target=lecteurCarte, args=(tsBatiment, badgeuseTest, carteTest1), daemon=True)
    # tsPersonne.OUT(("personnePresente", 1, 11, "batiment"))
    # personnesPresentes(tsPersonne)
    tabBadgeuse = allBadgeuse()
    agents = initialisationAgentBadgeuse(tsBatiment, tsAutorisation, tsPersonne, tabBadgeuse)

    agentLecteurCarte = Thread(target=lecteurCarte, args=(tsBatiment, badgeuseTest, cartes[0]), daemon=True)
    agentLecteurCarte.start()
    lancementAgents(agents)
    # agentAlarme = Thread(target=declencheAlarme, args=[tsBatiment], daemon=True)
    # agentVerifCarte = Thread(target=verifCarte, args=(tsBatiment, tsAutorisation,badgeuseTest), daemon=True)
    # agentScanCarte = Thread(target=scanCarte, args=(tsBatiment,badgeuseTest,"batiment"), daemon=True)
    # agentLumiereVerte = Thread(target=lumiereVerte, args=(tsBatiment,badgeuseTest), daemon=True)
    # agentLumiereRouge = Thread(target=lumiereRouge, args=(tsBatiment,badgeuseTest), daemon=True)
    # agentDetectionPassage = Thread(target=detectionPassage, args=(tsBatiment, tsPersonne,badgeuseTest), daemon=True)
    # agents = [agentLecteurCarte,agentAlarme]


def allBadgeuse():
    badgeuses = []
    for batiment in data['batiments']:
        for badgeuse in batiment['informations']['badgeuses']:
            badgeuses.append({
                "id": badgeuse["entree"],
                "batiment": badgeuse["batiment"]
            })
            badgeuses.append({
                "id": badgeuse["sortie"],
                "batiment": badgeuse["batiment"]
            })
    return badgeuses

tsPersonne = espaceDeTuples()
tsBatiment = espaceDeTuples()
tsAutorisation = espaceDeTuples()

def iniatilisationAgent():
    initialisationAutorisationTuple(tsAutorisation)

    tabBadgeuse = allBadgeuse()

    agents = initialisationAgentBadgeuse(tsBatiment, tsAutorisation, tsPersonne, tabBadgeuse)

    lancementAgents(agents)

    # TODO : Lancement fenetre Nico


def personnesPresentes(tsPersonne):
    f = open("personnePresente.txt", "w")
    i = 1
    for personne in tsPersonne.listeTuples:
        res = []
        res.append(personne[1])
        res.append(personne[2])
        res.append(personne[3])
        f.write(str(i) + " -  nom : " + str(data["cartes"][str(res[0])] ) +", id badgeuse : " + str(res[1]) + ", type badgeuse : " + str(res[2]))
        i += 1
    f.close()

def videFichiers():
    f1 = open("personnePresente.txt", "w")
    f2 = open("logPassage.txt", "w")
    f1.write('')
    f2.write('')
    f1.close()
    f2.close()

def main():
    videFichiers()
    test()
    #iniatilisationAgent()

    while (True):
        print("while loop")
        sleep(1)
        

if __name__ == '__main__':
    with open('config.json') as json_file:
        global data
        data = json.load(json_file)
    main()
