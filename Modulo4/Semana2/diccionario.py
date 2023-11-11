import csv
import datetime
import email
import smtplib
import sys
# These lines import necessary modules for working with CSV files, handling dates, sending emails, and interacting with the system.


def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print("    send_reminders 'date|Meeting Title|emails' ")
    return 1
# The usage function provides information about how to use the script. If the user doesn't provide the correct command
# line arguments, this function is called to display usage instructions.



def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strptime("%A")
# The dow (day of the week) function takes a date in the format "YYYY-MM-DD," converts it into a datetime object,
# and returns the corresponding day of the week.



def message_template(date, title, name):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
Hi {name}!

This is a quick mail to remind you all that we have a meeting about:
"{title}"
the {weekday} {date}.

See you there.
''')
    return message
# The message_template function creates an email message template based on the provided date, meeting title, and recipient
# name. It sets the subject and content of the email.



def read_names(contacts):
    names = {}
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            names[row[0]] = row[1]
    return names
# The read_names function reads a CSV file containing email addresses and corresponding names, creating a dictionary mapping emails to names.




def send_message(date, title, emails, contacts):
    smtp = smtplib.SMTP('localhost')  # Se conecta al servidor SMTP local
    names = read_names(contacts)  # Lee los nombres desde el archivo de contactos
    for email in emails.split(','):  # Itera sobre las direcciones de correo electrónico
        name = names[email]  # Obtiene el nombre asociado a la dirección de correo electrónico
        message = message_template(date, title, name)  # Crea el mensaje utilizando una plantilla
        message['From'] = 'noreply@example.com'  # Establece la dirección de correo electrónico del remitente
        message['To'] = email  # Establece la dirección de correo electrónico del destinatario
        smtp.send_message(message)  # Envía el mensaje por correo electrónico
    smtp.quit()  # Cierra la conexión SMTP
    pass
"""Ten en cuenta que la función asume un servidor SMTP local y utiliza una plantilla de mensaje. Además, espera que las
direcciones de correo electrónico estén separadas por comas en la cadena emails.(sin contar 'pass'"""



# La 'send_message' función envía recordatorios de reuniones a una lista de direcciones de correo electrónico. Utiliza el
# protocolo0 SMTP para enviar correos electrónicos. La dirección del remitente está configurada en ' noreply@example.com '. La función
# itera sobre las direcciones de correo electrónico proporcionadas, recupera el nombre del destinatario del 'names' diccionario, crea
# un mensaje usando 'message_template' y envía el mensaje.

"""Este script parece diseñado para leer detalles de reuniones desde la línea de comando, leer nombres de destinatarios de
un archivo CSV y enviar recordatorios de reuniones a direcciones de correo electrónico específicas."""
