from newspaper import Article
import nltk
nltk.download()

url = 'https://newspaper.readthedocs.io/en/latest/'

article = Article(url)
article.download()
article.parse()

print(article.html)
print(article.authors)
print(article.text)

article.nlp()

print(article.keywords)