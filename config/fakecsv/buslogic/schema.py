from ..models import Schema, FullName, Job, Email, Date, Address, Text, CompanyName, PhoneNumber, DomainName, SchemaColum
import random


COLUMNS = (
        (',', 'Comma(,)'),
        ('    ', 'TAB(    )'),
        (';', 'Semicolon(;)'),
        (' ', 'Space(  )'),
        )


CHARACTERS = (
        ('"', 'Double-quote(")'),
        ("'", "Single-quote(')"),
        )

TYPES = (
        ('Full name', 'Full name'),
        ('Job', 'Job'),
        ('Email', 'Email'),
        ('Domain name', 'Domain name'),
        ('Phone number', 'Phone number'),
        ('Company name', 'Company name'),
        ('Text', 'Text'),
        ('Integer', 'Integer'),
        ('Address', 'Address'),
        ('Date', 'Date'),
)


def update_schema(pk, user, name, column_separator, string_character):
    """Добавляет схему в базу данных с определеным ключем"""
    return Schema.objects.create(
        pk=pk,
        user=user,
        name=name,
        column_separator=column_separator,
        string_character=string_character
        )


def add_schema(user, name, column_separator, string_character):
    """Добавляет схему в БД"""
    return Schema.objects.create(
        user=user,
        name=name,
        column_separator=column_separator,
        string_character=string_character
        )

def get_item(col, content, string_character, separator):
    """Создает строку взависимости от типа"""
    if col.type == 'Full name':
        rand_item = choose_item(FullName.objects.all())
        content += f'{string_character}{rand_item.full_name}{string_character}{separator}'
    elif col.type == 'Integer':
        content += f'{string_character}{random.randint(int(col.from_int), int(col.to_int))}{string_character}{separator}'
    elif col.type == 'Email':
        rand_item = choose_item(Email.objects.all())
        content += f'{string_character}{rand_item.email}{string_character}{separator}'
    elif col.type == 'Job':
        rand_item = choose_item(Job.objects.all())
        content += f'{string_character}{rand_item.job}{string_character}{separator}'
    elif col.type == 'Domain name':
        rand_item = choose_item(DomainName.objects.all())
        content += f'{string_character}{rand_item.domain}{string_character}{separator}'
    elif col.type == 'Phone number':
        rand_item = choose_item(PhoneNumber.objects.all())
        content += f'{string_character}{rand_item.phone}{string_character}{separator}'
    elif col.type == 'Company name':
        rand_item = choose_item(CompanyName.objects.all())
        content += f'{string_character}{rand_item.company_name}{string_character}{separator}'
    elif col.type == 'Text':
        text_speechs = random.randint(int(col.from_int), int(col.to_int))
        random_speechs = random.sample(list(Text.objects.all()), text_speechs)
        text = '' 
        for i in random_speechs:
            text += f'{i.speech}. '
        content += f'{string_character}{text[:-1]}{string_character}{separator}'
    elif col.type == 'Address':
        rand_item = choose_item(Address.objects.all())
        content += f'{string_character}{rand_item.address}{string_character}{separator}'
    elif col.type == 'Date':
        rand_item = choose_item(Date.objects.all())
        content += f'{string_character}{rand_item.date}{string_character}{separator}'
    return content[:-1]


def choose_item(objs):
    """Выбирает и возвращает рандомный элемент из списка"""
    items = list(objs)
    rand_item = random.choice(items)
    return rand_item


def create_context_for_file(columns, string_character, separator, rows):
    """Создает и возвращает контент для csv файла"""
    header = ''
    content = ''
    for col in columns:
        header += string_character+col.column_name+string_character+separator
        
    for i in range(rows):
        print('-')
        for col in columns:
            print('+')    
            content = get_item(col, content, string_character, separator)
        content += '\n'
    header = header[:-1]
    file_text = header + '\n' + content
    return file_text


def create_shema_column(col, schema):
    if col['from_int']:
        SchemaColum.objects.create(
                column_name=col['column_name'],
                type=col['type'],
                from_int=int(col['from_int']),
                to_int=int(col['to_int']),
                order=col['order'],
                schema=schema
                )
    else:
        SchemaColum.objects.create(
                column_name=col['column_name'],
                type=col['type'],
                order=col['order'],
                schema=schema
                )

