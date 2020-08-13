autos = ["correcto","correcto","correcto","defectuoso","correcto","defectuoso","correcto"]

for estado in autos:
  if estado == "defectuoso":
    print("Auto Defectuoso, enviado a Revisión")
    #break
    continue
  print("Este auto está: " + estado )
  print("Enviado para Distribución")