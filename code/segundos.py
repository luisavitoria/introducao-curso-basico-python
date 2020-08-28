segundos= input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs= int(segundos)

dias= total_segs//86400
seg_rest= total_segs % 86400
horas= seg_rest // 3600
seg_rest2= seg_rest % 3600
minutos= seg_rest2 // 60
seg_rest_final= seg_rest2 % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",seg_rest_final,"segundos.")
