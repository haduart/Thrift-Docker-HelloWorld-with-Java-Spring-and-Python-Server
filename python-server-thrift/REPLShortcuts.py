from PythonServer import ReportServiceHandler
from ReportingService.ttypes import *

handler = ReportServiceHandler()

beans = []
beans.append(EventDTO(
    "L'ibèric o iber és una llengua paleohispànica coneguda per testimonis directes, " +
    "és a dir, una llengua que es parlava a la península Ibèrica abans que la llengua llatina hi " +
    "esdevingués la llengua dominant i de la qual se n'han conservat textos.",
    "system", "27/05/2016 09:44:32", 12, False, True, False, "OPERATIONEEL"))
beans.append(EventDTO(
    "Les inscripcions més antigues es documenten a finals del s. V aC i les més modernes a finals del " +
    "s. I aC o a principis del s. I dC. Les inscripcions en llengua ibèrica apareixen sobre suports molt " +
    "variats (monedes de plata i bronze, làmines de plom, ceràmiques àtiques, ceràmiques de vernís negre A i B," +
    " ceràmiques pintades, dòlies, àmfores, torteres, esteles i plaques de pedra, mosaics, etc.) i és amb diferència " +
    "la llengua paleohispànica més documentada per escrit, uns dos milers d'inscripcions que representen el 95% del total.",
    "system", "28/06/2016 09:45:32", 11, False, True, False, "OPERATIONEEL"))
beans.append(EventDTO(
    "Els texts en llengua ibèrica que usen el signari ibèric nord-oriental i l'alfabet grecoibèric poden llegir-se sense "
    "dificultats i amb alguna dificultat els que usen el signari ibèric sud-oriental",
    "system", "28/06/2016 09:45:32", "OPERATIONEEL", 11, False, True, False, "OPERATIONEEL"))
eventReport = EventDTO(
        "Tot el camp es un clam, som la gent Blau Grana.",
        "system", "28/06/2016 10:12:32", "OPERATIONEEL", 11, False, True, False, "OPERATIONEEL")
comment1 = Comments("Eduard", "6/06/2016 06:06:06", "I don't like this operation state")
comment2 = Comments("Rob", "6/06/2016 06:46:46", "I did this html/pdf from scratch :)")
eventReport.comments = []
eventReport.comments.append(comment1)
eventReport.comments.append(comment2)
beans.append(eventReport)
beans.append(EventDTO(
    "Tan se val d'on venim, si del sud o del nord ara estem d'acord una bandera ens agermana.",
    "system", "28/06/2016 10:12:32", "OPERATIONEEL", 11, False, False, True, "OPERATIONEEL"))

handler.createReport("Report1", beans, "Summary", "Eduard")
