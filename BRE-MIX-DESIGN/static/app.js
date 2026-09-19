/* ──────────────────────────────────────────────────────────────
   BRE Mix Design MVP – Application Logic
   ────────────────────────────────────────────────────────────── */

const form = document.getElementById('mixForm');
const inputPanel = document.getElementById('inputPanel');
const resultsPanel = document.getElementById('resultsPanel');
const resultsGrid = document.getElementById('resultsGrid');
const traceContent = document.getElementById('traceContent');
const btnCalculate = document.getElementById('btnCalculate');
const errorToast = document.getElementById('errorToast');
const errorMsg = document.getElementById('errorMsg');

// ── Form submission ──
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    hideError();
    
    btnCalculate.classList.add('loading');
    
    const data = {
        characteristic_strength: form.characteristic_strength.value,
        standard_deviation: form.standard_deviation.value || null,
        proportion_defective: form.proportion_defective.value,
        slump_class: form.slump_class.value,
        cement_strength_class: form.cement_strength_class.value,
        max_aggregate_size: form.max_aggregate_size.value,
        coarse_aggregate_type: form.aggregate_type.value,
        fine_aggregate_type: form.aggregate_type.value,
        relative_density: form.relative_density.value,
        fine_aggregate_proportion: form.fine_aggregate_proportion.value,
        max_wc_ratio: form.max_wc_ratio.value || null,
        min_cement_content: form.min_cement_content.value || null,
    };
    
    try {
        const resp = await fetch('/api/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });
        
        const json = await resp.json();
        
        if (!json.success) {
            showError(json.error);
            return;
        }
        
        renderResults(json.result, json.trace);
        showResults();
        
    } catch (err) {
        showError('Network error: ' + err.message);
    } finally {
        btnCalculate.classList.remove('loading');
    }
});

// ── Render results ──
function renderResults(result, trace) {
    const r = result;
    
    resultsGrid.innerHTML = `
        <div class="result-row section-header">
            <span class="result-label">Stage 1 — Target Strength</span>
        </div>
        <div class="result-row">
            <span class="result-label">Target Mean Strength</span>
            <span class="result-value">${r.target_mean_strength}<span class="unit-small">N/mm²</span></span>
        </div>
        
        <div class="result-row section-header">
            <span class="result-label">Stage 2 — Water / Cement</span>
        </div>
        <div class="result-row">
            <span class="result-label">Water/Cement Ratio</span>
            <span class="result-value">${r.water_cement_ratio}</span>
        </div>
        <div class="result-row">
            <span class="result-label">Free Water Content</span>
            <span class="result-value">${r.free_water_content}<span class="unit-small">kg/m³</span></span>
        </div>
        
        <div class="result-row section-header">
            <span class="result-label">Stage 3 — Cement</span>
        </div>
        <div class="result-row highlight">
            <span class="result-label">Cement Content</span>
            <span class="result-value">${r.cement_content}<span class="unit-small">kg/m³</span></span>
        </div>
        
        <div class="result-row section-header">
            <span class="result-label">Stage 4 — Density & Aggregate</span>
        </div>
        <div class="result-row">
            <span class="result-label">Total Aggregate</span>
            <span class="result-value">${r.total_aggregate}<span class="unit-small">kg/m³</span></span>
        </div>
        
        <div class="result-row section-header">
            <span class="result-label">Stage 5 — Aggregate Split</span>
        </div>
        <div class="result-row highlight">
            <span class="result-label">Fine Aggregate</span>
            <span class="result-value">${r.fine_aggregate}<span class="unit-small">kg/m³</span></span>
        </div>
        <div class="result-row highlight">
            <span class="result-label">Coarse Aggregate</span>
            <span class="result-value">${r.coarse_aggregate}<span class="unit-small">kg/m³</span></span>
        </div>
    `;
    
    // Render trace
    traceContent.innerHTML = trace.map(step => `
        <div class="trace-step">
            <div class="trace-step-header">
                <span class="trace-step-id">${step.step_id}</span>
                <span class="trace-step-source">${step.source}</span>
            </div>
            <div class="trace-step-desc">${step.description}</div>
            <div class="trace-step-eq">${step.equation}</div>
            <div class="trace-io">
                <div class="trace-io-block">
                    <h5>Inputs</h5>
                    <pre>${formatObj(step.inputs)}</pre>
                </div>
                <div class="trace-io-block">
                    <h5>Output</h5>
                    <pre>${formatObj(step.output)}</pre>
                </div>
            </div>
            ${step.warnings.length ? `<div style="margin-top:6px;font-size:11px;color:var(--warning)">⚠ ${step.warnings.join(', ')}</div>` : ''}
        </div>
    `).join('');
}

function formatObj(obj) {
    if (typeof obj !== 'object' || obj === null) return String(obj);
    return Object.entries(obj)
        .map(([k, v]) => {
            const val = typeof v === 'number' ? (Number.isInteger(v) ? v : v.toFixed(4)) : v;
            return `${k}: ${val}`;
        })
        .join('\n');
}

// ── Navigation ──
function showResults() {
    inputPanel.classList.add('hidden');
    resultsPanel.classList.remove('hidden');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function showInput() {
    resultsPanel.classList.add('hidden');
    inputPanel.classList.remove('hidden');
}

// ── Trace toggle ──
function toggleTrace() {
    const btn = document.querySelector('.trace-toggle');
    const content = document.getElementById('traceContent');
    btn.classList.toggle('open');
    content.classList.toggle('hidden');
}

// ── Error handling ──
function showError(msg) {
    errorMsg.textContent = msg;
    errorToast.classList.remove('hidden');
    setTimeout(hideError, 8000);
}

function hideError() {
    errorToast.classList.add('hidden');
}
