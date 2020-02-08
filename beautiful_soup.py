from bs4 import BeautifulSoup
import requests
import csv
# html_string = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>WDP</title>
#     <style type="text/css">
#         h1{
#             color: white;
#             background: red;
#         }
#
#         li{
#             color: red;
#         }
#         #css-li{
#                 color:blue;
#                 }
#         .green {
#                 color: green;
#                 }
#     </style>
# </head>
# <body>
#     <h1> Web Development </h1>
#     <h1 class="green">Web</h1>
#     <h3>Programming Languages</h3>
#     <ol>
#         <li>Html</li>
#         <li id="css-li">CSS</li>
#         <li class ="green">JavaScript</li>
#         <li class="green bold" id ="python-li">Python</li>
#     </ol>
# </body>
# </html>
# """

# parsed_html = BeautifulSoup(html_string, 'html.parser')
# print(parsed_html)
# print(type(parsed_html))
# print(parsed_html.body.ol.li)
# print(parsed_html.find_all('li')
# print(parsed_html.find(id='css-li'))
# print(parsed_html.select('#css-li'))
# print(parsed_html.find_all(class_='green'))
# print(parsed_html.select('.green')[1])
# html_elem = parsed_html.select('.green')[1]
# print(html_elem.get_text())
# html_elem_list = parsed_html.select('li')
# for html_elem in html_elem_list:
#     print(html_elem.get_text())
# green_class_elem_list = parsed_html.select('li')
# for html_elem in green_class_elem_list:
#     print(html_elem.attrs)
# print(html_elem['class'][0])

# html_elem_list = parsed_html.select('li')[3]
# # print(html_elem_list['id'])
# print(html_elem_list['class'][0])

# data = parsed_html.body.contents[1].next_sibling.next_sibling.next_sibling.next_sibling
# data = parsed_html.find(id='css-li').parent.previous_sibling.previous_sibling
# data = parsed_html.find(id='css-li').find_next_sibling().find_previous_sibling()
# data = parsed_html.find(id='css-li').find_next_sibling(class_='bold')
# data = parsed_html.find(id='css-li').find_next_sibling(class_='bold').find_parent().find_parent()
# data = parsed_html.body.findChildren()[2]
# print(data)


response = requests.get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text, 'html.parser')
quotes = html_data.find_all(class_='quote')
# print(quotes)
# for quote in quotes:
#     print(quote.find(class_='text').get_text())
#     print(quote.find(class_='author').get_text())
#     print(quote.find(class_='keywords'))

with open ('beautifulSoup.csv', 'w', encoding='utf-16') as file:
    # csv_writer = csv.writer(file)
    # csv_writer.writerow(['Text', 'Author'])
    headers_list = ['Make', 'Model']
    csv_writer = csv.DictWriter(file, fieldnames=headers_list)
    csv_writer.writeheader()
    for quote in quotes:
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        # csv_writer.writerow([text, author])
        # quote.find(class_='keywords')
        csv_writer.writerow({'Make': text, 'Model': author})
