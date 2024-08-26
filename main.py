import requests


class Website:
    def __init__(self, url):
        self.url = url
    def fetch_html(self):
        response = requests.get(self.url)
        return response.text


if __name__ == '__main__':
    url = "https://yle.fi/a/74-20105264"
    website = Website(url)
    html = website.fetch_html()

    #parse html with beautiful soup
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find('section', {'class':'yle__article__content'}).text

    # save text to a file
    with open("selkouutiset.html", "w", encoding="utf-8") as file:
        file.write(content)

