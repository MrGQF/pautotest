import Infrastructure.Data.DbContext as context
from sqlalchemy import and_
import Infrastructure.Data.MarshalExtend as MarshalExtend


db = context.db


class Daily(db.Model):

    __tablename__ = "USHA600000"
    DateTime = db.Column(db.INTEGER, primary_key=True, autoincrement=False)
    Open = db.Column(db.FLOAT)
    HIGH = db.Column(db.FLOAT)
    Low = db.Column(db.FLOAT)
    Close = db.Column(db.FLOAT)

    def ToObj(str):
        return {
            "DateTime": str.DateTime,
            "Open": str.Open
        }


@MarshalExtend.marshal_with_model(Daily)
def Query(code, dateTimeStart, dateTimeEnd):
    filters = (
        and_(Daily.DateTime >= dateTimeStart, Daily.DateTime <= dateTimeEnd),
    )
    Daily.__table__.name = code
    return Daily.query.filter(*filters)


@MarshalExtend.marshal_with_model(Daily)
def QueryByCount(code, count):
    Daily.__table__.name = code
    return Daily.query.order_by(Daily.DateTime).limit(count).all()


if __name__ == '__main__':
    obj = Query(code="USHA600000", dateTimeStart=942163200,
                dateTimeEnd=942249600)
    print(obj)
