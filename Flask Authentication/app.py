from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, current_user, logout_user, login_required
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_bcrypt import Bcrypt
           
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
app.config['SECRET_KEY'] = 'thisisasecretkey'  

db = SQLAlchemy(app)          
bcrypt = Bcrypt(app)    

login_manager = LoginManager()
login_manager.init_app(app) 
login_manager.login_view = 'login'  # Redirect to login page if user is not authenticated                       
                                        
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')                         
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in ') 
                            
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return render_template("dashboard.html")
        else:
            return render_template("login.html", form=form, error="Invalid username or password.")
    return render_template("login.html", form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
  return render_template("dashboard.html")

@app.route('/logout' , methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))    
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return render_template("login.html", form=LoginForm())              
    return render_template("register.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)