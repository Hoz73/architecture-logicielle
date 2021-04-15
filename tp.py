from multiprocessing import Process, Value, Array
from threading import Thread, Event
from time import sleep
import math


data = {
    "batiments" :
        [
            {
                "name": "8A", 
                "informations" : {
                    "badgeuses" : 
                    [
                        {"name": "est"  , "entree" : 11, "sortie" : 12, "batiment": True,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name": "ouest" , "entree" : 13, "sortie" : 14, "batiment": True,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "8A-42", "entree" : 11, "sortie" : 12, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "8A-43", "entree" : 13, "sortie" : 14, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "8A-44", "entree" : 15, "sortie" : 16, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "8A-45", "entree" : 17, "sortie" : 18, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                    ],
                },
            },
            {
                "name" : "4A",
                "informations" : {
                    "badgeuses" : 
                    [
                        {"name" : "4A-42", "entree" : 21, "sortie" : 22, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":True},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "4A-43", "entree" : 23, "sortie" : 24, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":True},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":True},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "A4-44", "entree" : 25, "sortie" : 26, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "A4-45", "entree" : 27, "sortie" : 28, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "nord",  "entree" : 21, "sortie" : 22, "batiment": True,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":True},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "sud" ,  "entree" : 23, "sortie" : 24, "batiment": True,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":True},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        }
                    ],
                }
            },

            {
                "name":"10B",
                "informations":
                {
                    "badgeuses" : 
                    [
                        {"name" : "10B-42", "entree" : 31, "sortie" : 32, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":True},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":True},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "10B-43", "entree" : 33, "sortie" : 34, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":True},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":True},
                        ]
                        },
                        {"name" : "10B-44", "entree" : 35, "sortie" : 36, "batiment": False,"cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":False},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":True},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "10B-45", "entree" : 37, "sortie" : 38, "batiment": False,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":True},
                            {"id" : 3, "autorise":False},
                            {"id" : 4, "autorise":False},
                            {"id" : 5, "autorise":False},
                            {"id" : 6, "autorise":False},
                        ]
                        },
                        {"name" : "sud" ,   "entree" : 31, "sortie" : 32, "batiment": True,
                        "cartes":
                        [
                            {"id"  : 1, "autorise":True},
                            {"id" : 2, "autorise":True},
                            {"id" : 3, "autorise":True},
                            {"id" : 4, "autorise":True},
                            {"id" : 5, "autorise":True},
                            {"id" : 6, "autorise":True},
                        ]
                        },
                        {"name" : "nord",   "entree" : 33, "sortie" : 34, "batiment": True,
                        "cartes":
                        [
                            {"id" : 1, "autorise":True},
                            {"id" : 2, "autorise":True},
                            {"id" : 3, "autorise":True},
                            {"id" : 4, "autorise":True},
                            {"id" : 5, "autorise":True},
                            {"id" : 6, "autorise":True},
                        ]
                        }
                    ],
                }
            }            
        ]     
}

delai = 15

tabAgent = list()


cartes = [1,2,3]

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class espaceDeTuples():
    def OUT(self,element):
        self.listeTuples.append(element)

    def IN(self,element,tab):
        resTemp = self.existe(element,tab)
        res = list()
        for index in tab:
            res.append(resTemp[index])
        self.listeTuples.remove(resTemp)
        return res

    def RD(self, element, tab):
        resTemp = self.existe(element,tab)
        res = list()
        for index in tab:
            res.append(resTemp[index])
        return res

    def ADD(self, element, tab):
        resTemp = self.existe(element,tab)
        index = self.listeTuples.index(resTemp)
        listTuple = list(self.listeTuples[index])
        for i in tab:
            listTuple[i] = element[i]
        self.listeTuples[index] = tuple(listTuple)

    def INUNBLOCKED(self,element,tab):
        resTemp = self.existeNonBloquant(element,tab)
        if None == resTemp:
            # res = list()
            # for index in tab:
            #     res.append(element[index])
            # return res
            return None
        res = list()
        for index in tab:
            res.append(resTemp[index])
        self.listeTuples.remove(resTemp)
        return res


    def existe(self, template, tab):
        tuplePossible = []
        while(True):
            for tupleI in self.listeTuples:
                flag = True
                if len(tupleI) == len(template):
                    for i in range(len(template)):
                        if type(template[i]) != type(tupleI[i]):
                            flag = False
                    if flag:
                        tuplePossible.append(tupleI)
            for tupleI in tuplePossible:
                allIndex = list(range(len(tupleI)))
                for i in tab:
                    for j in allIndex:
                        if i == j:
                            allIndex.remove(j)
                flag = True
                for i in allIndex:
                    if template[i] != tupleI[i]:
                        flag = False
                if flag :
                    return tupleI
    
    def existeNonBloquant(self, template, tab):
        tuplePossible = []
        for tupleI in self.listeTuples:
            flag = True
            if len(tupleI) == len(template):
                for i in range(len(template)):
                    if type(template[i]) != type(tupleI[i]):
                        flag = False
                if flag:
                    tuplePossible.append(tupleI)
            for tupleI in tuplePossible:
                allIndex = list(range(len(tupleI)))
                for i in tab:
                    for j in allIndex:
                        if i == j:
                            allIndex.remove(j)
                flag = True
                for i in allIndex:
                    if template[i] != tupleI[i]:
                        flag = False
                if flag :
                    return tupleI

    def __init__(self):
        self.listeTuples= list()



