from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    birthday = db.Column(db.String(), unique=True)

    def __repr__(self):
        return f"Zookeeper {self.name}, {self.birthday}"


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(), nullable=False)
    open_to_visitors = db.Column(db.Boolean, default=False)
    animal_id = db.Column(db.Integer, db.ForeignKey(
        'animals.id'))

    def __repr__(self):
        return f"Enclosure {self.enviroment}, {self.open_to_visitors}"


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    # Changed "spicie" to "species"
    species = db.Column(db.String(), nullable=False, unique=True)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey(
        'zookeepers.id'))  # Added ForeignKey for zookeeper
    enclosure_id = db.Column(db.Integer, db.ForeignKey(
        'enclosures.id'))  # Added ForeignKey for enclosure

    enclosure = db.relationship("Enclosure", backref="animals")
    zookeeper = db.relationship("Zookeeper", backref="animals")

    def __repr__(self):
        return f"Animal {self.name} {self.species}"
