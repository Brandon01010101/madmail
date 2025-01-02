import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# Configuration de votre compte Gmail
GMAIL_USER = "votre_adresse_email@gmail.com"
GMAIL_PASSWORD = "votre_mot_de_passe_d_application"  # Utilisez un mot de passe d'application

# Configuration du serveur SMTP de Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def envoyer_email(destinataire, sujet, message):
    """
    Envoie un e-mail à un destinataire spécifique.
    """
    try:
        # Création du message e-mail
        msg = MIMEMultipart()
        msg["From"] = GMAIL_USER
        msg["To"] = destinataire
        msg["Subject"] = sujet
        msg.attach(MIMEText(message, "plain"))

        # Connexion au serveur SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Démarrer une connexion sécurisée
            server.login(GMAIL_USER, GMAIL_PASSWORD)  # Connexion à votre compte Gmail
            server.sendmail(GMAIL_USER, destinataire, msg.as_string())  # Envoi de l'e-mail

        print(f"[SUCCÈS] Email sent 📩 {destinataire}")
    except Exception as e:
        print(f"[ERROR] Unable to send email 🔌📩 {destinataire}: {e}")

def envoyer_emails_en_masse(fichier_csv, sujet):
    """
    Lit un fichier CSV contenant les adresses e-mail et les messages,
    puis envoie les e-mails en masse.
    """
    try:
        with open(fichier_csv, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            print(f"[INFO] Sending emails from the CSV file 📩📗 : {fichier_csv}")
            for row in reader:
                destinataire = row["email"]
                message = row["message"]
                envoyer_email(destinataire, sujet, message)

    except FileNotFoundError:
        print(f"[ERROR] The file {fichier_csv} is not found 📗")
    except KeyError:
        print("[ERROR] The CSV file should contain the 'email' and 'message' columns 📗")
    except Exception as e:
        print(f"[ERROR] An error occurred 🔌 : {e}")

if __name__ == "__main__":
    # Paramètres de l'envoi
    fichier_csv = "emails.csv"  # Nom du fichier CSV contenant les adresses et les messages
    sujet = "Votre sujet ici"  # Sujet de l'e-mail

    print("Start sending bulk emails 📩📨")
    envoyer_emails_en_masse(fichier_csv, sujet)
    print("Sending Completed 📪 Thank you for using this program created by Brandon 💻👍")
