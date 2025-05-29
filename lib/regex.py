import re

# Name regex (already working)
name = r"^[A-Z][a-z]*(?:[-'][A-Z][a-z]*)?(?: [A-Z][a-z]*(?:[-'][A-Z][a-z]*)?)?$"
name_regex = re.compile(name)

# Phone number regex
phone_number = r"^(\(\d{3}\)\s*|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)

# Email regex (now disallows starting with a number)
email_address = r"^[a-zA-Z][\w\.-]*@[\w\.-]+\.\w{2,}$"
email_regex = re.compile(email_address)
