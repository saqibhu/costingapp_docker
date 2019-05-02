# Generated by Django 2.2 on 2019-05-02 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblprice',
            name='tblpricetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costingapp.TblPriceType'),
        ),
        migrations.AlterField(
            model_name='tblprice',
            name='tblproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tblprice', to='costingapp.TblProduct'),
        ),
        migrations.AlterField(
            model_name='tblproduct',
            name='full_title',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='tblproduct',
            name='impression',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tblproduct',
            name='isbn13',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='tblproduct',
            name='tblstatus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tblproduct', to='costingapp.TblStatus'),
        ),
    ]
