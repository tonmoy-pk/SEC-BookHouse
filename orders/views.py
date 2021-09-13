import stripe # import stripe library we already installed it.it look for a secret key called stripe.api_key which we can set to that value
from django.shortcuts import render  # render is using for function based charge view
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.models import Permission

# stripe.api_key = settings.STRIPE_TEST_SECRET_KEY # using stripe secret key from settings


class OrdersPageView(TemplateView): # simply use templateview for shows only template
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs): # when you submit the pay button in your stripe then it's can't works,by overriding get_context_data() we can elegently pass this information with our templateview
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context 

    def charge(request):
        permission = Permission.objects.get(codename='special_status') # get the permission,'special_status' means this book can access by this user because he buy this book using strpe
        u = request.user # get user
        u.user_permissions.add(permission)  # add to user's permission set,user can access the detailview of book,becuase he buy this book using stripe
        
        if request.method == 'POST' # we are sending data to Stripe here
            charge = stripe.Charge.create( # we make a charge that includes the amount,currency,description and source which has the unique token Stripe generated for this transaction called stripeToken
                amount = 3900,
                currency = usd,
                description = 'Purchase all books'
                source = request.POST['stripeToken']
            )
        return render(request, 'orders/charge.html') # lastly return the request object and load the charge.html template

