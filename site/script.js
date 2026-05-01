const copyButton = document.querySelector("[data-copy-target]");

if (copyButton) {
  copyButton.addEventListener("click", async () => {
    const targetId = copyButton.getAttribute("data-copy-target");
    const target = targetId ? document.getElementById(targetId) : null;

    if (!target) {
      return;
    }

    const copyText = target.dataset.copyText || target.textContent.trim();

    try {
      await navigator.clipboard.writeText(copyText);
      copyButton.textContent = "복사됨";
      window.setTimeout(() => {
        copyButton.textContent = "복사";
      }, 1400);
    } catch {
      copyButton.textContent = "선택";
      window.setTimeout(() => {
        copyButton.textContent = "복사";
      }, 1400);
    }
  });
}
