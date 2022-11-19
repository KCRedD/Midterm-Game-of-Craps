import random
from random import randint

#define define a class called dice
class Dice:
    
    def __init__(self,sides=6):
        self.sides=sides
                
    def diceroll(self):
        while True:
            self.die1 = random.randint(1,self.sides)                    #Holds the value of die 1
            self.die2 = random.randint(1,self.sides)                    #Holds the value of die 2
            self.dice = self.die1 + self.die2                           #Prints the summation of both dice
            self.roll_dice = input("press 'd' to roll dice")            #Prompts user to roll the dice
            #print(self.die1)
            #print(self.die2)
            if self.roll_dice == 'd' or self.roll_dice == 'D':
                print (self.dice)
                break
            else:
                print("please press d to roll")                         #diceroll error handling
                
        return self.dice
    
#define define a class called dice
class Dice:
    
    def __init__(self,sides=6):
        self.sides=sides
                
    def diceroll(self):
        while True:
            self.die1 = random.randint(1,self.sides)                    #Holds the value of die 1
            self.die2 = random.randint(1,self.sides)                    #Holds the value of die 2
            self.dice = self.die1 + self.die2                           #Prints the summation of both dice
            self.roll_dice = input("press 'd' to roll dice")            #Prompts user to roll the dice
            #print(self.die1)
            #print(self.die2)
            if self.roll_dice == 'd' or self.roll_dice == 'D':
                print (self.dice)
                break
            else:
                print("please press d to roll")                         #diceroll error handling
                
        return self.dice
    
#Define a class called table
#Inherit the Dice class

class Table(Dice):
    
    def __init__(self,point_set=False):
        super().__init__()
        self.point_set = point_set
    
    def __bool__(self):
        return False

#Table point is not set initially

#Define a class for the player
#Inherit the Table class

class Player(Table):
    
    def __init__(self):
        super().__init__()
        self.name = input("Please enter your name: ")           #asks the user to input their name at initialization
        print("Welcome to the table {}".format(self.name))      #prints welcome message
        self.bankroll_list = []                                 #empty list to track bankroll updates
        
    #def bankroll(self):
        
        while True:
            try:
                self.roll = int(input("Please enter you Bankroll: "))  #asks the user to input their bankroll at initialization
                

            except ValueError: 
                print("Please enter a valid number\nOnly Dollars accepted on this table")  #bankroll input error handling

            else:
                
                print("Your bankroll is {}".format(self.roll))      #print bankroll amount given
                break
            
            
            return self.roll
        self.bankroll_list.append(self.roll)
        
#Define a class for bets
#Inherit from the Player class

