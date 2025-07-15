from flask import Flask, render_template_string # Use render_template_string for embedded HTML

# --- Initialize Flask (even for static generation, we use its templating engine) ---
app = Flask(__name__)

# --- Dummy Data (replace with database integration in a real app) ---
def get_all_teachers():
    return [
        {"name": "Alice Wonderland", "language": "Spanish", "rating": 4.8, "reviews_count": 120, "bio": "Passionate about Spanish culture and making learning fun.", "image_url": "https://via.placeholder.com/150/FF5733/FFFFFF?text=Alice"},
        {"name": "Bob The Builder", "language": "French", "rating": 4.5, "reviews_count": 90, "bio": "Experienced in French literature and conversational fluency.", "image_url": "https://via.placeholder.com/150/33FF57/FFFFFF?text=Bob"},
        {"name": "Charlie Chaplin", "language": "German", "rating": 4.9, "reviews_count": 150, "bio": "Native German speaker with a focus on practical communication.", "image_url": "https://via.placeholder.com/150/5733FF/FFFFFF?text=Charlie"},
        {"name": "Diana Prince", "language": "Japanese", "rating": 4.7, "reviews_count": 110, "bio": "Loves teaching Japanese through anime and pop culture.", "image_url": "https://via.placeholder.com/150/FF33DA/FFFFFF?text=Diana"},
        {"name": "Eve Adams", "language": "Mandarin", "rating": 4.6, "reviews_count": 85, "bio": "Helps students master tones and characters with ease.", "image_url": "https://via.placeholder.com/150/33A0FF/FFFFFF?text=Eve"},
        {"name": "Frankenstein", "language": "Italian", "rating": 4.2, "reviews_count": 70, "bio": "Bringing the beauty of Italian language and opera to life.", "image_url": "https://via.placeholder.com/150/A0FF33/FFFFFF?text=Frank"},
    ]

def get_all_testimonials():
    return [
        {"author": "Student A", "role": "Beginner Spanish Learner", "rating": 5, "text": "LinguaLearn made learning Spanish incredibly engaging! The interactive lessons are fantastic.", "image_url": "https://via.placeholder.com/100/FF5733/FFFFFF?text=SA", "language_flag": "https://flagsapi.com/ES/flat/32.png"},
        {"author": "Student B", "role": "Intermediate French Speaker", "rating": 4.5, "text": "The personalized path kept me motivated, and I saw significant improvement in my French speaking.", "image_url": "https://via.placeholder.com/100/33FF57/FFFFFF?text=SB", "language_flag": "https://flagsapi.com/FR/flat/32.png"},
        {"author": "Student C", "role": "Advanced German Student", "rating": 5, "text": "The conversation practice with native teachers was a game-changer for my German fluency.", "image_url": "https://via.placeholder.com/100/5733FF/FFFFFF?text=SC", "language_flag": "https://flagsapi.com/DE/flat/32.png"},
        {"author": "Student D", "role": "Japanese Enthusiast", "rating": 4, "text": "Cultural immersion content is superb! Learning Japanese nuances was never this fun.", "image_url": "https://via.placeholder.com/100/FF33DA/FFFFFF?text=SD", "language_flag": "https://flagsapi.com/JP/flat/32.png"},
        {"author": "Student E", "role": "Mandarin Explorer", "rating": 5, "text": "I appreciate the detailed progress tracking. It truly shows how far I've come.", "image_url": "https://via.placeholder.com/100/33A0FF/FFFFFF?text=SE", "language_flag": "https://flagsapi.com/CN/flat/32.png"},
    ]

