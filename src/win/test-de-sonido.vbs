Dim message, sapi
message=InputBox("¿Qué quieres que diga?","Háblame")
Set sapi=CreateObject("sapi.spvoice")
sapi.Speak message
