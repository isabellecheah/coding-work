print("messages for you :)")
print()
while True:
    description = input("could you describe how you feel? [happy/sad/tired/angry/idontknow]")

    list_of_words = description.split()

    feelings_list = []
    encouragement_list = []
    counter = 0

    for each_word in list_of_words:

        if each_word == "sad":
            feelings_list.append("sad")
            encouragement_list.append("tomorrow will be a better day and don't forget to look on the bight side of things")
            counter += 1
        if each_word == "happy":
            feelings_list.append("happy")
            encouragement_list.append("remember to keep on smiling and not give up despite the challenges you face, you can do it! Jia youzz")
            counter += 1
        if each_word == "tired":
            feelings_list.append("tired")
            encouragement_list.append("you are stronger than you think and you can do it, grit your teeth and persevere on.")
            counter += 1
        if each_word == "stressed":
            feelings_list.append("stressed")
            encouragement_list.append("take a break and relax! im sure you'll do well so dont be too stressed!!")
            counter += 1
         if each_word == "angry":
            feelings_list.append("angry")
            encouragement_list.append("why? just relax and dont think about it. breathe in and breathe out!")
            counter += 1
    if counter == 0:
        output = "please only reply with the selected words"

    elif counter == 1:
        output = "it seems that you are feeling" + feelings_list[0] + ". however, do remember "+ encouragement_list[0] + "! hope you feel better :)"

    else:
        feelings = ""
        for i in range(len(feelings_list)-1):
            feelings += feelings_list[i] + ", "
            feelings += "and " + feelings_list[-1]
        
            encouragement = ""
            for j in range(len(encouragement_list)-1):
                encouragement += encouragement_list[i] + ", "
                encouragement += "and " + encouragement_list[-1]
    
        output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "!! Hope you feel better :)"

    print()
    print(output)
    print()
