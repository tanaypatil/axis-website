from django.conf.urls import url
from . import views

urlpatterns = [
    # main
    url(r'^$', views.index, name='start'),
    url(r'^index', views.index, name='index'),
    url(r'^events.html$', views.events, name='events'),
    url(r'^workshops.html$', views.workshops, name='workshops'),
    url(r'^attractions', views.attractions, name='attractions'),
    url(r'^contact.html', views.contact, name='contact'),
    url(r'^socini.html', views.socialini, name='socialini'),
    url(r'^feed', views.feed, name='feed'),
    url(r'^first', views.first, name='first'),
    url(r'^google6f282865ac0ed8e0.html$', views.google, name='google'),
    url(r'^sitemap.xml$', views.sitemap, name='sitemap'),
    url(r'^attr/amish.html$', views.amish, name='amish'),
    url(r'^attr/Inaug.html$', views.inaug, name='inaug'),
    url(r'^attr/afishal.html$', views.afishal, name='afishal'),

    # workshops
    # pages
    url(r'^workshops/android.html$', views.android, name='android'),
    url(r'^workshops/mobile.html$', views.mobile, name='mobile'),
    url(r'^workshops/selfbal.html$', views.selfbal, name='selfbal'),
    url(r'^workshops/ornitho.html$', views.ornitho, name='ornitho'),
    # regs
    url(r'^workshops/mobilereg$', views.mobilereg, name='mobilereg'),
    url(r'^workshops/androidreg$', views.androidreg, name='androidreg'),
    url(r'^workshops/selfbalreg$', views.selfbalreg, name='selfbalreg'),
    url(r'^workshops/ornithoreg$', views.ornithoreg, name='ornithoreg'),

    # social
    url(r'^socini/colors.html$', views.colors, name='colors'),
    url(r'^socini/envday.html$', views.envday, name='envday'),
    url(r'^socini/nosmoke.html$', views.nosmoke, name='envday'),
    url(r'^socini/mad.html$', views.mad, name='mad'),
    url(r'^socini/blood.html$', views.blood, name='blood'),

    # team
    url(r'^team/teamct', views.teamct, name='teamct'),
    url(r'^team/core', views.core, name='core'),
    url(r'^team/profs', views.profs, name='profs'),
    url(r'^team/pub', views.publicity, name='publicity'),
    url(r'^team/web', views.webt, name='webt'),

    # sponsors
    url(r'^sponsors', views.sponsors, name='sponsors'),

    # events

    # anr

    # pages
    url(r'^events/anr/robowars.html$', views.robowars, name='robowars'),
    url(r'^events/anr/aquahunt.html$', views.aquahunt, name='aquahunt'),
    url(r'^events/anr/autobot.html$', views.autobot, name='autobot'),
    url(r'^events/anr/mechatryst.html$', views.mechatryst, name='mechatryst'),
    url(r'^events/anr/robo-saviour.html$', views.robocup, name='robocup'),
    # regis
    url(r'^events/anr/robowarsreg$', views.robowarsreg, name='robowarsreg'),
    url(r'^events/anr/mechareg$', views.mechareg, name='mechareg'),
    url(r'^events/anr/autobotreg$', views.autobotreg, name='autobotreg'),
    url(r'^events/anr/aquahuntreg$', views.aquahuntreg, name='aquahuntreg'),
    url(r'^events/anr/manualroboreg$', views.manualroboreg, name='manualroboreg'),

    # cnd

    # pages
    url(r'^events/cnd/aquaskylark.html$', views.sky, name='sky'),
    url(r'^events/cnd/crepido.html$', views.crepido, name='crepido'),
    url(r'^events/cnd/devise.html$', views.devise, name='devise'),
    url(r'^events/cnd/paradiegma.html$', views.paradiegma, name='paradiegma'),
    url(r'^events/cnd/turboflux.html$', views.turbo, name='turbo'),
    # regis
    url(r'^events/cnd/skyreg$', views.skyreg, name='skyreg'),
    url(r'^events/cnd/crepidoreg$', views.crepidoreg, name='crepidoreg'),
    url(r'^events/cnd/parareg$', views.parareg, name='parareg'),
    url(r'^events/cnd/turboreg$', views.turboreg, name='turboreg'),
    url(r'^events/cnd/architechreg$', views.architechreg, name='architechreg'),
    url(r'^events/cnd/desigreg$', views.desigreg, name='desigreg'),
    url(r'^events/cnd/photoscreg$', views.photoscreg, name='photoscreg'),


    # sne

    # pages
    url(r'^events/sne/animazion.html$', views.anim, name='anim'),
    url(r'^events/sne/insomnia.html$', views.inso, name='indo'),
    url(r'^events/sne/cryptocrux.html$', views.crypto, name='crypto'),
    url(r'^events/sne/posterolic.html$', views.poster, name='poster'),
    # regis
    url(r'^events/sne/animreg$', views.animreg, name='animreg'),
    url(r'^events/sne/cryptoreg$', views.cryptoreg, name='cryptoreg'),
    url(r'^events/sne/posterreg$', views.posterreg, name='posterreg'),


    # se

    # pages
    url(r'^events/se/js.html$', views.js, name='js'),
    url(r'^events/se/dexter.html$', views.dexter, name='dexter'),


    # mno

    # pages
    url(r'^events/mno/wallstreet.html$', views.wall, name='wall'),
    url(r'^events/mno/whosdboss.html$', views.boss, name='boss'),
    url(r'^events/mno/221baker.html$', views.baker, name='baker'),
    url(r'^events/mno/freakomatrix.html$', views.freako, name='freako'),
    url(r'^events/mno/gamesutra.html$', views.games, name='games'),
    url(r'^events/mno/informals.html$', views.informals, name='informals'),
    # regis
    url(r'^events/mno/wallreg$', views.wallreg, name='wallreg'),
    url(r'^events/mno/bossreg$', views.bossreg, name='bossreg'),
    url(r'^events/mno/freakoreg$', views.freakoreg, name='freakoreg'),
    url(r'^events/mno/csreg$', views.csreg, name='csreg'),
    url(r'^events/mno/nfsreg$', views.nfsreg, name='nfsreg'),
    url(r'^events/mno/fifareg$', views.fifareg, name='fifareg'),
    url(r'^events/mno/bakerreg$', views.bakerreg, name='bakerreg'),


    # xxx
    # pages
    url(r'^events/xxx/coll.html$', views.coll, name='coll'),
    url(r'^events/xxx/kart.html$', views.kart, name='kart'),
    url(r'^events/xxx/technodocx.html$', views.techno, name='techno'),
    # regis
    url(r'^events/xxx/technoreg$', views.technoreg, name='technoreg'),
    url(r'^events/xxx/kartreg$', views.kartreg, name='kartreg'),
    url(r'^events/xxx/collreg$', views.collreg, name='collreg'),



    #new
    #pages
    url(r'^events/new/brain.html$', views.brain, name='brain'),
    url(r'^events/new/laser.html$', views.laser, name='laser'),
    url(r'^events/new/minute.html$', views.minute, name='minute'),
    # regis
    url(r'^events/new/minutereg$', views.minutereg, name='minutereg'),
    url(r'^events/new/brainreg$', views.brainreg, name='brainreg'),
    url(r'^events/new/laserreg$', views.laserreg, name='laserreg'),
]
