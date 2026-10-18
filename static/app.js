document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("checkinForm");
  if (!form) return;
  const inputs = [...form.querySelectorAll('input[type="radio"]')];
  const bar = document.getElementById("progressBar");
  const text = document.getElementById("progressText");
  const total = new Set(inputs.map(input => input.name)).size;
  function updateProgress() {
    const answered = new Set(inputs.filter(input => input.checked).map(input => input.name)).size;
    bar.style.width = `${(answered / total) * 100}%`;
    const isTelugu = document.documentElement.lang === "te";
    text.textContent = isTelugu ? `${total}లో ${answered} సమాధానాలు` : `${answered} of ${total} answered`;
  }
  inputs.forEach(input => input.addEventListener("change", updateProgress));
  updateProgress();
});
