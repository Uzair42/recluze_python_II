import re


heystack = "The quick brown fox jumps over the lazy dog."

neddle = "fox"

match = re.search(neddle, heystack)
if match :
    print(f"Found '{neddle}' in the string at position {match.start()} to {match.end()}.")

else :
    print(f"'{neddle}' not found in the string.")


#----------------------------------

stringText=""" uzair , phone number is 123-456-7890 , email is uzair@gmail.com , another phone number is 987-654-3210 , another email is 
abc@gmail.com
"""


pattern=r"is*"

m1=re.search(pattern,stringText)

print(m1)
print(f"match text is : {m1.group()}   ")


#-------------------------------------
pattern=r"\d{3}-\d{3}-\d{4}"
matches=re.findall(pattern,stringText)
for match in matches:
    print(f"Found phone number: {match}")


#--------------------------------------------
pattern_email=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email_matches=re.findall(pattern_email,stringText)
for email in email_matches:
    print(f"Found email address: {email}")  


#----------------------------------
# Replacing phone numbers with a placeholder
redacted_text=re.sub(pattern,"[hide PHONE]",stringText)
print("Redacted Text:")
print(redacted_text)

#-----------------------------------
# Splitting the text based on commas
parts=re.split(r",\s*",stringText)
print("Splitted Parts:")
for part in parts:
    print(part)

#-----------------------------------
# Using groups to extract area codes from phone numbers
pattern_group=r"(\d{3})-(\d{3})-(\d{4})"
group_matches=re.findall(pattern_group,stringText)
for area_code, central_office, line_number in group_matches:
    print(f"Area Code: {area_code}, Central Office: {central_office}, Line Number: {line_number}")
#-----------------------------------
# Using raw strings to define a pattern for Windows file paths
windows_path=r"C:\\Users\\Username\\Documents\\file.txt"
pattern_path=r"C:\\\\Users\\\\[a-zA-Z0-9]+\\\\Documents\\\\file\.txt"
if re.match(pattern_path, windows_path):
    print("Valid Windows file path.")
else:
    print("Invalid Windows file path.")
#-----------------------------------
# Compiling a regex pattern for better performance
compiled_pattern=re.compile(r"\d{3}-\d{3}-\d{4}")
for match in compiled_pattern.finditer(stringText):
    print(f"Found phone number using compiled pattern: {match.group(0)}")