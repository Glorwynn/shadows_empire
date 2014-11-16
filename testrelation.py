def talk(conversation):
    print(conversation[0])
    if len(conversation) > 1:
        for rep in conversation[1:]:
            print(str(conversation.index(rep)) + ": " + rep)
        response = input("Reponse : ")
    print(response)


r1 = ['Salut !']
r2 = ["Salut !", "Salut mec !", "Vas te faire foutre !"]
talk(r2)