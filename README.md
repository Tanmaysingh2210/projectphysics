# projectphysics

├── README.md
├── The-Compton-Effect.pptx
├── comp.py
└── simulation.html


/README.md:
--------------------------------------------------------------------------------
1 | # projectphysics


--------------------------------------------------------------------------------
/The-Compton-Effect.pptx:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/Tanmaysingh2210/projectphysics/2805d5028712a4d3a0cf7f03ac8f7f8ebb60bb02/The-Compton-Effect.pptx


--------------------------------------------------------------------------------
/comp.py:
--------------------------------------------------------------------------------
 1 | import numpy as np
 2 | import matplotlib.pyplot as plt
 3 | 
 4 | # Constants
 5 | h = 6.626e-34
 6 | c = 3e8
 7 | me = 9.11e-31
 8 | compton_const = h / (me * c)
 9 | 
10 | # User input
11 | initial_wavelength = float(input("Enter initial wavelength (nm): ")) * 1e-9
12 | theta_deg = float(input("Enter scattering angle (degrees): "))
13 | theta_rad = np.radians(theta_deg)
14 | 
15 | # Compton shift
16 | delta_lambda = compton_const * (1 - np.cos(theta_rad))
17 | scattered_wavelength = initial_wavelength + delta_lambda
18 | 
19 | # Energies
20 | E_initial = h * c / initial_wavelength
21 | E_scattered = h * c / scattered_wavelength
22 | KE = E_initial - E_scattered
23 | 
24 | # Output
25 | print(f"Compton Shift: {delta_lambda:.3e} m")
26 | print(f"Scattered Wavelength: {scattered_wavelength*1e9:.3f} nm")
27 | print(f"Kinetic Energy: {KE:.3e} J")
28 | 
29 | # Plot Compton shift vs angle only
30 | angles = np.linspace(0, 180, 360)
31 | shifts = compton_const * (1 - np.cos(np.radians(angles)))
32 | 
33 | plt.figure(figsize=(6, 5))
34 | plt.plot(angles, shifts * 1e12, color='blue')
35 | plt.title("Compton Shift vs Scattering Angle")
36 | plt.xlabel("Scattering Angle (°)")
37 | plt.ylabel("Δλ (pm)")
38 | plt.grid(True)
39 | plt.tight_layout()
40 | plt.show()
41 | 


--------------------------------------------------------------------------------
/simulation.html:
--------------------------------------------------------------------------------
  1 | <!DOCTYPE html>
  2 | <html lang="en">
  3 | 
  4 | <head>
  5 |     <meta charset="UTF-8">
  6 |     <title>Compton Effect Simulation</title>
  7 |     <style>
  8 |         @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');
  9 |     </style>
 10 |     <style>
 11 |         body {
 12 |             font-family: Arial, sans-serif;
 13 |             background-color: #2e2a2a;
 14 |             color: #fff;
 15 |             text-align: center;
 16 |             padding: 30px;
 17 |             border: 2px solid rgb(146, 142, 142);
 18 |             font-family: "Baloo 2", sans-serif;
 19 |         }
 20 | 
 21 |         input,
 22 |         button {
 23 |             padding: 10px;
 24 |             margin: 10px;
 25 |             font-size: 16px;
 26 |             border-radius: 8px;
 27 |             border: none;
 28 |         }
 29 | 
 30 |         h1 {
 31 |             text-decoration: underline;
 32 | 
 33 |         }
 34 | 
 35 |         #initialWavelength {
 36 |             border: 2px solid black;
 37 |         }
 38 | 
 39 |         .container {
 40 |             margin-top: 40px;
 41 |         }
 42 | 
 43 |         .container label {
 44 |             font-size: 23px;
 45 |             font-weight: 500;
 46 |         }
 47 |         .container button{
 48 |             border: 2px solid rgb(178, 172, 172);
 49 |             background-color: rgb(133, 123, 123);
 50 |             color: white;
 51 |             font-weight: 600;
 52 |         }
 53 | 
 54 |         .simulation {
 55 |             position: relative;
 56 |             width: 600px;
 57 |             height: 300px;
 58 |             margin: 40px auto;
 59 |             border: 2px solid #444;
 60 |             background-color: #222;
 61 |         }
 62 | 
 63 |         .photon,
 64 |         .scattered {
 65 |             width: 10px;
 66 |             height: 10px;
 67 |             border-radius: 50%;
 68 |             background-color: yellow;
 69 |             position: absolute;
 70 |             top: 140px;
 71 |         }
 72 | 
 73 |         .electron {
 74 |             width: 20px;
 75 |             height: 20px;
 76 |             background-color: cyan;
 77 |             border-radius: 50%;
 78 |             position: absolute;
 79 |             left: 280px;
 80 |             top: 140px;
 81 |         }
 82 |         
 83 |     </style>
 84 | </head>
 85 | 
 86 | <body>
 87 | 
 88 |     <h1>Compton Scattering Simulation</h1>
 89 | 
 90 |     <div class="container">
 91 |         <label>Initial Wavelength (nm):</label>
 92 |         <input type="number" id="initialWavelength" placeholder="Enter wavelength" />
 93 | 
 94 |         <div class="slider-container">
 95 |             <h2>Angle Selector (0° to 180°)</h2>
 96 |             <input type="range" id="angleSlider" min="0" max="180" value="90">
 97 |             <div class="value">Selected: <span id="sliderValue">90</span>°</div>
 98 |         </div>
 99 | 
