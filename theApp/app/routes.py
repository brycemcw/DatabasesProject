from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, SearchForm, RegistrationForm, changeFavoriteForm
from flask_login import current_user, login_user, logout_user
from app.orm import User, teamsfranchises, batting, pitching, managers, people, teams, fielding


@app.route('/')
@app.route('/index')
def index():
	if current_user.is_authenticated:
		user = User.query.filter_by(username=current_user.username).first()
		return render_template('index.html', title='Logged In User', user=user)
	return render_template('index.html',title='Home')


@app.route('/search', methods=['GET', 'POST'])
def search():
	form = SearchForm()
	if form.validate_on_submit():
		stats = teamsfranchises.query.filter_by(franchName=form.team.data).all()

		teamStats = teams.query.filter_by(yearID=form.yearID.data).join(teamsfranchises, teamsfranchises.franchID == teams.franchID).filter_by(franchName=form.team.data).all()


		batStats = batting.query.filter_by(yearID=form.yearID.data).join(teams, teams.teamID == batting.teamID).join(teamsfranchises, teamsfranchises.franchID == teams.franchID).filter_by(franchName=form.team.data).all()
		for row in batStats:
			if row.pa is None:
				row.setValues()


			
		pitchStats = pitching.query.filter_by(yearID=form.yearID.data).join(teams, teams.teamID==pitching.teamID).join(teamsfranchises, teamsfranchises.franchID == teams.franchID).filter_by(franchName=form.team.data).all()
		for row in pitchStats:
			if row.ip is None:
				row.setIP()

		fieldingStats = fielding.query.filter_by(yearID=form.yearID.data).join(teams, teams.teamID==fielding.teamID).join(teamsfranchises, teamsfranchises.franchID == teams.franchID).filter_by(franchName=form.team.data).all()


		# I'm afraid this query is incorrect in its calculation for all players on the team. I was trying to figure out the union operator from SQL Alchemy but i couldn't figure it out in time. I would assume that you would use the union operator and separate queries for the three positions (fielding, batting, and pitching) to find all of the players on the team. 
		players = people.query.join(pitching, pitching.playerID==people.playerID).join(batting, batting.playerID==people.playerID).filter_by(yearID=form.yearID.data).join(teamsfranchises, teamsfranchises.franchID==batting.teamID).filter_by(franchName=form.team.data).all()


		teamManagers = managers.query.filter_by(yearID=form.yearID.data).join(teamsfranchises, teamsfranchises.franchID==managers.teamID).filter_by(franchName=form.team.data).all()


		
		return render_template('search.html',title='Results',form=form, stats=stats, batStats=batStats, pitchStats=pitchStats, teamManagers=teamManagers, players=players, teamStats=teamStats)
	return render_template('search.html', title='Search', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user)
		return render_template('login.html', title='Logged in', form=form, user=user)
	return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, password=form.password.data, favoriteTeam=form.favoriteTeam.data, favoriteYear=form.favoriteYear.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/changeTeam', methods=['GET', 'POST'])
def changeTeam():
	form = changeFavoriteForm()
	if form.validate_on_submit():
		test = teams.query.filter_by(yearID=form.favoriteYear.data).join(teamsfranchises, teamsfranchises.franchID == teams.franchID).filter_by(franchName=form.favoriteTeam.data).first()

		user = User.query.filter_by(username=current_user.username).first()

		if test is not None:
			user.favoriteTeam = form.favoriteTeam.data
			user.favoriteYear = form.favoriteYear.data
			db.session.commit()

		return render_template('changeTeam.html', title='team changed', form=form, user=user, test=test)
		
		
	return render_template('changeTeam.html', title='change team', form=form)