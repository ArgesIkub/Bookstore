# 1- Gjeni te gjithe librat e Shtepise botuese 'Dituria'
# 2- Gjeni numrin e te gjitha faqeve te librave me autor 'Dostojevski'
# 3- Gjeni numrin e te gjitha faqeve te te gjithe librave.
# 4- Gjeni numrin e te gjitha faqeve te librave per secilen shtepi botuese.
# 5- Gjeni numrin e te gjithe librave per secilin autor.4
# 6- Gjeni te gjithe librat me te vjeter se viti '2000'
# 7- Gjeni librat me me shume faqe se 200 ose qe jane me te rinj se viti '2010'
# 8- Gjeni shtepite botuese me me shume se 2 libra te botuar ose me asnje liber te botuar.
# 9- Gjeni librat me me shume se 1000 germa.
# 10- Gjeni autorin me librin qe ka 256 germa.

from django.db.models.query_utils import Q
from app.models import Author, Book, Page, Publisher

# 1
dituria_books = Book.objects.filter(publisher__name='Dituria')
print("Gjeni te gjithe librat e Shtepise botuese 'Dituria'")
print(dituria_books)
print("-------")

# 2
dostojevski_pages = Page.objects.filter(book__author__name='Dostojevski').count()
print("Gjeni numrin e te gjitha faqeve te librave me autor 'Dostojevski'")
print(dostojevski_pages)
print("-------")

# 3
all_pages = Page.objects.all().count()
print("Gjeni numrin e te gjitha faqeve te te gjithe librave.")
print(all_pages)
print("-------")

# 4

all_pages_for_house = [Page.objects.filter(book__publisher__id=house.id).count() for house in Publisher.objects.all()]
print("Gjeni numrin e te gjitha faqeve te librave per secilen shtepi botuese.")
print(all_pages_for_house)
print("-------")


# 5
all_author_books = [author.book_set.all().count() for author in Author.objects.all()]
print("Gjeni numrin e te gjithe librave per secilin autor.")
print(all_author_books)
print("-------")

# 6
old_books = Book.objects.filter(publish_date__year__lt=2000)
print("Gjeni te gjithe librat me te vjeter se viti '2000'")
print(old_books)
print("-------")

# 7
all_books = Book.objects.all()
books = [book for book in all_books if book.page_set.all().count()>200 or book.publish_date.year>2010]
print("Gjeni librat me me shume faqe se 200 ose qe jane me te rinj se viti '2010'")
print(books)
print("-------")

# 8
all_publishers = Publisher.objects.filter()
publishers = [house for house in all_publishers if house.book_set.all().count() == 0 or house.book_set.all().count() >= 2]
print("Gjeni shtepite botuese me me shume se 2 libra te botuar ose me asnje liber te botuar.")
print(publishers)
print("-------")

# 9
all_books = Book.objects.all()
books_over_1000 = [b for b in all_books if sum([len(page.content or '') for page in b.page_set.all()])>1000]
print("Gjeni librat me me shume se 1000 germa.")
print(books_over_1000)
print("-------")

# 10
book = Book.objects.all()
book_count = [b.author.all() for b in book if sum([len(page.content or '') for page in b.page_set.all()])==256]
print("Gjeni autorin me librin qe ka 256 germa.")
print(book_count)
print("-------")