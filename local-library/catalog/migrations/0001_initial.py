# Generated by Django 4.2.7 on 2023-11-22 19:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Имя и отчество (опционально) автора', max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Фамилия автора', max_length=100, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(blank=True, help_text='Дата рождения автора', null=True, verbose_name='Дата рождения')),
                ('date_of_death', models.DateField(blank=True, help_text='Дата смерти автора', null=True, verbose_name='Дата смерти')),
            ],
            options={
                'verbose_name': 'Автора',
                'verbose_name_plural': 'Авторы',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название книги', max_length=200, verbose_name='Название книги')),
                ('summary', models.TextField(help_text='Краткое описание книги', max_length=1000, verbose_name='Описание')),
                ('isbn', models.CharField(help_text='13-ти символьный <a href="https://www.isbn-international.org/content/what-isbn">ISBN номер</a>', max_length=13, verbose_name='ISBN')),
                ('author', models.ForeignKey(help_text='Автор книги', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книгу',
                'verbose_name_plural': 'Книги',
                'ordering': ['author', 'title', 'language'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название жанра (Научная фантастик, психология и т.п.)', max_length=200, unique=True, verbose_name='Название жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Язык, на котором написан оригинал', max_length=100, unique=True, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный идентификатор экземпляря книги', primary_key=True, serialize=False, verbose_name='UUID')),
                ('imprint', models.CharField(help_text='Дата издания книги, издатель и т.п.', max_length=200, verbose_name='Издание')),
                ('due_back', models.DateField(blank=True, help_text='Дата, когда экземпляр должен быть возвращен', null=True, verbose_name='Дата возрата')),
                ('status', models.CharField(blank=True, choices=[('m', 'На обслуживании'), ('o', 'Выдан'), ('a', 'Доступен'), ('r', 'Забронирован')], default='m', help_text='Доступность экземпляр', max_length=1, verbose_name='Статус экземпляра')),
                ('book', models.ForeignKey(help_text='Книга, к которой относится экземпляр', null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.book', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Экземпляр книги',
                'verbose_name_plural': 'Экземпляры книг',
                'ordering': ['book', 'due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Жанры, к которым относится книга', to='catalog.genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Язык, на котором написана книга', on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.language', verbose_name='Язык'),
        ),
    ]
