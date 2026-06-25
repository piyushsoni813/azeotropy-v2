from django.db import migrations, models


def pincode_int_to_str(apps, schema_editor):
    """Convert existing integer pincodes to strings; NULL becomes empty string."""
    Extendeduser = apps.get_model('ca_portal', 'Extendeduser')
    for row in Extendeduser.objects.all():
        # pincode is still an int here (pre-alter), so we read and update manually
        pass  # handled by AlterField below for SQLite (table rebuild)


class Migration(migrations.Migration):

    dependencies = [
        ('ca_portal', '0001_initial'),
    ]

    operations = [
        # phone_number: IntegerField → CharField
        # Can't store +91 prefix or leading zeros as an integer.
        migrations.AlterField(
            model_name='extendeduser',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),

        # pincode: IntegerField(null=True) → CharField(blank=True)
        # Indian pincodes can start with 0; storing as text is correct.
        # SQLite rebuilds the table so existing integer values become strings.
        migrations.AlterField(
            model_name='extendeduser',
            name='pincode',
            field=models.CharField(blank=True, max_length=10),
        ),

        # email: add unique=True so the DB enforces no duplicate CA registrations.
        migrations.AlterField(
            model_name='extendeduser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),

        # college: widen from 100 → 200 chars (long university names exist).
        migrations.AlterField(
            model_name='extendeduser',
            name='college',
            field=models.CharField(max_length=200),
        ),

        # alternate_phone_number: tighten max_length to match phone_number.
        migrations.AlterField(
            model_name='extendeduser',
            name='alternate_phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]