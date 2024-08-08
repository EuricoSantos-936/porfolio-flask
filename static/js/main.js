$(document).ready(function() {
    // Smooth scrolling for navigation links
    $(".nav-link").on('click', function(event) {
        var hash = this.hash;
        
        // Verify if hash is not empty and if element exists
        if (hash !== "" && $(hash).length) {
            event.preventDefault();
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function() {
                window.location.hash = hash;
            });
        }
    });

    // Check if the URL contains a hash and scroll to it on page load
    if (window.location.hash && $(window.location.hash).length) {
        var hash = window.location.hash;
        $('html, body').scrollTop($(hash).offset().top);
    }

    // Typewriter effect
    var typewriterElement = document.getElementById('typewriter');
    if (typewriterElement) {
        var typewriter = new Typewriter(typewriterElement, {
            loop: true
        });

        typewriter.typeString('Full-stack Developer')
            .pauseFor(2500)
            .deleteAll()
            .typeString('Python - Flask and Django')
            .pauseFor(2500)
            .deleteAll()
            .typeString('Javascript - React.js and Vue.js')
            .pauseFor(2500)
            .deleteAll()
            .typeString('Let\'s create new projects together!')
            .pauseFor(2500)
            .start();
    }

    // Lottie animation setup
    var lottieContainers = [
        { containerId: 'man-animation', path: 'static/animations/animation_lo4pd2il.json' },
        { containerId: 'avatar', path: 'static/animations/animation-1719093509398.json' }
    ];

    lottieContainers.forEach(function(config) {
        var container = document.getElementById(config.containerId);
        if (container) {
            lottie.loadAnimation({
                container: container,
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: config.path
            });
        }
    });

    // Contact form EmailJS
    emailjs.init('7ifx8mL0NF5Wsjynh');

    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();

        var formData = {
            from_name: document.getElementById('exampleInputName').value,
            reply_to: document.getElementById('exampleInputEmail1').value,
            message: document.querySelector('textarea[name="contact-message"]').value
        };

        emailjs.send('service_203xt6v', 'template_maljbz7', formData)
            .then(function(response) {
                console.log('Email sent with success!', response.status, response.text);
            }, function(error) {
                console.error('Error sending email:', error);
            });

        // Clear form fields
        document.getElementById('exampleInputName').value = '';
        document.getElementById('exampleInputEmail1').value = '';
        document.querySelector('textarea[name="contact-message"]').value = '';
    });
});

function toggleMenu() {
    var components = document.querySelector('.sidebar ul.components');
    components.classList.toggle('show');
}