def lecteurCarte(ts,idBadgeuse, idCarte):
    ts.OUT(("cartePosee", idBadgeuse, idCarte ))

#*******************************************************************

def verifCarte(tsBatiment, tsAutorisation, idBadgeuse):
    idCarte = tsBatiment.IN(("verifCarte", idBadgeuse, -1), [2])[0]
    res = tsAutorisation.RD(("autorisationCarte", idBadgeuse, idCarte, True), [3])[0]
    tsBatiment.OUT(("porteDebloquee", idBadgeuse, res))

#*******************************************************************

def scanCarte(ts, idBadgeuse, typeBadgeuse):
    idCarte = ts.IN(("cartePosee",idBadgeuse, -1 ), [2])[0]
    ts.OUT(("verifCarte", idBadgeuse, idCarte))
    res = ts.IN(("porteDebloquee", idBadgeuse, True ), [2])[0]
    if(res):
        ts.OUT(("lumiereVerte", idBadgeuse))
        ts.OUT(("detectionPassage", idBadgeuse, idCarte, typeBadgeuse))
        scanCarte(ts, idBadgeuse, typeBadgeuse)
    else:
        ts.OUT(("lumiereRouge", idBadgeuse))
        scanCarte(ts, idBadgeuse, typeBadgeuse)

#*******************************************************************

def lumiereVerte(ts, idBadgeuse):
    ts.IN(("lumiereVerte", idBadgeuse),[])
    ts.OUT((""))
    print(bcolors.OK + "Accès autorisée" + bcolors.RESET)
    sec = delai
    while(sec > 0):
        sleep(1)
        print(bcolors.WARNING + str(sec - 1) + " temps restant pour passer la porte " + bcolors.RESET)
        sec -= 1
    print(bcolors.FAIL + "Porte fermée" + bcolors.RESET)

#*******************************************************************

def lumiereRouge(ts, idBadgeuse):
    ts.IN(("lumiereRouge", idBadgeuse),[])
    print(bcolors.FAIL + "Accès non-autorisée" + bcolors.RESET)

#*******************************************************************

def detectionPassage(ts, tsPersonne, idBadgeuse):
    res = ts.IN(("detectionPassage", idBadgeuse, -1, ""),[2,3])
    idCarte = res[0]
    typeBadgeuse = res[1]
    sec = delai
    nbPersonne = 0
    while (sec > 0):
        if((sec % 4) == 0):
            print("sec : hoey "+ str(sec))
            ts.OUT(("capteurPassage", idBadgeuse))
        sleep(1)
        passage = ts.INUNBLOCKED(("capteurPassage", idBadgeuse),[])
        if(not None == passage):
            nbPersonnes = ts.RD(("nbPersonnesPassees", idBadgeuse, -1),[2])[0]
            ts.ADD(("nbPersonnesPassees", idBadgeuse, nbPersonnes+1),[2])
        sec -=1
    nbPersonnesPassees = ts.RD(("nbPersonnesPassees", idBadgeuse, -1),[2])[0]
    if nbPersonnesPassees > 1:
        print("if")
        print(nbPersonnesPassees)
        ts.OUT(("declencheAlarme", idBadgeuse, typeBadgeuse))
        ts.ADD(("nbPersonnesPassees", idBadgeuse, 0),[2])
        detectionPassage(ts, tsPersonne, idBadgeuse)
    elif nbPersonnesPassees == 1:
        if (idBadgeuse % 2) == 0:
            print("badgeuse entrée")
            tsPersonne.OUT(("personnePresente",idCarte,idBadgeuse,typeBadgeuse))
        else:
            print("badgeuse sortie")
            tsPersonne.IN(("personnePresente", idCarte, idBadgeuse, typeBadgeuse))
        print("elif")
        print(nbPersonnesPassees)
        ts.ADD(("nbPersonnesPassees", idBadgeuse, 0),[2])
        detectionPassage(ts, tsPersonne, idBadgeuse)   
    else :
        print("else")
        print(nbPersonnesPassees)
        ts.ADD(("nbPersonnesPassees", idBadgeuse, 0),[2])
        detectionPassage(ts, tsPersonne, idBadgeuse)
    
    
        
