from sys import maxsize

class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, home_phone=None, email=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.email = email
        self.id = id

    def __repr__(self):
        return "Объект включает в себя: %s, %s, %s" % (self.id, self.first_name,  self.last_name) #self.middle_name, , self.home_phone, self.email

    def __eq__(self, other):
        return self.first_name == other.first_name and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(cont):
        if cont.id:
            return int(cont.id)
        else:
            return maxsize