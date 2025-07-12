from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages


def index(request):
    """
    Handle GET and POST requests for the job application form.

    - On GET: renders the empty form.
    - On POST: validates the submitted form, saves it to the database if valid,
      and displays a success message.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page with form and messages.
    """
    if request.method == "POST":
        form = ApplicationForm(request.POST)  # Bind POST data to the form
        if form.is_valid():
            # Extract cleaned form data
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # Save the validated data to the database
            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )

            # Display a success message to the user
            messages.success(request, "Form submitted successfully!")

    # Render the form page (both GET and after POST)
    return render(request, "index.html")
