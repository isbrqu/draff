Dim message, sapi
message=InputBox("�Qu� quieres que diga?","H�blame")
Set sapi=CreateObject("sapi.spvoice")
sapi.Speak message
