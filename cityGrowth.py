#!/usr/bin/python3

import math

# Python code to satisfy curisity, variables to follow.
# TODO - vars go here
# isDebug - boolean - specifies if debug mode is toggled

isDebug = False


#debugging area
#prints log base 10 of 10, to make sure correct values are being used
#prints log base e of 10, to make sure correct values are being used
if isDebug:
    print("!!debug mode on!!")
    print("log base 10 of 10: ",end="")
    print(math.log(10,10), end = "")
    print(" (should be 1.0)")
    print("log base e of 10: ",end="")
    print(math.log(10), end = "")
    print(" (should be approx 2.302585092994)")
    print("log base 10 of 29,000,000,000: ",end="")
    print(math.log(29000000000,10), end = "")
    print(" (should be approx. 10.4623979979)")


#main code
print("Welcome to the City Growth calculator!\nDeveloped by Malokai Persoff\n\n\n")
print("This is designed to solve the following problem:", end="\n\n")
print("Country (name) has a growth rate of (growth rate)% per year")
print("The population is currently (population) and the land area is (land area) sq yards")
print("Assuming the growth rate continues and is exponential, how long until there will be one person for every sq yard of land?")
print("Loading functions...")


#converts percent num (example 100) to decimal (for 100 it would become 1.0)
#newPr - float - converts num to a float and devides by 100
def percentToDecimal( num ):
    if isinstance(num, str):
        num.strip('%')
        if isDebug: print("\n...(debug)converted input from string...\n")
    newPr = float(num)/100
    if isDebug: print("...(debug)function percentToDecimal converted \""+num+"\" to "+str(newPr)+"...")
    return newPr

if isDebug: print("function percentToDecimal loaded")


#do problem verbosely
def problemVerbose():
    print("Please input values as they appear")
    print("A country named ", end="")
    cName = str(input())
    print("Has a growth rate of (enter number)", end="")
    try:
        eGR = input()
        cGR = percentToDecimal(eGR)
    except ValueError:
        print("\nInvalid selection, please try again")
    else:
        print("% per year. The population is currently ", end="")
        try:
            popCount = int(input())
        except ValueError:
            print("\nInvalid selection, please try again")
        else:
        
            print("And the land area (in sq yards) of "+cName+" is currently ", end="")
            try:
                landA = int(input())
            except ValueError:
                print("\nInvalid selection, please try again")
            else:    
                print("Assuming the growth rate continues and is exponential, how long until there will be one person for every sq yard of land?\n\n\n")
                print("When the population will reach "+str(landA)+" there will be one person per square yard.")
                print("The formula for exponental growth is a(1+r)^(t), where a is the starting value, r is the percentage of growth, and t is the ammount of time\n")
                print("In this case, we are solving for t.\n")
                print("Our equasion is "+str(landA)+"="+str(popCount)+"(1+"+str(cGR)+")^t\n")
                print("We want to isolate t, so lets simplify and bring t down from its exponental position. we can do this by using log.\n")
                simplecGR = cGR+1
                print("Our equasion becomes log("+str(landA)+")=log("+str(popCount)+")+t log("+str(simplecGR)+").\n")
                print("We now covert all the log values into regular numbers. this makes the equasion ", end="")
                if isDebug: print("...(debug) calculating ... ")
                # calculate new values
                newLandA = float(math.log10(landA))
                if isDebug: print("...(debug)calculated land area log10 as "+str(newLandA)+"...")
                newPopCount = float(math.log10(popCount))
                if isDebug: print("...(debug)calculated population log10 as "+str(newPopCount)+"...")
                newSimplecGR = float(math.log10(simplecGR))
                if isDebug: print("...(debug)calculated simplified var b log10 as "+str(newSimplecGR)+"...")
                print(""+str(newLandA)+"="+str(newPopCount)+"+t("+str(newSimplecGR)+")", end="\n\n\n")
                print("We are solving for t, so lets isolate t by first subtracting "+str(newPopCount)+" from both sides.", end="\n\n\n")
                print("Our equasion is now "+str(newLandA)+"-"+str(newPopCount)+"= t("+str(newSimplecGR)+")", end="\n\n\n")
                print("Finaly we devide both sides by "+str(newSimplecGR)+" and flip the equasion.", end="\n\n\n")
                print("Our equasion is now t=("+str(newLandA)+"-"+str(newPopCount)+")/"+str(newSimplecGR))
                print("\n\n\nNow we just need to solve!")
                if isDebug: print("...(debug) calculating ... ")
                combin = float(newLandA-newPopCount)
                if isDebug: print("...(debug) combined terms are equal to"+str(combin)+" ... ")
                tIs = combin/newSimplecGR
                if isDebug: print("...(debug) t is calculated as "+str(tIs)+" ... ")
                print("By solving, we can now see that t="+str(tIs)+". How many decimal points should we round to? ", end="")
                try:
                    roundToThisDecimal = str(input("(defaults to 3): "))
                except ValueError:
                    print("\nInvalid selection, please try again!")
                else:
                    if roundToThisDecimal=="": roundToThisDecimal="3"
                    try:
                        roundTime=int(roundToThisDecimal)
                    except ValueError:
                        print("\nInvalid selection, please try again!")
                    else:
                        fullT=round(tIs, roundTime)
                        print("t, when rounded to "+str(roundTime)+" decimal points, is "+str(fullT))
                        print("Therefore, it will take "+str(fullT)+" years for "+cName+" to have one populaton for each square yard of land.")
                        print("Rounded to the nearest year, it becomes "+str(round(fullT)), end="\n\n\n\n\n\n\n\n")
                        if isDebug: print("...(debug) t is "+str(fullT)+" rounded t is "+str(round(fullT))+"... ")
        
