from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['bayjel13@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Благодарим вас за обращение. В ближайшее время мы ответим вам на указанный адрес почты.")
            return redirect("/")
    context = {
        'form': form
    }
    return render(request, "contacts/contact.html", context)
