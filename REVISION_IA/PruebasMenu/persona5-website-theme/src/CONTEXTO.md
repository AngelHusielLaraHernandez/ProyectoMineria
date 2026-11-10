# Carpeta: PruebasMenu/persona5-website-theme/src

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## AboutMe.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/AboutMe.jsx` · Bytes: 20307 · SHA-256: `209fc67f13ef877c2dac37aecb44230977ee0c7ad702cb739b22a42ada82c6bd`

````text
import { useState, useEffect, useRef } from "react";
import { playSelectSound } from "./utils/audio.js";
import { useNavigate } from "react-router-dom";
import char1 from "./assets/char1.png";
import char2 from "./assets/char2.png";
import char3 from "./assets/char3.png";
import icon1 from "./assets/icon1.png";
import icon2 from "./assets/icon2.png";
import icon3 from "./assets/icon3.png";
import mainm from "./assets/mainm.jpeg";
import mainm2 from "./assets/mainm2.jpeg";
import mainf from "./assets/mainf.jpeg";

const CHARS = [char1, char2, char3];
const MAIN_IMAGES = [mainm, mainm2, mainf];

const REVEAL_CONTENT = [
  {
    upper: ["name: Francisco", "age: 16 years ", "location: Brazil"],
    lower: "3rd year technical high school student - IT",
  },
  {
    upper: [
      "I study at IFPB Campus Itaporanga,",
      "taking the technical course in computer science.",
    ],
    lower: "Java | JavaScript | Web Development",
  },
  {
    upper: [
      "Focused in backend development",
      "Driven by cognition.",
    ],
    lower: "github: github.com/ffaneto",
  },
];

const ITEMS = [
  {
    id: "about", label: "ABOUT ME", handle: "@ffaneto", href: "https://github.com/ffaneto", icon: "👤", barIcon: icon1, bars: 1, newBars: [0], counts: ["16"],
    links: ["github.com/ffaneto"],
    stats: [
      { tag: "AGE", value: "16", color: "#d92323" },
      { tag: "YEAR", value: "3rd IFPB",  color: "#7b7b7b" },
    ],
  },
  {
    id: "fun", label: "EDUCATION", handle: "@ffaneto", href: "https://github.com/ffaneto", icon: "🏫", barIcon: icon2, bars: 2, newBars: [0, 1], counts: ["IFPB", "TECH"],
    links: ["ifpb/itaporanga", "it/course"],
    stats: [
      { tag: "MAJOR", value: "IT", color: "#d92323" },
      { tag: "CAMPUS", value: "ITAPORANGA",  color: "#732424" },
    ],
  },
  {
    id: "weird", label: "LANGUAGES", handle: "@ffaneto", href: "https://github.com/ffaneto", icon: "💻", barIcon: icon3, bars: 3, newBars: [0, 1, 2], counts: ["JAVA", "JS", "WEB"],
    links: ["learning/java", "learning/javascript", "web/development"],
    stats: [
      { tag: "FAV", value: "JAVA", color: "#ffffff" },
      { tag: "FAV", value: "JS",  color: "#d92323" },
    ],
  },
];

