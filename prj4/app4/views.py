from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vc(request,sentence): 
    vow_cnt=0
    cons_cnt=0
    vow_dict=dict()
    cons_dict=dict()
    for letter in sentence:
        if letter.isalpha():
            if letter in "aeiouAEIOU":
                vow_cnt+=1
                vow_dict[letter]=vow_dict.get(letter,0)+1
            else:
                cons_cnt+=1
                cons_dict[letter]=cons_dict.get(letter,0)+1

    result="<h1>%d Vowels and %d Consonants</h1>" % (vow_cnt,cons_cnt) 
    result+="<h2>Vowel Counter</h2>" 

    for key,value in vow_dict.items(): 
        result+="<p>%s:%d</p>"%(key,value) 
        result+="<h2>Consonant Counter</h2>"

        for key,value in cons_dict.items(): 
            result+="<p>%s:%d</p>"%(key,value) 
            return HttpResponse(result) 