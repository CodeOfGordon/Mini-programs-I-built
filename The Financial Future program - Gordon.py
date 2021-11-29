#Name:          Gordon
#Student ID:    [REDACTED]
#Teacher:       [REDACTED]
#Course:        [REDACTED]



'''FUNCTIONS'''

# LEAVE SECTION -----------------------------------------------------------
def leave(): # Exits the program.
    import time
    
    print("\nBefore you leave, can you provide some feedback on this program?")
    choice = input("\n-> ")

    # Receives feedback if yes.
    if choice == "YES" or choice == "Yes" or choice == "yes" or choice == "Y" \
       or choice == "y" or choice == "YEAH" or choice == "Yeah" \
       or choice == "yeah" or choice == "Sure" or choice == "sure":
        
        print("\nCool! Any constructive criticism is greatly appreciated!")
        feedback = input("\n-> ") # This doesn't actually do anything.
        print("\nThanks!", end=" ")

    else:
        pass
        print()

    print("And don't forget, I also have an Instagram account!")
    print("Follow me on Instagram at [REDACTED] for updates and more!\n")

    time.sleep(3) # Delays time before exitting, here it's for 3 seconds.
    
    print ("Ending program…")

    time.sleep(2)
    
    return True 




# REPEAT/REDIRECT SECTION -------------------------------------------------
def repeat(): # Gives the user the option to return to the main menu.
    
    while True: # Loops until response is made.
        
        print("\n\nDo you want to return to the main menu?")
        inp_repeat = input("\n-> ")

        # Returns to main menu if yes.
        if inp_repeat == "YES" or inp_repeat == "Yes" or inp_repeat == "yes" \
           or inp_repeat == "Y" or inp_repeat == "y" or inp_repeat == "YEAH" \
           or inp_repeat == "Yeah" or inp_repeat == "yeah":
            return False

        # Repeats program if no.
        elif inp_repeat == "NO" or inp_repeat == "No" or inp_repeat == "no" \
           or inp_repeat == "N" or inp_repeat == "n" or inp_repeat == "NAH" \
           or inp_repeat == "Nah" or inp_repeat == "nah":
            return True

        #Error check
        else:
            print("\n[Choose either yes or no!]")




# INFORMATION SECTION -----------------------------------------------------

def banking_commerce(): # Displays information on commercial banking.
    print('''
In the olden days, to access thy funds, thou had to travel far to the bank at
the break of morn to forbear the dreaded rush hour…

Now? You can just install your bank’s app and access it from your smartphone.

Before, if we wanted to send cash to someone, we had to telegram a cheque over
to them. Now, we just use PayPal.

Technology has massively impacted the way we do our banking, providing more
convenience towards the customer; us.


Along with accessing funds, technology has helped to improve
our individual experiences.

In the past, if you wanted to receive advice on your banking,
there were times when you had to schedule appointments DAYS in advance.
And while you still sometimes have to do this today, this need is drastically
reduced with the introduction of AI-powered chatbots,
ready to solve any urgent questions; 24/7.


Another major point of interest would be how technology affects mortgages.

When you want to own a house, most of the time, you won’t be able to pay it
right off the bat. So instead, you need a large loan from the bank in the form
of a mortgage. To receive one of these, you first need to pay off a portion
of the house (a downpayment), before agreeing to use your house as collateral
(essentially they take your house if you don’t repay). 

The banks, of course, need to make money. So after they loan you a mortgage,
they require you to return that amount, plus a percentage of extra money
called interest.

However some people may still not pay their mortgage, people whose history
reflect a high chance of this happening are deemed risky, and will need to pay
a higher interest. Banks have to determine which person is risky, and which
person will pay off their mortgage. The only problem is that there are a LOT
of people to sift through, which is why these mortgage applications take so
long to be accepted.


And this is where technology comes into play. Now, instead of writing a cheque
and mailing it to the bank, you can instead fill out an online application.
Once done, it’ll automatically be uploaded to a database, where it'll go
through some preset tests to be determined if its either a risky or secure
investment. This way, commercial banks will be able to review & approve
hundreds of applications at once!


As technology continues to change, maybe we’ll get to a point where
an AI bot can approve thousands of applications in an instant, who knows?
    ''')

