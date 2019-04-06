from bson.objectid import ObjectId
import time
import uuid


class Text:
    def __init__(self, user=None, tid=None, text=None,
        date=None, words=None, created=None, updated=None,
        structure=None, _id=None
    ):
        self.user = user
        self.tid = tid or uuid.uuid4().hex
        self.text = text
        self.words = words
        self.created = created or time.time()
        self.updated = updated or time.time()
        self.date = date
        self._id = _id
        self.structure = structure


    def to_dict(self, with_id=False):
        dic = dict(
            tid=self.tid,
            user=self.user,
            text=self.text,
            date=self.date,
            words=self.words,
            created=self.created,
            updated=self.updated
        )
        if with_id:
            dic['_id'] = ObjectId(self._id)
        return dic


    @classmethod
    def from_dict(cls, dic):
        if dic:
            return cls(
                tid=dic.get('tid', None),
                user=dic.get('user', None),
                text=dic.get('text', None),
                date=dic.get('date', None),
                words=dic.get('words', None),
                created=dic.get('created', None),
                updated=dic.get('updated', None),
                _id=dic.get('_id', None)
            )
