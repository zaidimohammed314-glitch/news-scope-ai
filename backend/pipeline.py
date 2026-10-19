# backend/config.py

SOURCES = [
    # English Sources
    {"name": "BBC News", "lang": "en", "url": "http://feeds.bbci.co.uk/news/rss.xml", "topic": "politics", "country": "UK"},
    {"name": "Reuters", "lang": "en", "url": "https://www.reutersagency.com/feed/?best-topics=political-general&post_type=best", "topic": "politics", "country": "Global"},
    {"name": "AP News", "lang": "en", "url": "https://apnews.com/hub/world-news?format=rss", "topic": "politics", "country": "USA"},
    {"name": "Al Jazeera English", "lang": "en", "url": "https://www.aljazeera.com/xml/rss/all.xml", "topic": "politics", "country": "Qatar"},
    {"name": "CNN World", "lang": "en", "url": "http://rss.cnn.com/rss/edition_world.rss", "topic": "politics", "country": "USA"},
    {"name": "The Guardian", "lang": "en", "url": "https://www.theguardian.com/world/rss", "topic": "politics", "country": "UK"},
    {"name": "RT International", "lang": "en", "url": "https://www.rt.com/rss/news/", "topic": "politics", "country": "Russia"},
    {"name": "DW World", "lang": "en", "url": "https://rss.dw.com/rdf/rss-en-world", "topic": "politics", "country": "Germany"},
    
    # Arabic Sources
    {"name": "Al Jazeera Arabic", "lang": "ar", "url": "https://www.aljazeera.net/rss", "topic": "politics", "country": "Qatar"},
    {"name": "BBC Arabic", "lang": "ar", "url": "https://www.bbc.com/arabic/index.xml", "topic": "politics", "country": "UK"},
    {"name": "France 24 Arabic", "lang": "ar", "url": "https://www.france24.com/ar/rss", "topic": "politics", "country": "France"},
    {"name": "Sky News Arabia", "lang": "ar", "url": "https://www.skynewsarabia.com/web/rss", "topic": "politics", "country": "UAE"},
    {"name": "RT Arabic", "lang": "ar", "url": "https://arabic.rt.com/rss/", "topic": "politics", "country": "Russia"},
    {"name": "Asharq News", "lang": "ar", "url": "https://asharq.com/rss", "topic": "economy", "country": "Saudi Arabia"},

    # Russian Sources
    {"name": "TASS", "lang": "ru", "url": "http://tass.ru/rss/v2.xml", "topic": "politics", "country": "Russia"},
    {"name": "RIA Novosti", "lang": "ru", "url": "https://ria.ru/export/rss2/index.xml", "topic": "politics", "country": "Russia"},
    {"name": "RT Russian", "lang": "ru", "url": "https://russian.rt.com/rss", "topic": "politics", "country": "Russia"},
    {"name": "Lenta.ru", "lang": "ru", "url": "https://lenta.ru/rss/news", "topic": "politics", "country": "Russia"},
    {"name": "Kommersant", "lang": "ru", "url": "https://www.kommersant.ru/RSS/news.xml", "topic": "economy", "country": "Russia"}
]
