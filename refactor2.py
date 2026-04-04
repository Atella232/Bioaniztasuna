import os

files = ['Bioaniztasuna.html', 'Bioaniztasuna_es.html', 'Bioaniztasuna_ar.html']
for fn in files:
    with open(fn, 'r') as f:
        content = f.read()

    # Feature image replacement
    old_feature_css = '''/* Nuevo diseño para Feature Cards */
.feature-image {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  border: 1px solid var(--border-subtle);
}'''
    
    new_feature_css = '''/* Nuevo diseño para Feature Cards */
.feature-image {
  width: calc(100% + 4rem);
  height: 180px;
  object-fit: cover;
  margin: -2.5rem -2rem 1.5rem -2rem;
  border-bottom: 1px solid var(--border-subtle);
  border-radius: 20px 20px 0 0;
  display: block;
}'''

    # Threat image replacement
    old_threat_css = '''/* Nuevo diseño para Threat Cards */
.threat-image {
  width: 100%;
  height: 160px;
  object-fit: cover;
  border-radius: 12px;
  margin-bottom: 1rem;
  border: 1px solid var(--border-subtle);
}'''

    new_threat_css = '''/* Nuevo diseño para Threat Cards */
.threat-image {
  width: calc(100% + 4rem);
  height: 160px;
  object-fit: cover;
  margin: -2rem -2rem 1.5rem -2rem;
  border-bottom: 1px solid var(--border-subtle);
  border-radius: 16px 16px 0 0;
  display: block;
}'''

    # Update z-index for the pseudo-elements so they hover nicely over the edge-to-edge images
    content = content.replace('.feature-card::before {\n  content: \'\';\n  position: absolute;', '.feature-card::before {\n  content: \'\';\n  position: absolute;\n  z-index: 1;')
    content = content.replace('.threat-card::before {\n  content: \'\';\n  position: absolute;', '.threat-card::before {\n  content: \'\';\n  position: absolute;\n  z-index: 1;')

    content = content.replace(old_feature_css, new_feature_css)
    content = content.replace(old_threat_css, new_threat_css)

    with open(fn, 'w') as f:
        f.write(content)
print("Archivos refactorizados correctamente para edge-to-edge.")
