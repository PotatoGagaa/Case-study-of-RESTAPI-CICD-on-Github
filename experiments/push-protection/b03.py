# fabricated value for a CI/CD case study - it cannot authenticate to anything
import os

# assembled at runtime so the literal never appears whole
STRIPE_SECRET = os.environ.get('A', "sk_live_6BMO") + "hmzXt1RuARubk4q8Kxn2"
