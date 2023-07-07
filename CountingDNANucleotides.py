#establish what are the 4 unique nucleotides
Nucleotides = ["A", "C", "G", "T"]

userDNA = input("Enter a DNA sequence: ") #ask user for unique DNA sequence of interest
if type(userDNA) == str: #ensure that the entered DNA is a string and continue to validate the sequence according to established nucleotides
   def validateSeq(dna_seq): #validatesequence function accepts a string, creating a tmpseq
    tmpseq = dna_seq.upper() #capitalizes all nucleotides to avoid case sensitivity
    for nuc in tmpseq: #loops through each to ensure user's input matches the 4-characters from Nucleotides, and if not will prompt user to re-enter a valid sequence
        if nuc not in Nucleotides:
            print("This is not a DNA sequence. Please enter a valid DNA sequence next time.")
            quit()
    return tmpseq 
   
print("Your sequence has been validated as:", validateSeq(userDNA)) #checkpoint 1: check whether DNA sequence will be processed to avoid case sensitivity.
userDNA = userDNA.upper() #Python string methods do not modify the string; they only return the modified version. As such must modify the validated string to enter next function

#this function counts the frequency of unique nucleotides based on user input and accepts a string (seq) which was validated above
def countNucleotides(seq):
    tmpFreq = {"A": 0, "C":0, "G":0, "T":0} #defines a temporary frequency dictionary to index the starting
    for nuc in seq: #loops through the function and creates a value for every iteration the unique letter code is registered
        tmpFreq[nuc] += 1
    return tmpFreq

result = countNucleotides(userDNA)
print("Your sequence has the following nucleotide frequencies:", result) #displays frequency of lettering

#updating the code on 7.6.23 to include the Guanine-to-Cytosine (GC) content statistic. The GC content influences binding stability and it is known that primer sequences with 40% - 60% GC content ensures stable binding of primers to templates.
#GC-rich sequences are more stable than those compare to sequences with low GC content.
def guanineCytosine(seq): #will provide the GC content for the sequence
    return round((seq.count('C') + seq.count('G'))/len(seq) * 100)

print("The Guanine-to-Cytosine (GC) content of your sequence is: ", guanineCytosine(validatedSeq),"%")
print()
