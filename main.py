import os
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("SiGSzIaAYRIzpHCjn4BV9acRS", "hMOpYtESFHdiwQ1epChevduOwxYggKFNnEfvvGTgkdItoJhKNf")
auth.set_access_token("2450112084-LRpxOlZG5KqPgJXGlV4Z60gT0SjY5qKK84IewHR", "GJk859TxZQCKhsxKq4RnG8P3XVcEBnSRMXiByx28H6RQL")

access_token= "2450112084-LRpxOlZG5KqPgJXGlV4Z60gT0SjY5qKK84IewHR"

access_token_secret= "GJk859TxZQCKhsxKq4RnG8P3XVcEBnSRMXiByx28H6RQL"

API_key = "SiGSzIaAYRIzpHCjn4BV9acRS"

API_secret_key= "hMOpYtESFHdiwQ1epChevduOwxYggKFNnEfvvGTgkdItoJhKNf"

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Meow")


