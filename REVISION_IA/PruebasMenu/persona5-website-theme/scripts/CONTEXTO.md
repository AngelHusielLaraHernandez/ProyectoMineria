# Carpeta: PruebasMenu/persona5-website-theme/scripts

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## watch-build.mjs

Ruta: `PruebasMenu/persona5-website-theme/scripts/watch-build.mjs` · Bytes: 1555 · SHA-256: `ef743a2be962f3cac44b2a94b407c8283e7c6c016d914a21807f5890de4bff91`

````text
import { spawn } from "node:child_process";
import { watch } from "node:fs";
import path from "node:path";

const rootDir = process.cwd();
const watchDirs = ["src", "public"];
const watchFiles = ["index.html", "package.json", "vite.config.js"];

let buildRunning = false;
let buildQueued = false;
let debounceTimer;

function shouldIgnore(filePath = "") {
  return (
    filePath.includes(`${path.sep}dist${path.sep}`) ||
    filePath.includes(`${path.sep}node_modules${path.sep}`) ||
    filePath.endsWith(".swp") ||
    filePath.endsWith(".tmp")
  );
}

function runBuild() {
  if (buildRunning) {
    buildQueued = true;
    return;
  }

  buildRunning = true;
  console.log(`[watch-build] ${new Date().toLocaleTimeString()} running npm run build`);

  const npmCommand = process.platform === "win32" ? "npm.cmd" : "npm";

  const child = spawn(npmCommand, ["run", "build"], {
    cwd: rootDir,
    stdio: "inherit",
  });

  child.on("exit", () => {
    buildRunning = false;

    if (buildQueued) {
      buildQueued = false;
      runBuild();
    }
  });
}

function queueBuild(filePath) {
  if (shouldIgnore(filePath)) return;

  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => runBuild(), 180);
}

for (const dir of watchDirs) {
  watch(path.join(rootDir, dir), { recursive: true }, (_, filename) => {
    queueBuild(filename ? path.join(dir, filename) : dir);
  });
}

for (const file of watchFiles) {
  watch(path.join(rootDir, file), () => queueBuild(file));
}

console.log("[watch-build] watching for changes...");
runBuild();

````

