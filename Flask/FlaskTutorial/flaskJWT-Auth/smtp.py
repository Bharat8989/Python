import smtplib

sender = "Private Person <hello@bnk.com>"
receiver = "A Test User <bk2905190@gmail.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "2d39ca943669502e06d76996e11c945d")
    server.sendmail(sender, receiver, message)


