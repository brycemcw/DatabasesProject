from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# User ORM
class User(UserMixin, db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(9), index=True, unique=True)
	password = db.Column(db.String(9))
	password_hash = db.Column(db.String(128))
	favoriteTeam = db.Column(db.String(50))
	favoriteYear = db.Column(db.Integer)

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
	return User.query.get(int(id))





class batting(db.Model):
	__tablename__ = "batting"
	id = db.Column(db.Integer, primary_key=True)
	playerID = db.Column(db.String(9), unique=True)
	yearID = db.Column(db.Integer)
	stint = db.Column(db.Integer)
	teamID = db.Column(db.String(3))
	team_ID = db.Column(db.Integer)
	lgID = db.Column(db.String(2))
	G = db.Column(db.Integer)
	G_batting = db.Column(db.Integer)
	ab = db.Column(db.Integer)
	r = db.Column(db.Integer)
	h = db.Column(db.Integer)
	b2 = db.Column(db.Integer)
	b3 = db.Column(db.Integer)
	hr = db.Column(db.Integer)
	rbi = db.Column(db.Integer)
	sb = db.Column(db.Integer)
	cs = db.Column(db.Integer)
	bb = db.Column(db.Integer)
	so = db.Column(db.Integer)
	ibb = db.Column(db.Integer)
	hbp = db.Column(db.Integer)
	sh = db.Column(db.Integer)
	sf = db.Column(db.Integer)
	gidp = db.Column(db.Integer)
	pa = db.Column(db.Integer)
	ba = db.Column(db.Float)
	obPercent = db.Column(db.Float)
	slugPercent = db.Column(db.Float)


	def setPA(self):
		self.pa = self.h + self.bb + self.so + self.hbp + self.coalecse(self.sh) + self.coalecse(self.sf)
		

	def setBA(self):
		top = self.h + self.b2 + self.b3 * 2 + 3 * self.hr
		if(self.ab == 0):
			self.ba = 0
		else:
			self.ba = top / self.ab

	def setOBP(self):
		top = self.h + self.bb + self.hbp
		bottom = self.ab + self.bb + self.hbp + self.coalecse(self.sh)
		if(bottom == 0):
			self.obPercent = 0
		else:
			self.obPercent = top / bottom

	def setSlugPercent(self):
		top = self.h + 2 * self.b2 + self.b3 * 3 + 4 * self.hr
		if(self.ab == 0):
			self.slugPercent = 0
		else:
			self.slugPercent = top / self.ab


	def coalecse(self, x):
		if x is None:
			return 0
		else:
			return x


	def setValues(self):
		self.setPA()
		self.setBA()
		self.setOBP()
		self.setSlugPercent()
		db.session.commit()


class teamsfranchises(db.Model):
	__tablename__ = "teamsfranchises"
	franchID = db.Column(db.String(3), primary_key=True)
	franchName = db.Column(db.String(50))
	active = db.Column(db.String(1))
	NAassoc = db.Column(db.String(3))

class teams(db.Model):
	__tablename__="teams"
	id = db.Column(db.Integer, primary_key=True)
	yearID = db.Column(db.Integer)
	lgID = db.Column(db.String(2))
	teamID = db.Column(db.String(3))
	franchID = db.Column(db.String(3))
	divID = db.Column(db.String(1))
	div_ID = db.Column(db.Integer)
	teamRank = db.Column(db.Integer)
	G = db.Column(db.Integer)
	W = db.Column(db.Integer)
	L = db.Column(db.Integer)
	DivWin = db.Column(db.String(1))
	WCWin = db.Column(db.String(1))
	LgWin = db.Column(db.String(1))
	WSWin = db.Column(db.String(1))
	r = db.Column(db.Integer)
	ab = db.Column(db.Integer)
	h = db.Column(db.Integer)
	b2 = db.Column(db.Integer)
	b3 = db.Column(db.Integer)
	hr = db.Column(db.Integer)
	bb = db.Column(db.Integer)
	so = db.Column(db.Integer)
	sb = db.Column(db.Integer)
	cs = db.Column(db.Integer)
	hbp = db.Column(db.Integer)
	sf = db.Column(db.Integer)
	ra = db.Column(db.Integer)
	er = db.Column(db.Integer)
	era = db.Column(db.Float)
	cg = db.Column(db.Integer)
	sho = db.Column(db.Integer)
	sv = db.Column(db.Integer)
	ipouts = db.Column(db.Integer)
	ha = db.Column(db.Integer)
	hra = db.Column(db.Integer)
	bba = db.Column(db.Integer)
	soa = db.Column(db.Integer)
	e = db.Column(db.Integer)
	dp = db.Column(db.Integer)
	fp = db.Column(db.Float)
	name = db.Column(db.String(50))
	park = db.Column(db.String(255))
	attendance = db.Column(db.Integer)
	bpf = db.Column(db.Integer)
	ppf = db.Column(db.Integer)
	teamIDBR = db.Column(db.String(3))
	teamIDlahman45 = db.Column(db.String(3))
	teamIDretro = db.Column(db.String(3))










