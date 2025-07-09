from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

Books = [
    {
        'Id' : 1,
        "Name" : 'How to win friends',
        "Author" : "Dale Carngie",
        'Description' : 'Influence people with your words'
    },
    {
        'Id': 2,
        "Name": 'Measure your life',
        "Author": "Tyrn Fischo",
        'Description' : '17 Modules for to shine your Spiritual Growth'
    },
    {
        'Id': 3,
        "Name": 'Rich Dad Poor Dad',
        "Author": "Robort kiyosaki",
        'Description' : 'Invest your money in variety fields'
    }
]


def BooksCollection(request):
    html = ""
    for book in Books:
        html += f"""
        <div>
        <p>Nameofthe book :{book['Name']}, Author : {book['Author']}</p>
        <h1>Description : {book['Description']}</h1>
        
        </div>
        """
    return HttpResponse(html)



# def CurrentPage(request,id):
#     print(id + 2)
#     print(type(id))
#     return HttpResponse(id + 2)


def Research(request, id):
    for book in Books:

        if book['Id'] == id:
            book_dict = book
            break

    html = f"""
    <div>
    <h2>{book_dict['Name']}</h2>
    <p>{book_dict['Description']}</p>
    </div>

    """
    return HttpResponse(html)
