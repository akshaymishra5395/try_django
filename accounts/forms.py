from django import forms
from django.contrib.auth  import authenticate,get_user_model
User=get_user_model()
class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            user=authenticate(username=username , password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm,self).clean(*args,**kwargs)

class RegisterForm(forms.ModelForm):
    firstName=forms.CharField(label='firstname')
    lastname =forms.CharField(label='lastname')
    email =forms.EmailField(label='email')
    password  =forms.CharField(widget=forms.PasswordInput,label='password')
    password2  =forms.CharField(widget=forms.PasswordInput,label='confirmPassword')
    class Meta:
        model = User
        fields=['username','firstName','lastname','email','password']

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise form.ValidationError('This email is already being used')
        return email
    
    def clean_password(self):
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password!=password2:
            raise forms.ValidationError('Password must match')
        return password

