// espace de tuples batiment 
<cartePosee, string, idBadgeuse, int>
<cartePosee, string, idBadgeuse, int, idCarte, int>
<verifCarte, string, idBadgeuse, int, idCarte, int>
<porteDebloquee, string, idBadgeuse, int, res, bool>
<detectionPassage, string, idBadgeuse, int, idCarte, int, typeBadgeuse, string>
<lumiereRouge, string, idBadgeuse, int>
<lumiereVerte, string, idBadgeuse, int>
<AutorisationCarte, string, idBadgeuse, int, idCarte, int, res, bool>

//espace de tuples personnePresente
<idCarte, int, idBadgeuse, int, typeBadgeuse, string>


**********************************************************************************************************************************************************************

scanCarte(idBadgeuse,typeBadgeuse) = 
    in(<|cartePosee, string, idBadgeuse, int, idCarte, int|>).
    out(<verifCarte, string, idBadgeuse, int, idCarte, int>).
    in(<|porteDebloquee, string, idBadgeuse, int, ?res, bool|>).
    (
        [res].
            out(<lumiereVerte, string, idBadgeuse, int>).
            out(<detectionPassage, string, idBadgeuse, int, idCarte, int, typeBadgeuse, string>).
            scanCarte(idBadgeuse)
        +
        [!res].
            out(<lumiereRouge, string, idBadgeuse, int>).
            scanCarte(idBadgeuse,typeBadgeuse)
    )

***************************************

lecteurCarte(idBadgeuse, idCarte) = 
    out(<cartePosee, string, idBadgeuse, int, idCarte, int>).
    lecteurCarte(idBadgeuse, idCarte)

***************************************

verifCarte(idBadgeuse) = 
    in(<|verifCarte, string, idBadgeuse, int, ?idCarte, int|>).
    rd(<|AutorisationCarte, string, idBadgeuse, int, idCarte, int, ?res, bool|>).
    out(<porteDebloquee, string, idBadgeuse, int, res, bool>).
    verifCarte(idBadgeuse)

***************************************

lumiereVerte(idBadgeuse) = 
    in(<|lumiereVerte, string, idBadgeuse, int|>).
    lumiereVerte(idBadgeuse)
    //déclencher la lumière verte

****************************************
lumiereRouge(idBadgeuse) = 
    in(<|lumiereRouge, string, idBadgeuse, int|>).
    lumiereRouge(idBadgeuse)
    //déclencher la lumière rouge

****************************************

detectionPassage(idBadgeuse) = 
    in(<|detectionPassage, string, ?idBadgeuse, int, ?idCarte, int, ?typeBadgeuse, string|>).
    add(<|capteurPassage, string,idBadgeuse, int !detection, int|>).
    //Attend la detection pendant 30 sec
    (
        [detection > 1] 
            out(<declencheAlarme, string, idBadgeuse, int>).
            detectionPassage(idBadgeuse)
        +
        [detection == 1]
            (
                [idBadgeuse % 2 == 1]
                (
                    out(personnePresente, <idCarte, int, idBadgeuse, int, typeBadgeuse, string>)
                    detectionPassage(idBadgeuse)
                )
                +
                [idBadgeuse % 2 == 0]
                (
                    in(personnePresente, <|idCarte, int, idBadgeuse, int, typeBadgeuse, string|>)
                    detectionPassage(idBadgeuse)
                )
            )
        + 
        [detection < 1]
            detectionPassage(idBadgeuse)
    )


******************************************declencheAlarme(idBadgeuse, typeBadgeuse) = 
    in(<|declencheAlarme, string, idBadgeuse, int|>)
    // code alarme







