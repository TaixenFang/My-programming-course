#5 - sample data
dna = 'atcgcgatgcgatgcg'

#6
dna = 'gctagctagctagcta'
exons = [ (0,3) , (5,8) ] # This defines the range of exons that we want to annotate
annot = list(dna.lower()) # This converts the sequence into a list of lowercase characters
for s,e in exons: # For loop in each exon range
    for i in range (s,e): # For loop for each position within that exon range
        annot[i] = annot [i].upper() # Making the annotated exons uppercase
print(''.join(annot)) # Joins the list back into string and prints it

#7 count number of times each nucleotide occurs
dna = 'gctagctagctagcta'
counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'} # Converting the DNA sequence to uppercase and prints the count of each nucleotide in the sequence
print(counts)

#8
dna = 'gtctagctagctagcta'
print(dna[::-1]) # Printing the DNA sequence in reverse order via python slicing