from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    #forms.pyで定義したフォームのクラス
    form_class = CustomUserCreationForm
    #レンダリングするテンプレート
    template_name = "signup.html"
    #サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')

    def form_vaild(self, form):
        #formオブジェクトのフィールド値をデータベースに保存
        user = form.save()
        self.object = user
        #戻り値はスーパークラスのform_vaild(form)
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    #レンダリングするテンプレート
    template_name = "signup_success.html"