#/usr/bin/python3
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class book(db.Model):
    __tablename__ = 'book'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.INTEGER, nullable=False, primary_key=True,autoincrement=True)
    name = db.Column(db.String(55),nullable=False)
    desc = db.Column(db.TEXT, nullable=True)
    source_url = db.Column(db.TEXT, nullable=False)
    book_url = db.Column(db.TEXT, nullable=False)
    writer = db.Column(db.String(55),nullable=True)
    is_finish = db.Column(db.Boolean,nullable=False,default=False)
    create_at=db.Column(db.DateTime,default=datetime.now())
    is_delete = db.Column(db.BOOLEAN, nullable=False, default=False)

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.applicationId)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


class chapter(db.Model):
    __tablename__ = 'chapter'
    id = db.Column(db.INTEGER, nullable=False, primary_key=True,autoincrement=True)
    name = db.Column(db.String(55),nullable=False)
    book_id = db.Column(db.INTEGER, nullable=False)
    url = db.Column(db.TEXT, nullable=False)
    chapter_id = db.Column(db.INTEGER,nullable=False)
    create_at=db.Column(db.DateTime,default=datetime.now())
    is_delete = db.Column(db.BOOLEAN, nullable=False, default=False)

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.applicationId)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}