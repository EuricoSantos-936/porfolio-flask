document.addEventListener('DOMContentLoaded', (event) => {
    const typewriterElement = document.getElementById('typewriter');
    if (typewriterElement) {
        const typewriter = new Typewriter(typewriterElement, {
            loop: true
        });

        typewriter
            .typeString('Python Developer')
            .pauseFor(2000)
            .deleteAll()
            .typeString('Backend Developer')
            .pauseFor(2000)
            .deleteAll()
            .start();
    } else {
        console.error('Element with id "typewriter" not found.');
    }
});
