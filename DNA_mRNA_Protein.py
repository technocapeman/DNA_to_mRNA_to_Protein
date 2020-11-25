# ---------- Import Statements ----------
import sys

# ---------- Dictionaries for Transcription and Translation ----------
transcription = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C",
    " ": " ",
}

translation = {
    "['U', 'U', 'U']": "Phenylalanine",
    "['U', 'U', 'C']": "Phenylalanine",
    "['U', 'U', 'A']": "Leucine",
    "['U', 'U', 'G']": "Leucine",
    "['U', 'C', 'U']": "Serine",
    "['U', 'C', 'C']": "Serine",
    "['U', 'C', 'A']": "Serine",
    "['U', 'C', 'G']": "Serine",
    "['U', 'A', 'U']": "Tyrosine",
    "['U', 'A', 'C']": "Tyrosine",
    "['U', 'A', 'A']": "STOP",
    "['U', 'A', 'G']": "STOP",
    "['U', 'G', 'U']": "Cysteine",
    "['U', 'G', 'C']": "Cysteine",
    "['U', 'G', 'A']": "STOP",
    "['U', 'G', 'G']": "Tryptophan",
    "['C', 'U', 'U']": "Leucine",
    "['C', 'U', 'C']": "Leucine",
    "['C', 'U', 'A']": "Leucine",
    "['C', 'U', 'G']": "Leucine",
    "['C', 'C', 'U']": "Proline",
    "['C', 'C', 'C']": "Proline",
    "['C', 'C', 'A']": "Proline",
    "['C', 'C', 'G']": "Proline",
    "['C', 'A', 'U']": "Histidine",
    "['C', 'A', 'C']": "Histidine",
    "['C', 'A', 'A']": "Glutamine",
    "['C', 'A', 'G']": "Glutamine",
    "['C', 'G', 'U']": "Arginine",
    "['C', 'G', 'C']": "Arginine",
    "['C', 'G', 'A']": "Arginine",
    "['C', 'G', 'G']": "Arginine",
    "['A', 'U', 'U']": "Isoleucine",
    "['A', 'U', 'C']": "Isoleucine",
    "['A', 'U', 'A']": "Isoleucine",
    "['A', 'U', 'G']": "Methionine (START)",
    "['A', 'C', 'U']": "Threonine",
    "['A', 'C', 'C']": "Threonine",
    "['A', 'C', 'A']": "Threonine",
    "['A', 'C', 'G']": "Threonine",
    "['A', 'A', 'U']": "Asparagine",
    "['A', 'A', 'C']": "Asparagine",
    "['A', 'A', 'A']": "Lysine",
    "['A', 'A', 'G']": "Lysine",
    "['A', 'G', 'U']": "Serine",
    "['A', 'G', 'C']": "Serine",
    "['A', 'G', 'A']": "Arginine",
    "['A', 'G', 'G']": "Arginine",
    "['G', 'U', 'U']": "Valine",
    "['G', 'U', 'C']": "Valine",
    "['G', 'U', 'A']": "Valine",
    "['G', 'U', 'G']": "Valine",
    "['G', 'C', 'U']": "Alanine",
    "['G', 'C', 'C']": "Alanine",
    "['G', 'C', 'A']": "Alanine",
    "['G', 'C', 'G']": "Alanine",
    "['G', 'A', 'U']": "Aspartate",
    "['G', 'A', 'C']": "Aspartate",
    "['G', 'A', 'A']": "Glutamate",
    "['G', 'A', 'G']": "Glutamate",
    "['G', 'G', 'U']": "Glycine",
    "['G', 'G', 'C']": "Glycine",
    "['G', 'G', 'A']": "Glycine",
    "['G', 'G', 'G']": "Glycine",
}

# ---------- User Input (DNA Sequence) ----------
input_prompt = input(
    "Please enter the DNA sequence to be converted to mRNA. Please make sure that your DNA sequence starts with the start codon for accurate results: "
)
user_input = input_prompt.upper()
dna_sequence = user_input
list_dna_sequence = list(dna_sequence)
mRNA_sequence = ""
try:
    for i in dna_sequence:
        mRNA_sequence += transcription[i]
except:
    print(
        "Please make sure that your DNA sequence is valid. Re-run this program to re-enter a valid sequence."
    )
    sys.exit()
modified_mRNA_sequence = mRNA_sequence.replace(" ", "")
list_mRNA_sequence = list(modified_mRNA_sequence)
formatted_mRNA_list = [
    str(list_mRNA_sequence[x:x + 3])
    for x in range(0, len(list_mRNA_sequence), 3)
]

# ---------- Output (Amino Acids and mRNA Codons) ----------
amino_acid_number = 0
print(
    "After transcription and translation, here are the amino acids and their respective mRNA codons:"
)
try:
    for i in formatted_mRNA_list:
        amino_acid_number += 1
        if translation.get(i) == "STOP":
            print(amino_acid_number, ".", translation.get(i), i)
            print("\n")
            sys.exit()
        else:
            print(amino_acid_number, ".", translation.get(i), i)
except:
    print(
        "Please make sure that your DNA sequence is valid. Re-run this program to re-enter a valid sequence."
    )
    sys.exit()