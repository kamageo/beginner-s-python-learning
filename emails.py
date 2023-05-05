emails = {
    'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],

    'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],

    'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],

    'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],

    'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],

    'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']
}

email_list = []
for domain, names in emails.items():
    for name in names:
        email_list.append(name + '@' + domain)
email_list.sort()
for name in email_list:
    print(name)

# Не знаю, где здесь можно использовать генератор словарей