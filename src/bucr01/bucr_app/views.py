from .forms import UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Reservation, Review
from django.contrib.auth.forms import UserCreationForm
from .forms import RestaurantRegistrationForm, ReservationForm, ReviewForm, UserProfileForm
from .models import UserProfile


def homepage(request):
    # Logic to fetch and display featured restaurants
    featured_restaurants = Restaurant.objects.all()
    context = {'featured_restaurants': featured_restaurants}
    return render(request, 'homepage.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        # form = UserLoginForm(request.POST)
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('homepage')


@login_required
def my_reservations(request):
    # Logic to fetch and display user's reservations
    reservations = Reservation.objects.filter(user=request.user)
    context = {'reservations': reservations}
    return render(request, 'reservations.html', context)


def restaurant_detail(request, restaurant_id):
    # Logic to fetch and display restaurant details
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    reviews = Review.objects.all()
    context = {'restaurant': restaurant, 'reviews': reviews}
    return render(request, 'restaurant_detail.html', context)


def restaurant_list(request,):
    # Logic to fetch and display restaurant details
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'restaurant_list.html', context)


@login_required
def create_reservation(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        print(form)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.restaurant = restaurant
            # Retrieve the table ID from the form or any other means
            # table_id = form.cleaned_data['table_id']

            reservation.save()
            return redirect('reservation_success')
            return render(request, 'create_reservation.html', context)
    else:
        form = ReservationForm()

    context = {
        'form': form,
        'restaurant': restaurant.id
    }
    return render(request, 'create_reservation.html', context)


def reservation_success(request):
    return render(request, 'reservation_success.html')


@login_required
def leave_review(request, restaurant_id):
    # Logic to leave a review for a restaurant
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant_detail', restaurant_id=restaurant_id)
    else:
        form = ReviewForm()

    context = {'form': form, 'restaurant': restaurant}
    return render(request, 'leave_review.html', context)


def user_registration(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()  # Save the User instance first
            profile = profile_form.save(commit=False)
            profile.user = user  # Assign the User instance to the user field of UserProfile
            profile.save()  # Save the UserProfile instance

            # Redirect to the desired page after successful registration
            return redirect('homepage')
    else:
        user_form = UserCreationForm()
        profile_form = UserProfileForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'user_registration.html', context)

# def user_registration(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             profile = UserProfile(user=form)
#             return redirect('homepage')
#         else:
#             print(messages.error)

#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'user_registration.html', context)


def restaurant_registration(request):
    if request.method == 'POST':
        form = RestaurantRegistrationForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Restaurant registered Successfully")
            return redirect('homepage')
        else:
            messages.error(request, 'an error occured')
    else:
        form = RestaurantRegistrationForm()
    context = {'form': form}
    return render(request, 'restaurant_registration.html', context)


@login_required
def user_profile(request):
    # Assuming a OneToOne relationship between User and UserProfile
    profile = UserProfile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'user_profile.html', context)


# Search View


def search_view(request):
    query = request.GET.get('query')
    results = Restaurant.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})
