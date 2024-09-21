from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def mental_health(request):
    professionals = [
        {'name': 'Dr. Sarah Thompson', 'profession': 'Clinical Psychologist'},
        {'name': 'Mr. John Doe', 'profession': 'Counseling Therapist'},
        {'name': 'Dr. Emily Johnson', 'profession': 'Licensed Mental Health Counselor'},
        {'name': 'Ms. Maria Garcia', 'profession': 'School Psychologist'},
        {'name': 'Dr. David Lee', 'profession': 'Psychiatrist'},
        {'name': 'Ms. Linda White', 'profession': 'Clinical Social Worker'},
        {'name': 'Dr. James Brown', 'profession': 'Family Therapist'},
        {'name': 'Ms. Anna Patel', 'profession': 'Substance Abuse Counselor'},
        {'name': 'Dr. Michael Smith', 'profession': 'Cognitive Behavioral Therapist'},
        {'name': 'Ms. Olivia Taylor', 'profession': 'Art Therapist'},
        {'name': 'Dr. Robert Wilson', 'profession': 'Clinical Psychologist'},
        {'name': 'Ms. Sophia Harris', 'profession': 'Play Therapist'},
        {'name': 'Dr. Kevin Lewis', 'profession': 'Neuropsychologist'},
        {'name': 'Ms. Emma Clark', 'profession': 'Marriage and Family Therapist'},
        {'name': 'Dr. Mia Walker', 'profession': 'Health Psychologist'},
        # Add more professionals as needed
    ]
    return render(request, 'main/mental_health.html', {'professionals': professionals})

def college_counselor(request):
    return render(request, 'main/college_counselor.html')

def self_help(request):
    return render(request, 'main/self_help.html')

def about_us(request):
    return render(request, 'main/about_us.html')
