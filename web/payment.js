// Payment page functionality
let selectedPlanData = {
    type: '',
    amount: 0
};

function selectPlan(planType, amount) {
    selectedPlanData = { type: planType, amount: amount };

    // Hide plans, show payment form
    document.querySelector('.payment-plans').style.display = 'none';
    document.getElementById('paymentForm').style.display = 'block';

    // Update selected plan info
    const planInfo = document.getElementById('selectedPlanInfo');
    const planName = planType === 'monthly' ? 'Oylik obuna' : 'Yillik obuna';
    planInfo.innerHTML = `
        <div class="plan-summary">
            <div class="plan-summary-header">
                <h4>${planName}</h4>
                <button class="change-plan-btn" onclick="backToPlans()">O'zgartirish</button>
            </div>
            <div class="plan-summary-price">
                <span class="total-label">Jami:</span>
                <span class="total-amount">${amount.toLocaleString('uz-UZ')} so'm</span>
            </div>
        </div>
    `;

    // Scroll to form
    document.getElementById('paymentForm').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function backToPlans() {
    document.querySelector('.payment-plans').style.display = 'grid';
    document.getElementById('paymentForm').style.display = 'none';
    document.getElementById('paymentSuccess').style.display = 'none';

    // Scroll to plans
    document.querySelector('.payment-plans').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function processPayment(event) {
    event.preventDefault();

    // Get form data
    const telegram = document.getElementById('telegram').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
    const paymentMethod = document.querySelector('input[name="payment-method"]:checked').value;

    // Show loading
    const submitBtn = event.target.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Kutilmoqda...';
    submitBtn.disabled = true;

    // Simulate payment processing
    setTimeout(() => {
        // In real implementation, send data to backend
        console.log('Payment data:', {
            plan: selectedPlanData,
            telegram,
            phone,
            email,
            paymentMethod
        });

        // Store payment info in localStorage (for demo)
        localStorage.setItem('premiumUser', JSON.stringify({
            telegram,
            phone,
            plan: selectedPlanData.type,
            activatedAt: new Date().toISOString(),
            expiresAt: new Date(Date.now() + (selectedPlanData.type === 'monthly' ? 30 : 365) * 24 * 60 * 60 * 1000).toISOString()
        }));

        // Hide form, show success
        document.getElementById('paymentForm').style.display = 'none';
        document.getElementById('paymentSuccess').style.display = 'block';

        // Scroll to success message
        document.getElementById('paymentSuccess').scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Reset button
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }, 2000);
}

// Highlight selected payment method
document.addEventListener('DOMContentLoaded', () => {
    const methodCards = document.querySelectorAll('.method-card');

    methodCards.forEach(card => {
        card.addEventListener('click', () => {
            methodCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
        });
    });

    // Set first method as selected by default
    if (methodCards.length > 0) {
        methodCards[0].classList.add('selected');
    }
});

// Phone number formatting
document.addEventListener('DOMContentLoaded', () => {
    const phoneInput = document.getElementById('phone');
    if (phoneInput) {
        phoneInput.addEventListener('input', (e) => {
            let value = e.target.value.replace(/\D/g, '');
            if (value.startsWith('998')) {
                value = value.substring(3);
            }
            if (value.length > 0) {
                value = '+998 ' + value.substring(0, 2) + (value.length > 2 ? ' ' + value.substring(2, 5) : '') +
                    (value.length > 5 ? ' ' + value.substring(5, 7) : '') +
                    (value.length > 7 ? ' ' + value.substring(7, 9) : '');
            }
            e.target.value = value;
        });
    }
});
