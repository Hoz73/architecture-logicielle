from multiprocessing import Process, Value, Array
from threading import Thread, Event
from time import sleep

batiments = ["1","2","3"]

salles = ["info", "reseau", "geo", "math"]

batiments_badgeuses = [
    (batiments[0],11,12,13,14),
    (batiments[1],21,22,23,24),
    (batiments[2],31,32,33,34)
]

salles_badgeuses = [
    (salles[0],11,12),
    (salles[1],21,22),
    (salles[2],31,32),
    (salles[3],41,42)
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

class espaceDeTuples():
    listeTuples= list()

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

def lecteurCarte(ts,idBadgeuse, idCarte):
    ts.OUT(("cartePosee", idBadgeuse, idCarte ))
    print("Carte depose", '\n')

# def scanCarte(idBadgeuse, typeBadgeuse):
#     espaceDeTupleBatiment.IN(("cartePosee",idBadgeuse, ?idCarte ))
#     espaceDeTupleBatiment.OUT(("verifCarte", idBadgeuse, idCarte))
#     espaceDeTupleBatiment.IN(("porteDebloquee", idBadgeuse, ?res))
#     if(res):
#         espaceDeTupleBatiment.OUT(("lumiereVerte", idBadgeuse))
#         espaceDeTupleBatiment.OUT(("detectionPassage", idBadgeuse, idCarte, typeBadgeuse))
#         scanCarte(idBadgeuse, typeBadgeuse, idCarte)
#     else:
#         espaceDeTupleBatiment.OUT(("lumiereRouge", idBadgeuse))
#         scanCarte(idBadgeuse, typeBadgeuse, idCarte)

# def verifCarte(idBadgeuse):
#     espaceDeTupleBatiment.IN(("verifCarte", idBadgeuse, ?idCarte))
#     for e in cartesBatiment:
#         if
#     espaceDeTupleBatiment.RD(("autorisationCarte", idBadgeuse, idCarte, res))
#     espaceDeTupleBatiment.OUT((""))

# def lumiereVerte(idBadgeuse):

# def lumiereRouge(idBadgeuse):

# def detectionPassage(idBadgeuse):

# def declancheAlarme(idBadgeuse, typeBadgeuse):



def main():
    print("hoey")
    
    tsPersonne = espaceDeTuples()
    tsBatiment = espaceDeTuples()

    agentLecteurCarte = Thread(target=lecteurCarte, args=(tsBatiment,1,2), daemon=True)
    agentLecteurCarte.start()
    print(tsBatiment.listeTuples, '\n')
    agentLecteurCarte = Thread(target=lecteurCarte, args=(tsBatiment,1,5), daemon=True)
    agentLecteurCarte.start()
    print(tsBatiment.listeTuples, '\n')

    tsBatiment.IN(("cartePosee", 1, -1),[2] )
    print(tsBatiment.listeTuples, '\n')
    # tsBatiment.OUT(("recupe", 7, "idBadgeuse", 5))
    # tsBatiment.OUT(("recupe", 8, "idBadgeuse", 4))
    # tsBatiment.OUT(("recupe", 4, "idBadgeuse", 2))
    
    # print(tsBatiment.IN(("recupe", 5, "idBadgeuse", -1), [3]))
    # print(tsBatiment.IN(("recupe", 7, "idBadgeuse", -1), [3]))
    # tsBatiment.ADD(("recupe", 8, "idBadgeuse", 60), [3])
    # print(tsBatiment.IN(("recupe", 8, "idBadgeuse", 60), [3]))

if __name__ == '__main__':
    main()
    