100 |         <br>
101 |         <button style="cursor: pointer;" onclick="simulate()">Simulate</button>
102 |     </div>
103 | 
104 |     <p id="result"></p>
105 |     <p id="result2"></p>
106 | 
107 | 
108 |     <div class="simulation" id="simArea" style="position: relative;">
109 |         <svg id="scatteringSVG" width="600" height="300" style="position:absolute;top:0;left:0;z-index:0;"></svg>
110 |         <div class="photon" id="incomingPhoton" style="z-index:1;"></div>
111 |         <div class="electron" id="electron" style="z-index:1;"></div>
112 |         <div class="photon" id="scatteredPhoton" style="background-color: orange; z-index:1;"></div>
113 |     </div>
114 | 
115 |     <script>
116 |         const h = 6.626e-34;
117 |         const c = 3e8;
118 |         const me = 9.11e-31;
119 |         const comptonConst = h / (me * c);  // ≈ 2.43e-12 m
120 | 
121 |         const slider = document.getElementById('angleSlider');
122 |         const output = document.getElementById('sliderValue');
123 | 
124 | 
125 | 
126 |         function simulate() {
127 |             const lambda = parseFloat(document.getElementById('initialWavelength').value) * 1e-9;
128 |             const thetaDeg = parseFloat(slider.value);
129 |             const thetaRad = thetaDeg * Math.PI / 180;
130 | 
131 |             const deltaLambda = comptonConst * (1 - Math.cos(thetaRad));
132 |             const lambdaScattered = lambda + deltaLambda;
133 |             const lambdaScattered_nm = lambdaScattered * 1e9;
134 |             electron.style.left = 270 + "px";
135 |             electron.style.top = 130 + "px";
136 | 
137 |             document.getElementById("result").innerHTML =
138 |                 `Scattered Wavelength: <strong>${lambdaScattered_nm.toFixed(4)} nm</strong>`;
139 |             
140 |             
141 | 
142 |             drawScatteringDiagram(thetaDeg, lambda);
143 |             animateScattering(thetaDeg, lambda);
144 |         }
145 | 
146 |         slider.addEventListener('input', () => {
147 |             output.textContent = slider.value;
148 |         });
149 | 
150 |         function drawScatteringDiagram(angle, lambda) {
151 |             const svg = document.getElementById("scatteringSVG");
152 |             svg.innerHTML = ""; // Clear previous
153 | 
154 |             const cx = 280, cy = 140;
155 |             const r = 150; // Length for lines
156 | 
157 |             const theta1 = angle * Math.PI / 180;
158 | 
159 |             const incidentLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
160 |             const deltaLambda = comptonConst * (1 - Math.cos(theta1));
161 |             const lambdaScattered = lambda + deltaLambda;
162 |             const numerator = lambda * Math.sin(theta1);
163 |             const denominator = lambdaScattered - lambda * Math.cos(theta1);
164 |             const phi = Math.atan2(numerator, denominator); // radians, measured from x-axis
165 |             const electronVx = cx + r * Math.cos(phi) * 0.5;
166 |             const electronVy = cy - r * Math.sin(phi) * 0.5;
167 |             incidentLine.setAttribute("x1", cx);
168 |             incidentLine.setAttribute("y1", cy);
169 |             incidentLine.setAttribute("x2", electronVx);
170 |             incidentLine.setAttribute("y2", electronVy);
171 |             incidentLine.setAttribute("stroke", "#0ff");
172 |             incidentLine.setAttribute("stroke-width", "2");
173 |             svg.appendChild(incidentLine);
174 | 
175 |             const thetaRad = angle * Math.PI / 180;
176 |             const x2 = cx + r * Math.cos(thetaRad);
177 |             const y2 = cy + r * Math.sin(thetaRad);
178 |             const scatteredLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
179 |             scatteredLine.setAttribute("x1", cx);
180 |             scatteredLine.setAttribute("y1", cy);
181 |             scatteredLine.setAttribute("x2", x2);
182 |             scatteredLine.setAttribute("y2", y2);
183 |             scatteredLine.setAttribute("stroke", "orange");
184 |             scatteredLine.setAttribute("stroke-width", "2");
185 |             svg.appendChild(scatteredLine);
186 | 
187 |             const axisX = document.createElementNS("http://www.w3.org/2000/svg", "line");
188 |             axisX.setAttribute("x1", 0);
189 |             axisX.setAttribute("y1", cy);
190 |             axisX.setAttribute("x2", 600);
191 |             axisX.setAttribute("y2", cy);
192 |             axisX.setAttribute("stroke", "#888");
193 |             axisX.setAttribute("stroke-dasharray", "4,4");
194 |             svg.appendChild(axisX);
195 | 
196 |             const axisY = document.createElementNS("http://www.w3.org/2000/svg", "line");
197 |             axisY.setAttribute("x1", cx);
198 |             axisY.setAttribute("y1", 0);
199 |             axisY.setAttribute("x2", cx);
200 |             axisY.setAttribute("y2", 300);
201 |             axisY.setAttribute("stroke", "#888");
202 |             axisY.setAttribute("stroke-dasharray", "4,4");
203 |             svg.appendChild(axisY);
204 | 
205 |             const arcRadius = 30;
206 |             const arcStartAngle = 0; // 180 deg (left)
207 |             const arcEndAngle = thetaRad; // left + scattering angle
208 |             const arcStartX = cx + arcRadius * Math.cos(arcStartAngle);
209 |             const arcStartY = cy + arcRadius * Math.sin(arcStartAngle);
210 |             const arcEndX = cx + arcRadius * Math.cos(arcEndAngle);
211 |             const arcEndY = cy + arcRadius * Math.sin(arcEndAngle);
212 |             const arcFlag = angle > 180 ? 1 : 0;
213 |             const arcPath = document.createElementNS("http://www.w3.org/2000/svg", "path");
214 |             arcPath.setAttribute(
215 |                 "d",
216 |                 `M ${arcStartX} ${arcStartY} A ${arcRadius} ${arcRadius} 0 ${arcFlag} 1 ${arcEndX} ${arcEndY}`
217 |             );
218 |             arcPath.setAttribute("stroke", "orange");
219 |             arcPath.setAttribute("stroke-width", "2");
220 |             arcPath.setAttribute("fill", "none");
221 |             svg.appendChild(arcPath);
222 | 
223 |             const arcStartAngle1 = 0; // 180 deg (left)
224 |             const arcEndAngle1 = thetaRad; // left + scattering angle
225 |             const arcStartX1 = cx + arcRadius * Math.cos(arcStartAngle1);
226 |             const arcStartY1 = cy + arcRadius * Math.sin(arcStartAngle1);
227 |             const arcEndX1 = cx + arcRadius * Math.cos(arcEndAngle1);
228 |             const arcEndY1 = cy + arcRadius * Math.sin(arcEndAngle1);
229 |             const arcFlag1 = (180 / 3.14) * phi > 180 ? 1 : 0;
230 |             const arcPath1 = document.createElementNS("http://www.w3.org/2000/svg", "path");
231 |             arcPath.setAttribute(
232 |                 "d",
233 |                 `M ${arcStartX1} ${arcStartY1} A ${arcRadius} ${arcRadius} 0 ${arcFlag1} 1 ${arcEndX1} ${arcEndY1}`
234 |             );
235 |             arcPath1.setAttribute("stroke", "orange");
236 |             arcPath1.setAttribute("stroke-width", "2");
237 |             arcPath1.setAttribute("fill", "none");
238 |             svg.appendChild(arcPath1);
239 | 
240 |             const labelAngle = arcStartAngle + thetaRad / 2;
241 |             const labelX = cx + (arcRadius + 15) * Math.cos(labelAngle);
242 |             const labelY = cy + (arcRadius + 15) * Math.sin(labelAngle);
243 |             const angleText = document.createElementNS("http://www.w3.org/2000/svg", "text");
244 |             angleText.setAttribute("x", labelX);
245 |             angleText.setAttribute("y", labelY);
246 |             angleText.setAttribute("fill", "orange");
247 |             angleText.setAttribute("font-size", "16");
248 |             angleText.textContent = `${angle}°`;
249 |             svg.appendChild(angleText);
250 | 
251 |             const labelAngle1 = arcStartAngle1 + phi / 2;
252 |             const labelX1 = cx + (arcRadius + 40) * Math.cos(labelAngle1);
253 |             const labelY1 = cy - (arcRadius + 35) * Math.sin(labelAngle1);
254 |             const angleText1 = document.createElementNS("http://www.w3.org/2000/svg", "text");
255 |             angleText1.setAttribute("x", labelX1);
256 |             angleText1.setAttribute("y", labelY1);
257 |             angleText1.setAttribute("fill", "#0ff");
258 |             angleText1.setAttribute("font-size", "16");
259 |             angleText1.textContent = `${(180 / 3.14) * phi}°`;
260 |             svg.appendChild(angleText1);
261 |         }
262 |         function animateScattering(angle, lambda) {
263 |             const incoming = document.getElementById("incomingPhoton");
264 |             const scattered = document.getElementById("scatteredPhoton");
265 |             const electron = document.getElementById("electron");
266 | 
267 |             incoming.style.left = "0px";
268 |             incoming.style.top = "140px";
269 |             incoming.style.display = "block";
270 |             scattered.style.left = "280px";
271 |             scattered.style.top = "140px";
272 |             scattered.style.display = "none"; // Hide until scattering
273 | 
274 |             let t = 0;
275 |             const interval = setInterval(() => {
276 |                 if (t > 280) {
277 |                     clearInterval(interval);
278 |                     incoming.style.display = "none"; // Hide incoming photon at collision
279 |                     scatterPhoton(angle);
280 |                     return;
281 |                 }
282 |                 incoming.style.left = t + "px";
283 |                 t += 4;
284 |             }, 10);
285 |         }
286 |         function scatterPhoton(angle) {
287 |             const incoming = document.getElementById("incomingPhoton");
288 |             const scattered = document.getElementById("scatteredPhoton");
289 |             const electron = document.getElementById("electron");
290 |             incoming.style.left = "280px"; // Ensure at collision point
291 |             scattered.style.display = "block"; // Show scattered photon
292 | 
293 |             let t = 0;
294 |             const thetaRad = angle * Math.PI / 180;
295 | 
296 |             const lambda0 = parseFloat(document.getElementById('initialWavelength').value) * 1e-9;
297 |             const deltaLambda = comptonConst * (1 - Math.cos(thetaRad));
298 |             const lambdaScattered = lambda0 + deltaLambda;
299 | 
300 |             const numerator = lambda0 * Math.sin(thetaRad);
301 |             const denominator = lambdaScattered - lambda0 * Math.cos(thetaRad);
302 |             const phi = Math.atan2(numerator, denominator); // radians, measured from x-axis
303 | 
304 |             const vx = Math.cos(thetaRad);
305 |             const vy = Math.sin(thetaRad);
306 | 
307 |             const electronVx = Math.cos(phi) * 0.5;
308 |             const electronVy = -Math.sin(phi) * 0.5;
309 | 
310 |             const interval = setInterval(() => {
311 |                 if (t > 100) {
312 |                     clearInterval(interval);
313 |                     return;
314 |                 }
315 |                 scattered.style.left = (280 + vx * t - 5) + "px";
316 |                 scattered.style.top = (140 + vy * t - 5) + "px";
317 |                 electron.style.left = (280 + electronVx * t - 10) + "px";
318 |                 electron.style.top = (140 + electronVy * t - 10) + "px";
319 |                 t += 2;
320 |             }, 20);
321 |         }
322 |     </script>
323 | 
324 | </body>
325 | 
326 | </html>


--------------------------------------------------------------------------------
