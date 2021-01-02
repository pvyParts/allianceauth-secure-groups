# Generated by Django 3.1.1 on 2021-01-03 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eveonline', '0012_index_additions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartFilter',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='SmartGroup',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('auto_group', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=True)),
                ('include_in_updates', models.BooleanField(default=True)),
                ('can_grace', models.BooleanField(default=False)),
                ('filters', models.ManyToManyField(to='securegroups.SmartFilter')),
                ('group', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
            options={
                'permissions': (('access_sec_group', 'Can access sec group requests screen.'),),
            },
        ),
        migrations.CreateModel(
            name='GroupUpdateWebhook',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('webhook', models.TextField()),
                ('extra_message', models.TextField(blank=True, default='')),
                ('group', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='GracePeriodRecord',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('grace_filter', models.CharField(max_length=100)),
                ('expires', models.DateTimeField()),
                ('group', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='securegroups.smartgroup')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AltCorpFilter',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('alt_corp', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='eveonline.evecorporationinfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AltAllianceFilter',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('alt_alli', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='eveonline.eveallianceinfo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
