from pdf_to_string import extract_with_pypdf
from quick_sort import QuickSortR

tekst = extract_with_pypdf('biblia.pdf')

def divide_text(text, length=4):
    text = text.split()
    lst = []
    for i in range(len(text)-3):
        fours = []
        for j in range(length): 
            try:
                fours.append(text[i+j])
            except IndexError:
                break
        lst.append(fours)
    return lst

def get_acronym(seq):
    acronym = ''
    for element in seq:
        acronym += element[0].capitalize()
    return (acronym, seq)

def get_sequences_with_acr(text):
    return [get_acronym(seq) for seq in divide_text(text)]

skroty = get_sequences_with_acr(tekst)

# print(skroty)

QuickSortR(skroty, 0, len(skroty)-1, 1)

print(skroty)
