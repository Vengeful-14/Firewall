import os
import subprocess
import time
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def fetch_ipaddress():
    while True:
        users_ref = db.collection("ipaddress")
        port_ref = db.collection("PORTs")

        docs = users_ref.stream()
        ports = port_ref.stream()

        for doc in docs:
            ip_address = doc.to_dict().get('ipaddress', '').strip()
            status = doc.to_dict().get('status','').strip()
            if status == 'blocked':
                   print(ip_address)
            elif status == "allowed":
                    print(ip_address)
            #command = f"sudo ufw route deny to {ip_address}"
            #subprocess.run(command, shell=True, check=True)
            #print(ip_address)
            #print(f"Successfully blocked IP address: {ip_address}")
        
        for port in ports:
            myport = port.to_dict().get('url_name','').strip()
            #command = f"sudo ufw route deny proto tcp to any port {myport}"
            print(myport)
            #print(f"Successfully blocked Port: {myport}")
        # Wait for 2 minutes before fetching data again
        print("Waiting for 2 minutes before the next fetch...")
        time.sleep(10)  # Sleep for 120 seconds (2 minutes)

if __name__ == "__main__":
    print("Attaching Firestore listeners...")
    fetch_ipaddress()

