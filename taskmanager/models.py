from taskmanager import db


class Book(db.Model):
    # schema for the Book model
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), unique=True, nullable=False)
    book_author = db.Column(db.String(25), unique=True, nullable=False)
    reviews = db.relationship("Review", backref="book", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Review(db.Model):
    # schema for the Review model
    id = db.Column(db.Integer, primary_key=True)
    review_title = db.Column(db.String(50), unique=True, nullable=False)
    review = db.Column(db.Text, nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey("review.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "Your review {1} has been added. It is review number {2}".format(
            self.review_title, self.id
        )