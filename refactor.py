import os
import re

files = ['Bioaniztasuna.html', 'Bioaniztasuna_es.html', 'Bioaniztasuna_ar.html']
for fn in files:
    with open(fn, 'r') as f:
        content = f.read()
    
    # 1. Replace CSS
    content = content.replace('.card-icon {', '''/* Nuevo diseño para Feature Cards */
.feature-image {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  border: 1px solid var(--border-subtle);
}

.card-icon {''')
    
    content = content.replace('.threat-icon {', '''/* Nuevo diseño para Threat Cards */
.threat-image {
  width: 100%;
  height: 160px;
  object-fit: cover;
  border-radius: 12px;
  margin-bottom: 1rem;
  border: 1px solid var(--border-subtle);
}

.threat-icon {''')

    content = content.replace('.cell-type-btn .btn-emoji {', '''/* Nuevo diseño para Células Selector */
.btn-icon-img {
  width: 48px;
  height: 48px;
  object-fit: cover;
  border-radius: 50%;
  margin: 0 auto 0.8rem auto;
  display: block;
  border: 2px solid var(--border-subtle);
  box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

.cell-type-btn .btn-emoji {''')

    # 2. Replace HTML divs for card-icon
    content = re.sub(
        r'<div class="card-icon[^"]*" style="background: url\(\'img/([^\']+)\'\)[^>]*></div>(?: <!-- TODO:[^>]+-->)?',
        r'<img class="feature-image" src="img/\1" alt="">',
        content
    )
    
    # 3. Replace HTML divs for threat-icon
    content = re.sub(
        r'<div class="threat-icon" style="background: url\(\'img/([^\']+)\'\)[^>]*></div>(?: <!-- TODO:[^>]+-->)?',
        r'<img class="threat-image" src="img/\1" alt="">',
        content
    )
    
    # 4. Cell type buttons emojis
    content = content.replace('<span class="btn-emoji">🦠</span>', '<img class="btn-icon-img" src="img/cell_prokariota_1775266305927.png" alt="">')
    content = content.replace('<span class="btn-emoji">🔴</span>', '<img class="btn-icon-img" src="img/cell_animalia_1775265919180.png" alt="">')
    content = content.replace('<span class="btn-emoji">🟢</span>', '<img class="btn-icon-img" src="img/cell_plantae_1775266319103.png" alt="">')
    content = content.replace('<span class="btn-emoji">⚖️</span>', '<span class="btn-emoji">⚖️</span>') 
    
    with open(fn, 'w') as f:
        f.write(content)
print("Archivos refactorizados correctamente.")