#*******************************************************************


def declencheAlarme(ts):
    res = ts.IN(("declencheAlarme", -1, ""),[1,2])
    print(res)
    idBadgeuse = res[0]
    typeBadgeuse = res[1]

    if typeBadgeuse == "batiment" :
        for batiment in data["batiments"]:
            for badgeuse in batiment["informations"]["badgeuses"]:
                if badgeuse["batiment"]: 
                    if idBadgeuse == badgeuse["sortie"] or idBadgeuse == badgeuse["entree"]:
                        if badgeuse["sortie"] == idBadgeuse:
                            print(bcolors.FAIL + "alerte déclenchée à la sortie du batiment : "+ batiment["name"] +", porte : " + badgeuse["name"] + bcolors.RESET)
                        else:
                            print(bcolors.FAIL + "alerte déclenchée à l'entree du batiment : "+ batiment["name"] +", porte : " + badgeuse["name"] + bcolors.RESET)

    # if typeBadgeuse == "batiment":
    #     for e in batiments_badgeuses:
    #         for i in range(len(e)):
    #             if idBadgeuse == e[i]:
    #                 batiment = e[0]
    #                 if idBadgeuse % 2 == 0:
    #                     print(bcolors.FAIL + "alerte déclenchée à la sortie du batiment : "+batiment+", porte numéro : " + str(math.ceil((idBadgeuse % 10)/2)) + bcolors.RESET)
    #                 else:
    #                     print(bcolors.FAIL + "alerte déclenchée à l'entree du batiment : "+batiment+", porte numéro : " + str(math.ceil((idBadgeuse % 10)/2)) + bcolors.RESET)
    else:
        for e in data["batiments"]:
            for badgeuse in batiment["informations"]["badgeuses"]:
                if not badgeuse["batiment"]:
                    if idBadgeuse == badgeuse["sortie"] or idBadgeuse == badgeuse["entree"]:
                        if badgeuse["sortie"] == idBadgeuse:
                            print(bcolors.FAIL + "alerte déclenchée à la sortie de la salle : "+ badgeuse["name"] + bcolors.RESET)
                        else:
                            print(bcolors.FAIL + "alerte déclenchée à l'entree de la salle : "+badgeuse["name"]+ bcolors.RESET)

def switchCarte(argument):
    switcher = {
        cartes[0]: cartes[0],
        cartes[1]: cartes[1],
        cartes[2]: cartes[2]
    }
    return (switcher.get(argument, -1))

def switchBatiment(argument):
    switcher = {
        batiments[0] : batiments[0],
        batiments[1] : batiments[1],
        batiments[2] : batiments[2]
    }
    return (switcher.get(argument, str(-1)))

def switchPorte(argument):
    switcher = {
        "1": 1,
        "2": 2
    }
    return (switcher.get(argument, -1))

def switchSalle(argument):
    switcher = {
        salles[0]: salles[0],
        salles[1]: salles[1],
        salles[2]: salles[2],
        salles[3]: salles[3],
    }
    return (switcher.get(argument, str(-1)))

def menu():
    res = False
    print(cartes)
    choixCarte = input("choisissez votre carte : ")
    if(switchCarte(choixCarte) != -1):
        print(batiments)
        choixBatiment = input("choisissez dans quel batiment voulez vous entrer :")
        if(switchBatiment(choixBatiment) != "-1"):
            porte = ["1","2"]
            print("porte " + str(porte))
            choixPorte = input("par quelle porte ?")
            if(switchPorte(choixPorte) != -1):
                print(salles)
                choixSalle = input("dans quelle salle ?")
                if(switchSalle(choixSalle)):
                    res = True
                else:
                    print("salle invalide")
            else:
                print("porte invalide")
        else:
            print("batiment invalide")
    else:
        print("carte invalide")
    return res

