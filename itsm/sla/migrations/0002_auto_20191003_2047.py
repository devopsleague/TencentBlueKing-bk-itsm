# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-ITSM 蓝鲸流程服务 available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

BK-ITSM 蓝鲸流程服务 is licensed under the MIT License.

License for BK-ITSM 蓝鲸流程服务:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Generated by Django 1.11.24 on 2019-10-03 20:47


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sla', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={
                'ordering': ['-id'],
                'verbose_name': '\u670d\u52a1\u8fd0\u8425\u65f6\u95f4',
                'verbose_name_plural': '\u670d\u52a1\u8fd0\u8425\u65f6\u95f4',
            },
        ),
        migrations.AlterModelOptions(
            name='sla',
            options={
                'ordering': ['-id'],
                'verbose_name': '\u670d\u52a1\u534f\u8bae',
                'verbose_name_plural': '\u670d\u52a1\u534f\u8bae',
            },
        ),
        migrations.AddField(
            model_name='schedule',
            name='is_builtin',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5185\u7f6e'),
        ),
        migrations.AddField(
            model_name='sla',
            name='is_builtin',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5185\u7f6e'),
        ),
        migrations.AlterField(
            model_name='action',
            name='action_type',
            field=models.CharField(
                choices=[
                    ('alert', '\u544a\u8b66\u4e8b\u4ef6'),
                    ('update_ticket', '\u66f4\u65b0\u5355\u636e\u4fe1\u606f'),
                ],
                max_length=32,
                verbose_name='\u4e8b\u4ef6\u7c7b\u578b',
            ),
        ),
        migrations.AlterField(
            model_name='day',
            name='day_of_week',
            field=models.CharField(default=-1, max_length=32, verbose_name='\u661f\u671f\u51e0'),
        ),
        migrations.AlterField(
            model_name='prioritymatrix',
            name='priority',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u4f18\u5148\u7ea7'),
        ),
        migrations.AlterField(
            model_name='slatimerrule',
            name='condition_type',
            field=models.CharField(
                choices=[('START', '\u5f00\u59cb'), ('STOP', '\u7ed3\u675f'), ('PAUSE', '\u6682\u505c')],
                default='START',
                max_length=64,
                verbose_name='\u6761\u4ef6\u7c7b\u578b',
            ),
        ),
    ]
