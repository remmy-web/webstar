from django.shortcuts import render

def homepage(request):
    pictures=[
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvKcFf23qxD5_iu0LFWIUTTyZAwfJJxl3pGQ&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsUkXKqwXWQlviibXvObDBpkFYctZVikU0nQ&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtYQg-V_gV72l4vv1oIyGGipxfSGsY5LVHCw&usqp=CAU"
    ]


    context={'pictures':pictures}
    return render(request, 'h.html', context)

def aboutus(request):
    context={}
    return render(request, 'aboutus.html', context)



