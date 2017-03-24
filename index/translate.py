#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yandex_translate import YandexTranslate
from transya.settings import API_KEY

translate = YandexTranslate(API_KEY)


def ru_translate(text):
    return translate.translate(text=text, lang='ru')


def en_translate(text):
    return translate.translate(text=text, lang='en')


def do_translate(to_lang, text):
    if to_lang == 'ru':
        return ru_translate(text=text)
    else:
        return en_translate(text=text)
