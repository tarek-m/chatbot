import random
from weather import Weather, Unit


# weather = Weather(unit=Unit.CELSIUS)
# condition = weather.condition
# weather_new=str(condition)






def analize(_str):
    list_1 = ['fuck', 'shit', 'ass', 'bitch', 'asshole', 'idot']
    emoji_1 = ['no', 'takeoff', 'crying', 'confused']
    answer_1 = ['bad boy ', ' why are you using this kind of language ', 'Do you know yoav !!!!', 'Do you know yoav !!!!']
    list_2 = ['joke', 'laugh', 'fun', 'funny']
    emoji_2 = ['laughing', 'giggling', 'dancing']
    answer_2 = ['why did the chicken cross the road.   gordon ramsy  says : because you didnt cook it ','joke','yoav challenged gelaad and Lost!!', '']

    list_3 = ['you', 'who', 'story' ]
    emoji_3 = ['crying', 'dog', 'waiting']
    answer_3 = ['i am boto  ','the best robot yoav didnt make', 'i was born in python and javascript', 'I like dogs']
    list_4 = ['name', 'my','am']
    emoji_4 = ['excited', 'giggling', 'inlove']
    answer_4 = ['hi ', 'the best robot yoav didnt make', 'i was born in python and javascript', 'I like dogs']
    emoji_5 = ['confused']
    answer_5 = ['i dont understand please explain more ', 'please explain more', 'what do you mean', 'I dont know what you mean']


    user_input =_str.split()
    user_input_lower = [x.lower() for x in user_input]
    for x in user_input_lower:
        if x in list_1:
            return [emoji_1[random.randint(0,3)],answer_1[random.randint(0,3)]]
        if x in list_2:
            return [emoji_2[random.randint(0,2)],answer_2[random.randint(0,2)]]
        if x in list_3:
             return [emoji_3[random.randint(0,2)],answer_3[random.randint(0,3)]]
        if x in list_4:
            xx = user_input_lower[-1]
#user name
            return [emoji_4[random.randint(0, 2)],"hi %s i am so excited to meet you " % (xx)]
        else:
            return [emoji_5 , answer_5[random.randint(0, 3)]]






# def analize(_str):
#     if _str =="love":
#         return "you"

