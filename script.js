// script.js
async function sendPrediction() {
  // Example: gather inputs from form fields that have IDs matching feature names.
  // Make sure HTML inputs use ids equal to your FEATURE_ORDER names OR fill values array.
  // Example feature IDs in HTML: <input id="feature1" ... />

  // Option A: keyed object using IDs
  const payload = {};

  // list the same features as in server FEATURE_ORDER here (or request them dynamically)
  const FEATURE_ORDER = ["feature1", "feature2", "feature3"]; // EDIT to match server/app.py

  FEATURE_ORDER.forEach(name => {
    const el = document.getElementById(name);
    if (el) payload[name] = el.value;
  });

  // If no elements found, you might want to send a values array:
  // payload['values'] = [v1, v2, v3];

  try {
    const resp = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const data = await resp.json();
    if (!resp.ok) {
      showResult("Error: " + (data.error || JSON.stringify(data)));
      return;
    }
    // showResult: implement this to display to your page
    showResult("Prediction: " + JSON.stringify(data));
  } catch (err) {
    showResult("Request failed: " + err);
  }
}

function showResult(msg) {
  const el = document.getElementById("result");
  if (el) el.innerText = msg;
  else alert(msg);
}

// wire up if you have a button with id "predictBtn"
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("predictBtn");
  if (btn) btn.addEventListener("click", (e) => { e.preventDefault(); sendPrediction(); });
});
