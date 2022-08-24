from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Recruit
from .models import Company
from .forms import RecruitForm


def index(request):
    recruit_list = Recruit.objects.order_by('-id')
    context = {'recruit_list': recruit_list}
    return render(request, 'wanted/recruit_list.html', context)


def create(request):
    if request.method == 'POST':
        form = RecruitForm(request.POST)
        if form.is_valid():
            recruit = form.save(commit=False)
            company_id = recruit.company
            company = Company.objects.get(id=company_id)
            recruit.company_name = company.company_name
            recruit.country = company.country
            recruit.region = company.region
            recruit.save()
            return redirect('wanted:index')
    form = RecruitForm()
    return render(request, 'wanted/recruit_form.html', {'form': form})


def detail(request, recruit_id):
    recruit = get_object_or_404(Recruit, pk=recruit_id)
    own_recruit_list = Recruit.objects.filter(company_name=recruit.company_name)
    context = {'recruit': recruit, 'own_recruit_list': own_recruit_list}
    return render(request, 'wanted/recruit_detail.html', context)
