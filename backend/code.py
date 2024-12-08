# install this first
# pip install firebase-admin
# make sure na configure niyo yung raspi para i allow ang pag save ng configurations
# check niyo ang permissions and such
# need niyo din ifigure out kung paano magiging access point si raspi na sa kanya coconnect ang users para mablock yung mga naka save
# if okay na natest nyio na need niyo i-run using cron (you can search this naman) para on boot nag rrun yung program


import os
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# to block URLs
def block_urls(urls):
    for url in urls:
        command = f"echo 'ALL: {url}' >> /etc/hosts.deny"
        os.system(command)

# to unblock URLs
def unblock_urls(urls):
    for url in urls:
        command = f"sed -i '/ALL: {url}/d' /etc/hosts.deny"
        os.system(command)

# to block ports
def block_ports(ports):
    for port in ports:
        command = f"iptables -A OUTPUT -p tcp --dport {port} -j REJECT"
        os.system(command)

# to unblock ports
def unblock_ports(ports):
    for port in ports:
        command = f"iptables -D OUTPUT -p tcp --dport {port} -j REJECT"
        os.system(command)

# Ito yung function para maretrieve ni raspi ang chnages sa database
def urls_listener_callback(col_snapshot, changes, read_time):
    added_urls = []
    removed_urls = []

    for change in changes:
        doc = change.document
        url = doc.get("url_name")

        if change.type.name == "ADDED":
            added_urls.append(url)
        elif change.type.name == "REMOVED":
            removed_urls.append(url)

    if added_urls:
        block_urls(added_urls)
        print(f"Blocked new URLs: {added_urls}")
    if removed_urls:
        unblock_urls(removed_urls)
        print(f"Unblocked URLs: {removed_urls}")

# ito namna yung listener para sa ports
def ports_listener_callback(col_snapshot, changes, read_time):
    added_ports = []
    removed_ports = []

    for change in changes:
        doc = change.document
        port = doc.get("url_name")

        try:
            port = int(port)
        except ValueError:
            print(f"Invalid port value: {port}")
            continue

        if change.type.name == "ADDED":
            added_ports.append(port)
        elif change.type.name == "REMOVED":
            removed_ports.append(port)

    if added_ports:
        block_ports(added_ports)
        print(f"Blocked new Ports: {added_ports}")
    if removed_ports:
        unblock_ports(removed_ports)
        print(f"Unblocked Ports: {removed_ports}")


def attach_listeners():
    # listeners para sa URLS
    db.collection("URLs").on_snapshot(urls_listener_callback)

    # listeners para sa PORTs
    db.collection("PORTs").on_snapshot(ports_listener_callback)

if __name__ == "__main__":
    print("Attaching Firestore listeners...")
    attach_listeners()

    # para naka loop nagrrun yung script
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nStopped listening.")
