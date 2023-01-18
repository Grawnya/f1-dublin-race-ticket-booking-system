# Generated by Django 3.2.16 on 2023-01-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='fave_team',
            field=models.IntegerField(choices=[('red_bull', 'Red Bull'), ('ferrari', 'Ferrari'), ('mercedes', 'Mercedes'), ('alpine', 'Alpine'), ('mclaren', 'McLaren'), ('alfa_romeo', 'Alfa Romeo'), ('aston_martin', 'Aston Martin'), ('haas', 'Haas'), ('alphatauri', 'AlphaTauri'), ('williams', 'Williams')], default=1),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='nationality',
            field=models.CharField(choices=[('abw', 'Aruba'), ('afg', 'Afghanistan'), ('ago', 'Angola'), ('aia', 'Anguilla'), ('ala', 'Åland Islands'), ('alb', 'Albania'), ('and', 'Andorra'), ('are', 'United Arab Emirates'), ('arg', 'Argentina'), ('arm', 'Armenia'), ('asm', 'American Samoa'), ('ata', 'Antarctica'), ('atf', 'French Southern Territories'), ('atg', 'Antigua and Barbuda'), ('aus', 'Australia'), ('aut', 'Austria'), ('aze', 'Azerbaijan'), ('bdi', 'Burundi'), ('bel', 'Belgium'), ('ben', 'Benin'), ('bes', 'Bonaire, Sint Eustatius and Saba'), ('bfa', 'Burkina Faso'), ('bgd', 'Bangladesh'), ('bgr', 'Bulgaria'), ('bhr', 'Bahrain'), ('bhs', 'Bahamas'), ('bih', 'Bosnia and Herzegovina'), ('blm', 'Saint Barthélemy'), ('blr', 'Belarus'), ('blz', 'Belize'), ('bmu', 'Bermuda'), ('bol', 'Bolivia'), ('bra', 'Brasil'), ('brb', 'Barbados'), ('brn', 'Brunei Darussalam'), ('btn', 'Bhutan'), ('bvt', 'Bouvet Island'), ('bwa', 'Botswana'), ('caf', 'Central African Republic'), ('can', 'Canada'), ('cat', 'Catalonia (autonomous community in Spain)'), ('cck', 'Cocos (Keeling) Islands'), ('che', 'Switzerland'), ('chl', 'Chile'), ('chn', "China (People's Republic of China)"), ('civ', "Côte d'Ivoire"), ('cmr', 'Cameroon'), ('cod', 'Congo (Democratic Republic of the Congo)'), ('cog', 'Congo (Congo-Brazzaville)'), ('cok', 'Cook Islands'), ('col', 'Colombia'), ('com', 'Comoros'), ('cpv', 'Cabo Verde'), ('cri', 'Costa Rica'), ('cub', 'Cuba'), ('cuw', 'Curaçao'), ('cxr', 'Christmas Island'), ('cym', 'Cayman Islands'), ('cyp', 'Cyprus'), ('cze', 'Czech Republic'), ('deu', 'Germany'), ('dji', 'Djibouti'), ('dma', 'Dominica'), ('dnk', 'Denmark'), ('dom', 'Dominican Republic'), ('dza', 'Algeria'), ('ecu', 'Ecuador'), ('egy', 'Egypt'), ('eng', 'England'), ('eri', 'Eritrea'), ('esh', 'Western Sahara'), ('esp', 'Spain'), ('est', 'Estonia'), ('eth', 'Ethiopia'), ('eun', 'European Union'), ('fin', 'Finland'), ('fji', 'Fiji'), ('flk', 'Falkland Islands (Malvinas)'), ('fra', 'France'), ('fro', 'Faroe Islands'), ('fsm', 'Micronesia'), ('gab', 'Gabon'), ('gbr', 'United Kingdom'), ('geo', 'Georgia'), ('ggy', 'Guernsey'), ('gha', 'Ghana'), ('gib', 'Gibraltar'), ('gin', 'Guinea'), ('glp', 'Guadeloupe'), ('gmb', 'Gambia'), ('gnb', 'Guinea-Bissau'), ('gnq', 'Equatorial Guinea'), ('grc', 'Greece'), ('grd', 'Grenada'), ('grl', 'Greenland'), ('gtm', 'Guatemala'), ('guf', 'French Guiana'), ('gum', 'Guam'), ('guy', 'Guyana'), ('hkg', 'Hong Kong (Special Administrative Region of the China)'), ('hmd', 'Heard Island and McDonald Islands'), ('hnd', 'Honduras'), ('hrv', 'Croatia'), ('hti', 'Haiti'), ('hun', 'Hungary'), ('idn', 'Indonesia'), ('imn', 'Isle of Man'), ('ind', 'India'), ('iot', 'British Indian Ocean Territory'), ('irl', 'Ireland'), ('irn', 'Iran'), ('irq', 'Iraq'), ('isl', 'Iceland'), ('isr', 'Israel'), ('ita', 'Italy'), ('jam', 'Jamaica'), ('jey', 'Jersey'), ('jor', 'Jordan'), ('jpn', 'Japan'), ('kaz', 'Kazakstan'), ('ken', 'Kenya'), ('kgz', 'Kyrgyzstan'), ('khm', 'Cambodia'), ('kir', 'Kiribati'), ('kna', 'Saint Kitts and Nevis'), ('kor', 'Korea (Republic of Korea)'), ('kos', 'Kosovo (partially recognised state of Serbia)'), ('kwt', 'Kuwait'), ('lao', "Lao People's Democratic Republic"), ('lbn', 'Lebanon'), ('lbr', 'Liberia'), ('lby', 'Libya'), ('lca', 'Saint Lucia'), ('lie', 'Liechtenstein'), ('lka', 'Sri Lanka'), ('lso', 'Lesotho'), ('ltu', 'Lithuania'), ('lux', 'Luxembourg'), ('lva', 'Latvia'), ('mac', 'Macau (Macao Special Administrative Region of China)'), ('maf', 'Saint Martin (French part)'), ('mar', 'Marokko'), ('mco', 'Monaco'), ('mda', 'Moldova'), ('mdg', 'Madagascar'), ('mdv', 'Maldives'), ('mex', 'Mexico'), ('mhl', 'Marshall Islands'), ('mkd', 'Makedonia'), ('mli', 'Mali'), ('mlt', 'Malta'), ('mmr', 'Myanmar'), ('mne', 'Montenegro'), ('mng', 'Mongolia'), ('mnp', 'Northern Mariana Islands'), ('moz', 'Mozambique'), ('mrt', 'auritania'), ('msr', 'Montserrat'), ('mtq', 'Martinique'), ('mus', 'Mauritius'), ('mwi', 'Malawi'), ('mys', 'Malaysia'), ('myt', 'Mayotte'), ('nam', 'Namibia'), ('ncl', 'New Caledonia'), ('ner', 'Niger'), ('nfk', 'Norfolk Island'), ('nga', 'Nigeria'), ('nic', 'Nicaragua'), ('nir', 'Northern Ireland'), ('niu', 'Niue'), ('nld', 'Netherlands'), ('nor', 'Norway'), ('npl', 'Nepal'), ('nru', 'Nauru'), ('nzl', 'New Zealand'), ('omn', 'Oman'), ('pak', 'Pakistan'), ('pan', 'Panama'), ('pcn', 'Pitcairn'), ('per', 'Peru'), ('phl', 'Phillipines'), ('plw', 'Palau'), ('png', 'Papua New Guinea'), ('pol', 'Poland'), ('pri', 'Puerto Rico'), ('prk', "Korea (Democratic People's Republic of Korea)"), ('prt', 'Portugal'), ('pry', 'Paraguay'), ('pse', 'State of Palestine'), ('pyf', 'French Polynesia'), ('qat', 'Qatar'), ('reu', 'Réunion'), ('rou', 'Roumania'), ('rus', 'Russia'), ('rwa', 'Rwanda'), ('sau', 'Saudi Arabia'), ('sco', 'Scotland'), ('sdn', 'Sudan'), ('sen', 'Senegal'), ('sgp', 'Singapore'), ('sgs', 'South Georgia and the South Sandwich Islands'), ('shn', 'Saint Helena, Ascension and Tristan da Cunha'), ('sjm', 'Svalbard and Jan Mayen'), ('slb', 'Solomon Islands'), ('sle', 'Sierra Leone'), ('slv', 'El Salvador'), ('smr', 'San Marino'), ('som', 'Somalia'), ('spm', 'Saint Pierre and Miquelon'), ('srb', 'Serbia'), ('ssd', 'South Sudan'), ('stp', 'Sao Tome and Principe'), ('sun', 'Union of Soviet Socialist Republics (USSR)'), ('sur', 'Suriname'), ('svk', 'Slovakia'), ('svn', 'Slovenia'), ('swe', 'Sweden'), ('swz', 'Swaziland'), ('sxm', 'Sint Maarten (Dutch part)'), ('syc', 'Seychelles'), ('syr', 'Syrian Arab Republic'), ('tca', 'Turks and Caicos Islands'), ('tcd', 'Chad'), ('tgo', 'Togo'), ('tha', 'Thailand'), ('tjk', 'Tajikistan'), ('tkl', 'Tokelau'), ('tkm', 'Turkmenistan'), ('tls', 'Timor-Leste'), ('ton', 'Tonga'), ('tto', 'Trinidad and Tobago'), ('tun', 'Tunisia'), ('tur', 'Turkey'), ('tuv', 'Tuvalu'), ('twn', 'Taiwan'), ('tza', 'United Republic of Tanzania'), ('uga', 'Uganda'), ('ukr', 'Ukraine'), ('umi', 'United States Minor Outlying Islands'), ('ury', 'Uruguay'), ('usa', 'United States of America'), ('uzb', 'Uzbekistan'), ('vat', 'Vanuatu'), ('vct', 'Vatican'), ('ven', 'Venezuela'), ('vgb', 'Virgin Islands (British)'), ('vir', 'Virgin Islands (U.S.)'), ('vnm', 'Vietnam'), ('vut', 'Vanuatu'), ('wal', 'Wales'), ('wlf', 'Wallis and Futuna'), ('wsm', 'Samoa'), ('yem', 'Yemen'), ('zaf', 'South Africa'), ('zmb', 'Zambia'), ('zwe', 'Zimbabwe')], default='Ireland', max_length=250),
        ),
        migrations.AlterField(
            model_name='websiteuser',
            name='fave_team',
            field=models.IntegerField(choices=[('red_bull', 'Red Bull'), ('ferrari', 'Ferrari'), ('mercedes', 'Mercedes'), ('alpine', 'Alpine'), ('mclaren', 'McLaren'), ('alfa_romeo', 'Alfa Romeo'), ('aston_martin', 'Aston Martin'), ('haas', 'Haas'), ('alphatauri', 'AlphaTauri'), ('williams', 'Williams')], default=1),
        ),
        migrations.AlterField(
            model_name='websiteuser',
            name='nationality',
            field=models.CharField(choices=[('abw', 'Aruba'), ('afg', 'Afghanistan'), ('ago', 'Angola'), ('aia', 'Anguilla'), ('ala', 'Åland Islands'), ('alb', 'Albania'), ('and', 'Andorra'), ('are', 'United Arab Emirates'), ('arg', 'Argentina'), ('arm', 'Armenia'), ('asm', 'American Samoa'), ('ata', 'Antarctica'), ('atf', 'French Southern Territories'), ('atg', 'Antigua and Barbuda'), ('aus', 'Australia'), ('aut', 'Austria'), ('aze', 'Azerbaijan'), ('bdi', 'Burundi'), ('bel', 'Belgium'), ('ben', 'Benin'), ('bes', 'Bonaire, Sint Eustatius and Saba'), ('bfa', 'Burkina Faso'), ('bgd', 'Bangladesh'), ('bgr', 'Bulgaria'), ('bhr', 'Bahrain'), ('bhs', 'Bahamas'), ('bih', 'Bosnia and Herzegovina'), ('blm', 'Saint Barthélemy'), ('blr', 'Belarus'), ('blz', 'Belize'), ('bmu', 'Bermuda'), ('bol', 'Bolivia'), ('bra', 'Brasil'), ('brb', 'Barbados'), ('brn', 'Brunei Darussalam'), ('btn', 'Bhutan'), ('bvt', 'Bouvet Island'), ('bwa', 'Botswana'), ('caf', 'Central African Republic'), ('can', 'Canada'), ('cat', 'Catalonia (autonomous community in Spain)'), ('cck', 'Cocos (Keeling) Islands'), ('che', 'Switzerland'), ('chl', 'Chile'), ('chn', "China (People's Republic of China)"), ('civ', "Côte d'Ivoire"), ('cmr', 'Cameroon'), ('cod', 'Congo (Democratic Republic of the Congo)'), ('cog', 'Congo (Congo-Brazzaville)'), ('cok', 'Cook Islands'), ('col', 'Colombia'), ('com', 'Comoros'), ('cpv', 'Cabo Verde'), ('cri', 'Costa Rica'), ('cub', 'Cuba'), ('cuw', 'Curaçao'), ('cxr', 'Christmas Island'), ('cym', 'Cayman Islands'), ('cyp', 'Cyprus'), ('cze', 'Czech Republic'), ('deu', 'Germany'), ('dji', 'Djibouti'), ('dma', 'Dominica'), ('dnk', 'Denmark'), ('dom', 'Dominican Republic'), ('dza', 'Algeria'), ('ecu', 'Ecuador'), ('egy', 'Egypt'), ('eng', 'England'), ('eri', 'Eritrea'), ('esh', 'Western Sahara'), ('esp', 'Spain'), ('est', 'Estonia'), ('eth', 'Ethiopia'), ('eun', 'European Union'), ('fin', 'Finland'), ('fji', 'Fiji'), ('flk', 'Falkland Islands (Malvinas)'), ('fra', 'France'), ('fro', 'Faroe Islands'), ('fsm', 'Micronesia'), ('gab', 'Gabon'), ('gbr', 'United Kingdom'), ('geo', 'Georgia'), ('ggy', 'Guernsey'), ('gha', 'Ghana'), ('gib', 'Gibraltar'), ('gin', 'Guinea'), ('glp', 'Guadeloupe'), ('gmb', 'Gambia'), ('gnb', 'Guinea-Bissau'), ('gnq', 'Equatorial Guinea'), ('grc', 'Greece'), ('grd', 'Grenada'), ('grl', 'Greenland'), ('gtm', 'Guatemala'), ('guf', 'French Guiana'), ('gum', 'Guam'), ('guy', 'Guyana'), ('hkg', 'Hong Kong (Special Administrative Region of the China)'), ('hmd', 'Heard Island and McDonald Islands'), ('hnd', 'Honduras'), ('hrv', 'Croatia'), ('hti', 'Haiti'), ('hun', 'Hungary'), ('idn', 'Indonesia'), ('imn', 'Isle of Man'), ('ind', 'India'), ('iot', 'British Indian Ocean Territory'), ('irl', 'Ireland'), ('irn', 'Iran'), ('irq', 'Iraq'), ('isl', 'Iceland'), ('isr', 'Israel'), ('ita', 'Italy'), ('jam', 'Jamaica'), ('jey', 'Jersey'), ('jor', 'Jordan'), ('jpn', 'Japan'), ('kaz', 'Kazakstan'), ('ken', 'Kenya'), ('kgz', 'Kyrgyzstan'), ('khm', 'Cambodia'), ('kir', 'Kiribati'), ('kna', 'Saint Kitts and Nevis'), ('kor', 'Korea (Republic of Korea)'), ('kos', 'Kosovo (partially recognised state of Serbia)'), ('kwt', 'Kuwait'), ('lao', "Lao People's Democratic Republic"), ('lbn', 'Lebanon'), ('lbr', 'Liberia'), ('lby', 'Libya'), ('lca', 'Saint Lucia'), ('lie', 'Liechtenstein'), ('lka', 'Sri Lanka'), ('lso', 'Lesotho'), ('ltu', 'Lithuania'), ('lux', 'Luxembourg'), ('lva', 'Latvia'), ('mac', 'Macau (Macao Special Administrative Region of China)'), ('maf', 'Saint Martin (French part)'), ('mar', 'Marokko'), ('mco', 'Monaco'), ('mda', 'Moldova'), ('mdg', 'Madagascar'), ('mdv', 'Maldives'), ('mex', 'Mexico'), ('mhl', 'Marshall Islands'), ('mkd', 'Makedonia'), ('mli', 'Mali'), ('mlt', 'Malta'), ('mmr', 'Myanmar'), ('mne', 'Montenegro'), ('mng', 'Mongolia'), ('mnp', 'Northern Mariana Islands'), ('moz', 'Mozambique'), ('mrt', 'auritania'), ('msr', 'Montserrat'), ('mtq', 'Martinique'), ('mus', 'Mauritius'), ('mwi', 'Malawi'), ('mys', 'Malaysia'), ('myt', 'Mayotte'), ('nam', 'Namibia'), ('ncl', 'New Caledonia'), ('ner', 'Niger'), ('nfk', 'Norfolk Island'), ('nga', 'Nigeria'), ('nic', 'Nicaragua'), ('nir', 'Northern Ireland'), ('niu', 'Niue'), ('nld', 'Netherlands'), ('nor', 'Norway'), ('npl', 'Nepal'), ('nru', 'Nauru'), ('nzl', 'New Zealand'), ('omn', 'Oman'), ('pak', 'Pakistan'), ('pan', 'Panama'), ('pcn', 'Pitcairn'), ('per', 'Peru'), ('phl', 'Phillipines'), ('plw', 'Palau'), ('png', 'Papua New Guinea'), ('pol', 'Poland'), ('pri', 'Puerto Rico'), ('prk', "Korea (Democratic People's Republic of Korea)"), ('prt', 'Portugal'), ('pry', 'Paraguay'), ('pse', 'State of Palestine'), ('pyf', 'French Polynesia'), ('qat', 'Qatar'), ('reu', 'Réunion'), ('rou', 'Roumania'), ('rus', 'Russia'), ('rwa', 'Rwanda'), ('sau', 'Saudi Arabia'), ('sco', 'Scotland'), ('sdn', 'Sudan'), ('sen', 'Senegal'), ('sgp', 'Singapore'), ('sgs', 'South Georgia and the South Sandwich Islands'), ('shn', 'Saint Helena, Ascension and Tristan da Cunha'), ('sjm', 'Svalbard and Jan Mayen'), ('slb', 'Solomon Islands'), ('sle', 'Sierra Leone'), ('slv', 'El Salvador'), ('smr', 'San Marino'), ('som', 'Somalia'), ('spm', 'Saint Pierre and Miquelon'), ('srb', 'Serbia'), ('ssd', 'South Sudan'), ('stp', 'Sao Tome and Principe'), ('sun', 'Union of Soviet Socialist Republics (USSR)'), ('sur', 'Suriname'), ('svk', 'Slovakia'), ('svn', 'Slovenia'), ('swe', 'Sweden'), ('swz', 'Swaziland'), ('sxm', 'Sint Maarten (Dutch part)'), ('syc', 'Seychelles'), ('syr', 'Syrian Arab Republic'), ('tca', 'Turks and Caicos Islands'), ('tcd', 'Chad'), ('tgo', 'Togo'), ('tha', 'Thailand'), ('tjk', 'Tajikistan'), ('tkl', 'Tokelau'), ('tkm', 'Turkmenistan'), ('tls', 'Timor-Leste'), ('ton', 'Tonga'), ('tto', 'Trinidad and Tobago'), ('tun', 'Tunisia'), ('tur', 'Turkey'), ('tuv', 'Tuvalu'), ('twn', 'Taiwan'), ('tza', 'United Republic of Tanzania'), ('uga', 'Uganda'), ('ukr', 'Ukraine'), ('umi', 'United States Minor Outlying Islands'), ('ury', 'Uruguay'), ('usa', 'United States of America'), ('uzb', 'Uzbekistan'), ('vat', 'Vanuatu'), ('vct', 'Vatican'), ('ven', 'Venezuela'), ('vgb', 'Virgin Islands (British)'), ('vir', 'Virgin Islands (U.S.)'), ('vnm', 'Vietnam'), ('vut', 'Vanuatu'), ('wal', 'Wales'), ('wlf', 'Wallis and Futuna'), ('wsm', 'Samoa'), ('yem', 'Yemen'), ('zaf', 'South Africa'), ('zmb', 'Zambia'), ('zwe', 'Zimbabwe')], default='Ireland', max_length=250),
        ),
    ]
