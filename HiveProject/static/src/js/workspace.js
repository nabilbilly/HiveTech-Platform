function checkWorkspaceExists(workspaceName) {
    const teamExistsError = document.getElementById('team-exists-error'); // Error message container
    const submitButton = document.querySelector("button[type='submit']"); // Submit button

    if (workspaceName.trim()) {
        fetch(`/Teamworkspace/check_team_exists/?team_slug=${encodeURIComponent(workspaceName)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.team_exists) {
                    // Show error message
                    teamExistsError.style.display = 'block';
                } else {
                    // Hide error message if the team doesn't exist
                    teamExistsError.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error checking workspace existence:', error);
            });
    } else {
        // Reset the error message when the input is empty
        teamExistsError.style.display = 'none';
    }
}
