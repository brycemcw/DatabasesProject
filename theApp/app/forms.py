from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.orm import User

class SearchForm(FlaskForm):
	team = StringField('Team', validators=[DataRequired()])
	yearID = StringField('Year', validators=[DataRequired()])
	submit = SubmitField('Search')


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	favoriteTeam = StringField('Favorite Team', validators=[DataRequired()])
	favoriteYear = StringField('Favorite Year')
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField(
		'Repeat Password', validators=[DataRequired(), EqualTo('password')]
	)

	submit = SubmitField('Sign Up')

class changeFavoriteForm(FlaskForm):
	favoriteTeam = StringField('Favorite Team', validators=[DataRequired()])
	favoriteYear = StringField('Favorite Year')
	submit = SubmitField('Change Team')

	
def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
    	raise ValidationError('Please use a different username.')


