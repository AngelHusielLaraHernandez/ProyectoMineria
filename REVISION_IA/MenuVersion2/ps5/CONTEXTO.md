# Carpeta: MenuVersion2/ps5

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## README.md

Ruta: `MenuVersion2/ps5/README.md` · Bytes: 353 · SHA-256: `6ca6439665ee76b521bf2841a36f072ad7f8cc7c7a8d01d3984d5d62a1c8b0e5`

````text
# 🎮 PS5 Landing Page

My first ever front-end project — built with pure **HTML**, **CSS**, and **JavaScript**.  
No frameworks, no libraries — just curiosity and late-night code.

---

### ✨What I Tried
- Simple PS5-inspired UI  
- Basic navigation & styling  
- My first steps into web development  

> “Every master was once a beginner.”

````

## index.html

Ruta: `MenuVersion2/ps5/index.html` · Bytes: 3937 · SHA-256: `d1d6bcc954a962ba499f07704a93f016cf4c988691b0ca56622e72155cb64e3e`

````text
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PS5</title>

    <link
      rel="stylesheet"
      href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css"
      integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p"
      crossorigin="anonymous"
    />

    <link rel="icon" href="img/icon.png" />
    <link rel="stylesheet" href="css/style.css" />

    <!---font-->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
      rel="stylesheet"
    />
    <!---font-->
  </head>

  <body style="background-image: url(img/bg-spider-man.png);">
    <header class="header">
      <div class="container">
        <div class="profile-header">
          <ul>
            <li class="time-header">20:35 PM</li>
            <li class="image-header">
              <a href="#">
                <figure>
                  <img src="img/Majedjpg.jpg" alt="proile" />
                  <span></span>
                </figure>
              </a>
              <ul class="show-sub">
                <li>
                  <a href="#"><i class="fas fa-user-check"></i>Online Status</a>
                </li>
                <li>
                  <a href="profile.html"
                    ><i class="fas fa-user-circle"></i>Profile</a
                  >
                </li>
                <li>
                  <a href="#"><i class="fas fa-trophy"></i>Trophies</a>
                </li>
                <li>
                  <a href="#"><i class="fas fa-user-cog"></i>Swich User</a>
                </li>
                <li>
                  <a href="#"><i class="fas fa-sign-out-alt"></i>Log Out</a>
                </li>
              </ul>
            </li>
            <li class="icon-header">
              <a href="#"><i class="fas fa-cog"></i></a>
            </li>
            <li class="icon-header">
              <a href="#"><i class="fas fa-search"></i></a>
            </li>
          </ul>
        </div>
        <div class="select-header">
          <ul>
            <li><a href="#">Games</a></li>
            <li>
              <a href="#"><span>blog</span></a>
            </li>
          </ul>
        </div>
      </div>
    </header>

    <section class="slider">
      <div class="image-slider">
        <img src="img/game-thumbnail-dirt-5.png" />
      </div>
      <div class="image-slider">
        <img src="img/game-thumbnail-XIII.png" />
      </div>
      <div class="image-slider">
        <figure>
          <img src="img/call.jpg" />
          <span>Call of Duty: Black Ops Cold War PS5 </span>
        </figure>
      </div>

      <div class="image-slider">
        <img src="img/game-thumbnail-demons-souls.png" />
      </div>
      <div class="image-slider">
        <img src="img/game-thumbnail-sackboy.png" />
      </div>
      <div class="image-slider">
        <img src="img/game-thumbnail-yakuza.png" />
      </div>
      <div class="image-slider">
        <img src="img/game-thumbnail-spider-man.png" />
      </div>
      <div class="image-slider">
        <img src="img/god-of-war.jpg" />
      </div>
    </section>
    <section>
      <div class="btn-home">
        <a href="#">Play</a>
        <i class="fas fa-ellipsis-h"></i>
      </div>
    </section>

    <script
      src="https://code.jquery.com/jquery-3.6.0.min.js"
      integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
      crossorigin="anonymous"
    ></script>
    <script src="js/main.js"></script>
  </body>
</html>

````

## profile.html

Ruta: `MenuVersion2/ps5/profile.html` · Bytes: 2681 · SHA-256: `4fc41d03e149c4919b317cbad81a9886cc86a23f7834ad88244133e7dd5f47c9`

````text
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PS5</title>
   
    <link rel="stylesheet" href="css/all.css">
    <link rel="icon" href="img/icon.png">
    <link rel="stylesheet" href="style.css">

    <!---font-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    <!---font-->

</head>
<body class="profile-body">
    <header class="header">
        <div class="container">
            <div class="profile-header">
              <ul>
                  <li class="time-header">20:35 PM</li>
                  <li class="image-header">
                      <a href="file:///C:/Users/Majed/OneDrive/Desktop/ps5-2/index.html">
                      <figure>
                      <img src="img/Majedjpg.jpg" alt="proile">
                      <span></span>
                    </figure>
                  </a>
                    <ul>
                        <li><a href="#"><i class="fas fa-user-check"></i>Online Status</a></li>
                        <li><a href="#"><i class="fas fa-user-circle"></i>Profile</a></li>
                        <li><a href="#"><i class="fas fa-trophy"></i>Trophies</a></li>
                        <li><a href="#"><i class="fas fa-user-cog"></i>Swich User</a></li>
                        <li><a href="#"><i class="fas fa-sign-out-alt"></i>Log Out</a></li>
                    </ul>
                </li>
                  <li class="icon-header"><a href="#"><i class="fas fa-cog"></i></a></li>
                  <li class="icon-header"><a href="#"><i class="fas fa-search"></i></a></li>
              </ul>
            </div>
            <div class="select-profile-header">
                <a href="#">Profile</a>
            </div>
        </div>

    </header>
    <section class="select-profile">
        <div class="menu-profile">
            <ul>
                <li><a href="#">Name</a></li>
                <li><a href="#">Online ID</a></li>
                <li><a href="#">Profile Picture</a></li>
                <li><a href="#">Avatar</a></li>
                <li><a href="#">Cover Image</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Language</a></li>
            </ul>
        </div>
    </section>
    
   
</body>
</html>
````

