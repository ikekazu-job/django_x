
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_profiles_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='self_introDuction',
            new_name='self_introduction',
        ),
    ]