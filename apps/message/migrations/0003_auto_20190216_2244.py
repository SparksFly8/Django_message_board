# Generated by Django 2.1.7 on 2019-02-16 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20190216_2239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'ordering': ('-object_id',), 'verbose_name_plural': '用户留言信息'},
        ),
        migrations.AlterModelTable(
            name='usermessage',
            table='user_message',
        ),
    ]
