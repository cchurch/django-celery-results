"""Result Task Admin interface."""
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import TaskResult


class TaskResultAdmin(admin.ModelAdmin):
    """Admin-interface for results of tasks."""

    model = TaskResult
    list_display = ('task_name', 'task_id', 'date_done', 'status')
    list_filter = ('status', 'date_done')
    readonly_fields = ('task_name', 'task_id', 'status', 'content_type',
                       'content_encoding', 'task_args', 'task_kwargs',
                       'traceback', 'date_done', 'result', 'hidden', 'meta')
    fieldsets = (
        (None, {
            'fields': (
                'task_name',
                'task_id',
                'status',
                'content_type',
                'content_encoding',
            ),
            'classes': ('extrapretty', 'wide')
        }),
        (_('Parameters'), {
            'fields': (
                'task_args',
                'task_kwargs',
            ),
            'classes': ('extrapretty', 'wide')
        }),
        (_('Result'), {
            'fields': (
                'result',
                'date_done',
                'traceback',
                'hidden',
                'meta',
            ),
            'classes': ('extrapretty', 'wide')
        }),
    )

    def has_add_permission(self, request):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.setdefault('show_save', False)
        extra_context.setdefault('show_save_and_continue', False)
        return super(TaskResultAdmin, self).change_view(request, object_id, form_url, extra_context)


admin.site.register(TaskResult, TaskResultAdmin)
