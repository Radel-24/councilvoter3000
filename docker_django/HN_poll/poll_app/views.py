import sqlite3, requests, json
from pickle import FALSE, TRUE
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, login, authenticate
from .models import Candidate
from requests_oauthlib import OAuth2Session
import os

def	vote_cand(candidate):
	con = sqlite3.connect('/poll_app/HN_poll/db.sqlite3')
	cur = con.cursor()
	t = ('%'+candidate+'%',)
	cur.execute("UPDATE poll_app_candidate SET votes = votes + 1 WHERE intra LIKE ?", t)
	con.commit()
	con.close()

def	vote(vote1, vote2, vote3):
	votes = [vote1, vote2, vote3]
	for vote in votes:
		if vote:
			vote_cand(vote)

def	check_intra(candidate):
	con = sqlite3.connect('/poll_app/HN_poll/db.sqlite3')
	cur = con.cursor()
	t = ('%'+candidate+'%',)
	c = cur.execute("SELECT intra FROM poll_app_candidate WHERE intra LIKE ?", t)
	cand = c.fetchall()
	if cand and cand[0] and cand[0][0] == candidate:
		return TRUE
	else:
		return FALSE

def	check_votes(vote1, vote2, vote3):
	votes = [vote1, vote2, vote3]
	for vote in votes:
		if (vote):
			if (check_intra(vote) == TRUE):
				continue
			else:
				return FALSE
	return TRUE

def	end(request, message):
	content = dict(text = message)
	return render(request, 'poll_app/end.html', content)

def	index(request):
	logout(request)
	return render(request, 'poll_app/index.html')

def get_current_path(request):
	return {
		'current_path': request.get_full_path()
	}

def get_referer(request):
	referer = request.META.get('HTTP_REFERER')
	if not referer:
		return None
	return referer

@login_required(login_url='poll_app:index')
def election(request, voter):
	message = ""
	if request:
		vote1 = request.POST.get('vote1')
		vote2 = request.POST.get('vote2')
		vote3 = request.POST.get('vote3')
		votes_help = [vote1, vote2, vote3]
		votes = []
		for vo in votes_help:
			if vo != "":
				votes.append(vo)
		help = set(votes)
		if (vote1 or vote2 or vote3):
			if (len(votes) != len(help)):
				message = "error: only one vote per candidate is possible"
			else:
				if (check_votes(vote1, vote2, vote3) == TRUE):
					con = sqlite3.connect('/poll_app/HN_poll/db.sqlite3')
					cur = con.cursor()
					t = (voter, )
					cur.execute("INSERT INTO poll_app_voter (id_42) VALUES (?)", t)
					con.commit()
					con.close()
					vote(vote1, vote2, vote3)
					logout(request)
					return redirect('poll_app:end', message="Your vote has been submitted!")
				else:
					message = "error: make sure the intra names are spelled correctly"
	candidate_list = Candidate.objects.order_by('name')
	context = {'candidate_list': candidate_list, 'invalid': message}
	return render(request, 'poll_app/election.html', context)

def	validation(request):
	print("hello")
	logout(request)
	test = get_current_path(request)
	test2 = json.dumps(test)
	code = test2.split("code=", 1)[1]
	code = code[:-2]
	client_id = os.environ['CLIENT_ID']
	client_secret = os.environ['CLIENT_SECRET']
	redirect_uri = 'https://council-vote.42heilbronn.de/poll/validation'
	oauth = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri)
	token = oauth.fetch_token(token_url='https://api.intra.42.fr/oauth/token', code=code, client_secret=client_secret)
	response = requests.get("https://api.intra.42.fr/oauth/token/info", token)
	user = response.json()
	response = requests.get("https://api.intra.42.fr/v2/me", token)
	user = response.json()
	campus_id = user['campus_users'][0]['campus_id']
	user_id = user["id"]
	cursus_id = user['cursus_users'][1]['cursus']['id']

	#check if user  is valid for voting
	if (campus_id == 39 and cursus_id == 21):
		#//check as well for right cursus
		con = sqlite3.connect('/poll_app/HN_poll/db.sqlite3')
		cur = con.cursor()
		t = ('%'+str(user_id)+'%',)
		c = cur.execute("SELECT id_42 FROM poll_app_voter WHERE id_42 LIKE ?", t)
		voter = c.fetchall()
		if (voter):
			return (redirect('poll_app:end', message="You have already voted"))
		con.commit()
		con.close()
		user = authenticate(username='voter', password=os.environ['VOTER_PWD'])
		login(request, user)
	else:
		return (redirect('poll_app:end', message="You aren't allowed to vote"))
	return redirect('poll_app:election', voter=user_id)

@user_passes_test(lambda u: u.is_superuser)
def	result(request):
	candidate_list = Candidate.objects.order_by('votes')
	context = {'candidate_list': candidate_list,}
	return render(request, 'poll_app/result.html', context)

