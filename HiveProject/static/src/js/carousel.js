
    document.addEventListener('DOMContentLoaded', function () {
        const closeButtons = document.querySelectorAll('.close-btn');
        closeButtons.forEach(button => {
            button.addEventListener('click', function () {
                const message = this.parentElement;
                message.style.display = 'none';
            });
        });
    });
