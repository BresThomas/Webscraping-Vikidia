import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def home():
    # Make a request to the website
    url = "https://fr.vikidia.org/wiki/Pomme"
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract the title, image and all h1, h2, h3, p, ul, li tags from the article
    title = soup.find('title').text
    image = soup.find('div', class_='mw-parser-output').find('img')
    contents = soup.find_all(['h1', 'h2', 'h3', 'p', 'ul', 'li'])
    # Remove the string " [modifier | modifier le wikicode]" from each h2 tag's text
    remove_string = "[modifier | modifier le wikicode]"
    for h2 in soup.find_all('h2'):
        if remove_string in h2.text:
            h2.string = h2.text.replace(remove_string, "")
    # Render the data to the HTML template
    return render_template('home.html', title=title, image=image, contents=contents)

if __name__ == '__main__':
    app.run(debug=True)
