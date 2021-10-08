from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2d53034d22f76aad51693f6ab7ffffb0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='organization', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.campaign}', '{self.date_posted}')"

posts = [
    {
        "organization": "The One Campaign",
        "campaign": "The One Campaign",
        "content": "ONE is a global movement campaigning to end extreme poverty and preventable disease by 2030, so that everyone, everywhere can lead a life of dignity and opportunity. We believe the fight against poverty isn’t about charity, but about justice and equality. Helping secure at least $37.5 billion in funding for historic health initiatives",
        "date_posted": "09/26/2021",
        "imgage":"../static/images/the-one-campaign.jpg",
    },
        {
        "organization": "bread for the world",
        "campaign": "Bread for the world",
        "content": "Bread for the World is a collective Christian voice urging our nation’s decision makers to end hunger at home and abroad. By changing policies, programs, and conditions that allow hunger and poverty to persist, we provide help and opportunity at home and far beyond where we live. We can end hunger in our time. But churches and charities can’t do it all. Our government must also do its part.",
        "date_posted": "09/22/2021",
        "imgage":"../static/images/bread-world.jpg",
    },
    {
        "organization": "Feeding America",
        "campaign": "Feeding America",
        "content": "We are the nation’s largest domestic hunger-relief organization, working to connect people with food and end hunger. Food shouldn't be an impossible choice. This Hunger Action Month, choose to end the impossible choices of hunger. Your impact: $1 = 10 meals. Every dollar you give can provide at least 10 meals to families in need through the Feeding America network of food banks",
        "date_posted": "09/15/2021",
        "imgage":"../static/images/Feeding-America.png",
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/organization-portal")
def organization_portal():
    return render_template('organization-portal', title = "Portal", posts = posts)

@app.route("/volunteer-portal")
def volunteer_portal():
    return render_template('volunteer-portal', title = "Portal", posts = posts)

@app.route("/portal")
def portal():
    form = LoginForm()
    if form.email.data == "breadworld@gmail.com":
        return redirect(url_for('organization_portal'))
    else:
        return redirect(url_for('volunteer_portal'))
        


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "breadworld@gmail.com":
            return redirect(url_for('organization_portal'))
        else:
            return redirect(url_for('volunteer_portal'))
        # return redirect(url_for('home'))
        # if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        #     flash('You have been logged in!', 'success')
        #     return redirect(url_for('home'))
        # else:
        #     flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
