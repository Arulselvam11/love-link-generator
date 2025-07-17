// Love Link Generator - Client-side JavaScript
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize page animations
    initPageAnimations();
    
    // Initialize form enhancements
    initFormEnhancements();
    
});

// Page Animation Functions
function initPageAnimations() {
    // Fade in animation for love cards
    const loveCards = document.querySelectorAll('.love-card');
    loveCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.6s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 200);
    });
    
    // Animated hearts
    createFloatingHearts();
}

function createFloatingHearts() {
    const heartsContainer = document.querySelector('.hearts-background');
    if (!heartsContainer) return;
    
    // Add more dynamic hearts
    for (let i = 0; i < 5; i++) {
        setTimeout(() => {
            const heart = document.createElement('div');
            heart.className = 'heart floating-heart';
            heart.innerHTML = '♥';
            heart.style.left = Math.random() * 100 + '%';
            heart.style.top = Math.random() * 100 + '%';
            heart.style.animationDelay = Math.random() * 6 + 's';
            heart.style.fontSize = (Math.random() * 2 + 1) + 'rem';
            heart.style.opacity = Math.random() * 0.3 + 0.1;
            
            heartsContainer.appendChild(heart);
            
            // Remove heart after animation
            setTimeout(() => {
                if (heart.parentNode) {
                    heart.parentNode.removeChild(heart);
                }
            }, 6000);
        }, i * 1000);
    }
}

// Form Enhancement Functions
function initFormEnhancements() {
    // Add floating labels effect
    const inputs = document.querySelectorAll('.love-input');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            if (this.value === '') {
                this.parentElement.classList.remove('focused');
            }
        });
    });
    
    // Form submission enhancements
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn && submitBtn.classList.contains('love-btn')) {
                submitBtn.innerHTML = '<i class="fas fa-heart"></i> Creating Magic...';
                submitBtn.disabled = true;
            }
        });
    });
}

// Console Easter Egg
console.log(`
💕 Love Link Generator 💕
Made with ❤️ for spreading love
`);