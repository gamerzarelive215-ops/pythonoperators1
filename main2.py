#Write the progam to calculate the number of notes in the given amount
amount=int(input("Please Enter the amount to withdraw: "))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
note4=(((amount%100)%50)%10)//1
print(f"Notes of 100 are {note1}")
print(f"Notes of 50 are {note2}")
print(f"Notes of 10 {note3}")
print(f"Notes of 1 {note4}")