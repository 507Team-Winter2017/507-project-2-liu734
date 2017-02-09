#proj2.py
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import time
#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

base_url = 'http://www.nytimes.com'
uhand = urllib.request.urlopen(base_url)
html = uhand.read()
soup = BeautifulSoup(html, 'html.parser')

for story_heading in soup.find_all(class_="story-heading")[:10]:
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())

### Your Problem 1 solution goes here


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

base_url = 'https://www.michigandaily.com/'
uhand = urllib.request.urlopen(base_url)
html = uhand.read()
soup = BeautifulSoup(html, 'html.parser')

most_read_div= soup.find_all(class_="panel-pane pane-mostread")[0]
most_read_li= most_read_div.find_all("a")
for li in most_read_li:
    #print(li.get_text())
    print(li.string)

'''

print (most_read_div.get_text().strip())

for content in most_read_div.contents:
    if content.a:
        print

'''
### Your Problem 2 solution goes here


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

base_url = 'http://newmantaylor.com/gallery.html'
uhand = urllib.request.urlopen(base_url)
html = uhand.read()
soup = BeautifulSoup(html, 'html.parser')

all_imgs= soup.find_all("img")
for img in all_imgs:
    if 'alt' in img.attrs:
        print (img['alt'])
    else:
        print ('No alternative text provided!')

### Your Problem 3 solution goes here


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

to_visit=['https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4']

#visited=set()

all_email_links=[]

emails=[]

#base_url = 'http://newmantaylor.com/gallery.html'

while to_visit:
    url=to_visit.pop(0)
    uhand = urllib.request.urlopen(url)
    html = uhand.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    o= urllib.parse.urlparse(url)

    domain=o.scheme+"://"+o.netloc

    time.sleep(0.1)

    #Go to next page
    next_url_a=soup.find_all("a", {"title": "Go to next page"})
    
    if next_url_a:
        to_visit.append(domain+next_url_a[0]["href"])
        #print(domain+next_url_a[0]["href"])

    for contact in soup.find_all("a", text="Contact Details"):
        local_address=contact["href"]
        
        #print (domain+local_address)
        all_email_links.append(domain+local_address)




while all_email_links:
    
    time.sleep(0.1)
    
    url=all_email_links.pop(0)
    uhand = urllib.request.urlopen(url)
    html = uhand.read()
    soup = BeautifulSoup(html, 'html.parser')
    email_div = soup.find_all("div", {"class": "field field-name-field-person-email field-type-email field-label-inline clearfix"})[0]
    email= email_div.a.string
    #print (email_div)
    #print (email)
    emails.append(email)


for index, email in enumerate(emails):
    print (index+1, email)


### Your Problem 4 solution goes here
