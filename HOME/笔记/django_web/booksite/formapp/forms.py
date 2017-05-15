#coding=utf-8
from django import forms
from models import *

TOPOC_CHOICE = (
        ('lever1',' 差评'),
        ('lever2',' 中评'),
        ('lever3',' 好评'),
)
class RemarkForm(forms.Form):
    subject = forms.CharField(max_length = 100,label = '标题' )
    mail = forms.EmailField(label = '邮件')
    topic = forms.ChoiceField(choices = TOPOC_CHOICE,label = '评分')
    message = forms.CharField(label = '内容',widget  = forms.Textarea)
    cc_myself = forms.BooleanField(required = False,label = '订阅')

    def clean_message(self):
        message = self.cleaned_data['message']
        num = len(message.split())
        if num < 3:
            raise forms.ValidationError('Not enough words!')
        return message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Adver
        fields = ('orderID','title','content')