def insurance(): # Displays information on insurance.
    print('''
Many unexpected events happen in the average person’s life,
a lot of them very unfortunate.

This is where insurance companies come in. The customer would first pay
a sum of money monthly, known as a premium, to the company.
In turn, the company would promise a large amount of money,
known as a settlement, in case that unfortunate event ever happened.
When you receive this settlement amount, you are “claiming your insurance”.


Insurance companies cover anything from health and property, to cars and pets.
However, for each customer they have, they must change the amount of premium
paid. This depends on their related information, history, and the company’s
pricing models.

If you want property insurance and have a house in say, the world’s most
disaster prone area (though I don’t know why you would even live there),
they will charge you a large premium. If however,
you live in the world’s safest area, you will probably pay less.
Depending on the type of insurance, these companies need to look through
the specific circumstances & backgrounds of each individual, in order
to find a fair premium.

This is where technology comes into play. All the insurance company would have
to do is set up a database with all of their pricing models,
then whenever they get a customer, they type in their information and boom;
instant premium. 


Along with this, technology has allowed for insurance companies to make use
of 24/7 chatbots. This is especially useful in case of large scale disasters,
where many people rush to claim their insurance at once.


Technology also helps to detect insurance fraud, a case where the customer
tries to claim their insurance for an unfortunate event that either
never happened, or was purposefully caused by them.

Through machine learning, suspicious patterns can be detected and flagged
for review. Additionally, the company can also use the power of the internet
and social media to detect this as well.

If a person who claimed their car crashed yesterday, is seen bragging
in that same car today on Instagram, then something is definitely wrong.

Of course, not everyone is this dumb. Many insurance fraudsters are getting
smarter, and are starting to use more complex strategies. That’s why insurance
companies need technology, in order to continually adapt and overcome them.
    ''')

def banking_investment(): # Displays information on investment banking.
    print('''
The area of investment banking is heavily tied to the investing world,
and does a lot of work behind the scenes. These banks mainly work as advisors
of companies and governments, giving instructions on how to best roll out
their stocks/bonds to the public. 

If you don’t know stock market terminology, stocks are items that hold a small
percentage of the company, owning one means you are the owner
of a tiny percentage of that company. However if you were to buy some,
make sure to be careful, as stocks are notoriously volatile
in that their prices can change by A LOT. 

Bonds on the other hand, are long but secure loans given by the government,
this essentially means that the government will pay you back later
in the future.


Despite this knowledge, investment banks don’t just work for the big people,
but also for the small people as money managers. And in order to gain new
customers from this wide demographic, they need to get their name out there.

Back then, investment banks would do this through word of mouth
and their connections. Now, along with being able to advertise worldwide
through the internet, they can easily receive the cash they need to invest
via online payment.


With the job of managing money, investment banks need to be very careful,
yet adventurous enough to take chances.

As the saying goes: “The higher the risk, the higher the reward.”
Obviously, you also don’t want to just dump $100,000 of your customer’s money
down the drain. So investment banks have to sort through hundreds of companies,
before looking through their even larger pile of financial documents.

And that’s where technology comes to the rescue. Instead of manually searching
through every single company, investment banks can just use something called
a stock screener. These tools essentially filter out any companies
that don’t meet the requirements set by the user, a simple yet
mentally life saving tool.


Lastly, investment banks use technology to track the stock market,
and sometimes even predict its next move. Through the use of this,
they can accurately decide on how to next invest their customer’s money,
or how to best roll out the stocks/bonds of companies/governments.

Although these predictions are often misplaced, there may be a time
in the future when these banks can accurately judge the market’s directions.

I wonder how that’ll turn out.
    ''')

