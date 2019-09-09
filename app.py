from flask import Flask,render_template,url_for
app=Flask(__name__)

posts=[
    {
        "message":"Welcome to GROCESTORE",
        "promise":"Our Guarantee:",
        "point1":"Online Delivery",
        "point2":"Free Delivery",
        "point3":"Best Quality",
    }

]

@app.route('/home')
def home():
    return render_template('home.html',posts=posts,title='home')

#@app.route('/profile')
#def profile():
 #   return render_template('profile.html',title='profile')

if __name__ == "__main__":
    app.run(debug=True)
