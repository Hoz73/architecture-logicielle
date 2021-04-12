from multiprocessing import Process, Value, Array
from threading import Thread, Event
from time import sleep
import math

batiments = ["1","2","3"]

salles = ["info", "reseau", "geo", "math"]

badgeuses = [
    [11, 12, 13, 14],
    [21,22,23,24],
    [31,32,33,34],
    [41,42,43,44]
]

batiments_badgeuses = [
    [batiments[0],badgeuses[0][0],badgeuses[0][1],badgeuses[0][2],badgeuses[0][3]],
    [batiments[1],badgeuses[1][0],badgeuses[1][1],badgeuses[1][2],badgeuses[1][3]],
    [batiments[2],badgeuses[2][0],badgeuses[2][1],badgeuses[2][2],badgeuses[2][3]]
]

salles_badgeuses = [
    [salles[0],badgeuses[0][0],badgeuses[0][1]],
    [salles[1],badgeuses[1][0],badgeuses[1][1]],
    [salles[2],badgeuses[2][0],badgeuses[2][1]],
    [salles[3],badgeuses[3][0],badgeuses[3][1]]
]

cartes = [0,1,2]

carte_Batiments = [
    (cartes[0],batiments[0],batiments[1],batiments[2]),
    (cartes[1],batiments[0]),
    (cartes[2],batiments[0],batiments[0]),
]

carte_Salles = [
    (cartes[0],salles[0],salles[1],salles[2],salles[3]),
    (cartes[0],salles[0],salles[1],),
    (cartes[0],salles[0],salles[1],salles[2])
]

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
    print(bcolors.OK + "Accès autorisée" + bcolors.RESET)
    sec = 10
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

# def detectionPersonne(ts,tsPersonne, idBadgeuse):
#     global nbPersonne
#     while(True):
#         ts.IN(("capteurPassage", idBadgeuse),[])
#         tsPersonne.OUT(())
#         nbPersonne+=1
        
#         print("passage " + str(nbPersonne))

#*******************************************************************
def detectionPassage(ts, tsPersonne, idBadgeuse):
    res = ts.IN(("detectionPassage", idBadgeuse, -1, ""),[2,3])
    idCarte = res[0]
    typeBadgeuse = res[1]
    delai = 10
    nbPersonne = 0
    #processDetection = Thread(target=detectionPersonne, args=(ts, idBadgeuse), daemon=True)
    # processDetection.start()
    
    while (delai > 0):
        if((delai % 4) == 0):
            print("delai : hoey "+ str(delai))
            ts.OUT(("capteurPassage", idBadgeuse))
        sleep(1)
        passage = ts.INUNBLOCKED(("capteurPassage", idBadgeuse),[])
        if(not None == passage):
            nbPersonnes = ts.RD(("nbPersonnesPassees", idBadgeuse, -1),[2])[0]
            ts.ADD(("nbPersonnesPassees", idBadgeuse, nbPersonnes+1),[2])
        delai -=1
    # processDetection.join(0.0)
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
    if typeBadgeuse == "batiment":
        for e in batiments_badgeuses:
            for i in range(len(e)):
                if idBadgeuse == e[i]:
                    batiment = e[0]
                    if idBadgeuse % 2 == 0:
                        print(bcolors.FAIL + "alerte déclenchée à la sortie du batiment : "+batiment+", porte numéro : " + str(math.ceil((idBadgeuse % 10)/2)) + bcolors.RESET)
                    else:
                         print(bcolors.FAIL + "alerte déclenchée à l'entree du batiment : "+batiment+", porte numéro : " + str(math.ceil((idBadgeuse % 10)/2)) + bcolors.RESET)
    else:
        for e in salles_badgeuses:
            for i in range(len(e)):
                if idBadgeuse == e[i]:
                    salle = e[0]
                    if idBadgeuse % 2 == 0:
                        print(bcolors.FAIL + "alerte déclenchée à  la sortie de la salle : "+salle+", porte numéro : " + str(math.ceil((idBadgeuse % 10)/2)) + bcolors.RESET)
                    else:
                         print(bcolors.FAIL + "alerte déclenchée à l'entree de la salle : "+salle+", porte numéro : " + str(math.ceil((idBadgeuse % 10)/2)) + bcolors.RESET)


def main():
    #Création des espaces de tuples
    tupleSpaces = list()

    tsPersonne = espaceDeTuples()
    tsBatiment = espaceDeTuples()
    tsAutorisation = espaceDeTuples()
    
    tupleSpaces.append(tsPersonne)
    tupleSpaces.append(tsBatiment)
    tupleSpaces.append(tsAutorisation)

    badgeuseTest = badgeuses[1][1]
    carteTest1 = cartes[0]
    carteTest2 =cartes[1]

    #Ajout des cartes autorisées
    tsAutorisation.listeTuples.append(("autorisationCarte",badgeuseTest, carteTest1, True))
    tsAutorisation.listeTuples.append(("autorisationCarte",badgeuseTest, carteTest2, False))

    #nbPersonne dans les batiments
    tsBatiment.OUT(("nbPersonnesPassees",badgeuseTest, 0))

    #Création des agents
    agentLecteurCarte = Thread(target=lecteurCarte, args=(tsBatiment, badgeuseTest, cartes[0]), daemon=True)
    agentVerifCarte = Thread(target=verifCarte, args=(tsBatiment, tsAutorisation,badgeuseTest), daemon=True)
    agentScanCarte = Thread(target=scanCarte, args=(tsBatiment,badgeuseTest,"batiment"), daemon=True)
    agentLumiereVerte = Thread(target=lumiereVerte, args=(tsBatiment,badgeuseTest), daemon=True)
    agentLumiereRouge = Thread(target=lumiereRouge, args=(tsBatiment,badgeuseTest), daemon=True)
    agentDetectionPassage = Thread(target=detectionPassage, args=(tsBatiment, tsPersonne,badgeuseTest), daemon=True)
    agentAlarme = Thread(target=declencheAlarme, args=[tsBatiment], daemon=True)
    
    #Lancement des agents
    agentScanCarte.start()
    agentVerifCarte.start()
    agentLumiereVerte.start()
    agentLumiereRouge.start()
    agentDetectionPassage.start()
    agentAlarme.start()
    
    print(bcolors.WARNING +"sleep has started" + bcolors.RESET)
    print("Ts batiment : \n","\t", tsBatiment.listeTuples)
    print("Ts Personne : \n","\t", tsPersonne.listeTuples)
    print("Ts autorisation: \n","\t", tsAutorisation.listeTuples)
    sleep(3)
    print(bcolors.WARNING + 'sleep ended ' + bcolors.RESET)
    agentLecteurCarte.start()
    print("Ts batiment : \n","\t", tsBatiment.listeTuples)
    print("Ts Personne : \n","\t", tsPersonne.listeTuples)
    print("Ts autorisation: \n","\t", tsAutorisation.listeTuples)

    while(True):
        sleep(1)

if __name__ == '__main__':
    main()
    