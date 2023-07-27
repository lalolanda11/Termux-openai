import openai
import os
print(os.getcwd())
api="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"
openai.api_key=api
#dato=input('Dato ')
chat=[]
while True:
    pregunta=input('Xelastone@archroot \n $ ')
    if pregunta == 'c' or pregunta == "quit":
            break
    else:


        res=openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{"role":"user",'content':pregunta}]
        )
        info=res["choices"][0]['message']["content"]



        print(info)
        print(type(res))