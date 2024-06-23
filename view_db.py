from app import create_app, db
from app.models import User, Post

app = create_app()

with app.app_context():
    users = User.query.all()
    posts = Post.query.all()

    print("Users:")
    for user in users:
        print(user)

    print("\nPosts:")
    for post in posts:
        print(post)
