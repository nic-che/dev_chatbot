import googletrans
from googletrans import Translator

#cd to Bot_Functions before running
#running the library
translator = Translator()

#get the language codes
def lang_code(language):
    language = language.lower()
    lang_dict = googletrans.LANGUAGES

    for key in lang_dict.keys():
        if language == lang_dict[key]:
            return key
    
    return 'None'

#translate
def translator_func(msg, language='english'):
    if language.lower() == 'chinese':
        lc = 'zh-cn'
    elif language.lower() == 'kurdish':
        lc = 'ku'
    else:
        lc = lang_code(language)
        
    if lc == 'None':
        return 'Language not found.'

    return language + ":" + translator.translate(text=msg, dest=lc).text