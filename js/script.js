// JavaScript for Sticky Navbar, Smooth Scroll, Dropdown, and Additional Features

document.addEventListener("DOMContentLoaded", () => {
    // Create loading skeleton
    const loadingSkeleton = document.createElement("div");
    loadingSkeleton.id = "loading-skeleton";
    loadingSkeleton.style.position = "fixed";
    loadingSkeleton.style.top = "0";
    loadingSkeleton.style.left = "0";
    loadingSkeleton.style.width = "100%";
    loadingSkeleton.style.height = "100%";
    loadingSkeleton.style.backgroundColor = "#f4f4f4";
    loadingSkeleton.style.zIndex = "9999";
    loadingSkeleton.style.display = "flex";
    loadingSkeleton.style.justifyContent = "center";
    loadingSkeleton.style.alignItems = "center";
    loadingSkeleton.innerHTML = `
        <div class="skeleton-box" style="width: 50px; height: 50px; background-color: #ccc; border-radius: 50%;"></div>
    `;
    document.body.appendChild(loadingSkeleton);

    // Animate the skeleton using Anime.js
    anime({
        targets: ".skeleton-box",
        scale: [1, 1.5],
        opacity: [1, 0.5],
        duration: 1000,
        easing: "easeInOutQuad",
        direction: "alternate",
        loop: true,
    });

    // Remove loading skeleton after the page is fully loaded
    window.addEventListener("load", () => {
        anime({
            targets: "#loading-skeleton",
            opacity: [1, 0],
            duration: 500,
            easing: "easeOutQuad",
            complete: () => {
                loadingSkeleton.remove();
            },
        });
    });

    const navbar = document.querySelector(".navbar");
    const navItems = document.querySelectorAll(".nav-item");
    const links = document.querySelectorAll("a[href^='#']"); // Links for smooth scrolling

    // Sticky Navbar Effect
    window.addEventListener("scroll", () => {
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });

    // Dropdown Menu Hover Behavior
    navItems.forEach((navItem) => {
        const subNav = navItem.querySelector(".sub-nav");

        if (subNav) {
            navItem.addEventListener("mouseenter", () => {
                subNav.style.display = "block";
                subNav.style.opacity = "1";
                subNav.style.visibility = "visible";
                subNav.style.transform = "translateX(-50%) scale(1)";
            });

            navItem.addEventListener("mouseleave", () => {
                subNav.style.display = "none";
                subNav.style.opacity = "0";
                subNav.style.visibility = "hidden";
                subNav.style.transform = "translateX(-50%) scale(0.95)";
            });
        }
    });

    // Smooth Scrolling
    links.forEach((link) => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const targetId = link.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Adjust for navbar height
                    behavior: "smooth",
                });
            }
        });
    });

    // Basic UI Management (Dark Mode Toggle Example)
    const toggleDarkMode = document.createElement("button");
    toggleDarkMode.textContent = "Toggle Dark Mode";
    toggleDarkMode.style.position = "fixed";
    toggleDarkMode.style.bottom = "20px";
    toggleDarkMode.style.right = "20px";
    toggleDarkMode.style.padding = "10px 20px";
    toggleDarkMode.style.backgroundColor = "#2C3E50";
    toggleDarkMode.style.color = "#fff";
    toggleDarkMode.style.border = "none";
    toggleDarkMode.style.cursor = "pointer";
    toggleDarkMode.style.borderRadius = "5px";
    document.body.appendChild(toggleDarkMode);

    toggleDarkMode.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
    });

    // Data Encryption Example (AES Encryption using Web Crypto API)
    async function encryptData(plainText, secretKey) {
        const encoder = new TextEncoder();
        const data = encoder.encode(plainText);

        const key = await window.crypto.subtle.importKey(
            "raw",
            encoder.encode(secretKey),
            { name: "AES-GCM" },
            false,
            ["encrypt"]
        );

        const iv = window.crypto.getRandomValues(new Uint8Array(12)); // Initialization vector
        const encryptedData = await window.crypto.subtle.encrypt(
            { name: "AES-GCM", iv },
            key,
            data
        );

        return {
            cipherText: btoa(String.fromCharCode(...new Uint8Array(encryptedData))),
            iv: Array.from(iv),
        };
    }

    // Example usage of encryption
    const sampleData = "Sensitive User Data";
    const secretKey = "SuperSecretKey123";
    encryptData(sampleData, secretKey).then((encrypted) => {
        console.log("Encrypted Data:", encrypted);
    });
});