export default function AboutMe() {
  const [active, setActive]   = useState(0);
  const [mounted, setMounted] = useState(false);
  const isFirstRenderAudio = useRef(true);
  const [revealed, setRevealed] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const t = setTimeout(() => setMounted(true), 60);
    return () => clearTimeout(t);
  }, []);

  useEffect(() => {
    if (isFirstRenderAudio.current) {
      isFirstRenderAudio.current = false;
      return;
    }
    playSelectSound();
  }, [active]);

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === "ArrowUp") setActive(i => Math.max(0, i - 1));
      if (e.key === "ArrowDown") setActive(i => Math.min(ITEMS.length - 1, i + 1));
      if (e.key === "Enter") setRevealed(true);
      if (e.key === "ArrowRight") setRevealed(true);
      if (e.key === "ArrowLeft") {
        if (revealed) setRevealed(false);
        else navigate(-1);
      }
      if (e.key === "Escape" || e.key === "Backspace") navigate(-1);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [active, navigate, revealed]);

  return (
    <div id="menu-screen">
      {/* <video src={bgVideo} autoPlay loop muted playsInline /> */}
      {revealed && <div key={`dim-${active}`} className="sc-dim" />}
      {revealed && (
        <div key={`panel-${active}`} className={`sc-reveal-panel${mounted ? " mounted" : ""}`}>
          <div className="sc-reveal-upper-bar">
            {REVEAL_CONTENT[active].upper.map((line) => (
              <div className="sc-reveal-upper-line" key={line}>{line}</div>
            ))}
          </div>
          <div className="sc-reveal-lower-bar">{REVEAL_CONTENT[active].lower}</div>
        </div>
      )}
      {revealed && (
        <div key={`nav-${active}`} className="sc-right-nav">
          <span className="sc-nav-arrow left">◄</span>
          <span className="sc-nav-btn">LB</span>
          <span className="sc-nav-dot" />
          <span className="sc-nav-btn">RB</span>
          <span className="sc-nav-arrow right">►</span>
        </div>
      )}
      {revealed && (
        <div key={`portrait-${active}`} className={`sc-main-portrait-shell${mounted ? " mounted" : ""}`}>
          <img
            className="sc-main-portrait"
            src={MAIN_IMAGES[active]}
            alt=""
          />
        </div>
      )}
      <style>{`
        .sc-root {
          position: absolute;
          inset: 0;
          z-index: 6;
          pointer-events: none;
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          justify-content: center;
          gap: 6px;
          padding-left: 0;
        }

        .sc-dim {
          position: absolute;
          inset: 0;
          z-index: 12;
          background: rgba(13,13,13,0.68);
          pointer-events: none;
          animation: sc-dim-in 0.32s ease-out;
        }

        @keyframes sc-dim-in {
          from {
            opacity: 0;
          }
          to {
            opacity: 1;
          }
        }

        @keyframes sc-reveal-bar-in {
          0% {
            opacity: 0;
            transform: translateX(-120px) rotate(-20deg) scaleX(0.72);
          }
          60% {
            opacity: 0.96;
            transform: translateX(18px) rotate(-20deg) scaleX(1.03);
          }
          100% {
            opacity: 0.92;
            transform: translateX(0) rotate(-20deg) scaleX(1);
          }
        }

        @keyframes sc-portrait-in {
          0% {
            opacity: 0;
            transform: translateX(78px) skewX(-8deg) scale(0.94);
            filter: blur(8px);
          }
          55% {
            opacity: 0.96;
            transform: translateX(-8px) skewX(-8deg) scale(1.015);
            filter: blur(0);
          }
          100% {
            opacity: 1;
            transform: translateX(0) skewX(-8deg) scale(1);
            filter: blur(0);
          }
        }

        @keyframes sc-arrow-left {
          0%, 100% { transform: translateX(0); opacity: 1; }
          50% { transform: translateX(-5px); opacity: 0.4; }
        }

        @keyframes sc-arrow-right {
          0%, 100% { transform: translateX(0); opacity: 1; }
          50% { transform: translateX(5px); opacity: 0.4; }
        }

        .sc-main-portrait-shell {
          position: absolute;
          top: 0;
          right: -3vw;
          z-index: 13;
          pointer-events: none;
          width: 43vw;
          height: 100vh;
          overflow: hidden;
          opacity: 0;
          transform: translateX(24px) skewX(-8deg) scale(0.98);
          transition: opacity 0.35s ease, transform 0.35s ease;
        }
        .sc-main-portrait-shell.mounted {
          opacity: 0.30;
          transform: translateX(0) skewX(-8deg) scale(1);
          animation: sc-portrait-in 0.5s cubic-bezier(0.22, 1, 0.36, 1);
        }

        .sc-reveal-panel {
          position: absolute;
          top: 44vh;
          left: -6vw;
          width: 88vw;
          height: 60vh;
          z-index: 12;
          pointer-events: none;
          background:
            linear-gradient(180deg, rgba(255,255,255,0.98) 0%, rgba(255,255,255,0.98) 100%);
          clip-path: polygon(0 0, 100% 0, calc(100% - 88px) 100%, 0 100%);
          box-shadow:
            0 0 0 2px rgba(255,255,255,0.18),
            18px 0 0 rgba(217,35,35,0.82),
            28px 0 0 rgba(255,255,255,0.26);
          opacity: 0;
          transform: translateX(-40px) rotate(-20deg);
          transform-origin: left bottom;
          transition: opacity 0.3s ease, transform 0.35s ease;
        }
        .sc-reveal-panel.mounted {
          opacity: 0.92;
          transform: translateX(0) rotate(-20deg);
          animation: sc-reveal-bar-in 0.46s cubic-bezier(0.22, 1, 0.36, 1);
        }
        .sc-reveal-panel::before {
          content: "";
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 8px;
          background: linear-gradient(180deg, #d92323 0%, #d92323 100%);
          clip-path: inherit;
        }
        .sc-reveal-upper-bar {
          position: absolute;
          top: 10%;
          left: 0%;
          width: 100%;
          height: 40%;
          background: rgba(13,13,13,0.92);
          clip-path: polygon(0 0, 100% 0, calc(100% - 22px) 100%, 0 100%);
          box-shadow: 0 0 0 1px rgba(255,255,255,0.06);
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 10px;
          color: #ffffff;
          text-align: center;
        }
        .sc-reveal-upper-line {
          font-family: 'Persona5Main';
          font-weight: 300;
          font-size: 20px;
          letter-spacing: 0.5px;
          line-height: 1.15;
        }
        .sc-reveal-lower-bar {
          position: absolute;
          top: 58%;
          right: 0;
          width: 48%;
          height: 20%;
          background: rgba(13,13,13,0.92);
          clip-path: polygon(0 0, 100% 0, calc(100% - 22px) 100%, 0 100%);
          box-shadow: 0 0 0 1px rgba(255,255,255,0.06);
          display: flex;
          align-items: center;
          justify-content: flex-start;
          color: #ffffff;
          font-family: 'Bebas Neue';
          font-weight: 400;
          font-size: 22px;
          letter-spacing: 0px;
          text-transform: lowercase;
          padding-left: 22px;
        }

        @keyframes sc-right-nav-pop {
          0%   { opacity: 0; transform: scale(0.55) translateY(-10px); }
          65%  { opacity: 1; transform: scale(1.1) translateY(2px); }
          100% { opacity: 1; transform: scale(1) translateY(0); }
        }
        .sc-right-nav {
          position: absolute;
          top: 10vh;
          left: 6vw;
          display: flex;
          align-items: center;
          gap: 6px;
          pointer-events: none;
          z-index: 14;
          transform: translateX(-40px) rotate(-20deg);
          transform-origin: left bottom;
          animation: sc-right-nav-pop 0.38s cubic-bezier(0.22,1,0.36,1) both;
        }
        .sc-right-nav .sc-nav-btn {
          font-family: 'Persona5Main';
          font-size: 100px;
          letter-spacing: 3px;
          line-height: 1;
          user-select: none;
          color: #ffffff;
          -webkit-text-stroke: 2px #0d0d0d;
          paint-order: stroke fill;
          background: none;
          border: none;
          padding: 0 6px;
        }
        .sc-right-nav .sc-nav-dot {
          width: 16px;
          height: 16px;
          border-radius: 999px;
          background: #111;
          margin: 0 10px;
          flex-shrink: 0;
        }
        .sc-right-nav .sc-nav-arrow {
          font-family: 'Persona5Main';
          font-size: 22px;
          color: #d92323;
          display: inline-block;
          user-select: none;
        }
        .sc-right-nav .sc-nav-arrow.left  { animation: sc-arrow-left  0.8s ease-in-out infinite; }
        .sc-right-nav .sc-nav-arrow.right { animation: sc-arrow-right 0.8s ease-in-out infinite; }

        .sc-main-portrait {
          width: 100%;
          height: 100%;
          object-fit: cover;
          object-position: top right;
          transform: skewX(8deg) scale(1.08);
          transform-origin: top right;
        }

        /* ── Each bar ── */
        .sc-bar {
          position: relative;
          width: 45vw;
          height: 64px;
          transition: height 0.3s cubic-bezier(0.22,1,0.36,1);
          background: #111;
          cursor: pointer;
          pointer-events: all;
          clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
          box-shadow: 0 6px 24px rgba(13,13,13,0.65);
          z-index: 1;
        }

        /* wrapper holds both the red underlay and the bar */
        .sc-bar-outer {
          position: relative;
          flex-shrink: 0;
          transform: translateX(-100%);
          transition: transform 0.55s cubic-bezier(0.22, 1, 0.36, 1);
        }
        .sc-bar-outer.active .sc-bar     { height: 90px; }
        .sc-bar-outer.active .sc-bar-red { height: 90px; }
        .sc-bar-outer.mounted { transform: translateX(0); }
        .sc-bar-outer:nth-child(1) { transition-delay: 0ms; }
        .sc-bar-outer:nth-child(2) { transition-delay: 80ms; }
        .sc-bar-outer:nth-child(3) { transition-delay: 160ms; }

        /* red underlay — peeks out below the bar when active */
        .sc-bar-red {
          position: absolute;
          top: 0; left: 0;
          width: 45vw;
          height: 64px;
          background: #d92323;
          clip-path: polygon(50% 0, 100% 0, 100% 100%, calc(50% - 10px) 100%);
          transform: translateY(-7px);
          opacity: 0;
          transition: opacity 0.2s ease;
          z-index: 0;
          pointer-events: none;
        }
        .sc-bar-outer.active .sc-bar-red { opacity: 1; }

        /* white fill — skewed parallelogram on the right 25% */
        .sc-bar-fill {
          position: absolute;
          inset: 0;
          width: 100%;
          background: #ffffff;
          clip-path: polygon(100% 0, 100% 0, calc(100% - 32px) 100%, calc(100% - 32px) 100%);
          transition: clip-path 0.35s cubic-bezier(0.22, 1, 0.36, 1);
          z-index: 0;
        }
        .sc-bar-outer.active .sc-bar-fill {
          clip-path: polygon(22% 0, 100% 0, calc(100% - 14px) 100%, calc(22% + 138px) 100%);
        }

        /* shade on the left edge of the white fill */
        .sc-bar-shade {
          position: absolute;
          top: 0; bottom: 0;
          left: 73%;
          width: 6%;
          background: linear-gradient(90deg, rgba(13,13,13,0.15) 0%, rgba(13,13,13,0) 100%);
          z-index: 1;
          pointer-events: none;
          opacity: 0;
          transition: opacity 0.35s ease;
        }
        .sc-bar-outer.active .sc-bar-shade { opacity: 1; }

        /* bottom shadow line under each bar */
        .sc-bar::after {
          content: '';
          position: absolute;
          bottom: 0; left: 0; right: 0;
          height: 6px;
          background: linear-gradient(180deg, rgba(13,13,13,0) 0%, rgba(13,13,13,0.55) 100%);
          z-index: 10;
          pointer-events: none;
        }

        /* content layout inside each bar */
        .sc-bar-content {
          position: relative;
          z-index: 2;
          height: 100%;
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: 0 20px 0 20px;
        }

        /* left: role label */
        .sc-role {
          display: flex;
          align-items: center;
          flex-shrink: 0;
          font-family: 'Persona5Main';
          font-size: 50px;
          letter-spacing: -2px;
          color: #ffffff;
          transform: rotate(-30deg);
          user-select: none;
          line-height: 1;
          padding: 0 16px 0 8px;
        }

        /* left: icon + name centered in remaining space */
        .sc-main {
          flex: 1;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 3px;
          padding-left: 78px;
        }
        .sc-main-top {
          display: flex;
          align-items: center;
          gap: 12px;
        }

        .sc-icon {
          font-family: 'Persona5Main';
          font-size: 22px;
          width: 32px;
          text-align: center;
          flex-shrink: 0;
          color: rgba(255,255,255,0.15);
          transition: color 0.2s ease;
          user-select: none;
        }
        .sc-bar-outer.active .sc-icon { color: rgba(255,255,255,0.25); }

        .sc-label {
          font-family: 'Persona5Main';
          font-size: 28px;
          letter-spacing: 4px;
          line-height: 1;
          color: rgba(255,255,255,0.85);
          transition: color 0.2s ease;
          user-select: none;
        }
        .sc-bar-outer.active .sc-label { color: #0d0d0d; }

        /* right: stats group */
        .sc-stats {
          display: flex;
          align-items: center;
          gap: 10px;
          padding-right: 24px;
          flex-shrink: 0;
        }

        .sc-stat {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
        }

        .sc-stat-top {
          display: flex;
          align-items: baseline;
          gap: 4px;
        }

        .sc-stat-tag {
          font-family: 'Persona5Main';
          font-size: 9px;
          letter-spacing: 1.5px;
          padding: 1px 4px;
          border-width: 1px;
          border-style: solid;
          line-height: 1.4;
          user-select: none;
        }

        .sc-stat-num {
          font-family: 'Persona5Main';
          font-size: 26px;
          font-style: italic;
          line-height: 1;
          color: #ffffff;
          letter-spacing: 1px;
          user-select: none;
          transition: color 0.2s ease;
        }
        .sc-bar-outer.active .sc-stat-num { color: #0d0d0d; }

        .sc-stat-bars {
          width: 100%;
          display: flex;
          flex-direction: column;
          gap: 1px;
          margin-top: 2px;
        }
        .sc-stat-bar-color {
          height: 3px;
          width: 100%;
        }
        .sc-stat-bar-black {
          height: 2px;
          width: 100%;
          background: #0d0d0d;
        }

        /* character portrait */
        .sc-char {
          position: absolute;
          top: 0;
          left: 110px;
          height: 100%;
          width: auto;
          max-width: 160px;
          object-fit: cover;
          object-position: top;
          pointer-events: none;
          z-index: 3;
          clip-path: polygon(20px 0%, 100% 0%, calc(100% - 20px) 100%, 0% 100%);
        }

        /* footer hints */
        .sc-footer {
          position: fixed;
          bottom: 20px; right: 28px;
          display: flex; flex-direction: column;
          align-items: flex-end; gap: 5px;
          font-family: 'Persona5Main';
          z-index: 14;
          opacity: 0;
          transition: opacity 0.4s ease 0.6s;
        }
        .sc-footer.mounted { opacity: 1; }
        .sc-footer-row {
          display: flex; align-items: center; gap: 8px;
          font-size: 13px; letter-spacing: 2px;
          color: rgba(255,255,255,0.22);
        }
        .sc-footer-key {
          border: 1px solid rgba(255,255,255,0.15);
          border-radius: 3px;
          padding: 1px 6px; font-size: 11px;
        }
      `}</style>

      <div className="sc-root" role="navigation">
        {ITEMS.map((item, i) => (
          <div
            key={item.id}
            className={`sc-bar-outer${active === i ? " active" : ""}${mounted ? " mounted" : ""}`}
            onClick={() => {
              setActive(i);
            }}
            onMouseEnter={() => {
              setActive(i);
            }}
          >
            <div className="sc-bar-red" />
            <div className="sc-bar">
              <img className="sc-char" src={CHARS[i]} alt="" />
              <div className="sc-bar-fill" />
              <div className="sc-bar-shade" />
              <div className="sc-bar-content">
                <div className="sc-main">
                  <div className="sc-main-top">
                    <div className="sc-label">{item.label}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className={`sc-footer${mounted ? " mounted" : ""}`}>
        <div className="sc-footer-row"><span className="sc-footer-key">↑↓</span><span>SELECT</span></div>
        <div className="sc-footer-row"><span className="sc-footer-key">↵</span><span>REVEAL</span></div>
        <div className="sc-footer-row"><span className="sc-footer-key">ESC</span><span>BACK</span></div>
      </div>
    </div>
  );
}

````

## App.css

Ruta: `PruebasMenu/persona5-website-theme/src/App.css` · Bytes: 2171 · SHA-256: `f0d68f89896d4ae891ef44f6c77096499383d9f2a44223b00de39966d27dc12c`

````text
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: #0d0d0d;
  overflow: hidden;
  font-family: 'Persona5Main';
}

.site-bg-video {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
  pointer-events: none;
}

.site-content-layer {
  position: relative;
  z-index: 1;
}

#menu-screen {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}

#menu-screen video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

#main {
  width: 100vw;
  height: 100vh;
}

.bgm-panel {
  position: fixed;
  left: 20px;
  bottom: 20px;
  z-index: 120;
  display: flex;
  align-items: center;
  gap: 0; 
  background: rgba(13,13,13,0.82);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 8px 10px;
  clip-path: polygon(0 0, 100% 0, calc(100% - 10px) 100%, 0 100%);
  backdrop-filter: blur(2px);
  transition: gap 0.35s cubic-bezier(0.22, 1, 0.36, 1);
}

.bgm-panel:hover,
.bgm-panel:focus-within {
  gap: 10px; 
}

.bgm-toggle {
  border: 1px solid rgba(255, 255, 255, 0.45);
  background: rgba(13,13,13,0.86);
  color: #ffffff;
  padding: 8px 10px;
  min-width: 84px;
  font-size: 13px;
  letter-spacing: 1.2px;
  font-weight: 700;
  cursor: pointer;
  clip-path: polygon(0 0, 100% 0, calc(100% - 8px) 100%, 0 100%);
  transition: transform 0.15s ease, background 0.2s ease, color 0.2s ease;
}

.bgm-toggle:hover {
  transform: translateY(-1px);
}

.bgm-toggle.on {
  background: rgba(217,35,35,0.94);
  color: #ffffff;
}

.bgm-slider {
  width: 100%;
  accent-color: #d92323;
  cursor: pointer;
}

.bgm-slider-wrap {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  border: 1px solid rgba(255,255,255,0.4);
  background: rgba(13,13,13,0.8);
  clip-path: polygon(0 0, 100% 0, calc(100% - 8px) 100%, 0 100%);
  
  max-width: 0;
  padding: 0;
  border-width: 0;
  opacity: 0;
  overflow: hidden;
  white-space: nowrap;
  transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1);
}

.bgm-panel:hover .bgm-slider-wrap,
.bgm-panel:focus-within .bgm-slider-wrap {
  max-width: 200px;
  padding: 6px 8px;
  border-width: 1px;
  opacity: 1;
}

````

## App.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/App.jsx` · Bytes: 6371 · SHA-256: `f96c8147a9fd4dd40f895298698283420b79fdc18e484456e70419a8cec69d7d`

````text
import { useEffect, useRef, useState } from 'react'
import { Routes, Route, useLocation, useNavigate } from 'react-router-dom'
import { AnimatePresence } from 'framer-motion'
import P5Menu from './P5Menu'
import ResumePage from './ResumePage'
import PageTransition from './PageTransition'
import Socials from './Socials'
import AboutMe from './AboutMe'
import SideProjectsPage from './SideProjectsPage'
import mainVideo from './assets/main1.mp4'
import './App.css'

