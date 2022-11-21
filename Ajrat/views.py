from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная</h1>')

def info(request,name,age):
    return HttpResponse(f"""<h2>About</h2> <a href="http://127.0.0.1:8000/contact">Contact</a> <a href="http://127.0.0.1:8000/about">About (стр.2)</a> <br> <p>Имя: {name}</p> <br> <p>Возраст: {age}</p>""")

def about(request,From,uspev,stlo):
    return HttpResponse(f"""<h2>About (стр.2)</h2> <a href="http://127.0.0.1:8000/">About (стр.1)</a> <a href="http://127.0.0.1:8000/contact">Contact</a>  <br> <p>Откуда: {From}</p> <br> <p>Успеваемость в школе: {uspev}</p> <br> <p>Люблю ли я учиться:{stlo}</p>""")

def contact(request,Tg,Github,tel):
    return HttpResponse(f"""<h2>Contact </h2> <a href="http://127.0.0.1:8000/">About (стр.1)</a> <a href="http://127.0.0.1:8000/about">About (стр.2)</a> <br> <p>Мой телеграмм: {Tg}</p> <br> <p>Номер телефона: {tel}</p> <br> <p>Мой GitHub: {Github}</p>""")