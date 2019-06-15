email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor(email):
  return email.replace("learning algorithms","X")
#print(censor(email_one))
props = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
def censor_strong(email):
  for n in props:
    if n in email:
      email = email.replace(n,"X")
  return email
#print (censor_strong(email_two))
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
def censor_ultra(email):
  for n in negative_words:
    if n in email and email.count(n)>1:
      email = email.replace(n,"x")
  for m in props:
    if m in email:
      email = email.replace(m,"x")
  return email
#print (censor_strong(email_three))
def censor_all(email):

  for n in negative_words:
    if n in text and text.count(n)>1:
      i = email.find(n)
      email = email.replace(email[i-1],"m")
      email = email.replace(email[i+1],"n")
      email = email.replace(n,"x")
  for m in props:
    if m in email:
      i = email.find(n)
      email = email.replace(email[i-1],"m")
      email = email.replace(email[i+1],"n")
      email = email.replace(m,"x")
  return email
print (censor_all(email_four))