if isDebug: print("function problemVerbose loaded")

#do problem nonverbosely
def problemNVerbose():
    print("Please input values as they appear")
    print("A country named ", end="")
    cName = str(input())
    print("Has a growth rate of (enter number)", end="")
    try:
        eGR = input()
        cGR = percentToDecimal(eGR)
    except ValueError:
        print("\nInvalid selection, please try again")
    else:
        print("% per year. The population is currently ", end="")
        try:
            popCount = int(input())
        except ValueError:
            print("\nInvalid selection, please try again")
        else:
        
            print("And the land area (in sq yards) of "+cName+" is currently ", end="")
            try:
                landA = int(input())
            except ValueError:
                print("\nInvalid selection, please try again")
            else:    
                print("Assuming the growth rate continues and is exponential, how long until there will be one person for every sq yard of land?\n\n\n")
                simplecGR = cGR+1
                if isDebug: print("...(debug) calculating ... ")
                # calculate new values
                newLandA = float(math.log10(landA))
                if isDebug: print("...(debug)calculated land area log10 as "+str(newLandA)+"...")
                newPopCount = float(math.log10(popCount))
                if isDebug: print("...(debug)calculated population log10 as "+str(newPopCount)+"...")
                newSimplecGR = float(math.log10(simplecGR))
                if isDebug: print("...(debug)calculated simplified var b log10 as "+str(newSimplecGR)+"...")
                if isDebug: print("...(debug) calculating ... ")
                combin = float(newLandA-newPopCount)
                if isDebug: print("...(debug) combined terms are equal to"+str(combin)+" ... ")
                tIs = combin/newSimplecGR
                if isDebug: print("...(debug) t is calculated as "+str(tIs)+" ... ")
                print("t="+str(tIs)+". How many decimal points should we round to? ", end="")
                try:
                    roundToThisDecimal = str(input("(defaults to 3): "))
                except ValueError:
                    print("\nInvalid selection, please try again!")
                else:
                    if roundToThisDecimal=="": roundToThisDecimal="3"
                    try:
                        roundTime=int(roundToThisDecimal)
                    except ValueError:
                        print("\nInvalid selection, please try again!")
                    else:
                        fullT=round(tIs, roundTime)
                        print("t, when rounded to "+str(roundTime)+" decimal points, is "+str(fullT))
                        print("Therefore, it will take "+str(fullT)+" years for "+cName+" to have one populaton for each square yard of land.")
                        print("Rounded to the nearest year, it becomes "+str(round(fullT)), end="\n\n\n\n\n\n\n\n")
                        if isDebug: print("...(debug) t is "+str(fullT)+" rounded t is "+str(round(fullT))+"... ")

if isDebug: print("function problemNVerbose loaded")

#may add more functions

print("Done loading!")

#main loop, loops by recursion until exited
while True:
    print("Please select from the following options:")
    print("0: Exit program")
    print("1: Solve problem (verbose)")
    print("2: Sove Problem (non-verbose)")
    if isDebug: print("3: Disable debbug option\n")
    else: print("3: Enable debug option\n")
    usrre = input("I want to select: ")
    selection = int(usrre)
    if selection == 0:
        print("Ok, exiting.")
        break
    elif selection == 1:
        print("Ok, starting problem verbosely")
        problemVerbose()
    elif selection == 2:
        print("Ok, starting problem non-verbosely")
        problemNVerbose()
    elif selection == 3:
        print("Ok, toggling debug mode")
        if isDebug: print("dedbug mode turned off")
        if isDebug: isDebug = False
        else: isDebug = True
    else:
        print("selection not found, please try again.")
