"""Genera una lista que contenga direcciones de correo eléctronico completas(diana.prince@gmail.com)"""

def email_list(domains):
    emails = []
    for domain, users in domains.items():  # Cambié 'users' a 'domain' y 'user' a 'users'
        for user in users:
            emails.append(user + "@" + domain)  # Cambié 'users' a 'domain'
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
