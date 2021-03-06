# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-23 23:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('sb_thing', models.CharField(max_length=50, null=True)),
                ('sb_story', models.CharField(max_length=150, null=True)),
                ('sb_name', models.CharField(max_length=30, null=True)),
                ('sb_gender', models.CharField(choices=[('他', '他'), ('她', '她')], max_length=100, null=True)),
                ('sb_adv', models.CharField(choices=[('有點', '有點'), ('非常', '非常'), ('蠻', '蠻'), ('超級', '超級'), ('史上無敵', '史上無敵')], max_length=100, null=True)),
                ('sb_adj', models.CharField(choices=[('humor', 'humor'), ('奇怪', '奇怪'), ('白目', '白目'), ('有病', '有病'), ('自戀', '自戀'), ('搞笑', '搞笑'), ('孤僻', '孤僻'), ('嚴肅', '嚴肅'), ('無趣', '無趣'), ('奇耙', '奇耙'), ('可怕', '可怕'), ('笨蛋', '笨蛋'), ('健忘', '健忘'), ('厲害', '厲害'), ('正常', '正常'), ('懶惰', '懶惰')], max_length=100, null=True)),
                ('sb_about', models.CharField(choices=[('很喜歡', '很喜歡'), ('不喜歡', '不喜歡'), ('不吃', '不吃'), ('討厭', '討厭'), ('怕', '怕'), ('常常', '常常'), ('很會', '很會'), ('曾經', '曾經')], max_length=100, null=True)),
                ('who', models.CharField(choices=[('我們', '我們'), ('他', '他'), ('她', '她')], max_length=100, null=True)),
                ('sth_adj', models.CharField(choices=[('扯', '扯'), ('蠢', '蠢'), ('煩', '煩'), ('北七', '北七'), ('北爛', '北爛'), ('誇張', '誇張'), ('有趣', '有趣'), ('好笑', '好笑'), ('丟臉', '丟臉'), ('瘋狂', '瘋狂'), ('誇張', '誇張'), ('無聊', '無聊'), ('幼稚', '幼稚'), ('難忘', '難忘'), ('開心', '開心')], max_length=100, null=True)),
                ('itjcts', models.CharField(choices=[('哎', '哎'), ('哈哈', '哈哈'), ('呵呵', '呵呵'), ('顆顆', '顆顆'), ('嘿丟', '嘿丟')], max_length=100, null=True)),
                ('mark', models.CharField(choices=[('~', '~'), ('!', '!'), ('!!!', '!!!'), ('XD', 'XD'), ('>///<', '>///<'), ('^^', '^^'), (':)', ':)'), ('。', '。')], max_length=100, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoryAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThingAdjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='adjective_t',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='story.ThingAdjective'),
        ),
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='storys', to='story.StoryAuthor'),
        ),
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='story.Category'),
        ),
        migrations.AddField(
            model_name='story',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='story_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
