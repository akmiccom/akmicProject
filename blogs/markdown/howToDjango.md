---
title : How to django
category : python
author : Makoto Yaugchi
---

# How To django

[TOC]

## 調査履歴

結構難しい

### update_or_create()
[]()
```
obj, created = Person.objects.update_or_create(
    first_name="John",
    last_name="Lennon",
    defaults={"first_name": "Bob"},
)
```

## models

modelについて

### models Fields
```
|    Fields     | Description        |
| :-----------: | :----------------- |
|   CharField   | タイトル等の文字列 |
| IntegerField  | 数値               |
|   TextField   | テキスト           |
|   DateField   | 日付               |
| DateTimeField | 日時               |
|  EmailField   | email              |
|   UrlField    | URL                |
|   FileField   | upload files       |
|  ImageField   | image files        |
```


### models Options

[モデルフィールド 設定テンプレート](https://qiita.com/okoppe8/items/a1149b2be54441951de1)
```
|    Option    | Description        |
| :----------: | :----------------- |
| verbose_name | カラム名           |
|    blank     | ブランク           |
|     null     |                    |
|   default    | デフォルト値       |
|   editable   | フォームの表示     |
|  max_length  | 最大文字数         |
|  help_text   | ツールチップの内容 |
```

## genaral View Class
```
| Name         | OverView                        | Example |
| ------------ | ------------------------------- | ------- |
| View         | get(), post()などhttpメソッド用 |
| TemplateView | 代表的                          |
| ListView     | 一覧表示                        |
| DetailView   | 詳細表示                        |
| CreateView   | 作成                            |
| UpdateView   | 更新                            |
| DeleteView   | 削除                            |
| FormView     | フォーム                        |
| LoginView    | ログイン                        |
| APIView      | 外部API                         |
```

## TemplateView

TemplateViewの説明

## フォルダ構成(デフォルトからの変更点)

[Reference site : Django ディレクトリ構成とファイル設定](https://note.com/saito_pythonista/n/nb95c54f4c327)
```
<projectName>                 # project directry
├── config                   # setting
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py                
│   └── wsgi.py 
├── accounts                  # accounts app directry
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py             
│   ├── migrations  
│   ├── models.py
│   ├── tests.py
│   └── views.py              
├── blogs                     # blogs app
├── media                     # media files etc for user
├── QA                        # other app 
├── static                    # static files
│   ├── css
│   ├── images                # for admin
│   └── js
├── templates                 # html files
│   ├── accounts
│   ├── blogs
│   ├── QA
│   └── base.html
└── manage.py                 # manage.py
```

### Process

1. django-admin startproject config .
2. python manage.py startapp accounts
3. python manage.py startapp blogs
4. mkdir media
5. mkdir static
   1. cd static
   2. mkdir css
   3. mkdir js
6. mkdir templates
   1. cd templates
   2. mkdir accounts
      1. new-item urls.py
      2. new-item forms.py
   3. mkdir blogs
      1. new-item urls.py
      2. new-item forms.py
   4. new-item base.html

### Setting files

1. config/urls.py
   ```
   from django.contrib import admin
   from django.urls import path, include
   from config.views import TopPageView

   urlpatterns = [
      path('admin/', admin.site.urls), 
      path('', TopPageView.as_view(), name='topPage'),
      path('blogs/', include('blogs.urls')),
      path('accounts/', include('accounts.urls')),
   ]
   ```
2. config/setting.py
   1. INSTALLED_APPSの設定
   2. templatesの設定

