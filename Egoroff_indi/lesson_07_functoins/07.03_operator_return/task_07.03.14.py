""" Ваша задача написать функцию get_domain_name, которая принимает строку url, извлекает из нее доменное имя и
возвращает его в качестве строки:
get_domain_name("http://google.com") => "google"
get_domain_name("http://google.co.jp") => "google"
get_domain_name("www.xakep.ru") => "xakep"
get_domain_name("https://youtube.com") => "youtube"
get_domain_name("https://www.asos.com") => "asos"
get_domain_name("http://www.lenovo.com") => "lenovo"
    Строка url может начинаться с протоколов http://  https:// или с www. URL, начинающиеся с протоколов http://
https://, могут также содержать www.
    Ваша задача написать только определение функции get_domain_name"""


def get_domain_name(url: str):
    if 'http://' in url:
        url = url.replace('http://', '')
        if 'www.' in url:
            url = url.replace('www.', '', 1)
            return url.split('.')[0]
        else:
            url = url.split('.')[0]
            return url
    elif 'https://' in url:
        url = url.replace('https://', '')
        if 'www.' in url:
            url = url.replace('www.', '', 1)
            return url.split('.')[0]
        else:
            return url.split('.')[0]
    elif 'www' in url:
        url = url.replace('www.', '', 1)
        return url.split('.')[0]


# variant 2:
# def get_domain_name(url:str) -> str:
#     url = url.replace("http://", "").replace("https://", "").replace("www.", "", 1)
#     return url.split('.')[0]

# код ниже не стоит удалять, он нужен для проверки
assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") == 'github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')
