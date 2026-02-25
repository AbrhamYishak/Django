from django import forms
from .models import Article

class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.all().filter(title__icontains = title)
        if qs.exists():
            self.add_error('title',"title already in use")
        return data

class articleFormOld (forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data['title']
        if title.lower().strip() == "the office":
            raise forms.ValidationError("this title is taken")
        return title
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data['title']
        content = cleaned_data['content']
        if title.lower().strip() == "the office":
            self.add_error('title',"the title is taken")
        if "password" in content:
            self.add_error("content","the content should not contain password")
        return cleaned_data
