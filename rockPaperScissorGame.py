# Basic Game Project in Python
def rock_paper_scissor(num1,num2,bit1,bit2):#Creating functiom
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player1[p1]==player2[p2]):
        print("Draw")
    elif(player1[p1]=="Rock" and player2[p2]=="Scissor"):
        print("Player_1 win(Rock)!!")
    elif(player1[p1]=="Paper" and player2[p2]=="Rock"):
        print("Player_1 win(Paper)!!")
    elif(player1[p1]=="Scissor"and player2[p2]=="Paper"):
        print("Player_1 win(Scissor)!!")

    elif(player1[p1]=="Paper"and player2[p2]=="Scissor"):
        print("Player_2 win(Scissor)")
    elif(player1[p1]=="Rock" and player2[p2]=="Paper"):
        print("Player_2 win(Paper)!!")
    elif(player1[p1]=="Scissor" and player2[p2]=="Rock"):
        print("Player_2 win (Rock)!!" )

player1={0:'Rock',1:'Paper',2:'Scissor'}# This is two data dicsnary
player2={0:'Paper',1:'Rock',2:'Scissor'}
while(1):
    num1=input("Player_1 enter your choice:")
    num2=input("Player_2 enter your choice:")
    bit1=int(input("Player_1 enter the secrate position:"))# Secrate position of value
    bit2=int(input("Player_2 enter the secrate position:"))
    rock_paper_scissor(num1,num2,bit1,bit2)#Calling the function 
    ch=input("Do you continue?(y/n):")
    if(ch=='n'):# If input ch equal to n ,then break the iteration
        break

