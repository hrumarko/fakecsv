import json
from .buslogic import schema as sch
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewSchemaForm, AddColumnForm, RegisterUserForm
from .models import Schema, SchemaColum, CsvFile
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = NewSchemaForm()
    add_col = AddColumnForm()
    ctx = {
            'form': form,
            'add_col': add_col,
    }
    return render(request, 'fakecsv/base.html', ctx)


def create_schema(request):
    json_req = json.loads(request.POST['json_schema'])
    
    user = request.user
    name = json_req['name']
    column_separator = json_req['column_separator']
    string_character = json_req['string_character']
    cols = json_req['cols']
    
    try:
        pk = int(json_req['pk'])
        Schema.objects.filter(pk=pk).delete()
        schema = sch.update_schema(pk, user, name, column_separator, string_character)
        for col in cols.values():
            sch.create_shema_column(col, schema)
    except:
        schema = sch.add_schema(user, name, column_separator, string_character)
        for col in cols.values():
            sch.create_shema_column(col, schema)
    return HttpResponse('hello')


def data_schemas(request):
    if request.user.is_authenticated:
        schemas = Schema.objects.filter(user=request.user)
    else:
        schemas = ''
    ctx = {
            'schemas':schemas,
            }
    return render(request, 'fakecsv/dataschemas.html', ctx)


def delete_schema(request, pk):
    Schema.objects.filter(pk=pk).delete()
    return redirect('data-schemas')


def data_sets(request, pk):
    schema = Schema.objects.get(pk=pk)
    cols = SchemaColum.objects.filter(schema=schema)
    files = CsvFile.objects.filter(user=request.user, schema=schema)
    ctx = {
            'cols': cols,
            'pk': pk,
            'files': files,
            'schema': schema,
            }
    return render(request, 'fakecsv/datasets.html', ctx)


def edit_schema(request, pk):
    schema = Schema.objects.get(pk=pk)
    data_schema = {
            'name': schema.name,
            'column_separator': schema.column_separator,
            'string_character': schema.string_character,
            }
    form = NewSchemaForm(data_schema)
    objs = SchemaColum.objects.filter(schema=schema)
    add_col = AddColumnForm()
    forms = []
    for obj in objs:
        data = {
                'name_column':obj.column_name,
                'type':obj.type,
                'from_int':obj.from_int,
                'to_int':obj.to_int,
                'order':obj.order,
                }
        forms.append(AddColumnForm(data))
    ctx = {
            'form': form,
            'add_col': add_col,
            'objs': forms,
    }
    return render(request, 'fakecsv/base.html', context=ctx)


def create_file(request):
    json_req = json.loads(request.POST['json_dct'])
    
    schema = Schema.objects.get(pk=json_req['pk'])
    name = schema.name
    separator = schema.column_separator
    string_character = schema.string_character
    rows = int(json_req['rows'])
    
    columns = SchemaColum.objects.filter(schema=schema)
    file_text = sch.create_context_for_file(columns, string_character, separator, rows)
    name = name.replace(' ', '') + str(rows)
    print(file_text)
    f = ContentFile(file_text, name=name + '.csv')
    CsvFile.objects.create(
            user=request.user,
            title=name,
            file=f,
            schema=schema
            )
    return HttpResponse('hello')


class UserRegister(CreateView):
    form_class = RegisterUserForm
    template_name = 'fakecsv/register.html'

    def get_success_url(self):
        return reverse_lazy('login')


class UserLogin(LoginView):
    template_name = 'fakecsv/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
