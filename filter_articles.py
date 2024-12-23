def select_popular_articles(article_data, top_n=3):
    scored_articles = []
    for article in article_data:
        score = len(article["abstract"])
        scored_articles.append((score, article))
    
    scored_articles.sort(key=lambda x: x[0], reverse=True)
    return [art for _, art in scored_articles[:top_n]]
