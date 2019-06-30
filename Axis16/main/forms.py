from django import forms
from .models import RobowarsRegistration, MechaRegistration, SkyRegistration, CrepidoRegistration, ParaRegistration, \
    TurbofluxRegistration, AnimazioneRegistration, CryptocruxRegistration, PosterolicRegistration, \
    WallstreetRegistration, WhosTheBossRegistration, FreakoRegistration, CounterStrikeRegistration, NFSRegistration, \
    FifaRegistration, TechnoDocxRegistration, FeedbackMessage, AutobotRegistration, MobileRegistration, \
    AndroidRegistration, AquahuntRegistration, BakerRegistration, SelfBalRegistration, ManualroboRegistration, \
    ElectroRegistration, OrnithoRegistration, KartavyaRegistration, ArchitechRegistration, DesignoRegistration, \
    PhotoscopeRegistration, BrainRegistration, CollRegistration, LaserRegistration


class Robowars_Form(forms.ModelForm):

    class Meta:
        model = RobowarsRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity',
                  'siname', 'sicollege', 'sicon', 'simail', 'sicity']


class Mecha_Form(forms.ModelForm):

    class Meta:
        model = MechaRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity']


class Autobot_Form(forms.ModelForm):

    class Meta:
        model = AutobotRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity']


class Aquahunt_Form(forms.ModelForm):

    class Meta:
        model = AquahuntRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity']


class Sky_Form(forms.ModelForm):

    class Meta:
        model = SkyRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity']


class Crepido_Form(forms.ModelForm):

    class Meta:
        model = CrepidoRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity']


class Para_Form(forms.ModelForm):

    class Meta:
        model = ParaRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity']


class Turboflux_Form(forms.ModelForm):

    class Meta:
        model = TurbofluxRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity']


class Animazione_Form(forms.ModelForm):

    class Meta:
        model = AnimazioneRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity']


class Cryptocrux_Form(forms.ModelForm):

    class Meta:
        model = CryptocruxRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity']


class Posterolic_Form(forms.ModelForm):

    class Meta:
        model = PosterolicRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity']


class Wall_Form(forms.ModelForm):

    class Meta:
        model = WallstreetRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity']


class Boss_Form(forms.ModelForm):

    class Meta:
        model = WhosTheBossRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity']


class Freako_Form(forms.ModelForm):

    class Meta:
        model = FreakoRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity']


class Counter_Form(forms.ModelForm):

    class Meta:
        model = CounterStrikeRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity']


class NFS_Form(forms.ModelForm):

    class Meta:
        model = NFSRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity']


class Fifa_Form(forms.ModelForm):

    class Meta:
        model = FifaRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity']


class Techno_Form(forms.ModelForm):

    class Meta:
        model = TechnoDocxRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity']


class Mobile_Form(forms.ModelForm):

    class Meta:
        model = MobileRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity']


class SelfBal_Form(forms.ModelForm):

    class Meta:
        model = SelfBalRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity']


class Ornitho_Form(forms.ModelForm):

    class Meta:
        model = OrnithoRegistration
        fields = [
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity']


class Manualrobo_Form(forms.ModelForm):

    class Meta:
        model = ManualroboRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity']


class Electro_Form(forms.ModelForm):

    class Meta:
        model = ElectroRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity']


class Android_Form(forms.ModelForm):

    class Meta:
        model = AndroidRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity']


class Baker_Form(forms.ModelForm):

    class Meta:
        model = BakerRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity']


class Kartavya_Form(forms.ModelForm):

    class Meta:
        model = KartavyaRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity']


class Architech_Form(forms.ModelForm):

    class Meta:
        model = ArchitechRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity']


class Designo_Form(forms.ModelForm):

    class Meta:
        model = DesignoRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity']


class Photoscope_Form(forms.ModelForm):

    class Meta:
        model = PhotoscopeRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity']


class Brain_Form(forms.ModelForm):

    class Meta:
        model = BrainRegistration
        fields = ['fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity']


class Coll_Form(forms.ModelForm):

    class Meta:
        model = CollRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity',
                  'siname', 'sicollege', 'sicon', 'simail', 'sicity']


class Laser_Form(forms.ModelForm):

    class Meta:
        model = LaserRegistration
        fields = ['team',
                  'fname', 'fcollege', 'fcon', 'fmail', 'fcity',
                  'sname', 'scollege', 'scon', 'smail', 'scity',
                  'tname', 'tcollege', 'tcon', 'tmail', 'tcity',
                  'foname', 'focollege', 'focon', 'fomail', 'focity',
                  'finame', 'ficollege', 'ficon', 'fimail', 'ficity']


class FeedForm(forms.ModelForm):

    class Meta:
        model = FeedbackMessage
        fields = ['name', 'mail', 'con', 'msg']
