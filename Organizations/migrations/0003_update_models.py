# Generated by Django 2.2.7 on 2019-11-30 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0002_add_models'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ability',
            options={'get_latest_by': 'expires', 'verbose_name_plural': 'abilities'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'get_latest_by': 'begin', 'verbose_name_plural': 'statuses'},
        ),
        migrations.RemoveField(
            model_name='ability',
            name='member',
        ),
        migrations.AddField(
            model_name='ability',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='orga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Organizations.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('a', 'aktiv'), ('p', 'passiv (fördernd)'), ('e', 'Ehrenmitglied'), ('o', 'other'), ('x', 'ausgeschieden')], max_length=20),
        ),
    ]