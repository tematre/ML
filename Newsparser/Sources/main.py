from newspaper import Article

import newspaper
nyt_paper = newspaper.build(
    'http://nytimes.com/section/todayspaper', memoize_articles=False)
print(nyt_paper.size())



processed_link_list = []
for article_link in nyt_paper.articles:
    article = Article(url=article_link.url)
    article.download()
    article.parse()
    article.nlp()
    print(article.title)
    print(article.keywords)
    processed_link_list.append(article_link)