PRICING_PLANS = [
    {
        "id": "basic",
        "name": "Basic",
        "price": 9.99,
        "features": [
            "Access to all interactive lessons",
            "Basic progress tracking",
            "Community forum access",
        ],
        "excluded_features": [
            "Live group conversation sessions",
            "1-on-1 teacher support",
            "Personalized learning path",
            "Certificates of completion"
        ],
        "popular": False
    },
    {
        "id": "premium",
        "name": "Premium",
        "price": 29.99,
        "features": [
            "All Basic features",
            "Live group conversation sessions (5/month)",
            "Personalized learning path",
            "Enhanced progress reports",
        ],
        "excluded_features": [
            "1-on-1 teacher support",
            "Certificates of completion"
        ],
        "popular": True
    },
    {
        "id": "vip",
        "name": "VIP",
        "price": 49.99,
        "features": [
            "All Premium features",
            "1-on-1 teacher support (2 hours/month)",
            "Priority support",
            "Certificates of completion",
            "Exclusive cultural content"
        ],
        "excluded_features": [],
        "popular": False
    }
]

def get_all_blog_posts():
    return [
        {
            "title": "5 Tips for Mastering Pronunciation",
            "date": "July 10, 2025",
            "read_time": "5 min read",
            "content": "Improve your accent and speak like a native with these practical tips and exercises.",
            "image_url": "https://via.placeholder.com/400x200/FF5733/FFFFFF?text=Pronunciation"
        },
        {
            "title": "The Benefits of Learning a New Language",
            "date": "July 5, 2025",
            "read_time": "7 min read",
            "content": "Discover how language learning can boost your cognitive skills and open new opportunities.",
            "image_url": "https://via.placeholder.com/400x200/33FF57/FFFFFF?text=Benefits"
        },
        {
            "title": "Cultural Etiquette: Japanese Bowing",
            "date": "June 28, 2025",
            "read_time": "4 min read",
            "content": "Understand the nuances of bowing in Japanese culture for respectful communication.",
            "image_url": "https://via.placeholder.com/400x200/5733FF/FFFFFF?text=Culture"
        },
    ]

# --- HTML Template (Embedded as a string) ---
# IMPORTANT: The action for the contact form is set to '#' or a dummy value
# because this script is generating a STATIC HTML file.
# A static HTML file cannot process form submissions directly.
# If you need form functionality, you must run Flask as a web server.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LinguaLearn - Your Language Learning Journey</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        /* Custom animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in-up {
            animation: fadeIn 0.8s ease-out forwards;
            opacity: 0; /* Start invisible */
        }
        .delay-100 { animation-delay: 0.1s; }
        .delay-200 { animation-delay: 0.2s; }
        .delay-300 { animation-delay: 0.3s; }
        .delay-400 { animation-delay: 0.4s; }
        .delay-500 { animation-delay: 0.5s; }
        .delay-600 { animation-delay: 0.6s; }

        /* Smooth scrolling */
        html {
            scroll-behavior: smooth;
        }

        /* Hero section specific styles for background image overlay */
        .hero-background {
            background-image: url('https://images.unsplash.com/photo-1549247754-cf3d5371c19b?fit=crop&w=1920&h=1080&q=80'); /* Replace with your image */
            background-size: cover;
            background-position: center;
            position: relative;
        }
        .hero-background::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.6); /* Dark overlay */
        }
        .hero-content {
            position: relative;
            z-index: 10;
        }

        /* Mobile menu overlay */
        #mobile-menu.open {
            display: block;
        }
    </style>
