from main import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class OneTest():
    wpm = 0
    accuracy = 0
    def __init__(self, wpm, accuracy):
        self.wpm = wpm
        self.accuracy = accuracy

class User(db.Model, UserMixin):
    total_tests = 0
    allTests = []
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) #string of 20 characters, and cannot be duplicated
    email = db.Column(db.String(120), unique=True, nullable=False) #string of 20 characters, and cannot be duplicated
    image_file = db.Column(db.String(20),nullable=False, default='default.jpg') #string of 20 characters, and cannot be duplicated
    password = db.Column(db.String(60), nullable=False)
    
    
    def increment_total_tests(self):
        self.total_tests += 1
    def get_total_tests(self):
        return self.total_tests

    def average_speed(self):
        if len(self.allTests) == 0:
            return "No tests taken yet"
        return sum([test.wpm for test in self.allTests])/len(self.allTests)
    
    def average_accuracy(self):
        if len(self.allTests) == 0:
            return "No tests taken yet"
        return sum([test.accuracy for test in self.allTests])/len(self.allTests)

    def max_speed(self):
        if len(self.allTests) == 0:
            return "No tests taken yet"
        return max([test.wpm for test in self.allTests])
    
    def max_accuracy(self):
        if len(self.allTests) == 0:
            return "No tests taken yet"
        return max([test.accuracy for test in self.allTests])

    

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

