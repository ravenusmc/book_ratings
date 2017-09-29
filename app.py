#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

#Bring in personal files that I wrote. 
from user import * 

#Setting up Flask
app = Flask(__name__)

#This function will bring the user to the home page
@app.route('/', methods=['GET', 'POST'])
def landing():
  if request.method == 'POST':
    #Recieving the information from the form from the user.
    username = request.form['username']
    password = request.form['password']
    user = User()
    #Checking to see if the user is in the database.
    flag, not_found, password_no_match = user.check(username, password)
    #Conditional statement to test if the user is a member of the site.
    if flag == True:
        #If the user is in the database, the user gets sent to the index page.
        session['username'] = request.form['username']
        #Sending the user to the index page
        return redirect(url_for('home'))
    else:
        #If the user is not in the database then they will be sent to the
        #sign up page.
        if not_found:
          flash('Username not found, maybe sign up!')
        elif password_no_match:
          flash('Password does not match! Maybe sign up!')
  return render_template('login.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    #Recieving the information from the form from the user.
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    user = User()
    #Encrypting the password
    password, hashed = user.encrypt_pass(password)
    #Adding the user to the database
    user.insert(name, username, hashed)
    #Letting them into the index Page
    return redirect(url_for('home'))
  return render_template('sign_up.html')

@app.route('/home')
def home():
  if 'username' not in session:
    return redirect(url_for('signup'))
  return render_template('home.html')


#This function is what will log out the user.
@app.route('/sign_out')
def logout():
  # remove the username from the session if it's there
  session.pop('username', None)
  return redirect(url_for('landing'))

### Functions dealing with ajax calls below ###
@app.route('/book_look_up',methods=['POST'])
def book_look_up():
  #Recieving the data from the ajax call
  title = request.form['title']
  if title: 
    return jsonify(result = title)
  return jsonify({'error' : 'Missing Data'})

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)