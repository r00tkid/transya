from django.http import HttpResponse
from django.http import JsonResponse
from django.views import generic
import json
from index.models import Translation
from index.translate import do_translate


class IndexView(generic.TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        return context


class TranslateView(generic.TemplateView):
    template_name = 'index/translate.html'

    def get_context_data(self, **kwargs):
        context = super(TranslateView, self).get_context_data()
        to_lang = self.request.GET.get('to_lang')
        text = self.request.GET.get('text')
        result = do_translate(to_lang=to_lang, text=text)
        try:
            context['result'] = result
        except IndexError:
            pass
        return context


class SaveTranslateView(generic.TemplateView):
    template_name = 'index/translate.html'

    def get(self, request, *args, **kwargs):
        ru = request.GET.get('ru')
        en = request.GET.get('en')
        Translation.objects.create(ru=ru, en=en)
        return HttpResponse(200)


class ShowTranslateView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        translations = Translation.objects.all().order_by('-id')[:20]
        result = [obj.as_dict() for obj in translations]
        return HttpResponse(json.dumps({'data': result}))
