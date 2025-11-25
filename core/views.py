from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import MedicineForm, RegisterForm
from .models import Medicine, NGO, Donation
from .ocr import extract_expiry_date
from datetime import date, timedelta


# ------------------------------------
# Register New User
# ------------------------------------
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'core/register.html', {"form": form})


# ------------------------------------
# Home Page - Shows User Medicines
# ------------------------------------
@login_required
def home(request):
    meds = Medicine.objects.filter(user=request.user)
    return render(request, 'core/home.html', {"meds": meds})


# ------------------------------------
# Add Medicine
# ------------------------------------
@login_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            med = form.save(commit=False)
            med.user = request.user
            med.save()

            # Extract expiry from image using OCR
            exp = extract_expiry_date(med.image.path)
            if exp:
                try:
                    # Convert string to date object
                    day, month, year = exp.replace('-', '/').split('/')
                    med.expiry_date = date(int(year), int(month), int(day))
                    med.save()
                except:
                    pass

            return redirect('home')
    else:
        form = MedicineForm()

    return render(request, 'core/add_medicine.html', {"form": form})


# ------------------------------------
# Donation Page
# ------------------------------------
@login_required
def donate(request, med_id):
    med = Medicine.objects.get(id=med_id, user=request.user)
    ngos = NGO.objects.all()

    if request.method == 'POST':
        ngo = NGO.objects.get(id=request.POST['ngo'])
        Donation.objects.create(
            medicine=med,
            ngo=ngo,
            user=request.user
        )
        med.donated = True
        med.save()
        return redirect('home')

    return render(request, 'core/donate.html', {"med": med, "ngos": ngos})


# ------------------------------------
# Dashboard Page
# ------------------------------------
@login_required
def dashboard(request):
    meds = Medicine.objects.filter(user=request.user)

    total = meds.count()
    donated = meds.filter(donated=True).count()
    pending = meds.filter(donated=False).count()

    next_week = date.today() + timedelta(days=7)
    expiring = meds.filter(expiry_date__lte=next_week, donated=False)

    donations = Donation.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'core/dashboard.html', {
        "total": total,
        "donated": donated,
        "pending": pending,
        "expiring": expiring,
        "donations": donations
    })


# ------------------------------------
# NGO Map Page
# ------------------------------------
@login_required
def ngo_map(request):
    ngos = NGO.objects.all()
    return render(request, 'core/ngo_map.html', {"ngos": ngos})

