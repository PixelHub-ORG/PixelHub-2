from app import db


class Basedataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'Basedataset<{self.id}>'
