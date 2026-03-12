def generate_jsonld(title, description, keywords, author, date_published):

    jsonld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "keywords": keywords,
        "author": {
            "@type": "Person",
            "name": author
        },
        "datePublished": date_published

    }

    return jsonld