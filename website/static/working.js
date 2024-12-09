document.getElementById('fake-news-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const newsText = document.getElementById('news-input').value;
  const resultDiv = document.getElementById('result');

  // Simulate detection logic (replace with real logic or API call)
  const isFake = Math.random() > 0.5; // Randomized for demonstration
  resultDiv.textContent = isFake ? "Fake News Detected!" : "This news appears to be genuine.";
  resultDiv.style.color = isFake ? "#ff4500" : "#32cd32";
});
