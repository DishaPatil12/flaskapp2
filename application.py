
from flask import Flask, render_template, redirect, url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField

from wtforms.validators import InputRequired

application= Flask(__name__)
application.config['SECRET_KEY']='some_random_secret'

class SignUpForm(FlaskForm):
    name = StringField('Enter your name', validators=[InputRequired()])
    
    publicity = RadioField('How did you hear about us? ', choices=[('social', 'Social Media'),('poster','Psoter and flyers')])
    feedback = TextAreaField('Anything else you want to tell us')
    submit = SubmitField('submit')
    
@application.route('/', methods =['GET','POST'])
def hello_world():
    form= SignUpForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        
        session['publicity']= form.publicity.data
        session['feedback']=form.feedback.data
        print(session['name'])
        return redirect(url_for("thankyou"))
    return render_template('index.html', form=form)
        
        
        
@application.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ =='__main__':
    application.run(debug=True)
        
        
        
        
        
        
