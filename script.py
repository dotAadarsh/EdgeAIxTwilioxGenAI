import subprocess
import re
from xata.client import XataClient
import os
from twilio.rest import Client

def send_whatsapp_message(body):
    # Set up Twilio client
    account_sid = "TWILIO_ACCOUNT_SID"
    auth_token = "TWILIO_AUTH_ID"
    client = Client(account_sid, auth_token)

    # Send WhatsApp message
    message = client.messages.create(
        from_="whatsapp:+14151111111",
        body=body,
        to="whatsapp:+111111111"
    )

    print(message.body)

def run_command(command):
    # Send a WhatsApp message at the start
    send_whatsapp_message("Edge Impulse inferencing started.")
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    max_values = []
    xata = XataClient()  # Initialize the XataClient

    while True:
        output = process.stdout.readline().decode().strip()
        if output == '' and process.poll() is not None:
            break
        if output:
            if "Predictions" in output:
                predictions = []
                for _ in range(4):  # Read the next 4 lines for predictions
                    prediction_line = process.stdout.readline().decode().strip()
                    predictions.append(prediction_line)
                
                # Extract the label and value
                extracted_values = {}
                for prediction in predictions:
                    match = re.match(r"(.*):\s+(\d+\.\d+)", prediction)
                    if match:
                        label, value = match.groups()
                        extracted_values[label] = float(value)
                
                # Find the max value and corresponding label
                if extracted_values:
                    max_label = max(extracted_values, key=extracted_values.get)
                    max_value = extracted_values[max_label]
                    max_values.append(f"{max_label}: \t{max_value}")
                    
                    # Save to database
                    data = xata.records().insert("predictions", {
                        "label": max_label,
                        "value": max_value
                    })
                    print(data)
    
    # Write the max values to the file
    with open('output.txt', 'w') as file:
        for value in max_values:
            file.write(value + '\n')

    # Send a WhatsApp message at the end
    send_whatsapp_message("Edge Impulse inferencing ended.")
    
    return process.poll()

command = "edge-impulse-run-impulse"
run_command(command)
