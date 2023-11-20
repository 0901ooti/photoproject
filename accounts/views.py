from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):

    # 定義したフォームクラス
    form_class = CustomUserCreationForm
    # レンダリングするテンプレート
    template_name = 'signup.html'
    # サインアップ後のリダイレクト先
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        # フォームデータの登録、フィールド値をデータベースに保存

        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    # レンダリングするテンプレート
    template_name = 'signup_success.html'