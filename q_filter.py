from django.db.models.query_utils import Q

from django.db.models import CharField
from django.db.models.functions import Length
CharField.register_lookup(Length, 'length')
# 1- Librat me titullin 'Algorithms' ose 'C Language'
# 2- Librat me te vjeter se viti 2000 ose me te rinj se 2010
# 3- Librat me autorin me emrin 'Dritero' ose librat me autorin me moshe me te madhe se 60.
# 4- Librat me shtepine botuese ne Tirane ose Durres.
# 5- Faqet e librave me emrin 'Algorithms' ose 'C Language'
# 6- Faqet e librave me cmimin me te madh se 1000 ose me autor 'Dritero'
# 7- Autoret me moshe me te madhe se 50 ose me emrin 'Dritero'
# 8- Shtepite botuese me vendodhje ne Tirane ose Durres.
# 9- Faqet e librave me cmim 1000 ose 1500.
# 10- Faqet me kontent 1000 ose faqet e librave me cmim 1000.
# 11- Faqet me numer me te vogel se 100 ose 

# faqet me kontent me shum se 1000 karaktere dhe 
# liber me emrin 'Algorithms'























# - 1
from django.db.models.query_utils import Q
from app.models import Author, Book, Page, Publisher

from django.db.models import CharField
from django.db.models.functions import Length
CharField.register_lookup(Length, 'length')

# 1
algorithms_and_c = Book.objects.filter(Q(title='Algorithms') | (Q(title='C Language') & Q(price=1000)))
print("Librat me titullin 'Algorithms' ose 'C Language'")
print(algorithms_and_c)
print("-------")

# 2
books_age = Book.objects.filter(Q(publish_date__year__gt=2010) | Q(publish_date__year__lt=2000))
print("Librat me te vjeter se 2000 ose me te rinj se 2010")
print(books_age)
print("-------")

# 3
author_age = Book.objects.filter(Q(author__name='Dritero') | Q(author__age__gt=60))
print("Librat me autorin me emrin 'Dritero' ose me moshe me te madhe se 60.")
print(author_age)
print("-------")

# 4
publisher_city = Book.objects.filter(Q(publisher__city='Tirane') | Q(publisher__city='Durres'))
print("Librat me shtepine botuese ne Tirane ose Durres.")
print(publisher_city)
print("-------")

# 5
pages = Page.objects.filter(Q(book__title='Algorithms') | Q(book__title='C Language'))
print("Faqet e librave me emrin 'Algorithms' ose 'C Language'")
print(pages)
print("-------")

# 6
pages_price = Page.objects.filter(Q(book__price__gt=1000) | Q(book__author__name='Dritero'))
print("Faqet e librave me cmimin me te madh se 1000 ose me autor 'Dritero'")
print(pages_price)
print("-------")

# 7
author_age_name = Author.objects.filter(Q(age__gt=50) | Q(name='Dritero'))
print("Autoret me moshe me te madhe se 50 ose me emrin 'Dritero'")
print(author_age_name)
print("-------")

# 8
publish_house = Publisher.objects.filter(Q(city='Tirane') | Q(city='Durres'))
print("Shtepite botuese me vendodhje ne Tirane ose Durres.")
print(publish_house)
print("-------")

# 9
page_for_book_price = Page.objects.filter(Q(book__price=1000) | Q(book__price=1500))
print("Faqet e librave me cmim 1000 ose 1500.")
print(page_for_book_price)
print("-------")

# 10
page_content = Page.objects.filter(Q(content__length__gt=1000) | Q(book__price__gt=1000))
print("Faqet me kontent 1000 ose faqet e librave me cmim me te madh se 1000.")
print(page_content)
print("-------")

# 11
page_content = Page.objects.filter(Q(number__lt=100) | (Q(content__length__gt=1000) & Q(book__title='Algorithms')))
print("Faqet me numer me te vogel se 100 ose faqet me kontent me shum se 1000 karaktere dhe liber me emrin 'Algorithms'")
print(page_content)
print("-------")