const BGM_STATE_KEY = 'p5-bgm-enabled'
const BGM_VOLUME_KEY = 'p5-bgm-volume'
const DEFAULT_VOLUME = 0.45
const FADE_MS = 450

function BackgroundMusic() {
  const audioRef = useRef(null)
  const fadeRafRef = useRef(null)
  const autoStartRef = useRef(false)
  const [isPlaying, setIsPlaying] = useState(false)
  const [volume, setVolume] = useState(() => {
    const saved = Number(localStorage.getItem(BGM_VOLUME_KEY))
    if (Number.isFinite(saved)) return Math.min(1, Math.max(0, saved))
    return DEFAULT_VOLUME
  })

  const stopFade = () => {
    if (fadeRafRef.current) {
      cancelAnimationFrame(fadeRafRef.current)
      fadeRafRef.current = null
    }
  }

  const fadeTo = (target, done) => {
    const audio = audioRef.current
    if (!audio) return

    stopFade()
    const start = audio.volume
    const diff = target - start
    const begin = performance.now()

    const tick = (now) => {
      const p = Math.min(1, (now - begin) / FADE_MS)
      audio.volume = start + diff * p
      if (p < 1) {
        fadeRafRef.current = requestAnimationFrame(tick)
        return
      }
      fadeRafRef.current = null
      if (done) done()
    }

    fadeRafRef.current = requestAnimationFrame(tick)
  }

  const startMusic = async () => {
    const audio = audioRef.current
    if (!audio) return

    stopFade()
    audio.volume = 0

    try {
      await audio.play()
      fadeTo(volume)
      setIsPlaying(true)
      autoStartRef.current = false
    } catch {
      setIsPlaying(false)
    }
  }

  const stopMusic = () => {
    const audio = audioRef.current
    if (!audio) return

    fadeTo(0, () => {
      audio.pause()
      audio.currentTime = 0
      setIsPlaying(false)
    })
  }

  const toggleMusic = async () => {
    if (isPlaying) {
      stopMusic()
      return
    }

    await startMusic()
  }

  const onVolumeChange = (e) => {
    const next = Number(e.target.value)
    setVolume(next)
  }

  useEffect(() => {
    const audio = audioRef.current
    if (!audio) return
    if (isPlaying) audio.volume = volume
    localStorage.setItem(BGM_VOLUME_KEY, String(volume))
  }, [volume, isPlaying])

  useEffect(() => {
    localStorage.setItem(BGM_STATE_KEY, isPlaying ? '1' : '0')
  }, [isPlaying])

  useEffect(() => {
    const shouldAutoStart = localStorage.getItem(BGM_STATE_KEY) === '1'
    if (!shouldAutoStart) return

    autoStartRef.current = true
    const tryAutoplay = async () => {
      if (!autoStartRef.current) return
      await startMusic()
    }

    const unlock = async () => {
      if (!autoStartRef.current) return
      await tryAutoplay()
    }

    window.addEventListener('pointerdown', unlock, { once: true })
    window.addEventListener('keydown', unlock, { once: true })
    return () => {
      window.removeEventListener('pointerdown', unlock)
      window.removeEventListener('keydown', unlock)
    }
  }, [])

  useEffect(() => () => stopFade(), [])

  return (
    <div className="bgm-panel">
      <audio ref={audioRef} loop preload="none" src="/audio/background.mp3" />
      <button
        className={`bgm-toggle${isPlaying ? ' on' : ''}`}
        type="button"
        onClick={(e) => {
          toggleMusic()
          e.currentTarget.blur()
        }}
        aria-label={isPlaying ? 'Disable background music' : 'Enable background music'}
      >
        {isPlaying ? 'BGM ON' : 'BGM OFF'}
      </button>

      <div className="bgm-slider-wrap" aria-label="Background music volume">
        <span className="bgm-slider-label">VOL</span>
        <input
          className="bgm-slider"
          type="range"
          min="0"
          max="1"
          step="0.01"
          value={volume}
          onChange={onVolumeChange}
          onKeyDown={(e) => {
            if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
              e.preventDefault()
            }
          }}
        />
        <span className="bgm-slider-value">{Math.round(volume * 100)}</span>
      </div>
    </div>
  )
}

function MenuScreen() {
  const navigate = useNavigate()

  const handleNavigate = (page) => {
    if (page === 'github') {
      window.open('https://github.com/ffaneto', '_blank', 'noopener,noreferrer')
      return
    }
    navigate(`/${page}`)
  }

  return (
    <div id="menu-screen">
      {/* <video src={menuVideo} autoPlay loop muted playsInline /> */}
      <P5Menu onNavigate={handleNavigate} />
    </div>
  )
}

function SiteBackgroundVideo() {
  return (
    <video
      className="site-bg-video"
      src={mainVideo}
      autoPlay
      loop
      muted
      playsInline
      preload="auto"
      aria-hidden="true"
    />
  )
}

function AnimatedRoutes() {
  const location = useLocation()
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/" element={
          <PageTransition><MenuScreen /></PageTransition>
        } />
        <Route path="/about" element={
          <PageTransition variant="about"><AboutMe /></PageTransition>
        } />
        <Route path="/resume" element={
          <PageTransition><ResumePage /></PageTransition>
        } />
        <Route path="/socials" element={
          <PageTransition variant="socials"><Socials /></PageTransition>
        } />
        <Route path="/sideproj" element={
          <PageTransition><SideProjectsPage /></PageTransition>
        } />
      </Routes>
    </AnimatePresence>
  )
}

export default function App() {
  return (
    <>
      <SiteBackgroundVideo />
      <div className="site-content-layer">
        <AnimatedRoutes />
      </div>
      <BackgroundMusic />
    </>
  )
}

````

## FontPreview.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/FontPreview.jsx` · Bytes: 1595 · SHA-256: `507e4e1649e16b2d0865eff9e0672984df91f624f49e61f23cf163917d01e1d8`

````text
const FONTS = [
  { name: "Persona5Main", family: "'Persona5Main'" },
];

const LABELS = ["ABOUT ME", "RESUME", "GITHUB LINK", "SOCIALS", "SIDE PROJECTS"];
const SIZES  = [54, 44, 36, 44, 36];
const SKEWS  = [-6, -11, -16, -3, -4];

export default function FontPreview() {
  return (
    <div style={{
      display: 'flex',
      width: '100vw',
      minHeight: '100vh',
      background: '#0d0d0d',
      overflowX: 'auto',
    }}>
      {FONTS.map(font => (
        <div key={font.name} style={{
          flex: '1 0 0',
          minWidth: 220,
          borderRight: '1px solid rgba(255,255,255,0.08)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'flex-start',
          justifyContent: 'center',
          padding: '32px 24px',
          gap: 4,
        }}>
          <div style={{
            fontFamily: "'Persona5Main'",
            fontSize: 11,
            color: '#d92323',
            letterSpacing: 3,
            marginBottom: 20,
            textTransform: 'uppercase',
          }}>
            {font.name}
          </div>
          {LABELS.map((label, i) => (
            <span key={label} style={{
              fontFamily: font.family,
              fontStyle: 'italic',
              fontSize: SIZES[i],
              color: '#ffffff',
              letterSpacing: 1,
              lineHeight: 0.9,
              display: 'block',
              transform: `skewX(${SKEWS[i]}deg)`,
              whiteSpace: 'nowrap',
            }}>
              {label}
            </span>
          ))}
        </div>
      ))}
    </div>
  );
}

````

## P5Menu.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/P5Menu.jsx` · Bytes: 11756 · SHA-256: `fdcc8304e34aebe283cbfba3bf0ffe63b770a19c98c66fe886f5b4fd6c34fc3c`

````text
import { useState, useEffect, useRef } from "react";
import { playSelectSound } from "./utils/audio.js";

const ITEMS = [
  { id: "about",   label: "ABOUT ME",      page: "about",   fontSize: 64, offsetX: 0,  offsetY: 0,  skew: -6,  skewY: 10  },
  { id: "resume",  label: "RESUME",        page: "resume",  fontSize: 52, offsetX: 24, offsetY: 50,  skew: -11, skewY: -10 },
  { id: "github",  label: "GITHUB LINK",   page: "github",  fontSize: 54, offsetX: 10, offsetY: 28,  skew: 0, skewY: -4  },
  { id: "socials", label: "SOCIALS",       page: "socials", fontSize: 59, offsetX: 19, offsetY: 30,  skew: -3,  skewY: 5   },
  { id: "sideproj",label: "SIDE PROJECTS", page: "sideproj",fontSize: 45, offsetX: 12, offsetY: 28,  skew: -4,  skewY: 7   },
];

const CLIP_SHAPES = [
  () => "polygon(0% 44%, 24% 6%, 82% 0%, 100% 36%, 82% 100%, 18% 94%)",
  () => "polygon(0% 44%, 24% 6%, 82% 0%, 100% 36%, 82% 100%, 18% 94%)",
  () => "polygon(0% 44%, 24% 6%, 82% 0%, 100% 36%, 82% 100%, 18% 94%)",
  () => "polygon(0% 44%, 24% 6%, 82% 0%, 100% 36%, 82% 100%, 18% 94%)",
  () => "polygon(0% 44%, 24% 6%, 82% 0%, 100% 36%, 82% 100%, 18% 94%)",
];

