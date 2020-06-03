from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect


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
            messages.success(
                request, "Благодарим вас за обращение. В ближайшее время мы ответим вам на указанный адрес почты.")
            return HttpResponseRedirect(request.path_info)
            # return redirect("shop:product_list")
    context = {
        'form': form
    }
    return render(request, "contacts/contact.html", context)
