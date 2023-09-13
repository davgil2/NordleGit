document.addEventListener('DOMContentLoaded', function () {
    const guessForm = document.getElementById('guessForm');
    const userInput = document.getElementById('userInput');
    const feedbackTable = document.getElementById('feedbackTable');

    guessForm.addEventListener('submit', function (event) {
        event.preventDefault();
        
        // Send the user's guess to the Flask backend
        fetch('/guess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_input: userInput.value
            })
        })
        .then(response => response.json())
        .then(data => {
            // Use the feedback from Flask to update the table
            // Here, we assume the feedback is a list where each item is either 'grey', 'yellow', or 'green'
            const feedbackColors = data.feedback;

            for (let i = 0; i < feedbackColors.length; i++) {
                const row = feedbackTable.rows[Math.floor(i / 5)];
                const cell = row.cells[i % 5];
                cell.style.backgroundColor = feedbackColors[i];
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    
});