class people(db.Model):
	__tablename__ = "people"
	playerID = db.Column(db.String(9), primary_key=True)
	birthYear = db.Column(db.Integer)
	birthMonth = db.Column(db.Integer)
	birthDay = db.Column(db.Integer)
	birthCountry = db.Column(db.String(255))
	birthState = db.Column(db.String(255))
	birthCity = db.Column(db.String(255))
	deathYear = db.Column(db.Integer)
	deathMonth = db.Column(db.Integer)
	deathDay = db.Column(db.Integer)
	deathCountry = db.Column(db.String(255))
	deathState = db.Column(db.String(255))
	deathCity = db.Column(db.String(255))
	nameFirst = db.Column(db.String(255))
	nameLast = db.Column(db.String(255))
	nameGiven = db.Column(db.String(255))
	weight = db.Column(db.Integer)
	height = db.Column(db.Integer)
	bats = db.Column(db.String(255))
	throws = db.Column(db.String(255))
	debut = db.Column(db.String(255))
	finalGame = db.Column(db.String(255))
	retroID = db.Column(db.String(255))
	bbrefID = db.Column(db.String(255))
	birth_date = db.Column(db.Date)
	debut_date = db.Column(db.Date)
	finalgame_date = db.Column(db.Date)
	death_date = db.Column(db.Date)


class pitching(db.Model):
	__tablename__ = "pitching"
	id = db.Column(db.Integer, primary_key=True)
	playerID = db.Column(db.String(9))
	yearID = db.Column(db.Integer)
	stint = db.Column(db.Integer)
	teamID = db.Column(db.String(3))
	team_ID = db.Column(db.Integer)
	lgID = db.Column(db.String(2))
	W = db.Column(db.Integer)
	L = db.Column(db.Integer)
	G = db.Column(db.Integer)
	gs = db.Column(db.Integer)
	cg = db.Column(db.Integer)
	sho = db.Column(db.Integer)
	sv = db.Column(db.Integer)
	ip = db.Column(db.Float)
	IPouts = db.Column(db.Integer)
	H = db.Column(db.Integer)
	er = db.Column(db.Integer)
	hr = db.Column(db.Integer)
	bb = db.Column(db.Integer)
	so = db.Column(db.Integer)
	BAOpp = db.Column(db.Float)
	era = db.Column(db.Float)
	ibb = db.Column(db.Integer)
	wp = db.Column(db.Integer)
	hbp = db.Column(db.Integer)
	bk = db.Column(db.Integer)
	bfp = db.Column(db.Integer)
	gf = db.Column(db.Integer)
	r = db.Column(db.Integer)
	sh = db.Column(db.Integer)
	sf = db.Column(db.Integer)
	gidp = db.Column(db.Integer)

	def setIP(self):
		self.ip = self.IPouts / 3
		db.session.commit()


class fielding(db.Model):
	__tablename__ = "fielding"
	id = db.Column(db.Integer, primary_key=True)
	playerID = db.Column(db.String(9), unique=True)
	yearID = db.Column(db.Integer)
	stint = db.Column(db.Integer)
	teamID = db.Column(db.String(3))
	team_ID = db.Column(db.Integer)
	lgID = db.Column(db.String(2))
	pos = db.Column(db.String(2))
	G = db.Column(db.Integer)
	gs = db.Column(db.Integer)
	InnOuts = db.Column(db.Integer)
	po = db.Column(db.Integer)
	a = db.Column(db.Integer)
	e = db.Column(db.Integer)
	dp = db.Column(db.Integer)
	pb = db.Column(db.Integer)
	wp = db.Column(db.Integer)
	sb = db.Column(db.Integer)
	cs = db.Column(db.Integer)
	zr = db.Column(db.Integer)


class managers(db.Model):
	__tablename__ = "managers"
	id = db.Column(db.Integer, primary_key=True)
	playerID = db.Column(db.String(9), unique=True)
	yearID = db.Column(db.Integer)
	teamID = db.Column(db.String(3))
	team_ID = db.Column(db.Integer)
	lgID = db.Column(db.String(2))
	inseason = db.Column(db.Integer)
	G = db.Column(db.Integer)
	W = db.Column(db.Integer)
	L = db.Column(db.Integer)
	teamRank = db.Column(db.Integer)
	plyrMgr = db.Column(db.String(1))

