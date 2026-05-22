// ==========================
// GLOBAL CART SYSTEM (FIXED)
// ==========================

// Load saved cart total (works across pages)
let total = parseInt(localStorage.getItem("cart_total")) || 0;

// Update total on page load
document.addEventListener("DOMContentLoaded", () => {
    updateCartUI();
});

function updateCartUI() {
    let totalBox = document.getElementById("total");
    if (totalBox) {
        totalBox.innerText = total;
    }
}

// ==========================
// MENU CART SYSTEM (FIXED)
// ==========================

function addToCart(price) {
    total += price;

    localStorage.setItem("cart_total", total);

    updateCartUI();

    alert("Item added to cart!");
}

// ==========================
// CLEAR CART (ADDED)
// ==========================

function clearCart() {
    total = 0;
    localStorage.removeItem("cart_total");
    updateCartUI();
}

// ==========================
// CONTACT FORM
// ==========================

function submitForm(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;

    alert("Thank you " + name + "! We will contact you soon.");

    document.querySelector(".contact-form").reset();
}

// ==========================
// LOGIN FORM
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    let loginForm = document.querySelector(".log_in");

    if (loginForm) {

        loginForm.addEventListener("submit", function(event) {

            event.preventDefault();

            let user = document.querySelector('input[name="user"]').value;

            alert("Welcome " + user + "! Login successful.");

            loginForm.reset();
        });

    }
});

// ==========================
// CUSTOMIZE PAGE SELECTION
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    let options = document.querySelectorAll(".option");

    options.forEach(option => {

        option.addEventListener("click", () => {

            options.forEach(opt => opt.classList.remove("active"));

            option.classList.add("active");

        });

    });

});

// ==========================
// CUSTOM MESSAGE BUTTON
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    let addBtn = document.querySelector(".add-btn");

    if (addBtn) {

        addBtn.addEventListener("click", () => {

            let message = document.querySelector("textarea").value;

            if (message === "") {

                alert("Please enter a custom message.");

            } else {

                alert("Customized chocolate added!\nMessage: " + message);
            }

        });

    }

});

// ==========================
// PAYMENT PAGE
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    let paymentForm = document.querySelector(".payment-form");

    if (paymentForm) {

        paymentForm.addEventListener("submit", function(event) {

            event.preventDefault();

            alert("Payment Successful!");

            paymentForm.reset();
        });

    }

});

// ==========================
// SIMPLE AUTO SLIDER
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    let slides = document.querySelectorAll(".slide");

    let current = 0;

    function showSlide(index) {

        slides.forEach(slide => {
            slide.style.display = "none";
        });

        slides[index].style.display = "block";
    }

    if (slides.length > 0) {

        showSlide(current);

        setInterval(() => {

            current++;

            if (current >= slides.length) {
                current = 0;
            }

            showSlide(current);

        }, 3000);

    }

});