# I created the file _Anfrom
from django.http import HttpResponse
from django.shortcuts import render

def index2(request):
    return render(request,'index2.html') 

def analyze(request):
    # get the text from the user
    djtext=(request.GET.get('text','default'))
    removepunc=(request.GET.get('removepunc','off'))
    Uppercase=(request.GET.get('Uppercase','off'))
    Newline_remove=(request.GET.get('Newline_remove','off'))
    Extra_space_remove=(request.GET.get('Extra_space_remove','off'))
    
    if removepunc=='on' and Uppercase=='on' and (Newline_remove=='on' or Extra_space_remove=='on'):
        dict={}
        analyzed=""
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        analyzed=analyzed.upper()
        ans=""
        analyzed=analyzed.split()
        for index in range(len(analyzed)):
            if index==0:
                ans+=analyzed[index]
            else:
                ans+=" "
                ans+=analyzed[index]
        dict={'purpose':'Remove punctuations and Capitalize text and New line removed or Extra space removed' ,'analyzed_text':ans}
        return render(request,'analyze.html',dict)

    elif removepunc=='on' and Uppercase=='on':
        dict={}
        analyzed=""
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        analyzed=analyzed.upper()
        dict={'purpose':'Remove punctuations and Capitalized text','analyzed_text':analyzed}
        return render(request,'analyze.html',dict)

    elif removepunc=='on' and (Extra_space_remove=='on' or Newline_remove=='on'):
        dict={}
        analyzed=""
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        ans=""
        analyzed=analyzed.split()
        for index in range(len(analyzed)):
            if index==0:
                ans+=analyzed[index]
            else:
                ans+=" "
                ans+=analyzed[index]
        dict={'purpose':'Punctuations removed and Newline Removed ' ,'analyzed_text':ans}
        return render(request,'analyze.html',dict)        
    
    elif removepunc=='on':
        dict={}
        analyzed=""
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        dict={'purpose':'Remove punctuations' ,'analyzed_text':analyzed}
        return render(request,'analyze.html',dict)
    
    elif Uppercase=='on' and (Extra_space_remove=='on' or Newline_remove=='on'):
        djtext=djtext.upper()
        dict={}
        analyzed=""
        djtext=djtext.split()
        for index in range(len(djtext)):
            if index==0:
                analyzed+=djtext[index]
            else:
                analyzed+=" "
                analyzed+=djtext[index]
        dict={'purpose':'Capitalized text and Extra Space removed and New lined removed' ,'analyzed_text':analyzed}
        return render(request,'analyze.html',dict)
        
    elif Uppercase=='on' :
        dict={}
        analyzed=""
        for char in djtext:
                analyzed+=char.upper()
        dict={'purpose':'Capitalized text ' ,'analyzed_text':analyzed}
        return render(request,'analyze.html',dict)
    
    elif  Newline_remove=='on' or Extra_space_remove=='on':
        dict={}
        analyzed=""
        djtext=djtext.split()
        for index in range(len(djtext)):
            if index==0:
                analyzed+=djtext[index]
            else:
                analyzed+=" "
                analyzed+=djtext[index]
        dict={'purpose':'Newline Removed ' ,'analyzed_text':analyzed}
        return render(request,'analyze.html',dict)

    else:
        return HttpResponse("ERROR ! Please choose your option <br> What you want to do with your text")

# def cap_first(request):
#     return HttpResponse("capitalize")

# def newlineremover(request):
#     return HttpResponse("new line removed")

# def spaceRemove(request):
#     return HttpResponse("space removed")

# def charcount(request):
#     return HttpResponse("count the char")