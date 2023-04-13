from flask import Flask, render_template, request, redirect
    # import the class from friend.py
from users import User
#from table_name import Class_name
    # more imports here

app = Flask(__name__)


@app.route("/")
def index():
    # change 'users' to the table_name and 'User' to the Class_name
    users = User.get_all()
    # change all_users to be the list of what you're 'getting all of'
    return render_template("index.html", all_users = users)


@app.route('/user/new')
def new_user():
    return render_template("add_user.html")


#this method shows 1 user given their ID
@app.route('/user/show/<int:user_id>')
def show(user_id):
    # calling the get_one method from table_name.py
    # change 'user_id' and 'User' class to be the id of the table/class you're using
    user=User.get_one(user_id)
    # it's currently setup to render a show_user.html that includes the variable 'user'
    return render_template("show_user.html",user=user)


@app.route('/create_user', methods=["POST"]) # change /create_user to match the form action in the HTML
def create_user():
    #change "fname, lname" etc to match the form inputs in the HTML
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the user class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)