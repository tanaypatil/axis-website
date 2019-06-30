from django.contrib import admin
from .models import RobowarsRegistration, MechaRegistration, SkyRegistration, CrepidoRegistration, ParaRegistration, \
    TurbofluxRegistration, AnimazioneRegistration, CryptocruxRegistration, PosterolicRegistration, \
    WallstreetRegistration, WhosTheBossRegistration, FreakoRegistration, CounterStrikeRegistration, NFSRegistration, \
    FifaRegistration, TechnoDocxRegistration, FeedbackMessage, AutobotRegistration, MobileRegistration, \
    AndroidRegistration, AquahuntRegistration, BakerRegistration, SelfBalRegistration, ElectroRegistration, \
    ManualroboRegistration, OrnithoRegistration, KartavyaRegistration, ArchitechRegistration, DesignoRegistration, \
    PhotoscopeRegistration, BrainRegistration, CollRegistration, LaserRegistration


class RobowarsAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = RobowarsRegistration


class MechaAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = MechaRegistration


class AutobotAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = AutobotRegistration


class SkyAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = SkyRegistration


class AquahuntAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = AquahuntRegistration


class CrepidoAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = CrepidoRegistration


class ParaAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = ParaRegistration


class TurboAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = TurbofluxRegistration


class AnimAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = AnimazioneRegistration


class CryptoAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = CryptocruxRegistration


class Poster_Admin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = PosterolicRegistration


class Wall_Admin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = WallstreetRegistration


class Boss_Admin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = WhosTheBossRegistration


class Freako_Admin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = FreakoRegistration


class Counter_Admin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = CounterStrikeRegistration


class NFS_Admin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = NFSRegistration


class Fifa_Admin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = FifaRegistration


class Techno_Admin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = TechnoDocxRegistration


class MobileAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = MobileRegistration


class SelfBalAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['team', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = SelfBalRegistration


class AndroidAdmin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'fcon', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = AndroidRegistration


class OrnithoAdmin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'fcon', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = OrnithoRegistration


class BakerAdmin(admin.ModelAdmin):
    list_display = ['fname', 'level', 'fcollege', 'idnum', 'lastSubmit', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['level', 'fcollege', 'date_created']
    readonly_fields = ['date_created', 'lastSubmit']
    ordering = ['-level', 'lastSubmit']

    class Meta:
        model = BakerRegistration


class ElectroAdmin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = ElectroRegistration


class ManroAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = ManualroboRegistration


class CollAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = CollRegistration


class LaserAdmin(admin.ModelAdmin):
    list_display = ['team', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = LaserRegistration


class KartAdmin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = KartavyaRegistration


class ArchtAdmin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = ArchitechRegistration


class DesigAdmin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = DesignoRegistration


class PhotoscAdmin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = PhotoscopeRegistration


class BrainAdmin(admin.ModelAdmin):
    list_display = ['fname', 'idnum', 'date_created']
    search_fields = ['fname', 'idnum']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = BrainRegistration


class Feed_Admin(admin.ModelAdmin):
    list_display = ['name', 'mail', 'date_created']
    search_fields = ['name']
    list_filter = ['date_created']
    readonly_fields = ['date_created']

    class Meta:
        model = FeedbackMessage

admin.site.register(RobowarsRegistration, RobowarsAdmin)
admin.site.register(MechaRegistration, MechaAdmin)
admin.site.register(AutobotRegistration, AutobotAdmin)
admin.site.register(AquahuntRegistration, AquahuntAdmin)
admin.site.register(SkyRegistration, SkyAdmin)
admin.site.register(CrepidoRegistration, CrepidoAdmin)
admin.site.register(ParaRegistration, ParaAdmin)
admin.site.register(TurbofluxRegistration, TurboAdmin)
admin.site.register(AnimazioneRegistration, AnimAdmin)
admin.site.register(CryptocruxRegistration, CryptoAdmin)
admin.site.register(PosterolicRegistration, Poster_Admin)
admin.site.register(WallstreetRegistration, Wall_Admin)
admin.site.register(WhosTheBossRegistration, Boss_Admin)
admin.site.register(FreakoRegistration, Freako_Admin)
admin.site.register(CounterStrikeRegistration, Counter_Admin)
admin.site.register(NFSRegistration, NFS_Admin)
admin.site.register(FifaRegistration, Fifa_Admin)
admin.site.register(TechnoDocxRegistration, Techno_Admin)
admin.site.register(MobileRegistration, MobileAdmin)
admin.site.register(SelfBalRegistration, SelfBalAdmin)
admin.site.register(AndroidRegistration, AndroidAdmin)
admin.site.register(OrnithoRegistration, OrnithoAdmin)
admin.site.register(BakerRegistration, BakerAdmin)
admin.site.register(ElectroRegistration, ElectroAdmin)
admin.site.register(KartavyaRegistration, KartAdmin)
admin.site.register(ArchitechRegistration, ArchtAdmin)
admin.site.register(DesignoRegistration, DesigAdmin)
admin.site.register(PhotoscopeRegistration, PhotoscAdmin)
admin.site.register(ManualroboRegistration, ManroAdmin)
admin.site.register(BrainRegistration, BrainAdmin)
admin.site.register(CollRegistration, CollAdmin)
admin.site.register(LaserRegistration, LaserAdmin)
admin.site.register(FeedbackMessage, Feed_Admin)