export default function P5Menu({ onNavigate }) {
  const [active, setActive] = useState(() => {
    const saved = sessionStorage.getItem('p5-menu-active');
    return saved ? parseInt(saved, 10) : 0;
  });
  const [mounted, setMounted] = useState(false);
  const isFirstRenderAudio = useRef(true);
  const [animKey, setAnimKey] = useState(0);

  const activate = (idx) => {
    setActive(idx);
    setAnimKey(k => k + 1);
  };

  useEffect(() => {
    if (isFirstRenderAudio.current) {
      isFirstRenderAudio.current = false;
      return;
    }
    sessionStorage.setItem('p5-menu-active', active);
    playSelectSound();
  }, [active]);

  useEffect(() => {
    const t = setTimeout(() => setMounted(true), 1000);
    return () => clearTimeout(t);
  }, []);

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === "ArrowUp")   activate(Math.max(0, active - 1));
      if (e.key === "ArrowDown") activate(Math.min(ITEMS.length - 1, active + 1));
      if (e.key === "Enter") {
        onNavigate?.(ITEMS[active].page);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [active]);

  return (
    <>
      <style>{`
        .p5-overlay {
          position: absolute;
          inset: 0;
          z-index: 10;
          display: flex;
          align-items: center;
          justify-content: center;
          pointer-events: none;
        }

        .p5-stripe  { position:absolute; right:0; top:0; bottom:0; width:5px; background:#ffffff; z-index:10; pointer-events:none; }
        .p5-stripe2 { position:absolute; right:9px; top:0; bottom:0; width:2px; background:rgba(255,255,255,0.22); z-index:10; pointer-events:none; }

        .p5-menu {
          position: relative;
          z-index: 20;
          padding: 48px;
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 30px;
          pointer-events: all;
        }

        .p5-row {
          position: relative;
          cursor: pointer;
          display: flex;
          align-items: center;
          justify-content: center;
          line-height: 1;
          text-decoration: none;
          opacity: 0;
          transform: translateX(36px);
          transition: opacity 0.38s ease, transform 0.38s cubic-bezier(0.22,1,0.36,1);
        }
        .p5-row.mounted {
          opacity: 1 !important;
          transform: translateX(0) !important;
        }

        .p5-glow {
          position: absolute;
          top: 50%; left: 50%;
          transform: translate(-50%, -50%);
          width: 120%; height: 200%;
          background: radial-gradient(ellipse at center, rgba(255,255,255,0.35) 0%, transparent 70%);
          filter: blur(18px);
          z-index: 0;
          pointer-events: none;
          opacity: 0;
          transition: opacity 0.3s ease;
        }
        .p5-row.active .p5-glow { opacity: 1; }

        .p5-skew-wrap {
          position: relative;
          display: flex;
          align-items: center;
          isolation: isolate;
        }

        @keyframes p5-shadow-pop {
          0%   { transform: translateY(-40%) translateX(-12px) scaleX(0) scaleY(1); }
          55%  { transform: translateY(-46%) translateX(-15px) scaleX(1.22) scaleY(1.18); }
          75%  { transform: translateY(-39%) translateX(-11px) scaleX(0.96) scaleY(0.97); }
          100% { transform: translateY(-40%) translateX(-12px) scaleX(1) scaleY(1); }
        }

        @keyframes p5-wiggle-poly {
          0%   { clip-path: polygon(0% 56%, 16% 0%, 76% 7%, 100% 24%, 94% 100%, 8% 88%); }
          25%  { clip-path: polygon(0% 62%, 12% 6%, 84% 0%, 100% 34%, 88% 100%, 2% 94%); }
          50%  { clip-path: polygon(0% 40%, 28% 10%, 72% 0%, 100% 44%, 98% 92%, 14% 100%); }
          75%  { clip-path: polygon(0% 52%, 22% 0%, 80% 12%, 100% 28%, 90% 100%, 6% 82%); }
          100% { clip-path: polygon(0% 56%, 16% 0%, 76% 7%, 100% 24%, 94% 100%, 8% 88%); }
        }

        .p5-shadow-tri {
          position: absolute;
          top: 50%;
          transform-origin: left center;
          background: rgba(255,255,255,0.85);
          z-index: 1;
          pointer-events: none;
          transform: translateY(-40%) translateX(-12px) scaleX(0);
          transition: transform 0.18s ease;
        }
        .p5-shadow-tri.pop {
          animation: p5-shadow-pop 0.28s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
        }

        .p5-highlight {
          position: absolute;
          top: 50%;
          transform-origin: left center;
          background: #0dd9ff;
          z-index: 2;
          transition: transform 0.22s cubic-bezier(0.22,1,0.36,1);
          pointer-events: none;
        }
        .p5-row.active .p5-highlight {
          animation: p5-wiggle-poly 0.66s ease-in-out infinite;
        }

        .p5-label-wrap {
          position: relative;
          z-index: 3;
        }

        .p5-label-base {
          font-family: 'Persona5Main';
          font-style: italic;
          letter-spacing: 0.6px;
          line-height: 0.85;
          display: block;
          white-space: nowrap;
          user-select: none;
          color: #ffffff;
          -webkit-text-stroke: 18.2px rgba(0, 0, 0, 0.8);
          paint-order: stroke fill;
        }

        .p5-label-dark {
          color: #f6f3f3;
          transition: color 0.12s ease;
        }
        .p5-row.active .p5-label-dark { color: #ffffff; }
        .p5-row:hover:not(.active) .p5-label-dark { color: #ffffff; }

        .p5-label-bright {
          color: #1a1a1a;
          -webkit-text-stroke: 18.2px rgba(255, 255, 255, 0.9);
          position: absolute;
          inset: 0;
          z-index: 1;
          opacity: 0;
          transition: opacity 0.12s ease;
        }
        .p5-row.active .p5-label-bright { opacity: 1; }

        .p5-hint {
          position: absolute;
          bottom: 24px; right: 28px;
          z-index: 20;
          display: flex; flex-direction: column;
          align-items: flex-end; gap: 5px;
          font-family: 'Persona5Main';
          opacity: 0;
          transition: opacity 0.5s ease 0.9s;
        }
        .p5-hint.mounted { opacity: 1; }
        .p5-hint-row {
          display: flex; align-items: center; gap: 8px;
          font-size: 13px; letter-spacing: 2px;
          color: rgba(255,255,255,0.28);
        }
        .p5-hint-key {
          border: 1px solid rgba(255,255,255,0.2);
          border-radius: 3px;
          padding: 1px 6px; font-size: 11px;
        }

        .p5-name-tag {
          position: absolute;
          top: 18px;
          left: 40px;
          z-index: 20;
          font-family: 'Persona5Main';
          font-style: italic;
          font-size: 65px;
          line-height: 0.88;
          letter-spacing: 2px;
          color: #ffffff;
          transform: rotate(18deg);
          transform-origin: left top;
          user-select: none;
          pointer-events: none;
          display: flex;
          flex-direction: column;
          align-items: flex-start;
        }
        .p5-name-tag span:first-child {
          color: #ffffff;
        }
      `}</style>

      <div className="p5-overlay">
        <div className="p5-name-tag">
          <span>Francisco's</span>
          <span>persona</span>
        </div>

        <nav className="p5-menu">
          {ITEMS.map((item, i) => {
            const isActive = active === i;
            const dist = Math.abs(i - active);
            const opacity = isActive ? 1 : Math.max(0.5, 1 - dist * 0.2);
            const estW = item.label.length * item.fontSize * 0.6 + 80;
            const estH = item.fontSize * 0.94;
            const clipFn = CLIP_SHAPES[i] ?? CLIP_SHAPES[0];

            return (
              <a
                key={item.id}
                href="#"
                className={`p5-row ${isActive ? "active" : ""} ${mounted ? "mounted" : ""}`}
                style={{
                  marginRight: item.offsetX,
                  marginTop: item.offsetY,
                  transitionDelay: mounted ? `${i * 80}ms` : "0ms",
                }}
                onClick={(e) => { e.preventDefault(); onNavigate?.(item.page); }}
                onMouseEnter={() => activate(i)}
                aria-current={isActive ? "page" : undefined}
              >
                <div className="p5-glow" />
                <div
                  className="p5-skew-wrap"
                  style={{ transform: `skewX(${item.skew}deg) skewY(${item.skewY}deg)` }}
                >
                  <div
                    key={isActive ? `pop-${i}-${animKey}` : `idle-${i}`}
                    className={`p5-shadow-tri${isActive ? ' pop' : ''}`}
                    style={{
                      width: estW,
                      height: estH,
                      clipPath: clipFn(estW, estH),
                    }}
                  />
                  <div
                    className="p5-highlight"
                    style={{
                      width: estW,
                      height: estH,
                      clipPath: clipFn(estW, estH),
                      transform: `translateY(-50%) scaleX(${isActive ? 1 : 0})`,
                    }}
                  />
                  <div className="p5-label-wrap" style={{ opacity }}>
                    <span className="p5-label-base p5-label-dark" style={{ fontSize: item.fontSize }}>
                      {item.label}
                    </span>
                    <span
                      className="p5-label-base p5-label-bright"
                      style={{
                        fontSize: item.fontSize,
                        clipPath: clipFn(estW, estH),
                      }}
                    >
                      {item.label}
                    </span>
                  </div>
                </div>
              </a>
            );
          })}
        </nav>

        <div className={`p5-hint ${mounted ? "mounted" : ""}`}>
          <div className="p5-hint-row"><span className="p5-hint-key">↑↓</span><span>NAVIGATE</span></div>
          <div className="p5-hint-row"><span className="p5-hint-key">↵</span><span>CONFIRM</span></div>
        </div>
      </div>
    </>
  );
}

````

## PageTransition.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/PageTransition.jsx` · Bytes: 4757 · SHA-256: `b86a635837b14442ff644d7d5dcf80f26a5bac7c78a54780d0333c6a19ada924`

````text
import { motion, AnimatePresence } from "framer-motion";
import { useLocation } from "react-router-dom";
import { useEffect, useRef } from "react";
import { playSelectSound } from "./utils/audio.js";

function DefaultTransition() {
  const stripes = [
    { color: "#0d0d0d", left: "72vw", width: "24vw", delay: 0 },
    { color: "#d92323", left: "80vw", width: "14vw", delay: 0.06 },
    { color: "#ffffff", left: "88vw", width: "8vw", delay: 0.12 },
  ];

  return stripes.map((stripe, i) => (
    <motion.div
      key={i}
      style={{
        position: "fixed",
        top: "-6vh",
        left: stripe.left,
        width: stripe.width,
        height: "112vh",
        background: stripe.color,
        zIndex: 999 - i,
        transform: "skewX(-16deg)",
        transformOrigin: "top",
      }}
      initial={{ y: -1200, opacity: 1 }}
      animate={{ y: [-1200, 0, 0, 1200] }}
      transition={{
        duration: 0.56,
        delay: stripe.delay,
        times: [0, 0.42, 0.58, 1],
        ease: [0.76, 0, 0.24, 1],
      }}
    />
  ));
}

function AboutTransition() {
  const panels = [
    { color: "#0d0d0d", top: "-12vh", left: "-18vw", width: "86vw", delay: 0 },
    { color: "#ffffff", top: "24vh", left: "-10vw", width: "72vw", delay: 0.05 },
    { color: "#ffffff", top: "58vh", left: "-14vw", width: "82vw", delay: 0.1 },
  ];

  return panels.map((panel, i) => (
    <motion.div
      key={i}
      style={{
        position: "fixed",
        top: panel.top,
        left: panel.left,
        width: panel.width,
        height: "26vh",
        background: panel.color,
        zIndex: 999 - i,
        clipPath: "polygon(0 0, 100% 0, calc(100% - 120px) 100%, 0 100%)",
        transform: "rotate(-18deg)",
        transformOrigin: "left center",
      }}
      initial={{ x: -500, opacity: 0 }}
      animate={{ x: [-500, 20, 0], opacity: [1, 1, 0] }}
      transition={{
        duration: 0.52,
        delay: panel.delay,
        times: [0, 0.68, 1],
        ease: [0.22, 1, 0.36, 1],
      }}
    />
  ));
}

function SocialsTransition() {
  const stripes = [
    { color: "#0d0d0d", left: "72vw", width: "24vw", delay: 0 },
    { color: "#d92323", left: "80vw", width: "14vw", delay: 0.06 },
    { color: "#ffffff", left: "88vw", width: "8vw", delay: 0.12 },
  ];

  return stripes.map((stripe, i) => (
    <motion.div
      key={i}
      style={{
        position: "fixed",
        top: "-6vh",
        left: stripe.left,
        width: stripe.width,
        height: "112vh",
        background: stripe.color,
        zIndex: 999 - i,
        transform: "skewX(-16deg)",
        transformOrigin: "top",
      }}
      initial={{ y: -1200, opacity: 1 }}
      animate={{ y: [-1200, 0, 0, 1200] }}
      transition={{
        duration: 0.56,
        delay: stripe.delay,
        times: [0, 0.42, 0.58, 1],
        ease: [0.76, 0, 0.24, 1],
      }}
    />
  ));
}

function ResumeTransition() {
  const cards = [
    { top: "14vh", color: "#732424", delay: 0 },
    { top: "31vh", color: "#ffffff", delay: 0.05 },
    { top: "48vh", color: "#ffffff", delay: 0.1 },
    { top: "65vh", color: "#732424", delay: 0.15 },
  ];

  return cards.map((card, i) => (
    <motion.div
      key={i}
      style={{
        position: "fixed",
        left: "-6vw",
        top: card.top,
        width: "78vw",
        height: "14vh",
        background: card.color,
        zIndex: 999 - i,
        clipPath: "polygon(0 0, 97% 0, 100% 100%, 3% 100%)",
        boxShadow: card.color === "#ffffff" ? "10px 0 0 #d92323" : "none",
      }}
      initial={{ x: -900, opacity: 1 }}
      animate={{ x: [-900, 30, 0, 900] }}
      transition={{
        duration: 0.6,
        delay: card.delay,
        times: [0, 0.48, 0.7, 1],
        ease: [0.76, 0, 0.24, 1],
      }}
    />
  ));
}

