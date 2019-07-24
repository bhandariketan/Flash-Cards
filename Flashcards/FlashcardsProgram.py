import json
import time
import collections

print()
print("Hi, Welcome to Flash cards")
time.sleep(1)

flashCards = {
    'ceremony': 'a formal religious or public occasion',
    'apple': 'a fruit',
    'good': 'better than worse',
    'car': 'a vehicle'
}

f = open('StoredFlashcards.json', 'r')
flashCards = json.load(f)

while True:

    print()

    print("Press 1 - To print all the stored words with their meaning")
    print("Press 2 - To Search for the meaning of a word")
    print("Press 3 - To Exit")
    time.sleep(0.5)
    print()

    while True:
        try:

            n = int(input("Put n = "))
        except ValueError:
            print("Sorry, please choose one from the above options")

            continue
        else:

            break

    if (n == 1):
        print()
        order = collections.OrderedDict(sorted(flashCards.items()))
        print("Loading............")
        time.sleep(2)

        print()
        print("-----------------------------------------")
        for key, value in (order).items():
            print(key, ":", value)
            time.sleep(0.1)
        print("-----------------------------------------")
        time.sleep(2)

    elif (n == 2):
        wordPicker = str(input("Enter a word: "))
        print()
        print("Loading...........")
        print()
        time.sleep(2)

        if (wordPicker not in flashCards):
            print('Sorry, word not found')

            o = int(input(
                'Do you want to add the meaning of this word in the dictionary (1-Y OR 2-N): '))
            if (o == 1):
                print()
                meaning2 = str(input("Enter the meaning of the word: "))
                print("Updating.............")
                time.sleep(2)
                flashCards[wordPicker] = meaning2
                print("-----------------------------------------")
                print(wordPicker, ":", flashCards[wordPicker])
                print("-----------------------------------------")
                print("Meaning of the new word is saved successfully!")
                continue
            elif (o == 2):
                continue

        else:
            print("-----------------------------------------")
            print(wordPicker, ":", flashCards[wordPicker])
            print("-----------------------------------------")

            time.sleep(1)
            print()
            b = int(
                input("Is the meaning of the word is correct for you (1-Y OR 2-N): "))
            if (b == 1):
                continue
            elif (b == 2):
                m = int(input(
                    'If the meaning is not correct would you like to change the meaning or want to delete the word?(1-Change OR 2-Delete): '))
                if (m == 1):
                    print()
                    meaning = input('Enter the words meaning: ')
                    flashCards[wordPicker] = meaning
                    print("Updating...............")
                    time.sleep(2)
                    print("-----------------------------------------")
                    print(wordPicker, ":", flashCards[wordPicker])
                    print("-----------------------------------------")
                    print()
                    print('Meaning of the word updated successfully!')
                    continue

                elif (m == 2):

                    print("The word", wordPicker,
                          "is deleted from your Flash Card")
                    del flashCards[wordPicker]

                    continue

    elif n == 3:
        print()
        print('Thanks for using flash cards')

        with open('StoredFlashcards.json', 'w') as fp:
            json.dump(flashCards, fp)

        raise SystemExit

    else:
        print("Sorry, please choose one from the options")
        continue