def initialisationAutorisationTuple(ts):
    for batiment in data["batiments"]:
        for badgeuse in batiment['informations']['badgeuses']:
            for carte in badgeuse["cartes"]:
                ts.OUT(("autorisationCarte",badgeuse["entree"], carte['id'], carte["autorise"]))
                ts.OUT(("autorisationCarte",badgeuse["sortie"], carte['id'], carte["autorise"]))

def lancementAgents(tab):
    for agent in tab:
        agent.start()

def initialisationAgentBadgeuse(tsBatiment, tsAutorisation, tsPersonne, tabBadgeuse):
    res =[]
    for idBadgeuse in tabBadgeuse:
        agentVerifCarte = Thread(target=verifCarte, args=(tsBatiment, tsAutorisation,idBadgeuse), daemon=True)
        agentScanCarte = Thread(target=scanCarte, args=(tsBatiment,idBadgeuse,"batiment"), daemon=True)
        agentLumiereVerte = Thread(target=lumiereVerte, args=(tsBatiment,idBadgeuse), daemon=True)
        agentLumiereRouge = Thread(target=lumiereRouge, args=(tsBatiment,idBadgeuse), daemon=True)
        agentDetectionPassage = Thread(target=detectionPassage, args=(tsBatiment, tsPersonne,idBadgeuse), daemon=True)
        agentAlarme = Thread(target=declencheAlarme, args=[tsBatiment], daemon=True)
        tsBatiment.OUT(("nbPersonnesPassees",idBadgeuse, 0))

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
    
def start(tsBatiment, idBadgeuse, sens, carte):
    agentLecteurCarte = Thread(target=lecteurCarte, args=(tsBatiment, idBadgeuse, carte), daemon=True)
    agentLecteurCarte.start()

def initialisationAgent():
    tupleSpaces = list()

    badgeuseTest = data['batiments'][0]['informations']['badgeuses'][0]['entree']
    badgeuseTest2 = data['batiments'][1]['informations']['badgeuses'][0]['entree']
    badgeuseTest3 = data['batiments'][2]['informations']['badgeuses'][0]['entree']
    carteTest1 = cartes[0]
    carteTest2 =cartes[1]

    tsPersonne = espaceDeTuples()
    tsBatiment = espaceDeTuples()
    tsAutorisation = espaceDeTuples()
    
    tupleSpaces.append(tsPersonne)
    tupleSpaces.append(tsBatiment)
    tupleSpaces.append(tsAutorisation)

    initialisationAutorisationTuple(tsAutorisation)
    

    #agentLecteurCarte = Thread(target=lecteurCarte, args=(tsBatiment, badgeuseTest, carteTest1), daemon=True)

    tabBadgeuse = [badgeuseTest]
    agents = initialisationAgentBadgeuse(tsBatiment, tsAutorisation, tsPersonne, tabBadgeuse)
    
    agentLecteurCarte = Thread(target=lecteurCarte, args=(tsBatiment, badgeuseTest, cartes[0]), daemon=True)
    agentLecteurCarte.start()
    lancementAgents(agents)
    #agentAlarme = Thread(target=declencheAlarme, args=[tsBatiment], daemon=True)
    # agentVerifCarte = Thread(target=verifCarte, args=(tsBatiment, tsAutorisation,badgeuseTest), daemon=True)
    # agentScanCarte = Thread(target=scanCarte, args=(tsBatiment,badgeuseTest,"batiment"), daemon=True)
    # agentLumiereVerte = Thread(target=lumiereVerte, args=(tsBatiment,badgeuseTest), daemon=True)
    # agentLumiereRouge = Thread(target=lumiereRouge, args=(tsBatiment,badgeuseTest), daemon=True)
    # agentDetectionPassage = Thread(target=detectionPassage, args=(tsBatiment, tsPersonne,badgeuseTest), daemon=True)
    # agents = [agentLecteurCarte,agentAlarme]

def main():

    #menu()

    initialisationAgent()

    while(True):
        sleep(1)

if __name__ == '__main__':
    main()
    