from flask import Flask, render_template
app = Flask(__name__)








@app.route('/')
def home():
    return render_template('home.html')



@app.route('/workout')
def workout_planner():
    return render_template('workout.html')


@app.route('/remix')
def workout_remix():
    return render_template('remix.html')


@app.route('/profile')
def user_profile():
    return render_template('profile.html')
