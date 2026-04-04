import sys

files = ['Bioaniztasuna.html', 'Bioaniztasuna_es.html', 'Bioaniztasuna_ar.html']

for fn in files:
    with open(fn, 'r') as f:
        content = f.read()

    # We will replace the whole Image Modal Logic
    start_str = "// --- Image Modal Logic ---"
    start_idx = content.find(start_str)
    if start_idx == -1: continue
    
    end_idx = content.find("</script>", start_idx)
    
    new_js = """// --- Image Modal Logic ---
    function openImageModal(imgSrc) {
      if(!imgSrc) return;
      document.getElementById('imageModalImg').src = imgSrc;
      document.getElementById('imageModal').classList.add('active');
    }

    function closeImageModal() {
      document.getElementById('imageModal').classList.remove('active');
      document.getElementById('imageModalImg').src = '';
    }

    function initModals() {
      const modal = document.getElementById('imageModal');
      if (modal) {
        modal.addEventListener('click', function(e) {
          if(e.target === this || e.target.classList.contains('image-modal-close')) {
            closeImageModal();
          }
        });
      }

      const elements = document.querySelectorAll('.invasive-header, .threat-image, .feature-image, .kingdom-visual, .func-illustration');
      elements.forEach(el => {
        el.style.cursor = 'zoom-in';
        el.onclick = function(e) {
          e.preventDefault();
          e.stopPropagation();
          let srcUrl = this.getAttribute('src');
          if (!srcUrl) {
            const bgStr = window.getComputedStyle(this).backgroundImage;
            const match = bgStr.match(/url\\(["']?(.*?)["']?\\)/);
            if (match && match[1]) srcUrl = match[1];
          }
          if (srcUrl) {
              srcUrl = srcUrl.replace(/["']/g, '');
              openImageModal(srcUrl);
          }
        };
      });
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initModals);
    } else {
      initModals();
    }
  """
    
    content = content[:start_idx] + new_js + content[end_idx:]
    with open(fn, 'w') as f:
        f.write(content)
        
print("Fixed null pointer bugs")
