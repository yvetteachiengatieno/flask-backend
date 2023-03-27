from app.app import create_app
from app.cookies.models import Cookies
from app.extensions.databases import db


if __name__ == "__main__":
    app = create_app()
    app.app_context().push()


blog_articles = {
    "article_1": {
        "title": "bdbffkndfkdg",
        "text": "bsbdfbsbfgf",
    },
    "article_2": {
        "title": "bfsjhbfhjbsjfbj",
        "text": "fbjsbfbjsbf",
    },
    "article_3": {
        "title": "bfjbsrfjbrbf",
        "text": "dbjsbfbjsbfsfdb",
    },
    "article_4": {"title": "dc nsbcnbs", "text": "bcfdshbfhgdvghhv"},
}

for slug, article in blog_articles.items():
    new_article = Cookies(
        slug=slug, title=blog_articles[slug]["title"], text=blog_articles[slug]["text"]
    )
    db.session.add(new_article)

db.session.commit()