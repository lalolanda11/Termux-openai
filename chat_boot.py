import openai
import os
import base
basedatos=dato()                                                                                                                                                                                                   
print(os.getcwd())
#CXod
#Aqui va la api de openai 
#Si no tienes un api, debes de registrarte en la pagina oficial de openai pára tener un api
#Ingresa el api en la variable llamada api
api=""
openai.api_key=api
#dato=input('Dato ')
chat=[]
while True:
    #Puedes cambiar el nombre de la entrada 
    pregunta=input('Xelastone@archroot \n $ ')
    if pregunta == 'c' or pregunta == "quit":
            break
    elif pregunta == "quien creo el codigo" or pregunta == "cual es mi nombre":
        os.system("termux-tts-speak Este codigo fue creado por xela stone y mi nombre es elena stone")
        os.system("clear")
    else:


        res=openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{"role":"user",'content':pregunta}]
        )
        info=res["choices"][0]['message']["content"]



        print(info)
        print(type(res))
