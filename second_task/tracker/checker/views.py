from django.shortcuts import render

from django.db.models import Avg
from chartit import PivotDataPool, PivotChart

from .models import FileData
from .cron import update_filedata
from connect.dropbox import make_connection


def index(request):
    return render(request, 'index.html')


def chart(request):
    if request.method == 'POST':
        update_filedata()

    file_data = PivotDataPool(
        series=[{
            'options': {
                'source': FileData.objects.all(),
                'categories': ['modification_date'],
                'legend_by': 'name',
                #'top_n_per_cat': 3,
            },
            'terms': {
                'avg_occurence': Avg('occurence'),
            }
        }]
    )

    file_data_chart = PivotChart(
        datasource=file_data,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['avg_occurence']
        }],
        chart_options={
            'title': {
                'text': 'Occurence per files'
            },
            'xAxis': {
                'title': {
                    'text': 'modification_date'
                }
            }
        }
    )

    return render(
            request,
            'chart.html',
            {'file_data_chart': file_data_chart},
        )