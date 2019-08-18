from django.core.mail import EmailMessage, send_mail, BadHeaderError,EmailMultiAlternatives

#-- Sendmail with html template
def sendmail(subject, html_content, from_email, to_email):
    #-- Sendmail: (Subjetc, body, email user, email host, False)
    
    try:
        #msg = EmailMessage(subject, html_content, from_email, [to_email])
        if type(to_email) == list:
          msg = EmailMultiAlternatives(subject, html_content, from_email, to_email)
        else:
          msg = EmailMultiAlternatives(subject, html_content, from_email, [to_email])
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send(fail_silently=True)
    except BadHeaderError:
        return HttpResponse('Error al enviar el correo')
    return True