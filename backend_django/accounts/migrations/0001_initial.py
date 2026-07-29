from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=20, choices=[('woman', 'woman'), ('employer', 'employer'), ('admin', 'admin')], default='woman')),
                ('phone', models.CharField(max_length=50, null=True, blank=True)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
                ('avatar', models.CharField(max_length=1024, default='', blank=True)),
                ('totalEarnings', models.FloatField(default=0)),
                ('isVerified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
            },
        ),
    ]
