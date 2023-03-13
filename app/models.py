from . import db


class AddProperty(db.Model):
    __tablename__ = 'project1'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(200))
    No_Rooms = db.Column(db.String(20))
    No_bathrooms= db.Column(db.String(20))
    price = db.Column(db.String(20))
    property_type=db.Column(db.String(50))
    location=db.Column(db.String(100))
    photo=db.Column(db.String(),nullable=True)
    


def __init__(self,title,description,No_Rooms,No_bathrooms,price,property_type,location,photo):
        
        self.title= title
        self.description =description
        self.No_Rooms =No_Rooms
        self.No_bathrooms= No_bathrooms
        self.price = price 
        self.property_type=property_type
        self.location=location
        self.photo = photo

def is_authenticated(self):
    return True

def is_active(self):
    return True

def is_anonymous(self):
    return False

def get_id(self):
    try:
        return unicode(self.id)  # python 2 support
    except NameError:
        return str(self.id)  # python 3 support

def __repr__(self):
    return '<AddProperty "{}">'.format(self.id)