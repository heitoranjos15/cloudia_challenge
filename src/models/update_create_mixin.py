from datetime import datetime

from sqlalchemy import event

from src.builders.db_client import db


class UpdatedCreatedMixin(object):

    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, server_onupdate=db.func.current_timestamp(),
                        onupdate=datetime.utcnow, default=datetime.utcnow)


@event.listens_for(UpdatedCreatedMixin, 'after_update')
def updated_created_after_update(mapper, connection, target):
    target.updated = datetime.utcnow()