def accounting(): # Displays information on accounting.
    import time
    
    print("When you think of accounting, what do you think of?")

    time.sleep(3) #Time delay for thinking

    print('''
Well if you thought of a tired middle-aged worker with piles of documents
everywhere, then… You’re actually right. Although with the addition
of technology, this has been considerably toned down.

Instead of documents, it's become much less messy. Nowadays, accountants make
use of cloud-based databases that store all the information that they need.


And if there’s any information missing?
It can simply just be sent over the internet!


There’s also software specifically designed for accountants, aiding them
in their work, like instantly performing any repetitive actions.

Software like QuickBooks can easily be used to keep track
of the company’s finances, as well as present them in a visually appealing way
with graphs and diagrams.

These accounting software are very popular with small, medium, and big
businesses whose accountants all use them in some way.


Of course, accounting isn’t just for businesses, and these software can also
be found being used for individual people as well; especially with taxes!

In fact, I have an anecdote on this which happened some time ago in April 2021.

I was very nervous as my dad drove us to my aunt,
who was an on-and-off accountant.

I was clutching onto the documents my dad told me to be very careful with,
I was both nervous and excited to experience the infamous “doing taxes”.

When I finally got there, my aunt told me to boot up her laptop and start
doing it in this software called “TurboTax,” and so I opened it up with
still a lot of nervousness.

However when I actually got around to “doing taxes”, it quite literally looked
like a multiple choice quiz, and I honestly felt a little disappointed
with myself  for being nervous. What I essentially did was manually copy &
pasted what was on the documents, onto the computer.


Despite this though, the process still took hours, and by the end of the day
I was still not finished! With the ever-changing nature of technology,
hopefully we’ll be able to get rid of the repetitiveness of accounting,
and someday also be able to turn “doing taxes” into a 5 minute detour.
    ''')

def jobs(): # Displays information on the positive effects on jobs.
    print('''
Of course, we can’t talk about the future of technology without mentioning
that one. sole. barrier.

Jobs.

This is a large and very legitimate concern, as many people are worried about
being replaced and unable to make a living. Luckily, technology has little
intention of replacing people. In fact, they’re designed to help them,
freeing them up from repetitive jobs.

Additionally, there are some things that technology and AI will never be able
to truly accomplish.

-- Commercial Banking --

The needs of customers are specific, and very human. This is something
that 24/7 chatbots will never be able to understand. As such, bankers
will still be needed to give customers that touch of “human emotion” they may
need. The only thing these chatbots are really taking away are 24/7 phone calls
asking “how do I withdraw from my bank account”.

To add onto that, commercial banks will still need bankers to double check
the remaining mortgage applications as although technology is always changing,
it’s not always perfect.




-- Insurance --

Similar to commercial banks, the premium that is calculated by technology
needs to be double checked.

There’s also the danger of insurance fraud, an illegal activity
whose performers are constantly changing in strategies.
Some of their tactics can be picked up by AI pattern recognition & statistics,
heavy emphasis on “some”. This is because it cannot pick up on emotion or tone,
something that’s vital in this case. And so insurance investigators are tasked
with picking up on these emotional mistakes, hopefully blocking this blindspot.


-- Investment Banks --

Humans will always be needed here as most of the time, governments
and companies will probably want a person to be giving advice on selling
their stocks/bonds. This is mainly because of the human emotion factor which,
as mentioned before, cannot be replaced by technology.

There’s also the fact that in terms of investing, companies are different
from each other, and all have unique circumstances. This is why solely looking
at their documents and financial information won’t tell the whole story,
and should definitely not be used alone when investing.

Take Tesla for example, they’re known as one of the most innovative companies
out there, and yet as of their most recent quarter report on July 26th of 2021,
they’re about $775 MILLION in debt. 

A company’s financial documents are important, but so are its leaders and
overall industry among other things. Financial analysts, investment bankers,
and other jobs at investment banks will always be needed for this.


-- Accounting --

Keeping track of a company’s financials is extremely important, that’s why
accountants will always be needed, even as technology moves on. This fact
becomes even clearer when there’s the fact that companies will be penalized
if their financial information isn’t accurate.

Along with this accuracy system, governments have tax rebates,
each with specific requirements. If you didn’t know, tax rebates
can potentially reduce the amount of taxes paid. Though this is only if
they’re used correctly, as these rebates are buried under hundreds of documents
in various laws, and will result in penalties if misused.
Accountants are experts on this, looking at both the company’s situation
and specific legal documents to reduce as much taxes as possible; legally
of course. And this isn’t just for companies, accountants also help
reduce taxes for the average person as well.




Technology won’t replace everything, since its purpose isn’t to replace,
but to aid. Which is why hopefully, in the future, we can take note of this.
So that along with technology, we will also constantly change.
    ''')



