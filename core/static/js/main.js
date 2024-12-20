// static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });

    // Galeri Filtreleme
    const filterButtons = document.querySelectorAll('[data-filter]');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.dataset.filter;
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            galleryItems.forEach(item => {
                if (filter === 'all' || item.classList.contains(filter)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    // ESC tuşuna basıldığında aktif modalı kapat
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            const activeModal = document.querySelector('.video-modal[style*="display: block"]');
            if (activeModal) {
                closeVideoModal(activeModal.id);
            }
        }
    });

    // Modal dışına tıklandığında kapat
    const modals = document.querySelectorAll('.video-modal');
    modals.forEach(modal => {
        modal.addEventListener('click', function(event) {
            if (event.target === modal) {
                closeVideoModal(modal.id);
            }
        });
    });
});

// Video Modal Functions
function openVideoModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    // Body scroll'u devre dışı bırak
    document.body.style.overflow = 'hidden';
    modal.style.display = 'block';

    // Video'yu başlat
    const video = modal.querySelector('video');
    if (video) {
        try {
            video.play();
        } catch (error) {
            console.error('Video oynatma hatası:', error);
        }
    }
}

function closeVideoModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    // Body scroll'u tekrar etkinleştir
    document.body.style.overflow = 'auto';
    modal.style.display = 'none';

    // Video'yu durdur ve sıfırla
    const video = modal.querySelector('video');
    if (video) {
        video.pause();
        video.currentTime = 0;
    }

    // iframe varsa yeniden yükle (YouTube/Vimeo için)
    const iframe = modal.querySelector('iframe');
    if (iframe && iframe.src) {
        const currentSrc = iframe.src;
        iframe.src = '';
        setTimeout(() => {
            iframe.src = currentSrc;
        }, 100);
    }
}

// Image Modal Functions
function openImageModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    document.body.style.overflow = 'hidden';
    modal.style.display = 'block';
}

function closeImageModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    document.body.style.overflow = 'auto';
    modal.style.display = 'none';
}

// ESC tuşu için event listener'a resim modalı da ekleyin
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const activeImageModal = document.querySelector('.image-modal[style*="display: block"]');
        if (activeImageModal) {
            closeImageModal(activeImageModal.id);
        }
    }
});

// Modal dışına tıklama için image modalı da ekleyin
const imageModals = document.querySelectorAll('.image-modal');
imageModals.forEach(modal => {
    modal.addEventListener('click', function(event) {
        if (event.target === modal) {
            closeImageModal(modal.id);
        }
    });
});