function TransitionOverlay({ variant }) {
  if (variant === "about") return <AboutTransition />;
  if (variant === "resume") return <ResumeTransition />;
  if (variant === "socials") return <DefaultTransition />;
  return <DefaultTransition />;
}

export default function PageTransition({ children, variant = "default" }) {
  const location = useLocation();
  const selectSoundRef = useRef(null);

  useEffect(() => {
    playSelectSound();
  }, [location.pathname]);

  return (
    <>
      <AnimatePresence mode="wait">
        <motion.div key={location.pathname} style={{ position: "relative" }}>
          <TransitionOverlay variant={variant} />
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2, delay: 0.18 }}
          >
            {children}
          </motion.div>
        </motion.div>
      </AnimatePresence>
    </>
  );
}

````

## ResumePage.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/ResumePage.jsx` · Bytes: 14327 · SHA-256: `6bad91ec1ab2fc75e65500511c3f527315758fbfb6eacc78a6e6ff8b882a0e09`

````text
import { useEffect, useState, useRef } from "react";
import { playSelectSound } from "./utils/audio.js";
import { useNavigate } from "react-router-dom";
import mainVideo from "./assets/main1.mp4";

const ITEMS = [
  { id: "i", badge: "I", title: "EDUCATION", subtitle: "IFPB Itaporanga / IT Technician", rank: 3 },
  { id: "ii", badge: "II", title: "SKILLS", subtitle: "Java / JavaScript / Logic", rank: 4 },
  { id: "iii", badge: "III", title: "PROJECTS", subtitle: "Sales Mgmt / Calc / JS Exercises", rank: 4 },
  { id: "iv", badge: "IV", title: "FOCUS", subtitle: "Backend / Frontend", rank: 5 },
];

const EDUCATION_ROWS = [
  { index: "01", title: "IFPB Campus Itaporanga", status: "3rd Yr" },
  { index: "02", title: "IT Technician", status: "Active" },
  { index: "03", title: "Java + JavaScript", status: "Learning" },
  { index: "04", title: "Backend Practice", status: "Daily" },
];

