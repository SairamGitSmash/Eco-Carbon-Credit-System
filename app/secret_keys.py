import secrets

# Generate a secure SECRET_KEY
secret_key = secrets.token_hex(32)
print("SECRET_KEY:", secret_key)

# Generate a secure JWT_SECRET_KEY
jwt_secret_key = secrets.token_hex(32)
print("JWT_SECRET_KEY:", jwt_secret_key)