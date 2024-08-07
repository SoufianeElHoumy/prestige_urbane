# Generated by Django 5.0.6 on 2024-06-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3)),
                ('item_color', models.CharField(choices=[('RED', 'Red'), ('GREEN', 'Green'), ('BLUE', 'Blue'), ('YELLOW', 'Yellow'), ('BLACK', 'Black'), ('WHITE', 'White'), ('ORANGE', 'Orange'), ('PURPLE', 'Purple'), ('PINK', 'Pink'), ('BROWN', 'Brown'), ('GRAY', 'Gray'), ('SILVER', 'Silver'), ('GOLD', 'Gold'), ('CYAN', 'Cyan'), ('TURQUOISE', 'Turquoise'), ('MAGENTA', 'Magenta'), ('KHAKI', 'Khaki'), ('CRIMSON', 'Crimson'), ('CORAL', 'Coral'), ('TEAL', 'Teal'), ('NAVY', 'Navy'), ('PEACH', 'Peach'), ('LAVENDER', 'Lavender'), ('SAGE', 'Sage'), ('MINT', 'Mint'), ('CREAM', 'Cream')], max_length=10)),
                ('item_gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=10)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_image_url', models.URLField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
