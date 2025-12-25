import re

# eamil extraction 

dummy_text="""Hello,my name is Babar Azam , With 4204 runs in T20 cricket he is one of the best batsman.
You can contact me at 0312-3456789 or at email : babarazam56@gmail.com and also follow me on my other socil media email : thepcb@gmail.com"""

#---------------------------------------------------
pattern_email=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# #------------------------------------------------------

# ---- str_prefix = ".*":
#  It expects some text at the very beginning.


# ------str_username = "[a-zA-Z0-9.]*": 
# It defines the part before the @. It says the username can be letters, numbers, or dots.


# ------str_domain = ".*\\..*?":
#  It defines the part after the @. It looks for some text,
#  a literal dot (like .com), and then a little bit more text.


# ------str_email: 
# It glues the username, the @ symbol, and the domain together.


# ------needle: 
# It adds a space (\\s) before and after the email.
#  This ensures it finds a standalone email address,
#  not just text that looks like one inside another word.
# #---------------------------------------------------------

str_prefix=".*"
username="[a-zA-Z0-9.]*"
domain=".*\\..*?"

#---------------------------------------------------------

emial_str=username + "@" + domain

needle= "\s" + emial_str + "\s" 

#---------------------------------------------------------

email_matchs=re.findall(needle,dummy_text)

for email in email_matchs:
    print(f"Found email address: {email}")


