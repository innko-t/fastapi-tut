from datetime import datetime
import stat

from fastapi import HTTPException, status
from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DbPost


def create(db: Session, request: PostBase, creater_id):
    new_post = DbPost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.now(),
        user_id = creater_id

    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def get_all(db: Session):
    return db.query(DbPost).all()

def delete(db: Session, id: int, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detal = 'Post with id {id} not found')
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
        detail = 'only post creater can delete')

    db.delete(post)
    db.commit()
    return 'Delete Post!'
    