export default function ResumePage() {
  const navigate = useNavigate();
  const [active, setActive] = useState(1);
  const [mounted, setMounted] = useState(false);
  const isFirstRenderAudio = useRef(true);

  useEffect(() => {
    if (isFirstRenderAudio.current) {
      isFirstRenderAudio.current = false;
      return;
    }
    playSelectSound();
  }, [active]);

  useEffect(() => {
    const t = setTimeout(() => setMounted(true), 80);
    return () => clearTimeout(t);
  }, []);

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === "ArrowUp") setActive((i) => Math.max(0, i - 1));
      if (e.key === "ArrowDown") setActive((i) => Math.min(ITEMS.length - 1, i + 1));
      if (e.key === "ArrowLeft") navigate(-1);
      if (e.key === "Escape" || e.key === "Backspace") navigate(-1);
    };

    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [navigate]);

  return (
    <div id="menu-screen">
      <div className="resume-entry-mask" aria-hidden="true">
        <video className="resume-entry-video" src={mainVideo} autoPlay loop muted playsInline />
      </div>
      <style>{`
        .resume-entry-mask {
          position: absolute;
          inset: 0;
          z-index: 9;
          overflow: hidden;
          background: #732424;
          clip-path: circle(0 at 50% 50%);
          animation: resume-entry-reveal 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
          pointer-events: none;
        }

        .resume-entry-video {
          position: absolute;
          inset: 0;
          width: 100%;
          height: 100%;
          object-fit: cover;
        }

        @keyframes resume-entry-reveal {
          from { clip-path: circle(0 at 50% 50%); }
          to { clip-path: circle(150vmax at 50% 50%); }
        }

        .resume-overlay {
          position: absolute;
          inset: 0;
          z-index: 10;
          pointer-events: none;
        }

        .resume-stack {
          position: absolute;
          top: 9vh;
          left: 2.8vw;
          width: min(52vw, 820px);
          display: flex;
          flex-direction: column;
          gap: 10px;
          pointer-events: none;
          transform: scale(0.9);
          transform-origin: top left;
        }

        .resume-list-tag {
          font-family: 'Persona5Main';
          font-size: 92px;
          line-height: 0.9;
          color: #ffffff;
          letter-spacing: 2px;
          margin: 0 0 6px 12px;
          text-shadow: 0 2px 0 rgba(13,13,13,0.18);
          opacity: 0;
          transform: translateX(-24px);
          transition: opacity 0.35s ease, transform 0.35s ease;
        }
        .resume-list-tag.mounted {
          opacity: 1;
          transform: translateX(0);
        }

        .resume-card-wrap {
          position: relative;
          opacity: 0;
          transform: translateX(-48px);
          transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.22, 1, 0.36, 1);
          pointer-events: all;
          cursor: pointer;
        }
        .resume-card-wrap.mounted {
          opacity: 1;
          transform: translateX(0);
        }

        .resume-card {
          position: relative;
          height: 112px;
          background: #0d0d0d;
          clip-path: polygon(0 0, 97% 0, 100% 100%, 3% 100%);
          box-shadow: 0 8px 0 rgba(13,13,13,0.85);
          transition: transform 0.22s ease, background 0.22s ease, box-shadow 0.22s ease;
          overflow: visible;
        }
        .resume-card-wrap.active .resume-card {
          background: #ffffff;
          box-shadow: 10px 8px 0 #d92323;
          transform: translateX(6px);
        }

        .resume-card-inner {
          position: absolute;
          inset: 0;
          padding: 14px 22px 14px 62px;
          display: flex;
          align-items: flex-start;
          justify-content: space-between;
          overflow: visible;
        }

        .resume-badge {
          position: absolute;
          top: 10px;
          left: -10px;
          width: 56px;
          height: 70px;
          background: #0d0d0d;
          border: 3px solid #ffffff;
          clip-path: polygon(14% 0, 100% 0, 84% 100%, 0 100%);
          display: flex;
          align-items: center;
          justify-content: center;
          transform: rotate(-8deg);
          box-shadow: 0 4px 0 rgba(13,13,13,0.28);
          transition: background 0.22s ease, border-color 0.22s ease;
        }
        .resume-badge-text {
          font-family: 'Persona5Main';
          font-size: 36px;
          color: #ffffff;
          letter-spacing: 1px;
          transform: rotate(8deg);
        }
        .resume-card-wrap.active .resume-badge {
          background: #0d0d0d;
          border-color: #0d0d0d;
        }
        .resume-card-wrap.active .resume-badge-text {
          color: #ffffff;
        }

        .resume-title {
          font-family: 'Persona5Main';
          font-size: 56px;
          line-height: 0.9;
          letter-spacing: 1px;
          color: #ffffff;
          transition: color 0.22s ease;
        }
        .resume-card-wrap.active .resume-title {
          color: #0d0d0d;
        }

        .resume-rank {
          display: flex;
          align-items: center;
          gap: 10px;
          margin-top: 2px;
          flex-shrink: 0;
        }
        .resume-rank-label {
          font-family: 'Persona5Main';
          font-size: 30px;
          letter-spacing: 2px;
          color: #ffffff;
          transition: color 0.22s ease;
        }
        .resume-rank-number {
          font-family: 'Persona5Main';
          font-size: 50px;
          line-height: 0.82;
          color: #ffffff;
          transition: color 0.22s ease;
        }
        .resume-card-wrap.active .resume-rank-label,
        .resume-card-wrap.active .resume-rank-number {
          color: #0d0d0d;
        }

        .resume-subtitle-bar {
          position: absolute;
          left: 64px;
          right: 14px;
          bottom: 12px;
          height: 34px;
          background: #ffffff;
          clip-path: polygon(0 0, 100% 0, calc(100% - 10px) 100%, 0 100%);
          display: flex;
          align-items: center;
          padding: 0 18px;
          transition: background 0.22s ease;
        }
        .resume-card-wrap.active .resume-subtitle-bar {
          background: #0d0d0d;
        }

        .resume-subtitle {
          font-family: 'Bebas Neue';
          font-size: 28px;
          line-height: 1;
          letter-spacing: 0px;
          color: #0d0d0d;
          transition: color 0.22s ease;
        }
        .resume-card-wrap.active .resume-subtitle {
          color: #ffffff;
        }

        .resume-detail-panel {
          position: absolute;
          top: 9.5vh;
          right: 3vw;
          width: min(44vw, 680px);
          min-height: 74vh;
          z-index: 12;
          padding: 22px 24px 24px 24px;
          background: linear-gradient(180deg, rgba(13,13,13,0.96) 0%, rgba(13,13,13,0.97) 100%);
          clip-path: polygon(0 0, 100% 0, calc(100% - 18px) 100%, 0 100%);
          box-shadow:
            inset 0 0 0 1px rgba(255,255,255,0.16),
            16px 16px 0 rgba(13,13,13,0.55);
          overflow: hidden;
        }
        .resume-detail-panel::before {
          content: "";
          position: absolute;
          inset: 0;
          background:
            linear-gradient(135deg, rgba(255,255,255,0.08) 0 15%, transparent 15% 100%),
            linear-gradient(180deg, rgba(255,255,255,0.05), transparent 24%);
          pointer-events: none;
        }
        .resume-detail-top {
          position: relative;
          display: grid;
          grid-template-columns: 70px 1fr auto;
          align-items: center;
          gap: 14px;
          min-height: 92px;
          padding: 0 18px;
          background: linear-gradient(90deg, #ffffff 0%, #ffffff 100%);
          clip-path: polygon(0 0, 100% 0, calc(100% - 16px) 100%, 0 100%);
          color: #0d0d0d;
          box-shadow: 10px 0 0 rgba(217,35,35,0.88);
        }
        .resume-detail-top-index {
          font-family: 'Persona5Main';
          font-size: 46px;
          line-height: 1;
        }
        .resume-detail-top-title {
          font-family: 'Persona5Main';
          font-size: 42px;
          line-height: 0.92;
          letter-spacing: 1px;
        }
        .resume-detail-top-progress {
          font-family: 'Persona5Main';
          font-size: 42px;
          letter-spacing: 2px;
          line-height: 1;
        }
        .resume-detail-list {
          position: relative;
          display: flex;
          flex-direction: column;
          gap: 10px;
          margin-top: 18px;
        }
        .resume-detail-row {
          display: grid;
          grid-template-columns: 50px 1fr auto;
          align-items: center;
          gap: 14px;
          min-height: 56px;
          padding: 0 14px;
          background: rgba(13,13,13,0.96);
          clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
          box-shadow: inset 0 0 0 1px rgba(255,255,255,0.12);
          transition: transform 0.16s ease, background 0.16s ease;
        }
        .resume-detail-row:hover {
          transform: translateX(4px);
          background: rgba(13,13,13,1);
        }
        .resume-detail-row-index {
          font-family: 'Bebas Neue';
          font-size: 26px;
          letter-spacing: 1px;
          color: #ffffff;
        }
        .resume-detail-row-title {
          font-family: 'Bebas Neue';
          font-size: 28px;
          line-height: 1;
          color: #ffffff;
        }
        .resume-detail-status {
          font-family: 'Bebas Neue';
          font-size: 22px;
          line-height: 1;
          letter-spacing: 1.1px;
          color: #0d0d0d;
          background: #ffffff;
          padding: 7px 12px;
          clip-path: polygon(0 0, 100% 0, calc(100% - 8px) 100%, 0 100%);
        }
        .resume-detail-bottom {
          position: relative;
          margin-top: 22px;
          padding: 18px;
          background: rgba(13,13,13,0.97);
          clip-path: polygon(0 0, 100% 0, calc(100% - 16px) 100%, 0 100%);
          box-shadow: inset 0 0 0 1px rgba(255,255,255,0.12);
        }
        .resume-detail-bottom-title {
          font-family: 'Persona5Main';
          font-size: 30px;
          letter-spacing: 2px;
          color: #ffffff;
          margin-bottom: 14px;
        }
        .resume-detail-bullets {
          display: flex;
          flex-direction: column;
          gap: 10px;
        }
        .resume-detail-bullet {
          font-family: 'Persona5Main';
          font-size: 21px;
          line-height: 1.15;
          color: #ffffff;
        }

      `}</style>

      <div className="resume-overlay">
        <div className="resume-stack">
          <div className={`resume-list-tag${mounted ? " mounted" : ""}`}>LIST</div>
          {ITEMS.map((item, index) => (
            <div
              key={item.id}
              className={`resume-card-wrap${active === index ? " active" : ""}${mounted ? " mounted" : ""}`}
              style={{ transitionDelay: `${index * 55}ms` }}
              onMouseEnter={() => {
                setActive(index);
              }}
              onClick={() => {
                setActive(index);
              }}
            >
              <div className="resume-card">
                <div className="resume-badge">
                  <div className="resume-badge-text">{item.badge}</div>
                </div>
                <div className="resume-card-inner">
                  <div className="resume-title">{item.title}</div>
                  <div className="resume-rank">
                    <div className="resume-rank-label">RANK</div>
                    <div className="resume-rank-number">{item.rank}</div>
                  </div>
                </div>
                <div className="resume-subtitle-bar">
                  <div className="resume-subtitle">{item.subtitle}</div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {active === 0 && (
          <div className="resume-detail-panel">
            <div className="resume-detail-top">
              <div className="resume-detail-top-index">01</div>
              <div className="resume-detail-top-title">EDUCATION LOG</div>
              <div className="resume-detail-top-progress">4/4</div>
            </div>

            <div className="resume-detail-list">
              {EDUCATION_ROWS.map((row) => (
                <div className="resume-detail-row" key={row.index}>
                  <div className="resume-detail-row-index">{row.index}</div>
                  <div className="resume-detail-row-title">{row.title}</div>
                  <div className="resume-detail-status">{row.status}</div>
                </div>
              ))}
            </div>

            <div className="resume-detail-bottom">
              <div className="resume-detail-bottom-title">DETAILS</div>
              <div className="resume-detail-bullets">
                <div className="resume-detail-bullet">- Born to backend.</div>
                <div className="resume-detail-bullet">- Focus: Java and Javascript.</div>
              </div>
            </div>
          </div>
        )}

      </div>
    </div>
  );
}

````

## SideProjectsPage.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/SideProjectsPage.jsx` · Bytes: 7876 · SHA-256: `b3d325cc1e650535461dbcaa76300b502456a3860695fd99013b896335c52299`

````text
import { useEffect, useState, useRef } from "react";
import { playSelectSound } from "./utils/audio.js";
import { useNavigate } from "react-router-dom";

const ITEMS = [
  {
    id: "gestao-vendas",
    title: "SALES MANAGEMENT",
    stack: "Java",
    summary: "Sales management system.",
    href: "https://github.com/ffaneto/gestao-vendas-3-info-vesp-1.0",
  },
  {
    id: "persona5-website",
    title: "PERSONA 5 WEBSITE",
    stack: "React",
    summary: "A website for the game Persona 5.",
    href: "https://github.com/ffaneto/persona5-website",
  },
  {
    id: "calculadora-arranjo",
    title: "ARRANGEMENT CALCULATOR",
    stack: "Java",
    summary: "Arrangements, combinations, and permutations calculator.",
    href: "https://github.com/ffaneto/calculadora-arranjo-combinacao-permutacao-java",
  },
  {
    id: "questoes-javascript",
    title: "JS EXERCISES",
    stack: "JavaScript",
    summary: "JavaScript functions-focused problem solving.",
    href: "https://github.com/ffaneto/questoes-funcoes-javascript",
  },
  {
    id: "curso-nelio",
    title: "NELIO ALVES LABS",
    stack: "Java",
    summary: "Projects and solved exercises from Nelio Alves's course.",
    href: "https://github.com/ffaneto/curso-nelio-alves",
  },
  {
    id: "outras-questoes",
    title: "MORE EXERCISES",
    stack: "Java",
    summary: "More solved exercises from Nelio Alves's course.",
    href: "https://github.com/ffaneto/outras-questoes-nelio-alves",
  }

];

export default function SideProjectsPage() {
  const navigate = useNavigate();
  const [active, setActive] = useState(0);
  const [mounted, setMounted] = useState(false);
  const isFirstRenderAudio = useRef(true);

  useEffect(() => {
    if (isFirstRenderAudio.current) {
      isFirstRenderAudio.current = false;
      return;
    }
    playSelectSound();
  }, [active]);

  useEffect(() => {
    const t = setTimeout(() => setMounted(true), 80);
    return () => clearTimeout(t);
  }, []);

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === "ArrowUp") setActive((i) => Math.max(0, i - 1));
      if (e.key === "ArrowDown") setActive((i) => Math.min(ITEMS.length - 1, i + 1));
      if (e.key === "Enter") window.open(ITEMS[active].href, "_blank", "noopener,noreferrer");
      if (e.key === "ArrowLeft" || e.key === "Escape" || e.key === "Backspace") navigate(-1);
    };

    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [active, navigate]);

  return (
    <div id="menu-screen">
      {/* <video src={bgVideo} autoPlay loop muted playsInline /> */}

      <style>{`
        .sp-shell {
          position: absolute;
          inset: 0;
          z-index: 10;
          display: grid;
          grid-template-columns: 48% 52%;
          gap: 20px;
          padding: 6vh 3vw;
        }

        .sp-left {
          display: flex;
          flex-direction: column;
          gap: 12px;
        }

        .sp-title {
          font-family: 'Persona5Main', sans-serif;
          font-size: 72px;
          color: #ffffff;
          line-height: 0.92;
          letter-spacing: 1px;
          text-shadow: 0 2px 0 rgba(13,13,13,0.3);
          margin-bottom: 8px;
          opacity: 0;
          transform: translateX(-24px);
          transition: opacity 0.35s ease, transform 0.35s ease;
        }
        .sp-title.mounted {
          opacity: 1;
          transform: translateX(0);
        }

        .sp-item {
          position: relative;
          min-height: 94px;
          background: rgba(13,13,13,0.94);
          clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
          box-shadow: inset 0 0 0 1px rgba(255,255,255,0.14), 0 8px 16px rgba(13,13,13,0.35);
          padding: 14px 16px;
          cursor: pointer;
          opacity: 0;
          transform: translateX(-36px);
          transition: transform 0.24s ease, background 0.24s ease, opacity 0.4s ease;
        }
        .sp-item.mounted {
          opacity: 1;
          transform: translateX(0);
        }
        .sp-item.active {
          background: rgba(255, 255, 255, 0.97);
          transform: translateX(6px);
        }

        .sp-item-title {
          font-family: 'Persona5Main', sans-serif;
          font-size: 42px;
          line-height: 0.9;
          color: #ffffff;
        }
        .sp-item.active .sp-item-title {
          color: #111;
        }

        .sp-item-stack {
          font-family: 'Persona5Main', sans-serif;
          font-size: 26px;
          letter-spacing: 1.4px;
          color: #ffffff;
          margin-top: 4px;
        }
        .sp-item.active .sp-item-stack {
          color: #0d0d0d;
        }

        .sp-right {
          position: relative;
          background: linear-gradient(180deg, rgba(13,13,13,0.96) 0%, rgba(13,13,13,0.96) 100%);
          clip-path: polygon(0 0, 100% 0, calc(100% - 18px) 100%, 0 100%);
          box-shadow: inset 0 0 0 1px rgba(255,255,255,0.16), 12px 12px 0 rgba(13,13,13,0.5);
          padding: 24px;
          overflow: hidden;
        }

        .sp-tag {
          display: inline-block;
          font-family: 'Persona5Main', sans-serif;
          font-size: 24px;
          letter-spacing: 1.6px;
          background: #ffffff;
          color: #0d0d0d;
          padding: 4px 10px;
          clip-path: polygon(0 0, 100% 0, calc(100% - 8px) 100%, 0 100%);
        }

        .sp-right-title {
          font-family: 'Persona5Main', sans-serif;
          font-size: 64px;
          line-height: 0.92;
          color: #ffffff;
          margin-top: 16px;
        }

        .sp-right-summary {
          margin-top: 16px;
          font-family: 'Bebas Neue', sans-serif;
          font-size: 38px;
          line-height: 1.05;
          letter-spacing: 1px;
          color: #ffffff;
        }

        .sp-link {
          margin-top: 24px;
          font-family: 'Bebas Neue', sans-serif;
          font-size: 28px;
          letter-spacing: 0px;
          color: #ffffff;
          background: #d92323;
          display: inline-flex;
          align-items: center;
          padding: 6px 12px;
          clip-path: polygon(0 0, 100% 0, calc(100% - 10px) 100%, 0 100%);
        }

        .sp-footer {
          position: fixed;
          right: 28px;
          bottom: 20px;
          z-index: 20;
          display: flex;
          flex-direction: column;
          align-items: flex-end;
          gap: 4px;
          font-family: 'Persona5Main', sans-serif;
          color: rgba(255,255,255,0.7);
          letter-spacing: 2px;
          font-size: 12px;
        }
      `}</style>

      <div className="sp-shell">
        <div className="sp-left">
          <div className={`sp-title${mounted ? " mounted" : ""}`}>PROJECT LOG</div>
          {ITEMS.map((item, index) => (
            <div
              key={item.id}
              className={`sp-item${active === index ? " active" : ""}${mounted ? " mounted" : ""}`}
              style={{ transitionDelay: `${index * 55}ms` }}
              onMouseEnter={() => setActive(index)}
              onClick={() => window.open(item.href, "_blank", "noopener,noreferrer")}
            >
              <div className="sp-item-title">{item.title}</div>
              <div className="sp-item-stack">{item.stack}</div>
            </div>
          ))}
        </div>

        <div className="sp-right">
          <div className="sp-tag">NEW SECTION</div>
          <div className="sp-right-title">{ITEMS[active].title}</div>
          <div className="sp-right-summary">{ITEMS[active].summary}</div>
          <div className="sp-link">OPEN LINK: {ITEMS[active].href.replace("https://", "")}</div>
        </div>
      </div>

      <div className="sp-footer">
        <div>UP / DOWN SELECT</div>
        <div>ENTER OPEN</div>
        <div>ESC BACK</div>
      </div>
    </div>
  );
}

````

## Socials.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/Socials.jsx` · Bytes: 22878 · SHA-256: `12083739ad4a26219fa698208d0f93eb150c8fd9f7ff7bb9b516d85ffc61079b`

