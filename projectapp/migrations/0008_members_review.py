# Generated by Django 3.1 on 2020-09-01 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0007_auto_20200824_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20, verbose_name='회원 아이디')),
                ('password', models.CharField(max_length=20, verbose_name='비밀 번호')),
                ('username', models.CharField(max_length=12, verbose_name='회원 이름')),
                ('class_type', models.IntegerField(verbose_name='반 유형 - 1:빅데이터, 2:AI, 3:Cloud, 4:IoT')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('state', models.IntegerField(verbose_name='회원 상태 - 0:회원, 1:탈퇴')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_star', models.IntegerField(verbose_name='리뷰 별점')),
                ('rev_content', models.TextField(verbose_name='리뷰 내용')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('deleted', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('res_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.resinfo', verbose_name='가게id')),
                ('rev_writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectapp.members', verbose_name='작성자')),
            ],
        ),
    ]
