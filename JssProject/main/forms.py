from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)
        # 모델안에서 어떤 것만 만들지(updated_at은 자동적으로 생성되어서 사용자가 입력할 필요가 없음)

    # 내장 함수 init, 항상 init이 클래스와 호출됨, 모델폼을 커스텀 해보자, 인자들은 모든걸 받는다는 뜻
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # 부모클래스에 있는 init을 가져와서 쓰자
        # why? 내부에 있는 자동으로 되는 것들을 참조해서 쓰려궁
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title',
            'placeholder' : '제목',
        })