</head>
<body class="bg-gray-900 text-white font-sans">

    <header class="bg-gray-900 shadow-lg fixed top-0 left-0 w-full z-50">
        <nav class="container mx-auto px-6 py-4 flex items-center justify-between">
            <a href="#" class="text-3xl font-bold text-blue-500 flex items-center">
                <i class="fas fa-language mr-2"></i> LinguaLearn
            </a>
            <div class="hidden md:flex space-x-8">
                <a href="#features" class="text-gray-300 hover:text-white transition duration-300">Features</a>
                <a href="#how-it-works" class="text-gray-300 hover:text-white transition duration-300">How It Works</a>
                <a href="#teachers" class="text-gray-300 hover:text-white transition duration-300">Teachers</a>
                <a href="#testimonials" class="text-gray-300 hover:text-white transition duration-300">Testimonials</a>
                <a href="#pricing" class="text-gray-300 hover:text-white transition duration-300">Pricing</a>
                <a href="#faq" class="text-gray-300 hover:text-white transition duration-300">FAQ</a>
                <a href="#blog" class="text-gray-300 hover:text-white transition duration-300">Blog</a>
                <a href="#contact" class="text-gray-300 hover:text-white transition duration-300">Contact</a>
            </div>
            <div class="hidden md:flex space-x-4">
                <a href="#" class="bg-gray-700 text-white px-6 py-2 rounded-full hover:bg-gray-600 transition duration-300">Sign In</a>
                <a href="#" class="bg-blue-600 text-white px-6 py-2 rounded-full hover:bg-blue-700 transition duration-300">Sign Up</a>
            </div>
            <div class="md:hidden">
                <button id="mobile-menu-button" class="text-gray-300 focus:outline-none focus:text-white">
                    <i class="fas fa-bars text-2xl"></i>
                </button>
            </div>
        </nav>
        <div id="mobile-menu" class="hidden md:hidden bg-gray-800 p-6">
            <ul class="flex flex-col space-y-4">
                <li><a href="#features" class="block text-gray-300 hover:text-white py-2">Features</a></li>
                <li><a href="#how-it-works" class="block text-gray-300 hover:text-white py-2">How It Works</a></li>
                <li><a href="#teachers" class="block text-gray-300 hover:text-white py-2">Teachers</a></li>
                <li><a href="#testimonials" class="block text-gray-300 hover:text-white py-2">Testimonials</a></li>
                <li><a href="#pricing" class="block text-gray-300 hover:text-white py-2">Pricing</a></li>
                <li><a href="#faq" class="block text-gray-300 hover:text-white py-2">FAQ</a></li>
                <li><a href="#blog" class="block text-gray-300 hover:text-white py-2">Blog</a></li>
                <li><a href="#contact" class="block bg-gray-700 text-white text-center px-4 py-2 rounded-full hover:bg-gray-600 mt-2">Sign In</a></li>
                <li><a href="#" class="block bg-blue-600 text-white text-center px-4 py-2 rounded-full hover:bg-blue-700 mt-2">Sign Up</a></li>
            </ul>
        </div>
    </header>

    <main class="pt-20"> <section class="hero-background relative py-20 md:py-32 text-center text-white flex items-center justify-center">
            <div class="hero-content container mx-auto px-6">
                <h1 class="text-5xl md:text-6xl font-extrabold leading-tight mb-6 animate-fade-in-up">
                    Unlock New Worlds Through Language
                </h1>
                <p class="text-xl md:text-2xl mb-8 animate-fade-in-up delay-100">
                    Master any language with interactive lessons, native teachers, and personalized learning paths.
                </p>
                <div class="space-x-4 animate-fade-in-up delay-200">
                    <a href="#pricing" class="bg-blue-600 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-blue-700 transition duration-300 transform hover:scale-105 inline-block">Start Learning Now</a>
                    <a href="#how-it-works" class="bg-transparent border-2 border-white text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-white hover:text-blue-600 transition duration-300 transform hover:scale-105 inline-block">How It Works</a>
                </div>
            </div>
        </section>

        <section id="features" class="py-16 bg-gray-900 text-white">
            <div class="container mx-auto px-6">
                <h2 class="text-4xl font-bold text-center mb-12 animate-fade-in-up">Why Choose LinguaLearn?</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                    <div class="bg-gray-800 p-8 rounded-lg shadow-xl text-center transform hover:scale-105 transition duration-300 animate-fade-in-up delay-200">
                        <i class="fas fa-laptop-code text-5xl text-green-500 mb-6"></i>
                        <h3 class="text-2xl font-bold mb-4">Interactive Lessons</h3>
                        <p class="text-gray-400">Engage with dynamic exercises, real-life simulations, and multimedia content that keeps learning exciting.</p>
                    </div>
                    <div class="bg-gray-800 p-8 rounded-lg shadow-xl text-center transform hover:scale-105 transition duration-300 animate-fade-in-up delay-300">
                        <i class="fas fa-route text-5xl text-purple-500 mb-6"></i>
                        <h3 class="text-2xl font-bold mb-4">Personalized Paths</h3>
                        <p class="text-gray-400">Customized curriculum tailored to your goals, pace, and learning style, ensuring effective progress.</p>
                    </div>
                    <div class="bg-gray-800 p-8 rounded-lg shadow-xl text-center transform hover:scale-105 transition duration-300 animate-fade-in-up delay-400">
                        <i class="fas fa-comments text-5xl text-yellow-500 mb-6"></i>
                        <h3 class="text-2xl font-bold mb-4">Conversation Practice</h3>
                        <p class="text-gray-400">Join small group sessions or 1-on-1 calls to practice speaking with confidence.</p>
                    </div>
                    <div class="bg-gray-800 p-8 rounded-lg shadow-xl text-center transform hover:scale-105 transition duration-300 animate-fade-in-up delay-500">
                        <i class="fas fa-globe-americas text-5xl text-red-500 mb-6"></i>
                        <h3 class="text-2xl font-bold mb-4">Cultural Immersion</h3>
                        <p class="text-gray-400">Go beyond grammar and vocabulary to understand the rich cultural contexts of your target language.</p>
                    </div>
                    <div class="bg-gray-800 p-8 rounded-lg shadow-xl text-center transform hover:scale-105 transition duration-300 animate-fade-in-up delay-600">
                        <i class="fas fa-certificate text-5xl text-teal-500 mb-6"></i>
                        <h3 class="text-2xl font-bold mb-4">Progress Tracking & Certificates</h3>
                        <p class="text-gray-400">Monitor your growth with detailed reports and earn certificates upon course completion.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="how-it-works" class="py-16 bg-gray-800 text-white">
            <div class="container mx-auto px-6">
                <h2 class="text-4xl font-bold text-center mb-12 animate-fade-in-up">How LinguaLearn Works</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
                    <div class="text-center animate-fade-in-up delay-100">
                        <div class="relative w-24 h-24 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-6 shadow-xl">
                            <span class="text-4xl font-extrabold">1</span>
                        </div>
                        <h3 class="text-2xl font-bold mb-3">Choose Your Language</h3>
                        <p class="text-gray-400">Select from a wide range of languages, from popular choices to unique dialects.</p>
                    </div>
                    <div class="text-center animate-fade-in-up delay-200">
                        <div class="relative w-24 h-24 bg-green-600 rounded-full flex items-center justify-center mx-auto mb-6 shadow-xl">
                            <span class="text-4xl font-extrabold">2</span>
                        </div>
                        <h3 class="text-2xl font-bold mb-3">Personalize Your Path</h3>
                        <p class="text-gray-400">Take a quick assessment to get a tailored learning plan based on your level and goals.</p>
                    </div>
                    <div class="text-center animate-fade-in-up delay-300">
                        <div class="relative w-24 h-24 bg-purple-600 rounded-full flex items-center justify-center mx-auto mb-6 shadow-xl">
                            <span class="text-4xl font-extrabold">3</span>
                        </div>
                        <h3 class="text-2xl font-bold mb-3">Start Learning & Speaking</h3>
                        <p class="text-gray-400">Engage with interactive lessons, practice with native teachers, and join conversation groups.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="teachers" class="py-16 bg-gray-900 text-white">
            <div class="container mx-auto px-6">
                <h2 class="text-4xl font-bold text-center mb-12 animate-fade-in-up">Meet Our Expert Teachers</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                    {% for teacher in teachers %}
                    <div class="bg-gray-800 p-6 rounded-lg shadow-sm hover:shadow-md transition duration-300 teacher-card animate-fade-in-up">
                        <div class="text-center mb-4">
                            <img src="{{ teacher.image_url }}" alt="{{ teacher.name }}" class="w-24 h-24 rounded-full object-cover mx-auto mb-3">
                            <h3 class="text-xl font-bold">{{ teacher.name }}</h3>
                        </div>
                        <div class="mb-3">
                            <span class="text-gray-400">{{ teacher.language }} Teacher</span>
                        </div>
                        <div class="text-yellow-400 mb-3">
                            {% for _ in range(teacher.rating | int) %}<i class="fas fa-star"></i>{% endfor %}
                            {% if teacher.rating % 1 != 0 %}<i class="fas fa-star-half-alt"></i>{% endif %}
                            <span class="text-gray-400 text-sm ml-1">({{ teacher.reviews_count }} reviews)</span>
                        </div>
                        <p class="text-gray-400 mb-4">{{ teacher.bio }}</p>
                        <a href="#" class="text-blue-500 hover:text-blue-400 font-medium">View Profile <i class="fas fa-arrow-right ml-1"></i></a>
                    </div>
                    {% endfor %}
                </div>
                <div class="text-center mt-12">
                    <a href="#" class="bg-blue-600 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-blue-700 transition duration-300 transform hover:scale-105">View All Teachers</a>
                </div>
            </div>
        </section>

        <section id="testimonials" class="py-16 bg-gray-800 text-white">
            <div class="container mx-auto px-6">
                <h2 class="text-4xl font-bold text-center mb-12 animate-fade-in-up">What Our Students Say</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                    {% for testimonial in testimonials %}
                    <div class="bg-gray-900 p-8 rounded-lg shadow-xl animate-fade-in-up">
                        <div class="flex items-center mb-4">
                            <img src="{{ testimonial.image_url }}" alt="{{ testimonial.author }}" class="w-16 h-16 rounded-full object-cover mr-4">
                            <div>
                                <p class="font-bold text-lg">{{ testimonial.author }}</p>
                                <p class="text-gray-400 text-sm">{{ testimonial.role }}</p>
                            </div>
                            <img src="{{ testimonial.language_flag }}" alt="Language Flag" class="w-8 h-6 ml-auto">
                        </div>
                        <div class="text-yellow-400 mb-4">
                            {% for _ in range(testimonial.rating | int) %}<i class="fas fa-star"></i>{% endfor %}
                            {% if testimonial.rating % 1 != 0 %}<i class="fas fa-star-half-alt"></i>{% endif %}
                        </div>
                        <p class="text-gray-300 italic">"{{ testimonial.text }}"</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section class="py-16 bg-blue-600 text-white text-center">
            <div class="container mx-auto px-6">
                <h2 class="text-4xl font-bold mb-4 animate-fade-in-up">Ready to Start Your Language Journey?</h2>
                <p class="text-xl mb-8 animate-fade-in-up delay-100">Join thousands of happy learners and unlock new possibilities.</p>
                <a href="#pricing" class="bg-white text-blue-600 px-10 py-5 rounded-full font-bold text-xl hover:bg-gray-100 transition duration-300 transform hover:scale-105 animate-fade-in-up delay-200">Get Started Today!</a>
            </div>
        </section>

        <section id="pricing" class="py-16 bg-gray-900 text-white">
            <div class="container mx-auto px-6">
                <h2 class="text-4xl font-bold text-center mb-12 animate-fade-in-up">Flexible Pricing Plans</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    {% for plan in pricing_plans %}
                    <div class="bg-gray-800 border {% if plan.popular %}border-2 border-blue-500 shadow-lg relative{% else %}border-gray-700{% endif %} rounded-lg p-8 hover:border-blue-500 transition duration-300 animate-fade-in-up">
                        {% if plan.popular %}
                        <div class="absolute top-0 right-0 bg-blue-600 text-white px-3 py-1 rounded-bl-lg rounded-tr-lg text-xs font-medium">
                            Most Popular
                        </div>
                        {% endif %}
                        <h3 class="text-xl font-bold mb-2">{{ plan.name }}</h3>
                        <p class="text-gray-400 mb-6">
                            {% if plan.id == 'basic' %}For casual learners who want to explore{% elif plan.id == 'premium' %}For serious learners who want fast results{% elif plan.id == 'vip' %}For maximum progress with personalized attention{% endif %}
                        </p>
                        <div class="mb-6">
                            <span class="text-4xl font-bold">${{ "%.2f"|format(plan.price) }}</span>
                            <span class="text-gray-400">/month</span>
                        </div>
                        <ul class="space-y-3 mb-8">
                            {% for feature in plan.features %}
                            <li class="flex items-start">
                                <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                <span class="text-gray-300">{{ feature }}</span>
                            </li>
                            {% endfor %}
                            {% for feature in plan.excluded_features %}
                            <li class="flex items-start text-gray-500">
                                <i class="fas fa-times mt-1 mr-2"></i>
                                <span>{{ feature }}</span>
                            </li>
                            {% endfor %}
                        </ul>
                        <a href="#" class="block w-full text-center px-6 py-3 {% if plan.popular %}bg-blue-600 text-white hover:bg-blue-700{% else %}border-2 border-blue-600 text-blue-500 hover:bg-blue-900{% endif %} rounded-md font-medium">Get Started</a>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section id="faq" class="py-16 bg-gray-800 text-white">
            <div class="container mx-auto px-6">
                <h2 class="text-4xl font-bold text-center mb-12 animate-fade-in-up">Frequently Asked Questions</h2>
                <div class="max-w-3xl mx-auto space-y-6">
                    <div class="bg-gray-900 p-6 rounded-lg shadow-md animate-fade-in-up">
                        <button class="faq-toggle w-full flex justify-between items-center text-left font-bold text-lg focus:outline-none">
                            <span>What languages do you offer?</span>
                            <i class="fas fa-chevron-down transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden mt-4 text-gray-300">
                            We offer a wide range of languages including Spanish, French, German, Japanese, Mandarin, Korean, Italian, Arabic, and many more. Our catalog is constantly expanding!
                        </div>
                    </div>
                    <div class="bg-gray-900 p-6 rounded-lg shadow-md animate-fade-in-up delay-100">
                        <button class="faq-toggle w-full flex justify-between items-center text-left font-bold text-lg focus:outline-none">
                            <span>How do live classes work?</span>
                            <i class="fas fa-chevron-down transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden mt-4 text-gray-300">
                            Our live classes are conducted via integrated video conferencing. You can join group sessions or schedule one-on-one lessons with your chosen teacher at a time that suits you.
                        </div>
                    </div>
                    <div class="bg-gray-900 p-6 rounded-lg shadow-md animate-fade-in-up delay-200">
                        <button class="faq-toggle w-full flex justify-between items-center text-left font-bold text-lg focus:outline-none">
                            <span>Can I get a refund?</span>
                            <i class="fas fa-chevron-down transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden mt-4 text-gray-300">
                            Please refer to our <a href="#" class="text-blue-400 hover:underline">Refund Policy</a> for detailed information on eligibility and procedures.
                        </div>
                    </div>
                    <div class="bg-gray-900 p-6 rounded-lg shadow-md animate-fade-in-up delay-300">
                        <button class="faq-toggle w-full flex justify-between items-center text-left font-bold text-lg focus:outline-none">
                            <span>Do you offer certification?</span>
                            <i class="fas fa-chevron-down transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden mt-4 text-gray-300">
                            Yes, upon successful completion of certain courses, you can earn a LinguaLearn certificate of proficiency.
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="blog" class="py-16 bg-gray-900 text-white">
            <div class="container mx-auto px-6">
                <h2 class="text-4xl font-bold text-center mb-12 animate-fade-in-up">Latest from Our Blog</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                    {% for post in blog_posts %}
                    <div class="bg-gray-800 rounded-lg shadow-lg overflow-hidden animate-fade-in-up">
                        <img src="{{ post.image_url }}" alt="{{ post.title }}" class="w-full h-48 object-cover">
                        <div class="p-6">
                            <h3 class="text-xl font-bold mb-2">{{ post.title }}</h3>
                            <p class="text-gray-400 text-sm mb-3">{{ post.date }} &bull; {{ post.read_time }}</p>
                            <p class="text-gray-300 mb-4">{{ post.content }}</p>
                            <a href="#" class="text-blue-500 hover:text-blue-400 font-medium">Read More <i class="fas fa-arrow-right ml-1"></i></a>
                        </div>
                    </div>
                    {% endfor %}
                </div>
                <div class="text-center mt-12">
                    <a href="#" class="bg-blue-600 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-blue-700 transition duration-300 transform hover:scale-105">View All Blog Posts</a>
                </div>
            </div>
        </section>

        <section id="contact" class="py-16 bg-gray-800 text-white">
            <div class="container mx-auto px-6">
                <h2 class="text-4xl font-bold text-center mb-12 animate-fade-in-up">Get in Touch</h2>
                <div class="max-w-xl mx-auto bg-gray-900 p-8 rounded-lg shadow-xl animate-fade-in-up">
                    <p class="text-gray-300 mb-6 text-center">Have questions? We're here to help!</p>
                    <form class="space-y-6" action="#" method="POST"> {# Action set to '#' for static file #}
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label for="first-name" class="block text-gray-300 text-sm font-bold mb-2">First Name</label>
                                <input type="text" id="first-name" name="first-name" class="shadow appearance-none border rounded w-full py-3 px-4 text-gray-900 leading-tight focus:outline-none focus:shadow-outline bg-gray-700 border-gray-600" required>
                            </div>
                            <div>
                                <label for="last-name" class="block text-gray-300 text-sm font-bold mb-2">Last Name</label>
                                <input type="text" id="last-name" name="last-name" class="shadow appearance-none border rounded w-full py-3 px-4 text-gray-900 leading-tight focus:outline-none focus:shadow-outline bg-gray-700 border-gray-600" required>
                            </div>
                        </div>
                        <div>
                            <label for="email" class="block text-gray-300 text-sm font-bold mb-2">Email</label>
                            <input type="email" id="email" name="email" class="shadow appearance-none border rounded w-full py-3 px-4 text-gray-900 leading-tight focus:outline-none focus:shadow-outline bg-gray-700 border-gray-600" required>
                        </div>
                        <div>
                            <label for="subject" class="block text-gray-300 text-sm font-bold mb-2">Subject</label>
                            <input type="text" id="subject" name="subject" class="shadow appearance-none border rounded w-full py-3 px-4 text-gray-900 leading-tight focus:outline-none focus:shadow-outline bg-gray-700 border-gray-600" required>
                        </div>
                        <div>
                            <label for="message" class="block text-gray-300 text-sm font-bold mb-2">Message</label>
                            <textarea id="message" name="message" rows="5" class="shadow appearance-none border rounded w-full py-3 px-4 text-gray-900 leading-tight focus:outline-none focus:shadow-outline bg-gray-700 border-gray-600" required></textarea>
                        </div>
                        <button type="submit" class="w-full px-6 py-3 bg-blue-600 text-white rounded-md font-medium hover:bg-blue-700 transition duration-300 transform hover:scale-105">Send Message</button>
                    </form>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-gray-900 text-white py-12">
        <div class="container mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12">
                <div>
                    <h3 class="text-xl font-bold mb-4 flex items-center">
                        <i class="fas fa-language mr-2"></i>
                        LinguaLearn
                    </h3>
                    <p class="text-gray-400 mb-4">Making language learning accessible, engaging, and effective for everyone, everywhere.</p>
                    <div class="flex space-x-4">
                        <a href="#" class="w-10 h-10 rounded-full bg-gray-700 text-white flex items-center justify-center hover:bg-blue-600">
                            <i class="fab fa-facebook-f"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full bg-gray-700 text-white flex items-center justify-center hover:bg-blue-400">
                            <i class="fab fa-twitter"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full bg-gray-700 text-white flex items-center justify-center hover:bg-pink-600">
                            <i class="fab fa-instagram"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full bg-gray-700 text-white flex items-center justify-center hover:bg-red-600">
                            <i class="fab fa-youtube"></i>
                        </a>
                    </div>
                </div>

                <div>
                    <h3 class="text-lg font-bold mb-4">Quick Links</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white">Home</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">About Us</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Courses</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Teachers</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Pricing</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Blog</a></li>
                    </ul>
                </div>

                <div>
                    <h3 class="text-lg font-bold mb-4">Support</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white">Help Center</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Contact Us</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">FAQs</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">System Requirements</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Feedback</a></li>
                    </ul>
                </div>

                <div>
                    <h3 class="text-lg font-bold mb-4">Legal</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white">Terms of Service</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Privacy Policy</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Cookie Policy</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Refund Policy</a></li>
                    </ul>
                </div>
            </div>

            <div class="pt-8 border-t border-gray-800">
                <div class="flex flex-col md:flex-row justify-between items-center">
                    <p class="text-gray-400 mb-4 md:mb-0">© 2025 LinguaLearn. All rights reserved.</p>
                    <div class="flex space-x-6">
                        <a href="#" class="text-gray-400 hover:text-white">Terms</a>
                        <a href="#" class="text-gray-400 hover:text-white">Privacy</a>
                        <a href="#" class="text-gray-400 hover:text-white">Cookies</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <script>
        // Mobile menu toggle
        document.getElementById('mobile-menu-button').addEventListener('click', function() {
            const menu = document.getElementById('mobile-menu');
            menu.classList.toggle('hidden'); // Assuming 'hidden' is used for visibility in Tailwind
            menu.classList.toggle('open');
        });

        // FAQ toggle functionality
        document.querySelectorAll('.faq-toggle').forEach(button => {
            button.addEventListener('click', () => {
                const content = button.nextElementSibling;
                const icon = button.querySelector('i');

                // Toggle content visibility
                content.classList.toggle('hidden');

                // Rotate icon: You'll need to define 'rotate-180' class in your CSS or directly manipulate
                // For Font Awesome chevron, toggle between 'fa-chevron-down' and 'fa-chevron-up'
                if (icon.classList.contains('fa-chevron-down')) {
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-up');
                } else {
                    icon.classList.remove('fa-chevron-up');
                    icon.classList.add('fa-chevron-down');
                }
            });
        });
    </script>
</body>
</html>
"""

# --- Function to generate the static HTML ---
def generate_static_html(output_filename="linguage_learning_platform.html"):
    """
    Renders the embedded HTML_TEMPLATE with data and saves it as a static HTML file.
    """
    # Create an application context to use render_template_string outside of a request
    with app.app_context():
        # Prepare the data for the template
        teachers = get_all_teachers()[:3]
        testimonials = get_all_testimonials()
        blog_posts = get_all_blog_posts()

        # Render the template string
        rendered_html = render_template_string(
            HTML_TEMPLATE,
            teachers=teachers,
            testimonials=testimonials,
            pricing_plans=PRICING_PLANS,
            blog_posts=blog_posts
        )

        # Write the rendered HTML to a file
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(rendered_html)

    print(f"HTML file '{output_filename}' generated successfully!")

# --- Main execution block ---
if __name__ == '__main__':
    generate_static_html()