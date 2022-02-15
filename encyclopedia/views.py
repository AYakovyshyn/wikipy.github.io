from django.shortcuts import render, redirect
from django import forms


from . import util

class NewWikiEntry(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': "form-t", "required style":"display:block"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': "form-c", "required style":"display:block"}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def add(request):
    if request.method == "POST":
        form = NewWikiEntry(request.POST, auto_id=False)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if util.get_entry(title) != None:
                return render(request, "encyclopedia/add.html", {
                    "form": form,
                    "message": "This Title is used on Another Page"
                })
            else:
                util.save_entry(title, content)
                return redirect('entry', title=title)
    else:
        form = NewWikiEntry(auto_id=False)
        return render(request, "encyclopedia/add.html", {
            "form": form,
            "message": ""
        })