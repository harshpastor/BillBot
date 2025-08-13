# provider_help.py

PROVIDER_GUIDE = {
    "gmail.com": {
        "imap": "imap.gmail.com",
        "instructions": """
Gmail Login Help:
1. Enable IMAP: Gmail → Settings → See all settings → Forwarding & POP/IMAP → Enable IMAP.
2. Enable 2FA in your Google Account.
3. Create an App Password: Google Account → Security → App passwords → Select 'Mail' and your device → Generate.
4. Use the generated 16-character password in place of your normal password.
"""
    },
    "outlook.com": {
        "imap": "imap-mail.outlook.com",
        "instructions": """
Outlook Login Help:
1. Enable 2FA in your Microsoft account.
2. Go to Security → App Passwords → Create new app password.
3. Use that password instead of your main password.
"""
    },
    "yahoo.com": {
        "imap": "imap.mail.yahoo.com",
        "instructions": """
Yahoo Login Help:
1. Enable 2FA in your Yahoo account.
2. Go to Account Security → Generate app password → Choose 'Mail'.
3. Use that instead of your main password.
"""
    },
    "icloud.com": {
        "imap": "imap.mail.me.com",
        "instructions": """
iCloud Login Help:
1. Enable 2FA in your Apple ID account.
2. Go to appleid.apple.com → Sign in → Security → Generate app-specific password.
3. Use that instead of your normal password.
"""
    },
    "zoho.com": {
        "imap": "imap.zoho.com",
        "instructions": """
Zoho Mail Login Help:
1. Enable IMAP in Zoho Mail Settings.
2. If 2FA is on, generate an app password from Zoho account security settings.
"""
    }
}

def get_provider_info(email):
    domain = email.split("@")[-1].lower()
    return PROVIDER_GUIDE.get(domain, None)
