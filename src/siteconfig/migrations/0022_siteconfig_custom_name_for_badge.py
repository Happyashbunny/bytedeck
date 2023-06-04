# Generated by Django 3.2.17 on 2023-05-29 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteconfig', '0021_siteconfig_custom_name_for_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='custom_name_for_badge',
            field=models.CharField(default='Badge', help_text='A custom name specific to your deck to replace "Badge". Badges are markers given to students either             automatically as a result of meeting a prerequisite, or manually by a staff user. Badges can grant students             XP, or act as prerequisites to other content. For example, "Achievement", "Medal", or             "Certificate" might be a more suitable name than Badge, depending on your context.', max_length=20),
        ),
    ]