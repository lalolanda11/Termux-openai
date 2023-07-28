import openai
import os
import time
import database
tabla=database.db()
print(os.getcwd())
api="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"
openai.api_key=api
#dato=input('Dato ')
chat=[]
import os
cuestion=["cual es tú nombre","quien te programo"]

while True:
    pregunta=input('Xelastone@archroot \n $ ')
    if pregunta == 'c' or pregunta == "quit":
            break
    elif pregunta in cuestion[:]:
                    os.system("termux-tts-speak mi nombre es chatgpt y este documento fue creado por Eduardo Stone. usando la libreria openai. El nombre que me otorgaron es elena stone. buenas vibras y excelente día")

    elif pregunta == "clear" or pregunta == "cls":
                    os.system("clear")
    else:


        res=openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{"role":"user",'content':pregunta}]
        )
        info=res["choices"][0]['message']["content"]
        with open("dato.txt","w") as f:
            f.write(str(info))
            f.flush()
            tabla.insert(str(time.ctime()),str(info))
        os.system("cat dato.txt | termux-tts-speak ")
        print(info)
        print(type(res))
