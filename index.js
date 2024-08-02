document.addEventListener('DOMContentLoaded', () => {
    // Interactivity for the Start Trading button
    document.getElementById('startButton').addEventListener('click', () => {
        alert('Trading is fun!');
    });

    // Toggle additional information in the About section
    document.getElementById('learnMoreButton').addEventListener('click', () => {
        const additionalInfo = document.getElementById('additionalInfo');
        if (additionalInfo.style.display === 'none') {
            additionalInfo.style.display = 'block';
        } else {
            additionalInfo.style.display = 'none';
        }
    });

    // Handle form submission
    document.getElementById('contactForm').addEventListener('submit', (event) => {
        event.preventDefault();
        document.getElementById('formFeedback').style.display = 'block';
    });
});