def information(): # Provides information on financial services to the user.
    again = True
    
    while again == True: # Keeps the loop going until again = False.
        print("\n----------------------------------------------------------\n")
        print("Please select the area of financial services \n\
you’re interested in learning more about\n")
        print("A - Commercial Banking")
        print("B - Insurance")
        print("C - Invesment Banking")
        print("D - Accounting")
        print("E - Impact on jobs")
        print("F - Return to main menu")
        inp_info = input("\n-> ")

        
        # Commercial Banking information
        if inp_info == "A" or inp_info == "a":
            banking_commerce()

        # Insurance information
        elif inp_info == "B" or inp_info == "b":
            insurance()
        
        # Investment Banking information
        elif inp_info == "C" or inp_info == "c":
            banking_investment()

        # Accounting information
        elif inp_info == "D" or inp_info == "d":
            accounting()

        # Impact on jobs information
        elif inp_info == "E" or inp_info == "e":
            jobs()


        # Allows return to main menu after choosing an area of information
        # or by choosing option E.
        if inp_info == "A" or inp_info == "a" or inp_info == "B" or \
           inp_info == "b" or inp_info == "C" or inp_info == "c" or \
           inp_info == "D" or inp_info == "d" or inp_info == "E" or \
           inp_info == "e" or inp_info == "F" or inp_info == "f":
            
            print()
            again = repeat() # Repeats if user doesn't want to return to menu.
            if again == False: # Returns to main menu.
                return False

        # Error check
        else:
            print("\n[Choose an actual option!]")
            pass




# QUIZ SECTION -----------------------------------------------------------

# Loops question until there's a valid input.
def question(problem,c1,c2,c3,c4):
    while True:
        print(problem)
        print()
        print(c1) # Choice 1 will be assigned the letter A in string.
        print(c2) # Choice 2 will be assigned the letter B in string.
        print(c3) # Choice 3 will be assigned the letter C in string.
        print(c4) # Choice 4 will be assigned the letter D in string.
        
        inp_answer = input("\n-> ")

        if inp_answer == "A" or inp_answer == "a" or inp_answer == "B" or \
           inp_answer == "b" or inp_answer == "C" or inp_answer == "c" or \
           inp_answer == "D" or inp_answer == "d":
            return inp_answer
        
        else: # Error check
            print("\n[Choose an actual answer!]")


def quiz():
    again = True
    
    while again == True: # Keeps the loop going until again = False.
        print("\n----------------------------------------------------------\n")
        print("This quiz will consist of 5 questions.")

        # QUESTIONS ---
        # Question 1
        a1 = question(
            "\nIn order to obtain a mortgage, you must...",
            "A - Pay a downpayment and agree to use the house as collateral",
            "B - Pay a downpayment and pray to god that they accept",
            "C - Buy the whole house",
            "D - Agree to use the house as collateral")


        # Question 2
        a2 = question(
            "\nMonthly insurance premiums for a specific insurance \n\
are calculated by the insurance company...",
            "A - Looking at the customer’s financial history",
            "B - Looking at the customer's related circumstances & background",
            "C - Examining the customer’s criminal history",
            "D - Looking at the customer’s ability to pay back loans")
        
        # Question 3
        a3 = question(
            "\nHow does technology help with insurance fraud?",
            "A - They detect it before sending in a robot hit squad",
            "B - They don’t",
            "C - They analyze people's social media accounts for evidence",
            "D - They flag it for the insurance company to review")
        
        # Question 4
        a4 = question(
            "\nWhat are stock screeners?",
            "A - Tools that predict the performance of a stock’s company",
            "B - Tools that analyze the performance of a stock’s company",
            "C - Tools that filter out companies depending on the inputted \
requirements",
            "D - Tools that keep track of the stock market")
        
        # Question 5
        a5 = question(
            "\nHow do accounting software impact businesses?",
            "A - They present them in a visually-appealing way",
            "B - They instantly perform repetitive tasks",
            "C - They make financial information available on databases, \n\
        which can be accessed anywhere",
            "D - They make basic accounting much easier")


        # ANSWERS ---
        correct = 0
        QUESTIONS = 5 #Constant

        #Q1: A is correct
        if a1 == "A" or a1 == "a":
            correct += 1
        #Q2: B is correct
        if a2 == "B" or a2 == "b":
            correct += 1
        #Q3: D is correct
        if a3 == "D" or a3 == "d":
            correct += 1
        #Q4: C is correct
        if a4 == "C" or a4 == "c":
            correct += 1
        #Q5: All are correct
        correct += 1

        score = (correct / QUESTIONS) * 100 #Score percentage
        
        print("\nYou got " + str(correct) + " questions correct, \
that's a " + str(int(score)) + "%!")
        
        #Responses if quiz went well or not.
        if correct < 3:
            print("Better luck next time!")
        else:
            print("Wow, great job!")


        again = repeat() # Repeats program if True.
        if again == False: # Again. User is returned to main menu if False.
            return False




