import os
import re

files = ['Bioaniztasuna.html', 'Bioaniztasuna_es.html', 'Bioaniztasuna_ar.html']
for fn in files:
    with open(fn, 'r') as f:
        content = f.read()

    # Kingdoms replacements
    content = re.sub(
        r'img/kingdom_animalia_[0-9]+\.png',
        'img/kingdom_animalia.png',
        content
    )
    content = re.sub(
        r'img/kingdom_plantae_[0-9]+\.png',
        'img/kingdom_plantae.png',
        content
    )
    content = re.sub(
        r'img/kingdom_fungi_[0-9]+\.png',
        'img/kingdom_fungi.png',
        content
    )
    content = re.sub(
        r'img/kingdom_protista_[0-9]+\.png',
        'img/kingdom_protista.png',
        content
    )
    content = re.sub(
        r'img/kingdom_monera_[0-9]+\.png',
        'img/kingdom_monera.png',
        content
    )

    # Functions replacements
    content = re.sub(
        r'img/func_elikadura_[0-9]+\.png',
        'img/func_elikadura.png',
        content
    )
    content = re.sub(
        r'img/func_erlazioa_[0-9]+\.png',
        'img/func_erlazioa.png',
        content
    )
    content = re.sub(
        r'img/func_ugalketa_[0-9]+\.png',
        'img/func_ugalketa.png',
        content
    )

    with open(fn, 'w') as f:
        f.write(content)

print("Kingdoms and Functions HTML references have been refactored.")
