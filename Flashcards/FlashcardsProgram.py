import json
import time

print()
print("Hi, Welcome to Flash cards")
time.sleep(1)


a = {
        'ceremony': 'a formal religious or public occasion',
        'apple': 'a fruit',
        'good': 'better than worse',
        'computer': 'a very fast, DUMB machine',
        'car': 'a vehicle'
        }

f = open('StoredFlashcards.json','r')
a = json.load(f)


while True:
        
        print()
        
        print("Press 1 - To print all the stored words with their meaning")
        print("Press 2 - To Search for the meaning of a word")
        print("Press 3 - To Exit")
        time.sleep(2)
                
        n = int(input("Put n = "))
        

        print()
        if (n == 1):
                print()
                print("Loading............")
                time.sleep(3)
                
                
                print()
                for key, value in (a).items():
                        print(key, ":", value)
                

                        

        elif (n == 2):
                wordPicker = str(input("Enter a word: "))
                print()
                print("Loading...........")
                time.sleep(3)
                
                
                
                if (wordPicker not in a):
                        print('Sorry, word not found')
                        
                        o = int(input('Do you want to add the meaning of this word in the dictionary (1-Y OR 2-N): '))
                        if (o == 1):
                                print()
                                meaning2 = str(input("Enter the meaning of the word: "))
                                print("Updating.............")
                                time.sleep(2)
                                a[wordPicker] = meaning2
                                
                                
                                
                                print("Meaning of the new word updated successfully!")
                                continue
                        elif (o == 2):
                                continue
                        
                                
                else:
                        print(a[wordPicker])
                        print()
                        b = int(input("Is the meaning of the word is correct for you (1-Y OR 2-N): "))
                        if (b == 1):
                                continue
                        elif (b == 2):
                                m = int(input('If the meaning is not correct would you like to change the meaning?(1-Y OR 2-N): '))
                                if (m == 1):
                                        print()
                                        meaning = input('Enter the words meaning: ')
                                        a[wordPicker] = meaning
                                        print("Updating...............")
                                        time.sleep(2)
                                        print()
                                        print('Meaning of the word updated successfully!')
                                        continue
                                
                               
                                elif (m == 2) :
                                        
                                        continue

        
        elif n == 3:
                print()
                print('Thanks for using flash cards')
                
                with open('StoredFlashcards.json', 'w') as fp:
                        json.dump(a, fp)

                raise SystemExit

        





      
                


                


