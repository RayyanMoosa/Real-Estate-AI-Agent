from dotenv import dotenv_values

# Load values from .env into a dictionary
env = dotenv_values(".env")

# Print the correct values using keys, NOT values
print("OPENAI_API_KEY:", env["OPENAI_API_KEY"])
print("TWILIO_ACCOUNT_SID:", env["TWILIO_ACCOUNT_SID"])
print("TWILIO_AUTH_TOKEN:", env["TWILIO_AUTH_TOKEN"])
print("TWILIO_WHATSAPP_NUMBER:", env["TWILIO_WHATSAPP_NUMBER"])