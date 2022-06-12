from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    commentBy = Column(Integer, ForeignKey("user.id"),nullable=False)
    commentOn = Column(Integer, ForeignKey("tweet.id"),nullable=False)
    comment = Column(String, nullable=False)
    commentAt = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return "<Comment(id='%s', commentBy='%s', commentOn='%s', comment='%s')>" % (self.id, self.commentBy, self.commentOn, self.comment)