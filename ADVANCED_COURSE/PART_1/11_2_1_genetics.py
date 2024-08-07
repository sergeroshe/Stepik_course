DNA_LIST = ['G', 'C', 'T', 'A']
RNA_LIST = ['C', 'G', 'A', 'U']
DNA_RNA_DICT = {dna: rna for dna, rna in zip(DNA_LIST, RNA_LIST)}

dna_input_string = input()
rna_result_string = ''
for dna_char in dna_input_string:
    rna_result_string += DNA_RNA_DICT[dna_char]

print(rna_result_string)