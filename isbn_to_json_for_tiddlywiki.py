from isbnlib import meta, desc, cover, classify, goom
import datetime

# \\n\\n<<<\\n{description}\\n<<<\\n
SERVICE = 'openl'

isbn = input("Type in ISBN: ")

current_time = datetime.datetime.now()
fmt = '%Y%m%d%H%M'

def isbn_to_book_desc(isbn):
    # get info from isbnlib
    book = meta(isbn)
    description = desc(isbn)
    image = f"[img[http://covers.openlibrary.org/b/isbn/{isbn}-L.jpg]]"
    title = book["Title"]
    author = book["Authors"]
    # convert author list to string
    str_author = ",".join(author)
    year_published = book["Year"]
    
    #remove line breaks and double quotes from description (TiddlyWiki can't have 'em)
    description = description.replace('\n', ' ').replace('\r', ' ').replace('"', '\'')

    #define the TiddlyWiki dictionary-like keys and values
    tiddler_title = f'"{title}"'
    created = f'"{current_time.strftime(fmt)}00000"'
    modified = f'"{current_time.strftime(fmt)}00001"'
    desc_field = f'"{description}"'
    author_field = f'"{str_author}"'
    book_year_published_field = f'"{year_published}"'
    image_field = f'"{image}"'
    tags = f'"Watched/Listened/Read"'
    type = '"text/vnd.tiddlywiki"'
    
    #translate all book info into transclusions for TiddlyWiki text field
    book_desc_field_view = "{{!!bookdesc}}"
    author_field_view = "{{!!bookauthors}}"
    title_field_view = "{{!!booktitle}}"
    year_published_field_view = "{{!!bookyearpublished}}"
    image_field_view = "{{!!image}}"
    
    text = f'"{title_field_view} by {author_field_view}\\n\\nPublished: {year_published_field_view}\\n\\n{book_desc_field_view}\\n\\n{image_field_view}"'
    
    start = '[{'
    end = '}]'
    

    tw5_code = f'{start}"image":{image_field},"bookauthors":{author_field},"bookyearpublished":{book_year_published_field},"created":{created},"text":{text},"type":{type},"title":{tiddler_title},"tags":{tags},"modified":{modified},"bookdesc":{desc_field}{end}'

    file = open(f"{title}.json", "w")
    file.write(tw5_code)
    file.close()

isbn_to_book_desc(isbn)


