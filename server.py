from flask import Flask, redirect, url_for, render_template, flash
from flask_login import LoginManager, login_user, current_user, UserMixin, login_required
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(70), unique=False, nullable=False)

    def __repr__(self):
        return 'Person Info (username): {self.username}\n(is): {self.id}\n password:{self.password}'
    
    def is_active(self):
        """True, as all users are active."""
        return True

    # def get_id(self):
    #     """Return the email address to satisfy Flask-Login's requirements."""
    #     return self.email

    # def is_authenticated(self):
    #     """Return True if the user is authenticated."""
    #     return self.authenticated

    # def is_anonymous(self):
    #     """False, as anonymous users aren't supported."""
        # return False

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and form.password.data == user.password:
            login_user(user)
            return redirect(url_for('home'))
            
        else:
            
            flash('Login Unsuccessfull please check username and password', 'danger')
    return render_template('login.html', form=form)

# @login_required
# @app.route('/req', methods=["GET", "POST"])
# def req():
#     return 'Loggin Required'


if __name__ == "__main__":
    app.run(debug=True)