# Carpeta: MenuVersion2/PS5-CONSOLE

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## README.md

Ruta: `MenuVersion2/PS5-CONSOLE/README.md` · Bytes: 1196 · SHA-256: `400faae9d56284a52d5f51f58d8212bf42fb66f8bae3a120ee8b9932490dd57c`

````text

# PS5-CONSOLE

A visually rich, responsive PlayStation 5 Console web project built with HTML and CSS.

## Overview

**PS5-CONSOLE** is a front-end project that recreates the look and feel of the PlayStation 5 console using only HTML and CSS. This project demonstrates advanced CSS techniques and responsive layouts, making it ideal for learning and showcasing front-end development skills.

## Features

- 🎮 Faithful recreation of the PS5 console design  
- 📱 Responsive layout for various screen sizes  
- 💡 Modern CSS (Flexbox, Grid, animations)  
- 🌙 Clean codebase for easy customization  

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/singharyan006/PS5-CONSOLE.git
   ```

2. **Open the project:**
   - Navigate to the project directory.
   - Open `index.html` in your browser.

## Folder Structure

```
PS5-CONSOLE/
├── index.html
├── style.css
├── assets/
│   └── (images, icons, etc.)
```
## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or new features.

## License

This project is open source and available under the [MIT License](LICENSE).

````

## index.html

Ruta: `MenuVersion2/PS5-CONSOLE/index.html` · Bytes: 4073 · SHA-256: `78c4ea310254ad98047448e63db3aaafd0146896911d131e83bc24e649c5eeec`

````text
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PlayStation 5</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Navigation Bar -->
    <header>
        <nav class="navbar">
            <div class="logo">
                <img src="assets/logo.webp n" alt="PlayStation Logo">
            </div>
            <ul class="nav-links">
                <li><a href="https://www.playstation.com/en-in/ps5"target="_main">PS5</a></li>
                <li><a href="https://www.playstation.com/en-in/ps4"target="_main">PS4</a></li>
                <li><a href="https://www.playstation.com/en-in/ps5/games"target="_main">Games</a></li>
                <li><a href="https://www.playstation.com/en-in/accessories"target="_main">Accessories</a></li>
                <li><a href="https://www.playstation.com/en-in/support"target="_main">Services</a></li>
                <li><a href="https://www.playstation.com/en-in/editorial/this-month-on-playstation/?smcid=pdc%3Aen-in%3Aps5%3Aprimary%20nav%3Amsg-news%3Athis-month-on-playstation"target="_main">News</a></li>
            </ul>
            <div class="search-bar">
                <input type="text" placeholder="Search">
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>PlayStation 5</h1>
            <p>Feel incredible gaming possibilities that go beyond the extraordinary with PlayStation 5 </p>
            <a href="https://www.google.com" class="cta-btn">Learn More</a>
        </div>
        <div class="hero-image">
            <img src="assets/ps5-console3.jpg" alt="PlayStation 5 Console">
        </div>
    </section>

    <!-- Product Introduction Section -->
    <section class="product-intro">
        <h2>Introducing the PlayStation 5</h2>
        <p>Explore a new generation of immersive gameplay and entertainment.</p>
        <a href="https://www.playstation.com/en-in/ps5/ps5-features" class="cta-btn">See Features</a>
        <div class="product-features">
            <div class="feature">
                <img src="assets/fps.png" alt="120FPS">
                <h3>120-Frames Per Second</h3>
                <p>A Brand New Experience of 120FPS, Immerse Yourself in the Games.</p>
            </div>
            <div class="feature">
                <img src="assets/raytracing.png" alt="Advanced-Ray-Tracing">
                <h3>Ray Tracing</h3>
                <p>Immerse yourself in worlds with a new level of realism thanks to ray tracing.</p>
            </div>
            <!-- Add more features if needed -->
        </div>
    </section>

    <!-- Game Gallery Section -->
    <section class="game-gallery">
        <h2>Latest and Upcoming Games</h2>
        <div class="games">
            <div class="game">
                <img src="assets/Spider Man.webp" alt="Game 1">
                <p>Spider-Man: Miles Morales</p>
            </div>
            <div class="game">
                <img src="assets/horizonforbiddonwest.webp" alt="Game 2">
                <p>Horizon Forbidden West</p>
            </div>
            <div class="game">
                <img src="assets/ratchetandclank.webp" alt="Game 3">
                <p>Ratchet & Clank: Rift Apart</p>
            </div>
            <div class="game">
                <img src="assets/Returnal.webp" alt="Game 3">
                <p>Returnal</p>
            </div>
            <div class="game">
                <img src="assets/Ghostoftsushima.webp" alt="Game 3">
                <p>Ghost of Tsushima-Director's Cut</p>
            </div>
            
            
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <p>&copy; 2024 Sony Interactive Entertainment LLC. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
````

## style.css

Ruta: `MenuVersion2/PS5-CONSOLE/style.css` · Bytes: 2948 · SHA-256: `12a984a64b559ded53eed643a1ede3e8c9fd8369ee047f6cca4d0b252db1b0ec`

````text
/* Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: 'Roboto', sans-serif;
    color: #333;
    background-color: #f5f5f5;
}

/* Navigation Bar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #073b9d;
}
.logo img {
    max-width: 300px;
    width: 50%;
}
.nav-links {
    list-style: none;
    display: flex;
    gap: 1.5rem;
}
.nav-links li a {
    color: white;
    text-decoration: none;
    font-weight: 500;
}
.search-bar input {
    padding: 0.5rem;
    border-radius: 5px;
    border: none;
}

/* Hero Section */
.hero {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 3rem;
    background-color: white;
    text-align: left;
}
.hero-content {
    max-width: 50%;
}
.hero h1 {
    font-size: 3rem;
    color: #003087;
    font-weight: 700;
}
.hero p {
    margin: 1rem 0;
    font-size: 1.2rem;
}
.cta-btn {
    padding: 0.7rem 1.5rem;
    background-color: #003087;
    color: white;
    border-radius: 5px;
    font-weight: 500;
    display: inline-block;
}
.hero-image img {
    max-width: 500px;
    max-height: 700px;
}

/* Product Introduction Section */
.product-intro {
    background-color: #f5f5f5;
    text-align: center;
    padding: 4rem 2rem;
}
.product-intro h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #003087;
}
.product-intro p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
}
.product-features {
    display: flex;
    justify-content: space-around;
    gap: 1rem;
}
.feature {
    text-align: center;
    max-width: 300px;
}
.feature img {
    max-width: 200px;
    margin-bottom: 1rem;
}
.feature h3 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}
.feature p {
    font-size: 1rem;
}

/* Game Gallery Section */
.game-gallery {
    background-color: white;
    padding: 4rem 2rem;
    text-align: center;
}
.game-gallery h2 {
    font-size: 2.5rem;
    color: #003087;
    margin-bottom: 2rem;
}
/* Game Gallery Styles */
.game-gallery {
    padding: 20px;
    text-align: center;
}

.games {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}

.game {
    width: 200px;
    transition: transform 0.3s ease-in-out;
}

.game img {
    width: 100%;
    height: auto;
    border-radius: 10px;
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.game img:hover {
    transform: scale(1.1);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.game p {
    margin-top: 10px;
    font-size: 16px;
    font-weight: 500;
    color: #333;
}


/* Footer */
footer {
    background-color: #003087;
    color: white;
    padding: 1rem 0;
    text-align: center;
    font-size: 0.9rem;
}

````

