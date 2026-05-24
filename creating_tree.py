from bst import tree
from pdf_to_string import extract_with_pypdf
from division import get_sequences_with_acr
from quick_sort import QuickSortR

text = extract_with_pypdf('biblia.pdf')

acronyms = get_sequences_with_acr(text)

t = tree()

for key, value in acronyms:
    t.Add(key, value)

t.PrintIO()
