from django.shortcuts import render


def index( request ):
    return render( request, 'index.html' )


def about( request ):
    return render( request, 'about.html' )


def contact( request ):
    return render( request, 'contacts.html' )


def signup( request ):
    return render( request, 'signup.html' )


def login( request ):
    return render( request, 'login.html' )


def thanks( request ):
    # global fname, lname, mail, country, phnum
    # variables = request.POST.get('user provided value for name from the form that was processed through action
    # # to the url that got this function indexed.', 'default value')
    # fname = request.POST.get('firstname','default')
    # lname = request.POST.get('lastname','default')
    # mail = request.POST.get('email','default')
    # country = request.POST.get('country','default')
    # phnum = request.POST.get('phnumber','default')
    # params = [fname,lname,mail,country,phnum]
    return render( request, 'thanks.html' )


def welcome( request ):
    fullnamee = request.POST.get( 'fullname', 'default' )
    # print(fullnamee)
    try:
        fullname = fullnamee.split( )
        params = { 'fname': fullname[ 0 ], 'lname': fullname[ 1 ] }
    except:
        params = { 'fname': fullnamee, 'lname': '' }

    # params = {'fname':(fullname.split(" "))[0],'lname':(fullname.split(" "))[1]}

    return render( request, 'welcome.html', params )


def user_profile( fname, lname, mail, country, phnum ):
    return 0


def analyzed( request ):
    user_text = request.POST.get( 'user_text', 'default' )
    # select box value
    purpose = request.POST.get( 'purpose', 'default' )
    bold = request.POST.get( 'bold', 'default' )
    # initializing final text to be blank and adding required changes to text
    analyzed_text = ''

    if purpose == 'removepunc':
        punc = '''~!@#$%^&*()_+`-=\{\}|[]\\:";'<>,.?/'''
        for char in user_text:
            if char not in punc:
                analyzed_text = analyzed_text + char

    elif purpose == "capfirst":
        sentences = user_text.split( "." )
        for i in range( len( sentences ) ):
            analyzed_text += sentences[ i ].capitalize( ) + '.'

    elif purpose == 'upper':
        analyzed_text = user_text.upper

    elif purpose == "lower":
        analyzed_text = user_text.lower

    elif purpose == "list":
        sentences = user_text.split( "." )
        for i in range( len( sentences ) ):
            analyzed_text += f'{i + 1}:  ' + sentences[ i ] + '\n'

    elif purpose == "charcount":
        n = len( user_text )
        for char in user_text:
            if char == "\n":
                n -= 2
        analyzed_text = f"Total number of character in text : {n}"

    elif purpose == "wordcount":
        mod_text = ''
        for index, char in enumerate( user_text ):
            if not (user_text[ index ] == " " and user_text[ index + 1 ] == " "):
                mod_text += char

        n = len( mod_text.split( " " ) )
        analyzed_text = f"Total number of words in text : {n}"

    else:
        analyzed_text = "Invalid Purpose"

    params = { 'analyzed': analyzed_text, 'initial': user_text }

    return render( request, './analyzed.html', params )


def textedit( request ):
    return render( request, 'index2.html' )
