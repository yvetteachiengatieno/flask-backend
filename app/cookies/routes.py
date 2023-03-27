from flask import Blueprint, render_template
from .models import Cookie

blog_cookies = {
    "article_1": {
        "title": "Travel blog",
        "text": "fjbdjhbvjfdbjbvhfhvjdjv",
    },
    "article_2": {
        "title": "Food blog",
        "text": "sbfdjbdjvhbdfjvbhjfbdjhv.",
    },
    "article_3": {
        "title": "Rituals blog",
        "text": "sbdbchbsdjfhvbjfbjv",
    },
    "article_4": {"About author": "bdjbdjbdjs", "text": "bcdbsjcbsjbjcb"},
}


cookies_data= {
    'france' : {'name': 'France', 'temperature': '30 degrees'},
    'monaco' : {'name': 'Monaco', 'temperature': '25 degrees'},
    'mombasa': {'name': 'Mombasa', 'temperature': '38 degrees'},
    'berlin' : {'name': 'Berlin', 'temperature': '18 degrees'},
}

blueprint = Blueprint('cookies', __name__)

@blueprint.route("/blog")
def blog():
    all_blogs = Cookies.query.all()
    print("hello")
    print(all_blogs)
    return render_template("travel.html", blogs=all_blogs)

@blueprint.route("/blog/<slug>")
def blogs(slug)
    blog = Cookies.query.filter_by(slug=slug).first()
    print(blog)
    if blog:
        title = blog.title
        text = blog.text
        return render_template("cookies/cookies.html", title=title, text=text")
    else:
        return "Cookie does not exist"


    