````text
import { useState, useEffect, useRef } from "react";
import { playSelectSound } from "./utils/audio.js";
import { useNavigate } from "react-router-dom";
import char1 from "./assets/char1.png";
import char2 from "./assets/char2.png";
import char3 from "./assets/char3.png";
import newsign from "./assets/newsign.png";
import icon1 from "./assets/icon1.png";
import icon2 from "./assets/icon2.png";
import icon3 from "./assets/icon3.png";

const CHARS = [char1, char2, char3];

const ROLES = [
  { text: "LEADER", color: "#d92323", bg: "rgba(217,35,35,0.12)", border: "rgba(217,35,35,0.5)" },
  { text: "PARTY",  color: "#d92323", bg: "rgba(217,35,35,0.12)", border: "rgba(217,35,35,0.5)" },
  { text: "PARTY",  color: "#d92323", bg: "rgba(217,35,35,0.12)", border: "rgba(217,35,35,0.5)" },
];

const ITEMS = [
  {
    id: "github", label: "GITHUB", handle: "@ffaneto", href: "https://github.com/ffaneto?tab=repositories", icon: "💻", barIcon: icon1, bars: 5, newBars: [0], counts: ["SALES", "SITE","CALC", "EXERCS", "NELIO", "MORE"],
    links: ["github.com/ffaneto/gestao-vendas-3-info-vesp-1.0","github.com/ffaneto/persona5-website", "github.com/ffaneto/calculadora-arranjo-combinacao-permutacao-java", "github.com/ffaneto/questoes-funcoes-javascript", "github.com/ffaneto/curso-nelio-alves", "github.com/ffaneto/outras-questoes-nelio-alves"],
    stats: [
      { tag: "USR", value: "ffaneto", color: "#7b7b7b" },
      { tag: "TOP", value: "PROJECTS",  color: "#7b7b7b" },
    ],
  },
  {
    id: "instagram", label: "INSTAGRAM", handle: "@ffaneto__", href: "https://instagram.com/ffaneto__", icon: "📷", barIcon: icon2, bars: 2, newBars: [1], counts: ["POSTS", "REELS"],
    links: ["instagram.com/ffaneto__", "instagram.com"],
    stats: [
      { tag: "SOCIAL", value: "PICS", color: "#d92323" },
      { tag: "MIND", value: "LIFE",  color: "#732424" },
    ],
  },
  {
    id: "email", label: "EMAIL", handle: "misteryshadbr@gmail.com", href: "mailto:misteryshadbr@gmail.com", icon: "✉️", barIcon: icon3, bars: 3, newBars: [2], counts: ["INBOX", "OUTBOX", "SPAM"],
    links: ["mailto:misteryshadbr@gmail.com", "gmail.com", "mail.google.com"],
    stats: [
      { tag: "CONTACT", value: "DIRECT", color: "#ffffff" },
      { tag: "TALK", value: "WORK",  color: "#d92323" },
    ],
  },
];

