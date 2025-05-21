# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split string by commas and/or whitespace
        potential_emails = re.split(r'[,\s]+', self.email_addresses)

        # Regex pattern for valid email addresses
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Filter valid emails, remove empty strings, ensure uniqueness, and sort
        valid_emails = sorted(set(
            email for email in potential_emails
            if re.match(email_pattern, email)
        ))

        return valid_emails
