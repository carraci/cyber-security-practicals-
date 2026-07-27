import hmac
import hashlib

secret_key = input("Enter the secret key: ").encode()
message = input("Enter the message: ").encode()

mac = hmac.new(secret_key, message, hashlib.sha256).hexdigest()

print("\nGenerated MAC:", mac)

received_message = input("\nEnter the message for verification: ").encode()

received_mac = hmac.new(secret_key, received_message, hashlib.sha256).hexdigest()

print("\nVerifying Message...")

if hmac.compare_digest(mac, received_mac):
    print("Authentication Successful!")
    print("Message Integrity Verified.")
else:
    print("Authentication Failed!")
    print("Message has been modified.")
