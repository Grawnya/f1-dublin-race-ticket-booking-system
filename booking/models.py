from django.db import models
from django.core.validators import MaxValueValidator

team_choices = (
    (1, 'Red Bull'),
    (2, 'Ferrari'),
    (3, 'Mercedes'),
    (4, 'Alpine'),
    (5, 'McLaren'),
    (6, 'Alfa Romeo'),
    (7, 'Aston Martin'),
    (8, 'Haas'),
    (9, 'AlphaTauri'),
    (10, 'Williams'),
    )

country_choices = (
    ('Aruba', 'abw'),
    ('Afghanistan', 'afg'),
    ('Angola', 'ago'),
    ('Anguilla', 'aia'),
    ('Åland Islands', 'ala'),
    ('Albania', 'alb'),
    ('Andorra', 'and'),
    ('United Arab Emirates', 'are'),
    ('Argentina', 'arg'),
    ('Armenia', 'arm'),
    ('American Samoa', 'asm'),
    ('Antarctica', 'ata'),
    ('French Southern Territories', 'atf'),
    ('Antigua and Barbuda', 'atg'),
    ('Australia', 'aus'),
    ('Austria', 'aut'),
    ('Azerbaijan', 'aze'),
    ('Burundi', 'bdi'),
    ('Belgium', 'bel'),
    ('Benin', 'ben'),
    ('Bonaire, Sint Eustatius and Saba', 'bes'),
    ('Burkina Faso', 'bfa'),
    ('Bangladesh', 'bgd'),
    ('Bulgaria', 'bgr'),
    ('Bahrain', 'bhr'),
    ('Bahamas', 'bhs'),
    ('Bosnia and Herzegovina', 'bih'),
    ('Saint Barthélemy', 'blm'),
    ('Belarus', 'blr'),
    ('Belize', 'blz'),
    ('Bermuda', 'bmu'),
    ('Bolivia', 'bol'),
    ('Brasil', 'bra'),
    ('Barbados', 'brb'),
    ('Brunei Darussalam', 'brn'),
    ('Bhutan', 'btn'),
    ('Bouvet Island', 'bvt'),
    ('Botswana', 'bwa'),
    ('Central African Republic', 'caf'),
    ('Canada', 'can'),
    ('Catalonia (autonomous community in Spain)', 'cat'),
    ('Cocos (Keeling) Islands', 'cck'),
    ('Switzerland', 'che'),
    ('Chile', 'chl'),
    ('China (People\'s Republic of China)', 'chn'),
    ('Côte d\'Ivoire', 'civ'),
    ('Cameroon', 'cmr'),
    ('Congo (Democratic Republic of the Congo)', 'cod'),
    ('Congo (Congo-Brazzaville)', 'cog'),
    ('Cook Islands', 'cok'),
    ('Colombia', 'col'),
    ('Comoros', 'com'),
    ('Cabo Verde', 'cpv'),
    ('Costa Rica', 'cri'),
    ('Cuba', 'cub'),
    ('Curaçao', 'cuw'),
    ('Christmas Island', 'cxr'),
    ('Cayman Islands', 'cym'),
    ('Cyprus', 'cyp'),
    ('Czech Republic', 'cze'),
    ('Germany', 'deu'),
    ('Djibouti', 'dji'),
    ('Dominica', 'dma'),
    ('Denmark', 'dnk'),
    ('Dominican Republic', 'dom'),
    ('Algeria', 'dza'),
    ('Ecuador', 'ecu'),
    ('Egypt', 'egy'),
    ('England', 'eng'),
    ('Eritrea', 'eri'),
    ('Western Sahara', 'esh'),
    ('Spain', 'esp'),
    ('Estonia', 'est'),
    ('Ethiopia', 'eth'),
    ('European Union', 'eun'),
    ('Finland', 'fin'),
    ('Fiji', 'fji'),
    ('Falkland Islands (Malvinas)', 'flk'),
    ('France', 'fra'),
    ('Faroe Islands', 'fro'),
    ('Micronesia', 'fsm'),
    ('Gabon', 'gab'),
    ('United Kingdom', 'gbr'),
    ('Georgia', 'geo'),
    ('Guernsey', 'ggy'),
    ('Ghana', 'gha'),
    ('Gibraltar', 'gib'),
    ('Guinea', 'gin'),
    ('Guadeloupe', 'glp'),
    ('Gambia', 'gmb'),
    ('Guinea-Bissau', 'gnb'),
    ('Equatorial Guinea', 'gnq'),
    ('Greece', 'grc'),
    ('Grenada', 'grd'),
    ('Greenland', 'grl'),
    ('Guatemala', 'gtm'),
    ('French Guiana', 'guf'),
    ('Guam', 'gum'),
    ('Guyana', 'guy'),
    ('Hong Kong (Special Administrative Region of the China)', 'hkg'),
    ('Heard Island and McDonald Islands', 'hmd'),
    ('Honduras', 'hnd'),
    ('Croatia', 'hrv'),
    ('Haiti', 'hti'),
    ('Hungary', 'hun'),
    ('Indonesia', 'idn'),
    ('Isle of Man', 'imn'),
    ('India', 'ind'),
    ('British Indian Ocean Territory', 'iot'),
    ('Ireland', 'irl'),
    ('Iran', 'irn'),
    ('Iraq', 'irq'),
    ('Iceland', 'isl'),
    ('Israel', 'isr'),
    ('Italy', 'ita'),
    ('Jamaica', 'jam'),
    ('Jersey', 'jey'),
    ('Jordan', 'jor'),
    ('Japan', 'jpn'),
    ('Kazakstan', 'kaz'),
    ('Kenya', 'ken'),
    ('Kyrgyzstan', 'kgz'),
    ('Cambodia', 'khm'),
    ('Kiribati', 'kir'),
    ('Saint Kitts and Nevis', 'kna'),
    ('Korea (Republic of Korea)', 'kor'),
    ('Kosovo (partially recognised state of Serbia)', 'kos'),
    ('Kuwait', 'kwt'),
    ('Lao People\'s Democratic Republic', 'lao'),
    ('Lebanon', 'lbn'),
    ('Liberia', 'lbr'),
    ('Libya', 'lby'),
    ('Saint Lucia', 'lca'),
    ('Liechtenstein', 'lie'),
    ('Sri Lanka', 'lka'),
    ('Lesotho', 'lso'),
    ('Lithuania', 'ltu'),
    ('Luxembourg', 'lux'),
    ('Latvia', 'lva'),
    ('Macau (Macao Special Administrative Region of China)', 'mac'),
    ('Saint Martin (French part)', 'maf'),
    ('Marokko', 'mar'),
    ('Monaco', 'mco'),
    ('Moldova', 'mda'),
    ('Madagascar', 'mdg'),
    ('Maldives', 'mdv'),
    ('Mexico', 'mex'),
    ('Marshall Islands', 'mhl'),
    ('Makedonia', 'mkd'),
    ('Mali', 'mli'),
    ('Malta', 'mlt'),
    ('Myanmar', 'mmr'),
    ('Montenegro', 'mne'),
    ('Mongolia', 'mng'),
    ('Northern Mariana Islands', 'mnp'),
    ('Mozambique', 'moz'),
    ('auritania', 'mrt'),
    ('Montserrat', 'msr'),
    ('Martinique', 'mtq'),
    ('Mauritius', 'mus'),
    ('Malawi', 'mwi'),
    ('Malaysia', 'mys'),
    ('Mayotte', 'myt'),
    ('Namibia', 'nam'),
    ('New Caledonia', 'ncl'),
    ('Niger', 'ner'),
    ('Norfolk Island', 'nfk'),
    ('Nigeria', 'nga'),
    ('Nicaragua', 'nic'),
    ('Northern Ireland', 'nir'),
    ('Niue', 'niu'),
    ('Netherlands', 'nld'),
    ('Norway', 'nor'),
    ('Nepal', 'npl'),
    ('Nauru', 'nru'),
    ('New Zealand', 'nzl'),
    ('Oman', 'omn'),
    ('Pakistan', 'pak'),
    ('Panama', 'pan'),
    ('Pitcairn', 'pcn'),
    ('Peru', 'per'),
    ('Phillipines', 'phl'),
    ('Palau', 'plw'),
    ('Papua New Guinea', 'png'),
    ('Poland', 'pol'),
    ('Puerto Rico', 'pri'),
    ('Korea (Democratic People\'s Republic of Korea)', 'prk'),
    ('Portugal', 'prt'),
    ('Paraguay', 'pry'),
    ('State of Palestine', 'pse'),
    ('French Polynesia', 'pyf'),
    ('Qatar', 'qat'),
    ('Réunion', 'reu'),
    ('Roumania', 'rou'),
    ('Russia', 'rus'),
    ('Rwanda', 'rwa'),
    ('Saudi Arabia', 'sau'),
    ('Scotland', 'sco'),
    ('Sudan', 'sdn'),
    ('Senegal', 'sen'),
    ('Singapore', 'sgp'),
    ('South Georgia and the South Sandwich Islands', 'sgs'),
    ('Saint Helena, Ascension and Tristan da Cunha', 'shn'),
    ('Svalbard and Jan Mayen', 'sjm'),
    ('Solomon Islands', 'slb'),
    ('Sierra Leone', 'sle'),
    ('El Salvador', 'slv'),
    ('San Marino', 'smr'),
    ('Somalia', 'som'),
    ('Saint Pierre and Miquelon', 'spm'),
    ('Serbia', 'srb'),
    ('South Sudan', 'ssd'),
    ('Sao Tome and Principe', 'stp'),
    ('Union of Soviet Socialist Republics (USSR)', 'sun'),
    ('Suriname', 'sur'),
    ('Slovakia', 'svk'),
    ('Slovenia', 'svn'),
    ('Sweden', 'swe'),
    ('Swaziland', 'swz'),
    ('Sint Maarten (Dutch part)', 'sxm'),
    ('Seychelles', 'syc'),
    ('Syrian Arab Republic', 'syr'),
    ('Turks and Caicos Islands', 'tca'),
    ('Chad', 'tcd'),
    ('Togo', 'tgo'),
    ('Thailand', 'tha'),
    ('Tajikistan', 'tjk'),
    ('Tokelau', 'tkl'),
    ('Turkmenistan', 'tkm'),
    ('Timor-Leste', 'tls'),
    ('Tonga', 'ton'),
    ('Trinidad and Tobago', 'tto'),
    ('Tunisia', 'tun'),
    ('Turkey', 'tur'),
    ('Tuvalu', 'tuv'),
    ('Taiwan', 'twn'),
    ('United Republic of Tanzania', 'tza'),
    ('Uganda', 'uga'),
    ('Ukraine', 'ukr'),
    ('United States Minor Outlying Islands', 'umi'),
    ('Uruguay', 'ury'),
    ('United States of America', 'usa'),
    ('Uzbekistan', 'uzb'),
    ('Vanuatu', 'vat'),
    ('Vatican', 'vct'),
    ('Venezuela', 'ven'),
    ('Virgin Islands (British)', 'vgb'),
    ('Virgin Islands (U.S.)', 'vir'),
    ('Vietnam', 'vnm'),
    ('Vanuatu', 'vut'),
    ('Wales', 'wal'),
    ('Wallis and Futuna', 'wlf'),
    ('Samoa', 'wsm'),
    ('Yemen', 'yem'),
    ('South Africa', 'zaf'),
    ('Zambia', 'zmb'),
    ('Zimbabwe', 'zwe')
)

# Create your models here.
class WebsiteUser(models.Model):
    '''WebsiteUser Information Model'''
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, default="")
    fave_team = models.IntegerField(choices=team_choices, default=1)
    nationality = models.CharField(max_length=250, choices=country_choices, default='Ireland')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Seat(models.Model):
    '''Seats Booked Model'''
    seat_number = models.IntegerField()
    row = models.IntegerField()
    stand = models.CharField(max_length=1)

    class Meta:
        ordering = ['stand', 'row', 'seat_number']
        unique_together = ['stand', 'row', 'seat_number']

    def __str__(self):
        return f'Ticket: {self.stand} {self.row} {self.seat_number}'


class Ticket(models.Model):
    '''Tickets Booked Model'''
    booked_by = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    booked_on = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=50)
    fave_team = models.IntegerField(choices=team_choices, default=1)
    nationality = models.CharField(max_length=250, choices=country_choices, default='Ireland')
    seat_number = models.IntegerField()
    row = models.IntegerField()
    stand = models.CharField(max_length=1)
    show = models.BooleanField(default=True)

    def __str__(self):
        return f'Ticket for {self.nickname} booked by {self.booked_by}'

