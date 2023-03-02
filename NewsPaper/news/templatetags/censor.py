from django import template

register = template.Library()

@register.filter(name='censor')

def censor(value):
    split_value = value.split()
    len_value = len(split_value)
    bad_words = ['корова', 'глупый']
    len_bad_words =len(bad_words)
    for i in range(0,len_value):
        for k in range(0,len_bad_words):
         if split_value[i].lower() == bad_words[k].lower():
            raise SyntaxError ("Найдены недопустимые слова")    
         
    return value        

        