// Check if user has premium access
function checkPremiumAccess() {
    const premiumUser = localStorage.getItem('premiumUser');

    if (!premiumUser) {
        // No premium access, redirect to payment
        window.location.href = 'payment.html';
        return false;
    }

    try {
        const userData = JSON.parse(premiumUser);
        const expiresAt = new Date(userData.expiresAt);
        const now = new Date();

        if (now > expiresAt) {
            // Premium expired
            localStorage.removeItem('premiumUser');
            alert('Premium obunangiz tugadi. Iltimos, yangilang.');
            window.location.href = 'payment.html';
            return false;
        }

        // Valid premium access
        return true;
    } catch (error) {
        // Invalid data
        localStorage.removeItem('premiumUser');
        window.location.href = 'payment.html';
        return false;
    }
}

// Show premium user info
function showPremiumUserInfo() {
    const premiumUser = localStorage.getItem('premiumUser');
    if (!premiumUser) return;

    try {
        const userData = JSON.parse(premiumUser);
        const expiresAt = new Date(userData.expiresAt);
        const daysLeft = Math.ceil((expiresAt - new Date()) / (1000 * 60 * 60 * 24));

        // Create user info banner
        const banner = document.createElement('div');
        banner.className = 'premium-user-banner';
        banner.innerHTML = `
            <div class="container">
                <div class="premium-user-info">
                    <div class="user-details">
                        <span class="premium-badge">⭐ Premium</span>
                        <span class="user-telegram">${userData.telegram}</span>
                        <span class="expiry-info">${daysLeft} kun qoldi</span>
                    </div>
                    <button class="logout-btn" onclick="logoutPremium()">Chiqish</button>
                </div>
            </div>
        `;

        // Insert after navbar
        const navbar = document.querySelector('.navbar');
        if (navbar) {
            navbar.after(banner);
        }
    } catch (error) {
        console.error('Error showing user info:', error);
    }
}

// Logout from premium
function logoutPremium() {
    if (confirm('Premium obunadan chiqmoqchimisiz?')) {
        localStorage.removeItem('premiumUser');
        window.location.href = 'index.html';
    }
}

// Run check on page load
if (window.location.pathname.includes('premium.html')) {
    document.addEventListener('DOMContentLoaded', () => {
        if (checkPremiumAccess()) {
            showPremiumUserInfo();
        }
    });
}