# SOURCES SECTION ---------------------------------------------------------

def sources():
    again = True
    
    while again == True: # You know the drill.
        print('''
                             ____CREDITS____

--General--
- https://www.michaelpage.ca/advice/career-advice/growing-your-career/
  11-types-financial-services-and-institutions [Fri 23]
  
- https://www.hcltech.com/technology-qa/what-is-the-impact-of-technology-on-
  financial-services  [Fri 23]
  
- Me ;)

------------------
--Commercial Banking--
- https://cba.ca/technology-innovation-banking [Fri 23]

- https://www.quora.com/How-do-people-do-financial-transactions-before-the-
  invention-of-the-ATM  [Fri 23]

---------
--Insurance--
- https://cadabra.studio/blog/how-is-the-technology-changing-the-insurance-
industry-everything-about-insurtech [Sat 24]

- https://www.ocs.help/blog/how-technology-helps-battle-insurance-fraud
  [Sat 24]

------------------
--Investment Banking--
- https://medium.com/banking-at-michigan/how-technology-impacts-and-will-change
  -the-investment-banking-industry-5d85903d2c9e  [Sat 24]
  
- https://www.hcltech.com/technology-qa/what-role-does-technology-play-in-
  investment-banking [Sat 24]
  
-  https://www.sec.gov/news/studies/techrp97.htm  [Sat 24]

- https://investorjunkie.com/robo-advisors/automatic-rebalancing/  [Sat 24]

- https://www.investopedia.com/articles/professionals/111715/day-life-
  investment-banker.asp [Sun 25]

- https://www.investopedia.com/articles/investing/111114/whats-role-investment
  -bank.asp [Sun 25]

----------
--Accounting--
- https://www.lsbf.edu.sg/blog/innovation-and-technology/how-has-technology-
  impacted-the-finance-and-accounting-industry/  [Sat 24]
  
- https://reader.elsevier.com/reader/sd/pii/S1877042811024621?token=EE07662A
  2B5C530E10FF44660A779666BDBDC306267162DF70107A580F6411492AB34FB5D3DC014F0E
  51E0B13DBAEE05&originRegion=us-east-1&originCreation=20210725012829  [Sat 24]
        ''')

        again = repeat() 
        if again == False: # You know the drill.
            return False







'''MAIN PROGRAM'''

# MAIN MENU ---------------------------------------------------------------
end = False #Used to end the main program.

while end == False: # Continuosly loops program until end is set to True.

    # Title
    print('''
-------------------------------------------------------------------------
 ___ _         ___ _                 _     _   ___      _               
|_ _| |_ ___  | __<_._ _ ___._ _ ___<_>___| | | ___ _ _| |_ _ _ _ _ ___ 
 | || . / ._> | _>| | ' <_> | ' / | | <_> | | | _| | | | | | | | '_/ ._>
 |_||_|_\___. |_| |_|_|_<___|_|_\_|_|_<___|_| |_|`___| |_| `___|_| \___.

-------------------------------------------------------------------------

BY GORDON
    ''') 

    # Welcome message
    print("Welcome to the Financial Future program! \n\n\
This program was made to inform you of the impacts that technology \n\
has made on financial services.") 

    # Options message
    print("\n__To get started, please choose an option from below__")
    print ("A - Exit  |  B - Information  |  C - Quiz  |  D - Sources") 

    # Input
    inp = input("\n-> ")


    
    # EXIT SECTION
    if inp == "A" or inp == "a":
        end = leave() # Ends the loop, always returns True.

    
    # INFORMATION SECTION
    elif inp == "B" or inp == "b":
        end = information() # Loops back to program, always returns False.


    # QUIZ SECTION
    elif inp == "C" or inp == "c":
        end = quiz() # Loops back to program, always returns False.


    # SOURCES SECTION
    elif inp == "D" or inp == "d":
        end = sources() # Loops back to program, always returns False.


    # Error check
    else:
        print("\n[Pick an actual option!]")
