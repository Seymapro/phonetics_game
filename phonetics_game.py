import random

place = {
    "bilabial": ["p", "b", "m", "w"],
    "labiodental": ["f", "v"],
    "dental": ["ð", "θ"],
    "alveolar": ["t", "d", "s", "z", "n", "l", "r"],
    "postalveolar": ["ʃ", "ʒ", "/tʃ/", "/dʒ/"],
    "velar": ["k", "g", "ŋ"],
    "nasal": ["m", "n"],
    "palatal": ["j"],
    "glottal": ["H"]
}

manner = {
    "plosives": ["p", "b", "t" ,"d", "g", "k"],
    "fricatives": ["ð", "θ", "f", "v", "s", "z", "ʃ", "ʒ", "H"],
    "affricates":["/tʃ/", "/dʒ/"],
    "nasals": ["m", "n", "ŋ"],
    "approximants": ["w", "j", "l", "r"]
}

def ask_phonetics():
    place_list = random.choice(list(place.keys()))  
    chosen_phoneme = random.choice(place[place_list])
        
    for place_list in place:
        if chosen_phoneme in place[place_list]:
            correct_place = place_list
            
    for manner_list in manner:
        if chosen_phoneme in manner[manner_list]:
            correct_manner = manner_list
    
    question = input(f"{chosen_phoneme} is in ... and ...")
    answers = question.split(" ")

    if correct_place == answers[0] and correct_manner == answers[1]:
        print("congrats!")
    else:
        print(f"your answer was: {answers[0]} and {answers[1]}")

ask_phonetics()