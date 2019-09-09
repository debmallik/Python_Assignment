from flask import Flask,render_template
app=Flask(__name__)

posts=[
    {
        "author":"Debashis",
        "title":"Blog post 1   ",
        "blog":"Proud to be Indian",
        "date":"8th Sept 2019"
    },
    {
        "author":"Mallik",
        "title":"Blog post 2",
        "blog":"I stay in Bangalore",
        "date":"8th Sept 2019"
    }
]

@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/profile')
def profile():
    return render_template('profile.html',title='profile')

if __name__ == "__main__":
    app.run(debug=True)