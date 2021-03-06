# Generated by Django 2.0.2 on 2018-02-12 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nadine', '0032_event_billing'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='e.g., Stripe, Visa, cash, bank transfer', max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='external_id',
            field=models.CharField(blank=True, help_text='ID used by payment service', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nadine.PaymentMethod'),
        ),
    ]
