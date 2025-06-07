import os
import csv
import datetime

log_file = 'logs.csv'

event = {
    "timestamp": datetime.datetime.now().isoformat(),
    "event_type": "Login Inválido",
    "source": "Sistema Windows",
    "details": "Tentativa de login com usuário inexistente"
}

file_exists = os.path.isfile(log_file)

with open(log_file, mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=event.keys())

    if not file_exists:
        writer.writeheader()

    writer.writerow(event)

print(f"[+] Log registrado: {event}")