# Generated by Django 2.2.27 on 2023-05-05 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='模板名称')),
                ('description', models.TextField(max_length=240, verbose_name='描述')),
                ('content', models.TextField(verbose_name='css内容')),
            ],
            options={
                'verbose_name': '简历模板',
                'verbose_name_plural': '简历模板',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='简历标题')),
                ('body', models.TextField(verbose_name='简历内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('slug', models.SlugField(unique=True, verbose_name='访问地址')),
                ('is_open', models.BooleanField(default=False, verbose_name='是否公开')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.ResumeTemplate', verbose_name='简历模板')),
            ],
            options={
                'verbose_name': '个人简历',
                'verbose_name_plural': '个人简历',
                'ordering': ['-create_date'],
            },
        ),
    ]