class Bets(Player):
    
    def __init__(self):
        super().__init__()
        
    def insufficient_funds():
        print("bet exceeds bankroll, please choose a bet within the bankroll limit")   #method for bet input error handling
    
    def ingest_bet(self):                                            #method for bet input
        self.initial_bet = 0

        while self.point_set == False :
            try:
                self.initial_bet = int(input("Enter bet amount: "))     #takes bet amount input for that round

                if self.initial_bet <= 0:
                    print("Please enter a bet")
                    continue
                elif self.initial_bet > self.roll:
                    Bets.insufficient_funds()
                    continue
            except ValueError:
                print("Please enter a valid number")
            else:
                self.roll = self.roll - self.initial_bet
                print ("your updated bankroll is {}".format(self.roll))      #prints updated bankroll after placing bet
                break
                
        while self.point_set==True:
            try:
                self.initial_bet = int(input("Enter bet amount: "))    #takes bet amount input for that round after table point is set
                if self.initial_bet <= 0:
                    print("Please enter a bet")
                    continue
                elif self.initial_bet > self.roll:
                    Bets.insufficient_funds()
                    continue
                elif self.initial_bet > self.odds_limit:
                    print("Please enter a bet within the allowed limit")
                    continue
            except ValueError:
                print("Please enter a valid number")
            else:
                self.roll = self.roll - self.initial_bet
                print ("your updated bankroll is {}".format(self.roll))      #prints updated bankroll after placing bet
                break
                
        self.bankroll_list.append(self.roll)             #add updated bankroll amount to bankroll list
        return self.initial_bet
    
    def shooter(self):                   #method to check active bets, evaluate winners, losers and payouts
        
        #check active bets
        self.pbet_won = False
        while self.point_set == False:   #while table point is not set
            self.table_point = 0
            
            self.active_bets = False
            Dice.diceroll(self)          #prompts user to roll dice
            
            if self.dice == 2 or self.dice ==3:    #pass line looses if comeout roll is 2 or 3
                print("Pass line loses")
                self.pbet_won = False 
                Bets.bet_loser(self)               #calls bet loser method
                Bets.payout(self)                  #calls payout method
                break
                
            elif self.dice == 7 or self.dice ==11:  #pass line wins if comeout roll is 7 or 11
                print("Pass line wins")
                self.pbet_won = True              
                Bets.bet_winner(self)             #calls bet winner method
                Bets.payout(self)                 #calls the payout method
                break
                
            elif self.dice == 12:
                print("It's a draw! please roll again")
                Bets.shooter(self)
                break
                
            else:
                print("Table point has been set to {}".format(self.dice))     # table point is set if come out roll is not 2,3,7,11 or 12
                self.table_point = self.dice
                self.active_bets = True                     #active bets now exist
                self.point_set = True                       #table point is now set
                Bets.odds(self)                             #call the odds bet method
                break
                
        else:
            self.table_point = self.dice      #while table point is set
            Dice.diceroll(self)               #prompts user to roll the dice
            if self.dice == 7:                # pass line loses at 7 after table point is set
                print("Pass line loses")
                self.pbet_won = False
                Bets.bet_loser(self)
                Bets.payout(self)
                
            elif self.dice == self.table_point:   #pass line wins at table point roll after table point is set
                print("Pass line wins")
                self.pbet_won = True
                Bets.bet_winner(self)
                Bets.payout(self)
                
            else:
                print("Nobody wins. Please roll again")    #prompts a reroll if it doesn't land on 7 or table point
                Bets.shooter(self)
                
    def pass_line(self):    
        pass
    
    def dont_pass_line(self):
        pass
    
    def betting_turn(self):                             #method to start a betting round
        self.comeout_betchoice = 'none'
        
        
        while self.point_set == False:                                                                     
            ask_bet = input("Do you want to place a bet? (Y or N) : ")       # ask user if they want to place a bet
            if ask_bet == 'y' or ask_bet == 'Y':
                self.comeout_betchoice = input("Where would you like to place your bet? 'P' for pass line, 'DP' for don't pass line : ")  #pass line or don't pass line bet option
                if self.comeout_betchoice == 'P' or self.comeout_betchoice == 'p':
                    print("you have chosen pass bet")
                    Bets.ingest_bet(self)      #calls the ingest bet method
                    Bets.shooter(self)         #calls the shooter method 
                    
                elif self.comeout_betchoice == 'DP' or self.comeout_betchoice =='dp' or self.comeout_betchoice =='Dp' or self.comeout_betchoice =='dP':
                    print("you have chosen don't pass bet")
                    Bets.ingest_bet(self)     #calls the ingest bet method
                    Bets.shooter(self)        #calls the shooter method 
                    
                else:
                    print("Please enter a valid choice")
            elif ask_bet == 'n' or ask_bet == 'N':
                Bets.payout(self)                       #call payout method if user chooses not to bet
                break
            else:
                print("Please make a valid choice")
                continue                               #bet choice error handling
    
    def bet_winner(self):                         #method to declare winning bet type and amount
        self.winning_bettype = 'none'
        
        while self.point_set == False:
            if self.pbet_won == True:
                self.winning_bettype = 'Pass line bet'
                print("You have won ${} from the {}".format(2*self.initial_bet,self.winning_bettype))
                self.roll = self.roll + (2*self.initial_bet)
                break
            if self.pbet_won == False:
                self.winning_bettype = 'Dont pass line bet'
                print("You have won ${} from the {}".format(2*self.initial_bet,self.winning_bettype))
                self.roll = self.roll + (2*self.initial_bet)
                break
            else:
                Bets.bet_loser(self)
                break
        self.bankroll_list.append(self.roll)         #add updated bankroll amount to bankroll list
            
            
       
                
    def bet_loser(self):                          #method to declare losing bet type and amount
        self.losing_bettype = 'none'
        
        while self.point_set == False:
            
            if self.pbet_won == False:
                self.losing_bettype = 'Pass bet'
                print("You have lost ${} from the {}".format(self.initial_bet,self.losing_bettype))
                break
                        
            elif self.pbet_won == True:
                self.losing_bettype = 'Dont pass bet'
                print("You have lost ${} from the {}".format(self.initial_bet,self.losing_bettype))
                break  
                
            else:
                ("please roll again")
                break
        self.bankroll_list.append(self.roll)       #add updated bankroll amount to bankroll list

    def odds(self):                 #method for odds bet after table point is set
                
        self.odds_betchoice = 'none'
        
        while self.point_set == True:
            self.odds_limit=0
           
            ask_oddsbet = input("Do you want to place an odds bet? (Y or N) : ")    # ask user if they want to place an odds bet
            if ask_oddsbet == 'y' or ask_oddsbet == 'Y':
                
                    print("you have chosen to bet odds on the pass line")
                    if self.table_point == 4 or self.table_point == 10:       #odds bet limit of 3x pass line bet if diceroll is 4 or 10
                        self.odds_limit = 3*self.initial_bet
                    elif self.table_point == 5 or self.table_point == 9:      #odds bet limit of 4x pass line bet if diceroll is 5 or 9
                        self.odds_limit = 4*self.initial_bet
                    elif self.table_point == 6 or self.table_point == 8:      #odds bet limit of 5x pass line bet if diceroll is 6 or 8
                        self.odds_limit = 5*self.initial_bet
                                            
                    print(f"you can bet a maximum of {min(self.roll,self.odds_limit)}")
                    Bets.ingest_bet(self)
                    Bets.shooter(self)
                    break                    
            elif ask_oddsbet == 'n' or ask_oddsbet == 'N':
                Bets.shooter(self)
                break
            else:
                print("Please make a valid choice")
                continue
            
    def payout(self):                                                                  #Method to evaluate payouts
        self.play_again = input("Would you like to play another round? (Y/N): ")
        while True:
            if self.play_again == 'Y' or self.play_again == 'y':
                Bets.betting_turn(self)
                break
            elif self.play_again == 'N' or self.play_again == 'n':
                
                print(f"You have made an overall profit of {self.bankroll_list[-1]-self.bankroll_list[0]}")     #print the overall change in bankroll
                print("Thank you for playing")
                
                break
            else:
                print("Please enter a valid choice")
        
bet = Bets()    
bet.betting_turn()
