import random

response_list = {
    1: "As I see it, yes",
    2: "Yes",
    3: "No",
    4: "Very likely",
    5: "Not even close",
    6: "Maybe",
    7: "Very unlikely",
    8: "Ask again later",
    9: "Better not tell you now",
    10: "Concentrate and ask again",
    11: "Don't count on it",
    12: " It is certain",
    13: "My sources say no",
    14: "Outlook good",
    15: "You may rely on it",
    16: "Very Doubtful",
    17: "Without a doubt"
}

iq_Score = {
    1: "you're dead... idk how you're still alive.. holy shit miracle ",
    2: "you are constructed uniquely",
    3: "Smoooothh brain, holy shit we can play soccer with this shit,it fliesss",
    4: "Cave man oo oo fire bad",
    5: "Average... for you maybe?",
    6: "Below average for the normal human",
    7: "Average you're just average not dumb or smart",
    8: "Yooo you know what 1+1 is its 3 right?",
    9: "ehh you kinda smart, not super smart kinda.",
    10: "Wrinkly brain",
    11: "Genius! you know what 3*3 is! OMG",
    12: "You are at the level of a very very very smart monkey good job",
    13: "Ehh you smart",
    14: "SUPER GENIUS HOLY SHIT MY BEAUTIFUL CREATOR"
}
def getIQScore(number):
    return str(iq_Score.get(number))


listOfDogs = {
    1: "https://imgur.com/r/dogs/oo67PIH",
    2: "https://imgur.com/r/dogs/ThWoXl7",
    3: "https://imgur.com/r/dogs/T0IYOxe",
    4: "https://imgur.com/a/mjIRx",
    5: "https://imgur.com/r/aww/kMT9xpn",
    6: "https://imgur.com/r/aww/7R1P3qn",
    7: "https://imgur.com/r/Eyebleach/ccWByZS",
    8: "https://i.imgur.com/goji65H.jpg",
    9: "https://i.imgur.com/9KY7dLJ.jpg",
    10: "https://imgur.com/gallery/7HRC8",
    11: "https://imgur.com/vA19fsO?nc=1",
    12: "https://imgur.com/gallery/04Hlhdd",
    13: "https://imgur.com/gallery/ix1Pc",
    14: "https://imgur.com/gallery/69SUs49?nc=1",
    15: "https://imgur.com/gallery/YRyKXwk",
    16: "https://imgur.com/gallery/RauFL/comment/765041823?nc=1",
    17: "https://imgur.com/gallery/MQHYB",
    18: "https://imgur.com/t/adorable/R2uWC?nc=1",
    19: "https://imgur.com/r/dogs/XsaLqi1",
    20: "https://imgur.com/r/dogs/2cGhWub",
    21: "https://imgur.com/r/dogs/TvGOeJ6",
    22: "https://imgur.com/r/dogs/a5qcGh7",
    23: "https://imgur.com/r/dogs/PsAC5iX",
    24: "https://imgur.com/r/dogs/T0IYOxe",
    25: "https://imgur.com/r/dogs/2rTetVo",
    26: "https://imgur.com/r/dogs/l8JfxuM",
    27: "https://imgur.com/gallery/HaVjb",
    28: "https://imgur.com/gallery/LyJD5",
    29: "https://imgur.com/gallery/M7yurJY",
    30: "https://imgur.com/gallery/zWeJ5",
    31: "https://imgur.com/gallery/0i0Vt6c",
    32: "https://imgur.com/gallery/Y104QOm",
    33: "https://imgur.com/gallery/kiPMApg",
    34: "https://imgur.com/gallery/CJyPLT5",
    35: "https://imgur.com/MVmKTub?nc=1",
    36: "https://imgur.com/HrAytvl?nc=1",
    37: "https://imgur.com/gallery/IFD14",
    38: "https://imgur.com/gallery/jGM0jGB",
    39: "https://imgur.com/gallery/DoL4gO7",
    40: "https://imgur.com/gallery/9ebJXU3",
    41: "https://imgur.com/gallery/mPzMNFJ",
}
def sendmagicballs():
    randomNum = random.randint(1, 17)
    return str(response_list.get(randomNum))

def sendDarkJokes():
    file = open('darkjokes.txt', encoding='utf-8-sig', errors='ignore')
    lines = file.read().splitlines()
    int = random.randint(0,86)
    myline = str(lines[int])
    return myline

def sendRandomPickupLines():
    file = open('pickupLines', encoding='utf-8-sig', errors='ignore')
    lines = file.read().splitlines()
    int = random.randint(0, 60)
    myline = str(lines[int])
    return myline

def sendDogsLinks():
    randomNum = random.randint(1, 41)
    return str(listOfDogs.get(randomNum))


def sendTwerking():
    return str("https://imgur.com/a/tvsO37N")
