from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login', views.login_user),
    path('logout', views.logout_request),
    path('register', views.registration),

    # Dealers
    path('get_dealers', views.get_dealerships),
    path('get_dealers/<str:state>', views.get_dealerships),

    # Dealer details
    path('dealer/<int:dealer_id>', views.get_dealer_details),

    # Reviews
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews),

    # POST review
    path('add_review', views.add_review),
]