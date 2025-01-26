import os
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def urls_listener_callback(col_snapshot, changes, read_time):
    added_urls = []
    removed_urls = []

    for change in changes:
        doc = change.document
        url = doc.get("ipaddress")

        if change.type.name == "ADDED":
            added_urls.append(url)
        elif change.type.name == "REMOVED":
            removed_urls.append(url)

      
        print(f"Blocked new URLs: {added_urls}")

        print(f"Unblocked URLs: {removed_urls}")

def attach_listeners():
    # listeners para sa URLS
    db.collection("ipaddress").on_snapshot(urls_listener_callback)

    # listeners para sa PORTs
    # db.collection("PORTs").on_snapshot(ports_listener_callback)

if __name__ == "__main__":
    print("Attaching Firestore listeners...")
    attach_listeners()

    # para naka loop nagrrun yung script
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nStopped listening.")
