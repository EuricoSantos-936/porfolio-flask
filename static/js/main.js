$(document).ready(function(){
	$(".nav-link").on('click', function(event) {

    	if (this.hash !== "") {

			event.preventDefault();

			var hash = this.hash;

			$('html, body').animate({
				scrollTop: $(hash).offset().top
			}, 700, function(){
				window.location.hash = hash;
			});
      	} 
    });
});

//Typewriter effect
var app = document.getElementById('typewriter');

        var typewriter = new Typewriter(app, {
            loop: true
        });

        typewriter.typeString('Python Developer')
            .pauseFor(2500)
            .deleteAll()
            .typeString('Back-end Developer')
            .pauseFor(2500)
            .deleteAll()
            .typeString('Let\'s create new projects together!')
            .pauseFor(2500)
            .start();


// Lottie animation setup
var animation = lottie.loadAnimation({
	container: document.getElementById('man-animation'),
	renderer: 'svg',
	loop: true,
	autoplay: true,
	path: 'static/animations/animation_lo4pd2il.json'
  });


  var animation = lottie.loadAnimation({
	container: document.getElementById('avatar'),
	renderer: 'svg',
	loop: true,
	autoplay: true,
	path: 'static/animations/Animation - 1719093509398.json'
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

	document.getElementById('exampleInputName').value = '';
	document.getElementById('exampleInputEmail1').value = '';
	document.querySelector('textarea[name="contact-message"]').value = '';
});
  