export default function Socials() {
  const [active, setActive]               = useState(0);
  const [mounted, setMounted]             = useState(false);
  const isFirstRenderAudio = useRef(true);
  const [activeInfoBar, setActiveInfoBar] = useState(0);
  const [focus, setFocus]                 = useState("left"); // "left" | "right"
  const navigate = useNavigate();

  useEffect(() => {
    const t = setTimeout(() => setMounted(true), 60);
    return () => clearTimeout(t);
  }, []);

  useEffect(() => {
    if (isFirstRenderAudio.current) {
      isFirstRenderAudio.current = false;
      return;
    }
    playSelectSound();
  }, [active, activeInfoBar, focus]);

  useEffect(() => {
    const onKey = (e) => {
      const getLink = (link) => link.startsWith("http") || link.startsWith("mailto") ? link : "https://" + link;

      if (e.key === "Tab") {
        e.preventDefault();
        if (focus === "left") {
          setFocus("right");
          setActiveInfoBar(0);
        } else {
          setFocus("left");
        }
        return;
      }

      const isUp = e.key === "ArrowUp" || e.key.toLowerCase() === "w" || e.key.toLowerCase() === "a";
      const isDown = e.key === "ArrowDown" || e.key.toLowerCase() === "s" || e.key.toLowerCase() === "d";

      if (focus === "left") {
        if (isUp)    setActive(i => Math.max(0, i - 1));
        if (isDown)  setActive(i => Math.min(ITEMS.length - 1, i + 1));
        if (e.key === "ArrowLeft")  { setFocus("right"); setActiveInfoBar(0); }
        if (e.key === "Enter")      window.open(ITEMS[active].href, "_blank");
      } else {
        const barCount = ITEMS[active].bars;
        if (isUp)   setActiveInfoBar(i => Math.max(0, i - 1));
        if (isDown) setActiveInfoBar(i => Math.min(barCount - 1, i + 1));
        if (e.key === "ArrowRight") setFocus("left");
        if (e.key === "Enter")     window.open(getLink(ITEMS[active].links[activeInfoBar]), "_blank");
      }
      if ((e.key === "ArrowRight" && focus === "left") || e.key === "Escape" || e.key === "Backspace") navigate(-1);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [active, navigate, focus, activeInfoBar]);

  return (
    <div id="menu-screen">
      {/* <video src={bgVideo} autoPlay loop muted playsInline /> */}
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow+Condensed:ital,wght@0,400;0,700;1,700&display=swap');

        .sc-root {
          position: absolute;
          inset: 0;
          z-index: 10;
          pointer-events: none;
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          justify-content: center;
          gap: 6px;
          padding-left: 0;
        }

        /* ── Each bar ── */
        .sc-bar {
          position: relative;
          width: 45vw;
          height: 64px;
          transition: height 0.3s cubic-bezier(0.22,1,0.36,1);
          background: #111;
          cursor: pointer;
          pointer-events: all;
          clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
          box-shadow: 0 6px 24px rgba(13,13,13,0.65);
          z-index: 1;
        }

        /* wrapper holds both the red underlay and the bar */
        .sc-bar-outer {
          position: relative;
          flex-shrink: 0;
          transform: translateX(-100%);
          transition: transform 0.55s cubic-bezier(0.22, 1, 0.36, 1);
        }
        .sc-bar-outer.active .sc-bar     { height: 90px; }
        .sc-bar-outer.active .sc-bar-red { height: 90px; }
        .sc-bar-outer.mounted { transform: translateX(0); }
        .sc-bar-outer:nth-child(1) { transition-delay: 0ms; }
        .sc-bar-outer:nth-child(2) { transition-delay: 80ms; }
        .sc-bar-outer:nth-child(3) { transition-delay: 160ms; }

        /* red underlay — peeks out below the bar when active */
        .sc-bar-red {
          position: absolute;
          top: 0; left: 0;
          width: 45vw;
          height: 64px;
          background: #d92323;
          clip-path: polygon(50% 0, 100% 0, 100% 100%, calc(50% - 10px) 100%);
          transform: translateY(-7px);
          opacity: 0;
          transition: opacity 0.2s ease;
          z-index: 0;
          pointer-events: none;
        }
        .sc-bar-outer.active .sc-bar-red { opacity: 1; }

        /* white fill — skewed parallelogram on the right 25% */
        .sc-bar-fill {
          position: absolute;
          inset: 0;
          width: 100%;
          background: #ffffff;
          clip-path: polygon(100% 0, 100% 0, calc(100% - 32px) 100%, calc(100% - 32px) 100%);
          transition: clip-path 0.35s cubic-bezier(0.22, 1, 0.36, 1);
          z-index: 0;
        }
        .sc-bar-outer.active .sc-bar-fill {
          clip-path: polygon(22% 0, 100% 0, calc(100% - 14px) 100%, calc(22% + 138px) 100%);
        }

        /* shade on the left edge of the white fill */
        .sc-bar-shade {
          position: absolute;
          top: 0; bottom: 0;
          left: 73%;
          width: 6%;
          background: linear-gradient(90deg, rgba(13,13,13,0.15) 0%, rgba(13,13,13,0) 100%);
          z-index: 1;
          pointer-events: none;
          opacity: 0;
          transition: opacity 0.35s ease;
        }
        .sc-bar-outer.active .sc-bar-shade { opacity: 1; }

        /* bottom shadow line under each bar */
        .sc-bar::after {
          content: '';
          position: absolute;
          bottom: 0; left: 0; right: 0;
          height: 6px;
          background: linear-gradient(180deg, rgba(13,13,13,0) 0%, rgba(13,13,13,0.55) 100%);
          z-index: 10;
          pointer-events: none;
        }

        /* content layout inside each bar */
        .sc-bar-content {
          position: relative;
          z-index: 2;
          height: 100%;
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: 0 20px 0 20px;
        }

        /* left: role label */
        .sc-role {
          display: flex;
          align-items: center;
          flex-shrink: 0;
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 50px;
          letter-spacing: -2px;
          color: #ffffff;
          transform: rotate(-30deg);
          user-select: none;
          line-height: 1;
          padding: 0 16px 0 8px;
        }

        /* left: icon + name centered in remaining space */
        .sc-main {
          flex: 1;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 3px;
        }
        .sc-main-top {
          display: flex;
          align-items: center;
          gap: 12px;
        }

        .sc-icon {
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 22px;
          width: 32px;
          text-align: center;
          flex-shrink: 0;
          color: rgba(255,255,255,0.15);
          transition: color 0.2s ease;
          user-select: none;
        }
        .sc-bar-outer.active .sc-icon { color: rgba(255,255,255,0.25); }

        .sc-label {
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 28px;
          letter-spacing: 1px;
          line-height: 1;
          color: rgba(255,255,255,0.85);
          transition: color 0.2s ease;
          user-select: none;
        }
        .sc-bar-outer.active .sc-label { color: #0d0d0d; }

        /* lb/rb nav row */
        @keyframes sc-arrow-left {
          0%, 100% { transform: translateX(0); opacity: 1; }
          50%       { transform: translateX(-5px); opacity: 0.4; }
        }
        @keyframes sc-arrow-right {
          0%, 100% { transform: translateX(0); opacity: 1; }
          50%       { transform: translateX(5px); opacity: 0.4; }
        }
        .sc-nav-btn {
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 12px;
          letter-spacing: 2px;
          color: #111;
          border: 1px solid rgba(13,13,13,0.35);
          padding: 1px 7px;
          line-height: 1.5;
          user-select: none;
        }
        .sc-nav-arrow {
          font-size: 12px;
          color: #d92323;
          display: inline-block;
        }
        .sc-nav-arrow.left  { animation: sc-arrow-left  0.8s ease-in-out infinite; }
        .sc-nav-arrow.right { animation: sc-arrow-right 0.8s ease-in-out infinite; }

        /* right: stats group */
        .sc-stats {
          display: flex;
          align-items: center;
          gap: 10px;
          padding-right: 24px;
          flex-shrink: 0;
        }

        .sc-stat {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
        }

        .sc-stat-top {
          display: flex;
          align-items: baseline;
          gap: 4px;
        }

        .sc-stat-tag {
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 9px;
          letter-spacing: 1.5px;
          padding: 1px 4px;
          border-width: 1px;
          border-style: solid;
          line-height: 1.4;
          user-select: none;
        }

        .sc-stat-num {
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 26px;
          font-style: italic;
          line-height: 1;
          color: #ffffff;
          letter-spacing: 1px;
          user-select: none;
          transition: color 0.2s ease;
        }
        .sc-bar-outer.active .sc-stat-num { color: #0d0d0d; }

        .sc-stat-bars {
          width: 100%;
          display: flex;
          flex-direction: column;
          gap: 1px;
          margin-top: 2px;
        }
        .sc-stat-bar-color {
          height: 3px;
          width: 100%;
        }
        .sc-stat-bar-black {
          height: 2px;
          width: 100%;
          background: #0d0d0d;
        }

        /* character portrait */
        .sc-char {
          position: absolute;
          top: 0;
          left: 110px;
          height: 100%;
          width: auto;
          max-width: 160px;
          object-fit: cover;
          object-position: top;
          pointer-events: none;
          z-index: 3;
          clip-path: polygon(20px 0%, 100% 0%, calc(100% - 20px) 100%, 0% 100%);
        }

        /* right-side nav bar */
        @keyframes sc-right-nav-pop {
          0%   { opacity: 0; transform: scale(0.55) translateY(-10px); }
          65%  { opacity: 1; transform: scale(1.1) translateY(2px); }
          100% { opacity: 1; transform: scale(1) translateY(0); }
        }
        .sc-right-nav {
          position: fixed;
          top: 40px;
          right: 40px;
          display: flex;
          align-items: center;
          gap: 6px;
          pointer-events: none;
          z-index: 50;
          animation: sc-right-nav-pop 0.38s cubic-bezier(0.22,1,0.36,1) both;
        }
        .sc-right-nav .sc-nav-btn {
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 100px;
          letter-spacing: 3px;
          line-height: 1;
          user-select: none;
          color: #ffffff;
          -webkit-text-stroke: 2px #0d0d0d;
          paint-order: stroke fill;
          background: none;
          border: none;
          padding: 0 6px;
        }
        .sc-right-nav .sc-nav-label {
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 28px;
          letter-spacing: 3px;
          line-height: 1;
          user-select: none;
          color: #111;
          padding: 0 8px;
        }
        .sc-right-nav .sc-nav-arrow {
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 22px;
          color: #d92323;
          display: inline-block;
          user-select: none;
        }
        .sc-right-nav .sc-nav-arrow.left  { animation: sc-arrow-left  0.8s ease-in-out infinite; }
        .sc-right-nav .sc-nav-arrow.right { animation: sc-arrow-right 0.8s ease-in-out infinite; }

        /* info bar under nav */
        @keyframes sc-infobar-in {
          0%   { opacity: 0; transform: translateX(40px); }
          60%  { opacity: 1; transform: translateX(-4px); }
          100% { opacity: 1; transform: translateX(0); }
        }
        .sc-info-bar-wrap {
          position: fixed;
          right: 0;
          left: 65%;
          height: 46px;
          background: transparent;
          pointer-events: all;
          cursor: pointer;
          z-index: 50;
          padding: 0;
          animation: sc-infobar-in 0.35s cubic-bezier(0.22,1,0.36,1) both;
        }
        .sc-info-bar-wrap.selected {
          background: #111;
          padding: 1.5px;
          border-radius: 8px;
        }
        .sc-info-bar {
          position: relative;
          width: 100%;
          height: 100%;
          background: transparent;
          display: flex;
          align-items: center;
          overflow: hidden;
        }
        .sc-info-bar-wrap.selected .sc-info-bar {
          background: #ffffff;
          border-radius: 7px;
        }
        .sc-info-bar-wrap.selected .sc-info-bar::after {
          content: '';
          position: absolute;
          right: 56px;
          top: 7px;
          width: 120px;
          height: 32px;
          border-radius: 6px;
          background: rgba(255,255,255,0.36);
          box-shadow: inset 0 0 0 1px rgba(255,255,255,0.55);
          pointer-events: none;
          z-index: 1;
        }
        .sc-info-bar-new {
          position: absolute;
          left: -40px;
          bottom: 0;
          height: 65%;
          width: auto;
          pointer-events: none;
          z-index: 3;
        }
        .sc-info-bar-wrap.selected .sc-info-bar::before {
          content: '';
          position: absolute;
          top: 0; left: 0; right: 0;
          height: 4px;
          background: #d92323;
          z-index: 1;
        }
        .sc-info-bar-text {
          flex: 1;
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 22px;
          letter-spacing: 0.5px;
          color: #111;
          padding: 0 14px;
          user-select: none;
        }
        .sc-info-bar-box {
          position: relative;
          z-index: 2;
          height: 70%;
          background: #0d0d0d;
          display: flex;
          align-items: center;
          padding: 0 12px;
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 20px;
          letter-spacing: 0px;
          color: #ffffff;
          flex-shrink: 0;
          border-radius: 6px;
          margin-right: 4px;
          user-select: none;
        }

        .sc-info-bar-icon-wrap {
          width: 56px;
          height: 26px;
          display: flex;
          align-items: center;
          justify-content: center;
          flex-shrink: 0;
          margin-left: 14px;
        }

        .sc-info-bar-icon-wrap.email {
          width: 46px;
          height: 22px;
        }

        .sc-info-bar-icon {
          max-width: 100%;
          max-height: 100%;
          width: auto;
          height: auto;
          object-fit: contain;
          pointer-events: none;
          user-select: none;
        }

        .sc-info-bar-count {
          position: relative;
          z-index: 2;
          font-family: 'Bebas Neue', 'Persona5Main';
          font-size: 22px;
          letter-spacing: 1px;
          color: #111;
          margin-right: 80px;
          flex-shrink: 0;
          user-select: none;
        }

        /* footer hints */
        .sc-footer {
          position: fixed;
          bottom: 20px; right: 28px;
          display: flex; flex-direction: column;
          align-items: flex-end; gap: 5px;
          font-family: 'Bebas Neue', 'Persona5Main';
          z-index: 50;
          opacity: 0;
          transition: opacity 0.4s ease 0.6s;
        }
        .sc-footer.mounted { opacity: 1; }
        .sc-footer-row {
          display: flex; align-items: center; gap: 8px;
          font-size: 13px; letter-spacing: 2px;
          color: rgba(255,255,255,0.22);
        }
        .sc-footer-key {
          border: 1px solid rgba(255,255,255,0.15);
          border-radius: 3px;
          padding: 1px 6px; font-size: 11px;
        }
      `}</style>

      <div className="sc-root" role="navigation">
        {ITEMS.map((item, i) => (
          <div
            key={item.id}
            className={`sc-bar-outer${active === i ? " active" : ""}${mounted ? " mounted" : ""}`}
            onClick={() => {
              if (active === i && focus === "left") window.open(item.href, "_blank");
              else {
                setActive(i);
                setFocus("left");
              }
            }}
            onMouseEnter={() => {
              setActive(i);
              setFocus("left");
            }}
          >
            <div className="sc-bar-red" />
            <div className="sc-bar">
              <img className="sc-char" src={CHARS[i]} alt="" />
              <div className="sc-bar-fill" />
              <div className="sc-bar-shade" />
              <div className="sc-bar-content">
                <div className="sc-role">{ROLES[i].text}</div>
                <div className="sc-main">
                  <div className="sc-main-top">
                    <div className="sc-icon">{item.icon}</div>
                    <div className="sc-label">{item.label}</div>
                  </div>
                </div>
                <div className="sc-stats">
                  {item.stats.map(s => (
                    <div className="sc-stat" key={s.tag}>
                      <div className="sc-stat-top">
                        <span className="sc-stat-tag" style={{ color: s.color, borderColor: s.color }}>{s.tag}</span>
                        <span className="sc-stat-num">{s.value}</span>
                      </div>
                      <div className="sc-stat-bars">
                        <div className="sc-stat-bar-color" style={{ background: s.color }} />
                        <div className="sc-stat-bar-black" />
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {mounted && (
        <div className="sc-right-nav" key={active}>
          <span className="sc-nav-arrow left">◄</span>
          <span className="sc-nav-btn">LB</span>
          <span className="sc-nav-label">{ITEMS[active].label}</span>
          <span className="sc-nav-btn">RB</span>
          <span className="sc-nav-arrow right">►</span>
        </div>
      )}

      {mounted && Array.from({ length: ITEMS[active].bars }).map((_, i) => (
        <div
          className={`sc-info-bar-wrap${activeInfoBar === i ? " selected" : ""}`}
          key={`bar-${active}-${i}`}
          style={{ top: `${155 + i * 52}px`, animationDelay: `${i * 50}ms` }}
          onClick={() => {
            const link = ITEMS[active].links[i];
            const url = link.startsWith("http") || link.startsWith("mailto") ? link : "https://" + link;
            window.open(url, "_blank");
            setActiveInfoBar(i);
            setFocus("right");
          }}
          onMouseEnter={() => {
            setActiveInfoBar(i);
            setFocus("right");
          }}
        >
          {ITEMS[active].newBars.includes(i) && (
            <img className="sc-info-bar-new" src={newsign} alt="" />
          )}
          <div className="sc-info-bar">
            <div className={`sc-info-bar-icon-wrap${ITEMS[active].id === "email" ? " email" : ""}`}>
              <img className="sc-info-bar-icon" src={ITEMS[active].barIcon} alt="" />
            </div>
            <span className="sc-info-bar-text">{ITEMS[active].links[i].slice(0, 10)}...</span>
            <span className="sc-info-bar-box">VIEWS</span>
            <span className="sc-info-bar-count">{ITEMS[active].counts[i]}</span>
          </div>
        </div>
      ))}

      <div className={`sc-footer${mounted ? " mounted" : ""}`}>
        <div className="sc-footer-row"><span className="sc-footer-key">TAB</span><span>SWITCH</span></div>
        <div className="sc-footer-row"><span className="sc-footer-key">W/S/A/D</span><span>SELECT</span></div>
        <div className="sc-footer-row"><span className="sc-footer-key">↵</span><span>OPEN</span></div>
        <div className="sc-footer-row"><span className="sc-footer-key">ESC</span><span>BACK</span></div>
      </div>
    </div>
  );
}

````

## VideoPage.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/VideoPage.jsx` · Bytes: 507 · SHA-256: `d79442b4eabb222cb21c45978c60254fe9e434a1541b860ead7972c479d9fa7b`

````text
import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

export default function VideoPage({ src }) {
  const navigate = useNavigate()

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === 'ArrowLeft') navigate(-1)
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [navigate])

  return (
    <div id="menu-screen">
      {/* <video src={src} autoPlay loop muted playsInline /> */}
    </div>
  )
}

````

## index.css

Ruta: `PruebasMenu/persona5-website-theme/src/index.css` · Bytes: 738 · SHA-256: `f262fc6df1d454d28b7f3ca1dc917d9194232fee45bc5c12a440a2dc53d6bbbf`

````text
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  --p5-black: #0d0d0d;
  --p5-red: #d92323;
  --p5-dark-red: #732424;
  --p5-gray: #7b7b7b;
  --p5-white: #ffffff;
}


@font-face {
  font-family: 'Persona5Main';
  src: url('/Persona5main.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

html, body, #root {
  width: 100%;
  height: 100%;
}

body {
  background:
    radial-gradient(circle at 15% 15%, rgba(217,35,35,0.35), rgba(13,13,13,0.92) 45%),
    linear-gradient(140deg, #0d0d0d 0%, #732424 55%, #0d0d0d 100%);
  overflow: hidden;
  font-family: 'Persona5Main';
}

````

## main.jsx

Ruta: `PruebasMenu/persona5-website-theme/src/main.jsx` · Bytes: 321 · SHA-256: `5e7aff51c18b9e1a6f047668a0c3e3fe362bc2c7ad990149e51f030593b7c476`

````text
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)

````

