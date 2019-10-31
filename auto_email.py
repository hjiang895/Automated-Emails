import smtplib
mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()

mailer.starttls()

with open('email_info.txt') as f:
    my_email = f.readline().strip('\n')
    my_pwd = f.readline().strip('\n')
    target_email = f.readline().strip('\n')
mailer.login(my_email, my_pwd)
mailer.sendmail(my_email, target_email,'Subject: Reminder: Homework Due Tomorrow.\n\
Hi class,\n    Please remember that homework is due tomorrow!')
mailer.quit()
