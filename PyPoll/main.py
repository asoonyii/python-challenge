import os
import csv

#Collect data
csvpath= os.path.join("election_data.csv")

#def last_row(election_data):
with open(csvpath, 'r') as csvfile:
    csvlines= csv.reader(csvfile, delimiter=',')
    csvheader= next(csvlines)
    #Set initial count for votes and each candidate
    count = 0
    candidateK=0
    candidateC= 0
    candidateL= 0
    candidateO = 0
    percentK= 0
    percentC =0
    percentL= 0
    percentO= 0
    for votes in csvlines:
        #Get number of votes using total rows
        count= count +1
        
        #Calculate votes and percentage per candidate
        if votes[2] == "Khan":
            candidateK += 1
            percentK = (candidateK/count)*100
        if votes[2] == "Correy":
            candidateC += 1
            percentC = (candidateC/count)*100
        if votes[2] == "Li":
            candidateL += 1
            percentL = (candidateL/count)*100
        if votes[2] == "O'Tooley":
            candidateO += 1
            percentO = (candidateO/count)*100

    #scores=["candidateK","candidateC","candidateL","candidateO"]
    print("")
    print("Election Results")
    print("-----------------------")
    print("Total Votes: ", str(count))
    print("-----------------------")
    print("Khan:", str(round(percentK)) + "%", "("+ str(candidateK) + ")")
    print("Correy:", str(round(percentC)) + "%", "("+ str(candidateC) + ")")
    print("Li:", str(round(percentL)) + "%", "("+ str(candidateL) + ")")
    print("O'Tooley:", str(round(percentO)) + "%", "("+ str(candidateO) + ")")
    print("-----------------------")
    print("-----------------------")

with open("main.txt","w") as textfile:
    textfile.write("")
    textfile.write("Election Results")
    textfile.write("\n-----------------------")
    textfile.write("\nTotal Votes: "+ str(count))
    textfile.write("\n-----------------------")
    textfile.write("\nKhan: "+ str(round(percentK)) + "%"+ " ("+ str(candidateK) + ")")
    textfile.write("\nCorrey: "+ str(round(percentC)) + "%"+ " ("+ str(candidateC) + ")")
    textfile.write("\nLi: "+ str(round(percentL)) + "%"+ " ("+ str(candidateL) + ")")
    textfile.write("\nO'Tooley: "+ str(round(percentO)) + "%"+ " ("+ str(candidateO) + ")")
    textfile.write("\n-----------------------")
    textfile.write("\n-----------------------")
    

        
