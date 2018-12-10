from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=2,required=True,
                            error_messages={
                                'required':'标题为必填'
                            })
    content = forms.CharField(min_length=10,required=True,
                              error_messages={
                                  'required':'文章内容必填'
                              })
    describe = forms.CharField(min_length=10,required=True,
                           error_messages={
                               'required':'简短描述必填'
                           })
    pic = forms.ImageField(required=False)
    category = forms.CharField(required=False)
    visibility = forms.CharField(required=False)


class TypeForm(forms.Form):
    name = forms.CharField(min_length=1,required=True,
                           error_messages={
                               'required': '栏目名必填'
                           })
    alias = forms.CharField(required=False)
    fid = forms.CharField(required=False)
    describe = forms.CharField(required=False)