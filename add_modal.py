import os

files = ['Bioaniztasuna.html', 'Bioaniztasuna_es.html', 'Bioaniztasuna_ar.html']

css_to_add = '''
/* Image Modal */
.image-modal {
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  background: rgba(0, 0, 0, 0.85);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
  backdrop-filter: blur(5px);
}
.image-modal.active {
  opacity: 1;
  pointer-events: auto;
}
.image-modal-content {
  max-width: 90%;
  max-height: 90vh;
  border-radius: 16px;
  box-shadow: 0 25px 50px rgba(0,0,0,0.5);
  transform: scale(0.9);
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.image-modal.active .image-modal-content {
  transform: scale(1);
}
.image-modal-close {
  position: absolute;
  top: 1.5rem; right: 2rem;
  font-size: 3rem;
  color: white;
  cursor: pointer;
  transition: color 0.3s;
}
.image-modal-close:hover { color: var(--accent-rose); }
</style>'''

html_to_add = '''
  <!-- Image Modal -->
  <div id="imageModal" class="image-modal">
    <span class="image-modal-close" onclick="closeImageModal()">&times;</span>
    <img id="imageModalImg" class="image-modal-content" src="" alt="Modal Image">
  </div>
</body>'''

js_to_add = '''
    // --- Image Modal Logic ---
    function openImageModal(imgSrc) {
      document.getElementById('imageModalImg').src = imgSrc;
      document.getElementById('imageModal').classList.add('active');
    }

    function closeImageModal() {
      document.getElementById('imageModal').classList.remove('active');
    }

    document.getElementById('imageModal').addEventListener('click', function(e) {
      if(e.target === this) {
        closeImageModal();
      }
    });

    document.addEventListener('DOMContentLoaded', () => {
      // Make invasive headers clickable
      document.querySelectorAll('.invasive-header').forEach(header => {
        header.style.cursor = 'zoom-in';
        header.addEventListener('click', function() {
          const bgInfo = this.style.background;
          const urlMatch = bgInfo.match(/url\(['"]?(.*?)['"]?\)/);
          if (urlMatch && urlMatch[1]) {
            openImageModal(urlMatch[1]);
          }
        });
      });
      // Optionally also for threat and feature images to make all images enlargeable
      document.querySelectorAll('.threat-image, .feature-image, .kingdom-visual').forEach(img => {
        img.style.cursor = 'zoom-in';
        img.addEventListener('click', function() {
          let src = this.src;
          if (!src) {
             const bgInfo = this.style.background;
             const urlMatch = bgInfo.match(/url\(['"]?(.*?)['"]?\)/);
             if (urlMatch && urlMatch[1]) src = urlMatch[1];
          }
          if (src) openImageModal(src);
        });
      });
    });
  </script>'''

for fn in files:
    with open(fn, 'r') as f:
        content = f.read()
    
    if 'image-modal' in content: 
        print(f"Modal already exists in {fn}")
        continue
        
    content = content.replace('</style>', css_to_add)
    content = content.replace('</body>', html_to_add)
    content = content.replace('</script>', js_to_add, 1) # Replace the last script tag closure, wait replacing only the first one is bad if there are multiple. We usually have one big script at the end. Let's do string surgery.
    
    # Better JS inject: 
    # find last </script>
    last_script_idx = content.rfind('</script>')
    if last_script_idx != -1:
        content = content[:last_script_idx] + js_to_add + content[last_script_idx+9:]
        
    with open(fn, 'w') as f:
        f.write(content)
        
print("Modal added successfully!")
