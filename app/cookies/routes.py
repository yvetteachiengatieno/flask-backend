from flask import Blueprint, render_template, request, current_app
from .models import Cookie

@blueprint.route('/cookies')
def cookies():
  page_number = request.args.get('page', 1, type=int)
  cookies_pagination = Cookie.query.paginate(page_number, current_app.config['COOKIES_PER_PAGE'])
  return render_template('cookies/index.html', cookies_pagination=cookies_pagination)



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
def blogs(slug):
    blog = Cookies.query.filter_by(slug=slug).first()
    print(blog)
    if blog:
        title = blog.title
        text = blog.text
        return render_template("cookies/cookies.html", title=title, text=text)
    else:
        return "Cookie does not exist"


    
