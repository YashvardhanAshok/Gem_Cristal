const toggleButton = document.getElementById('toggleButton');
const body = document.body;

toggleButton.addEventListener('click', () => {
    console.log("hi")
  body.classList.toggle('dark');
});

