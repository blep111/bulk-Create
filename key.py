import os

def approve_keys():
    # Hardcoded admin password (change this to your desired password)
    admin_password = "500"  # Replace with your secure password
    
    entered_password = input("Enter admin password: ").strip()
    if entered_password != admin_password:
        print("ACCESS DENIED: Incorrect password.")
        return
    
    key_file = "approved_keys.txt"
    print("ADMIN APPROVAL PANEL")
    print("Paste user keys one by one. Type 'done' to finish.")
    
    approved_keys = set()
    if os.path.exists(key_file):
        with open(key_file, 'r') as f:
            approved_keys = set(line.strip() for line in f if line.strip())
    
    while True:
        key = input("Enter user key to approve (or 'done' to exit): ").strip()
        if key.lower() == 'done':
            break
        if key and key not in approved_keys:
            approved_keys.add(key)
            print(f"Key '{key}' approved.")
        else:
            print(f"Key '{key}' already approved or invalid.")
    
    with open(key_file, 'w') as f:
        for key in approved_keys:
            f.write(key + '\n')
    
    print("Approved keys updated in 'approved_keys.txt'.")

if __name__ == "__main__":
    approve_keys()
