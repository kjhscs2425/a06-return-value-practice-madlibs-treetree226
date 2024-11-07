adjective0 = input("Give me an adjective: ")
noun0 = input("Give me a noun: ")
pluralnoun0=input("Give me a plural noun: ")
female_in_room=input("Give me a name of a female in this room: ")
adjective1=input("Give me another adjective: ")
clothes=input("Give me an article of clothing: ")
noun1=input("Give me another noun: ")
city= input("Give me a name of a city: ")
pluralnoun1=input("Give me another plural noun: ")
adjective2=input("Give me another adjective: ")

story = f"There are many {adjective0} ways to choose a/n {noun0} to read. First, you could ask for reccomendations for friends and {pluralnoun0}. Just don't ask Aunt {female_in_room}-- she only reads {adjective1} books with {clothes}-ripping goddesses on the cover. If your friends and family are no help, try checking out the {noun1} Review in The {city} Times. If the {pluralnoun1} featured there are too {adjective2} for your taste, try something a little"
print(story)