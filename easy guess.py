#number guess game
n=16
guess_the_number=1
print("Namaskar,Aadab,Sasriyakal")
print("Swagat hai aapka number guessing game mai")
print("Rules and Regulations:-")
print("*****Limited no of guess jo rahega wo sirf 9 rahega*****")
print("Hint:-Numbers are between 1 to 50")
print("Difficulty level-Medium")
print("To chaliye shuru karte hai game")
while(guess_the_number<=9):
    guess_no=int(input("Number batiye jo aapko lagta hai ki Harsh ne chupa rakha hai"))
    if guess_no>16:
        print("Aage chale gye aap thoda piche aaiye syd aap number guess kar le")
    elif guess_no<16:
        print("Piche chale gye aap thoda aage badhiye syd aap number guess kar le")
    else:
        print("Wah! aapne number guess kar liya BAHUT BAHUT BADHAI")
        print(guess_the_number,"Bar mai hi guess kr liya aapne number ko Gajab")
        break
    print(9-guess_the_number,"hi guess bache ab aapke pas")
    guess_the_number=guess_the_number+1


if(guess_the_number>9):
    print("Game khatam hua ab agle bar kosis kijiyega")
    print("Shukriya aapka mera game khelne ke liye")
    print("Game Creator= HARSH CHAUDHARY")

