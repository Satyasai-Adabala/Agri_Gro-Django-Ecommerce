from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, help_text='Paste a direct image link (e.g. from Unsplash) instead of uploading a file.', null=True),
        ),
    ]
