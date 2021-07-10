# api ornek
# https://collectapi.com/tr/api/health/nobetci-eczane-api
import http.client
import json
conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 5gjAsuvkWhjK9m9lKtWASe:30h6HLCmRbuYZ3dsyQFaXr"
    }
il=input("il giriniz")
if il=="":
    print("il bilgisini boş girdiniz varsayılan oalrak Ankara yapıldı")
    il=="Ankara"
else :
    il=il.strip().capitalize()
ilce=input("ilçe giriniz")
if ilce=="":
    print("ilçe bilgisini boş girdiniz varsayılan olarak Çankaya yapıldı")
    ilce=="Çankaya"
else :
    ilce=ilce.strip().capitalize()

print(il,ilce)
bilgi="/health/dutyPharmacy?ilce="+ilce+"&il="+il

conn.request("GET",bilgi , headers=headers)

res = conn.getresponse()
data = res.read()
veri=data.decode("utf-8")
json_veri=json.loads(veri)

if json_veri["success"]== True:
    bilgi=json_veri["result"][0]
    print("Eczane Adı : "+bilgi["name"]+" Adresi : "+bilgi["address"])
        
else :
    print("istek başarısız")

