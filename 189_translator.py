#https://pypi.org/project/translate/

from translate import Translator

translator_ja = Translator(to_lang = 'ja')
translator_bg = Translator(to_lang = 'bg')
translator_pl = Translator(to_lang = 'pl')
translator_it = Translator(to_lang = 'it')
translator_tl = Translator(to_lang = 'tl')

try:
    with open ('introduction.txt', mode = 'r') as my_file:
        text = my_file.read()
        #print(text)
        #translation_ja = translator_ja.translate(text)
        translation_bg = translator_bg.translate(text)
        translation_pl = translator_pl.translate(text)
        translation_it = translator_it.translate(text)
        translation_tl = translator_tl.translate(text)
        #print(translation_ja)
        #print(translation_bg)
        #print(translation_pl)
        #print(translation_it)
        #print(translation_tl)
        #with open ('translated_ja.txt', mode = 'w', encoding='utf-8') as my_translated_file_ja:
        #    my_translated_file_ja.write(translation_ja)
        with open ('translated_bg.txt', mode = 'w', encoding='utf-8') as my_translated_file_bg:
            my_translated_file_bg.write(translation_bg)
        with open ('translated_pl.txt', mode = 'w', encoding='utf-8') as my_translated_file_pl:
            my_translated_file_pl.write(translation_pl)
        with open ('translated_it.txt', mode = 'w', encoding='utf-8') as my_translated_file_it:
            my_translated_file_it.write(translation_it)
        with open ('translated_tl.txt', mode = 'w', encoding='utf-8') as my_translated_file_tl:
            my_translated_file_tl.write(translation_tl)
except FileNotFoundError as err:
    print('check the path and ensure the file exists')


#output:
#Hello, my name is Anna. I am new here in Sofia, Bulgaria.
#I am learning Cyrillic and Bulgarian language.
#How are you?

#こんにちは、Annaと申します。 私はブルガリアのソフィアに住んでいます。
#キリル語とブルガリア語を学んでいます。
#お元気ですか？

#modified to_lang = 'bg'
#Здравейте, казвам се Анна. Нов съм тук, в София, България.
#Уча кирилица и български език.
#Как си?

#modified to_lang = 'pl'
#Cześć, mam na imię Anna. Jestem tu nowy w Sofii w Bułgarii.
#Uczę się cyrylicy i języka bułgarskiego.
#Jak się masz?

#modified to_lang = 'it'
#Ciao, mi chiamo Anna. Sono nuovo qui a Sofia, in Bulgaria.
#Sto imparando il cirillico e il bulgaro.
#Come stai?

#modified to_lang = 'tl' (Tagalog)
#Hello, ang pangalan ko ay Anna. Bago lang ako dito sa Sofia, Bulgaria.
#Nag - aaral ako ng wikang Cyrillic at Bulgarian.
#Kamusta ka na?