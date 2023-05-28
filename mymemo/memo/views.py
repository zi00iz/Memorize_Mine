from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm
# Create your views here.

def memo_list(request):
    memoz = Memo.objects.all().order_by('created')
    return render(request, 'memo/memo_list.html', {'memoz':memoz})

def memo_detail(request, pk):
    memo = Memo.objects.get(id=pk)
    return render(request, 'memo/memo_detail.html', {'memo':memo})

def memo_post(request): 
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('memo_list')
    else:
        form = MemoForm()
    return render(request, 'memo/memo_post.html', {'form': form})

def memo_edit(request, pk):
    memo = Memo.objects.get(id=pk)
    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('memo_list')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memo/memo_post.html', {'form': form})

def memo_delete(request, pk):
    memo = Memo.objects.get(id=pk)
    memo.delete()
    return redirect('memo_list')