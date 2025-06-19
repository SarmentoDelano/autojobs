from django.contrib import admin
from .models import Vaga
from django.utils.html import format_html

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'fonte', 'salario', 'visualizar_link')
    list_filter = ('encontrado_em',)
    search_fields = ('cargo', 'empresa', 'descricao', 'tags')
    readonly_fields = ('empresa', 'cargo', 'descricao', 'salario', 'tags', 'link', 'encontrado_em')
    list_per_page = 25

    def visualizar_link(self, obj):
        if obj.link:
            return format_html(f"<a href='{obj.link}' target='_blank'>🔗 Acessar vaga</a>")
        return "-"
    visualizar_link.short_description = 'Link'

    def fonte(self, obj):
        emoji = {
            "InfoJobs": "💼",
            "RemoteOK": "🌐",
            "Programathor": "👨‍💻",
            "Remotar": "🚀",
            "Vagas.com": "🏢",
            "Gupy": "🧠",
        }.get(obj.encontrado_em, "📝")
        return f"{emoji} {obj.encontrado_em}"
    fonte.short_description = "Fonte"

    fieldsets = (
        (None, {
            'fields': ('empresa', 'cargo', 'descricao')
        }),
        ('Outros detalhes', {
            'fields': ('salario', 'tags', 'link', 'encontrado_em'),
            'classes': ('collapse',),
        }),
    )
