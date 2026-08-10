p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

ram_private = int(input("Enter Ram's private key: "))
sachine_private = int(input("Enter Sachine's private key: "))

ram_public = pow(g, ram_private, p)
sachine_public = pow(g, sachine_private, p)

print("\n--- Public Key Exchange ---")
print("Ram's public key:", ram_public)
print("Sachine's public key:", sachine_public)

ram_shared_secret = pow(sachine_public, ram_private, p)
sachine_shared_secret = pow(ram_public, sachine_private, p)

print("\n--- Shared Secret ---")
print("Ram's shared secret:", ram_shared_secret)
print("Sachine's shared secret:", sachine_shared_secret)

if ram_shared_secret == sachine_shared_secret:
    print("\nKey exchange successful!")
    print("Shared secret key:", ram_shared_secret)
else:
    print("\nKey exchange failed!")
