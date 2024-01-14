import re
import random

class Rulebot:
    negative_responses = ("no","nah","sorry","not a chance") #negatiive responses 
    exit_commands = ("Quit","exit","goodbye","later") # for exiting 
    
    random_questions = ("How to book tickets",
                        "How to cancel tickets",
                        "What are the safety measures",
                        "What instructions need to be followed before or after catching a flight")
    
    def __init__(self):
        self.flight = {'how_to_book_ticket': r'.*\s* book.*',
                       'how_to_cancel_tickets': r'.*\scancel.*',
                       'about_instructions': r'.*\s*safety instruction'}

    def greet(self):
        print("Greeting method executed.\n")
        self.name = input("What is your name?\n")
        will_help = input(f"Hi{self.name},I am a bot.How can i help you?\n")
        if will_help in self.negative_responses:
            print("OK,have a nice flight and safe journey!\n")
            return
        self.chat()    

    def make_exit(self,reply):
        print("Checking exiting methods.")
        for command in self.exit_commands:
            if reply == command:
                print("OK,have a nice flight and safe journey!\n")
                return True
        return False

    def chat(self):
        reply = input("Please tell your query:").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply)) 

    def match_reply(self,reply):
        print("Matching user reply.")
        for intent , regex_pattern in self.flight.items():
            found_match = re.search(regex_pattern,reply)
            if found_match and intent == 'how_to_book_ticket':
                return self.how_to_book_ticket()
            elif found_match and intent == 'how_to_cancel_tickets':
                return self.how_to_cancel_tickets()
            elif found_match and intent == 'about_instructions':
                return self.about_instructions()
        return self.no_match_intent()
    
    def how_to_book_ticket(self):
        responses = ("Search for flight.\n",
                     "Select a flight.\n",
                      "Enter passenger information.\n",
                     "Choose seat preference.\n" )
        for response in responses:
            print(response)
        return ""
    
    def how_to_cancel_tickets(self):
        responses = ("Review the cancellation policy.\n",
                     "Log into your account.\n",
                     "Retrieve your booking.\n",
                     "Check ability for refund.\n")
        
        for response in responses:
            print(response)
        return ""

        

    
    def about_instructions(self):
        responses = ("1.Check passport and visa requirements.\n",
                     "2.Arrive early.\n")
        for response in responses:
            print(response)
        return ""
    
    def no_match_intent(self):
        responses = ("I am sorry i could not understand it.Can you please rephrase it.\n")
        return random.choice(responses)

bot = Rulebot()
bot.greet()
