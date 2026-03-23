class Course:
    def __init__(self, cid='', name='', credit=0):
        self._id = cid
        self._name = name
        self._credit = credit

    def get_id(self):
        return self._id

    def get_credit(self):
        return self._credit

    def __str__(self):
        return f"{self._id} - {self._name} ({self._credit} credits)"
