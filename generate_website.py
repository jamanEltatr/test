import os

def create_urbanstyle_html():
    """
    Generates the HTML content for the UrbanStyle modern fashion shop
    and saves it to a specified HTML file with requested optimizations.
    """
    html_content = """
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UrbanStyle - Modern Fashion Shop</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class', // Enable dark mode via class
            theme: {
                extend: {
                    colors: {
                        primary: {
                            50: '#eef2ff',
                            100: '#e0e7ff',
                            200: '#c7d2fe',
                            300: '#a5b4fc',
                            400: '#818cf8',
                            500: '#6366f1', // Equivalent to original indigo-600
                            600: '#4f46e5',
                            700: '#4338ca',
                            800: '#3730a3',
                            900: '#312e81',
                            950: '#1e1b4b',
                        },
                        secondary: '#888', // Custom color for scrollbar thumb, etc.
                        accent: '#facc15', // Custom color for stars (yellow-400)
                        danger: '#ef4444', // Custom color for sale (red-500)
                        success: '#22c55e', // Custom color for new (green-500)
                        backgroundLight: '#f9fafb', // Replaced gray-50
                        backgroundDark: '#111827', // Dark mode background
                        textLight: '#1f2937', // Replaced gray-700
                        textDark: '#f3f4f6', // Dark mode text
                    },
                }
            }
        }
    </script>
    <style>
        /* Custom animations */
        @keyframes slideDownFadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-slideDownFadeIn {
            animation: slideDownFadeIn 0.3s ease-out forwards;
        }

        /* Navbar blur effect */
        .navbar-blur {
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            background-color: rgba(255, 255, 255, 0.8); /* Light mode */
        }
        .dark .navbar-blur {
            background-color: rgba(17, 24, 39, 0.8); /* Dark mode */
        }

        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: theme('colors.gray.200'); /* Tailwind gray-200 */
        }
        ::-webkit-scrollbar-thumb {
            background: theme('colors.primary.500'); /* Using primary color */
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: theme('colors.primary.600');
        }

        /* Cart dropdown animation (controlled by JS classes) */
        .cart-dropdown {
            display: none;
            opacity: 0;
            transform: translateY(-20px);
            transition: opacity 0.3s ease-out, transform 0.3s ease-out;
            pointer-events: none; /* Prevent interaction when hidden */
        }
        .cart-dropdown.open {
            display: block;
            opacity: 1;
            transform: translateY(0);
            pointer-events: auto;
        }
        
        /* Mobile menu */
        .mobile-menu {
            transform: translateX(100%);
            transition: transform 0.3s ease;
        }
        .mobile-menu.open {
            transform: translateX(0);
        }

        /* Product Quick View Modal */
        .modal {
            display: none;
            background-color: rgba(0, 0, 0, 0.6);
        }
        .modal.open {
            display: flex;
        }
    </style>
</head>
<body class="bg-backgroundLight dark:bg-backgroundDark text-textLight dark:text-textDark font-sans transition-colors duration-300">
    <div id="quick-view-modal" class="modal fixed inset-0 z-[100] items-center justify-center p-4">
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-2xl w-full p-6 relative transform transition-all duration-300 scale-95 opacity-0" aria-modal="true" role="dialog" aria-labelledby="quick-view-title">
            <button class="absolute top-4 right-4 text-gray-500 hover:text-gray-700 dark:hover:text-gray-300" id="close-quick-view" aria-label="Close Quick View">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
            <h3 id="quick-view-title" class="text-2xl font-bold mb-4 text-textLight dark:text-textDark">Product Quick View</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <img id="quick-view-image" src="" alt="Product Image" class="w-full h-auto rounded-md object-cover">
                </div>
                <div>
                    <h4 id="quick-view-name" class="text-xl font-bold mb-2"></h4>
                    <p id="quick-view-price" class="text-primary-600 dark:text-primary-400 text-lg font-semibold mb-4"></p>
                    <p class="text-gray-600 dark:text-gray-300 text-sm mb-4">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                    </p>
                    <button class="add-to-cart bg-primary-600 hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-md transition" id="quick-view-add-to-cart" aria-label="Add to cart from quick view">
                        Add to Cart
                    </button>
                </div>
            </div>
        </div>
    </div>

    <header class="navbar-blur shadow-sm sticky top-0 z-50 transition-colors duration-300">
        <div class="container mx-auto px-4 py-3 flex justify-between items-center">
            <div class="flex items-center">
                <a href="#" class="text-2xl font-bold text-primary-600 dark:text-primary-400 flex items-center" aria-label="UrbanStyle Home">
                    <svg class="h-8 w-8 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 21v-4m0 0a2 2 0 01-2-2V9m0 0a2 2 0 012-2h4a2 2 0 012 2v6a2 2 0 01-2 2m0 0h-4m-4 0a2 2 0 002 2h4a2 2 0 002-2m-4 0V9m0 0H8m4 0a2 2 0 012-2H8a2 2 0 01-2 2v6a2 2 0 012 2m0 0h4m-4 0a2 2 0 002 2h4a2 2 0 002-2" />
                    </svg>
                    UrbanStyle
                </a>
            </div>
            
            <nav class="hidden md:flex space-x-8">
                <div class="relative group">
                    <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400 font-medium py-3" aria-haspopup="true" aria-expanded="false">
                        Shop
                        <svg class="inline-block h-4 w-4 ml-1 transform group-hover:rotate-180 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                        </svg>
                    </a>
                    <div class="absolute left-0 mt-0 w-48 bg-white dark:bg-gray-700 shadow-lg rounded-md opacity-0 invisible group-hover:opacity-100 group-hover:visible translate-y-2 group-hover:translate-y-0 transition-all duration-300 ease-out z-40">
                        <a href="#" class="block px-4 py-2 text-textLight dark:text-textDark hover:bg-gray-100 dark:hover:bg-gray-600 rounded-t-md">Men's</a>
                        <a href="#" class="block px-4 py-2 text-textLight dark:text-textDark hover:bg-gray-100 dark:hover:bg-gray-600">Women's</a>
                        <a href="#" class="block px-4 py-2 text-textLight dark:text-textDark hover:bg-gray-100 dark:hover:bg-gray-600">Accessories</a>
                        <a href="#" class="block px-4 py-2 text-textLight dark:text-textDark hover:bg-gray-100 dark:hover:bg-gray-600 rounded-b-md">Footwear</a>
                    </div>
                </div>
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400 font-medium">Collections</a>
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400 font-medium">About</a>
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400 font-medium">Contact</a>
            </nav>
            
            <div class="flex items-center space-x-4">
                <button id="theme-toggle" type="button" aria-label="Toggle dark mode"
                    class="text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5">
                    <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>
                    <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 4a1 1 0 011 1v1a1 1 0 11-2 0V7a1 1 0 011-1zm-4 7a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zm-4-4a1 1 0 011 1v1a1 1 0 11-2 0V9a1 1 0 011-1z"></path><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm0-2a6 6 0 100-12 6 6 0 000 12z" clip-rule="evenodd"></path></svg>
                </button>

                <div class="hidden md:block relative cart">
                    <button id="cart-btn" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400" aria-label="View shopping cart" aria-haspopup="true" aria-expanded="false">
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                        </svg>
                        <span id="cart-count" class="absolute -top-2 -right-2 bg-primary-600 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">0</span>
                    </button>
                    <div id="cart-dropdown" class="cart-dropdown absolute right-0 mt-2 w-72 bg-white dark:bg-gray-800 rounded-md shadow-lg p-4 z-40" role="menu">
                        <h3 class="font-bold text-textLight dark:text-textDark mb-2">Your Cart</h3>
                        <div id="cart-items" class="max-h-60 overflow-y-auto">
                            <p class="text-gray-500 text-center py-4">Your cart is empty</p>
                        </div>
                        <div class="border-t border-gray-200 dark:border-gray-700 mt-3 pt-3">
                            <div class="flex justify-between font-bold text-textLight dark:text-textDark mb-3">
                                <span>Total:</span>
                                <span id="cart-total">$0.00</span>
                            </div>
                            <a href="#" class="block w-full bg-primary-600 text-white text-center py-2 rounded-md hover:bg-primary-700 transition" role="menuitem">Checkout</a>
                        </div>
                    </div>
                </div>
                
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400" aria-label="User Account">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                </a>
                
                <button id="mobile-menu-btn" class="md:hidden text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400" aria-label="Open mobile menu">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
                    </svg>
                </button>
            </div>
        </div>
        
        <div id="mobile-menu" class="mobile-menu fixed inset-0 bg-white dark:bg-gray-900 z-50 p-6 md:hidden">
            <div class="flex justify-between items-center mb-8">
                <a href="#" class="text-2xl font-bold text-primary-600 dark:text-primary-400" aria-label="UrbanStyle Home">
                    <svg class="h-8 w-8 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 21v-4m0 0a2 2 0 01-2-2V9m0 0a2 2 0 012-2h4a2 2 0 012 2v6a2 2 0 01-2 2m0 0h-4m-4 0a2 2 0 002 2h4a2 2 0 002-2m-4 0V9m0 0H8m4 0a2 2 0 012-2H8a2 2 0 01-2 2v6a2 2 0 012 2m0 0h4m-4 0a2 2 0 002 2h4a2 2 0 002-2" />
                    </svg>
                    UrbanStyle
                </a>
                <button id="close-menu-btn" class="text-textLight dark:text-textDark" aria-label="Close mobile menu">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
            
            <nav class="flex flex-col space-y-4 mb-8">
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400 font-medium py-2 border-b border-gray-200 dark:border-gray-700" role="menuitem">Home</a>
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400 font-medium py-2 border-b border-gray-200 dark:border-gray-700" role="menuitem">Shop</a>
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400 font-medium py-2 border-b border-gray-200 dark:border-gray-700" role="menuitem">Collections</a>
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400 font-medium py-2 border-b border-gray-200 dark:border-gray-700" role="menuitem">About</a>
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400 font-medium py-2 border-b border-gray-200 dark:border-gray-700" role="menuitem">Contact</a>
            </nav>
            
            <div class="flex items-center space-x-4">
                <a href="#" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400" aria-label="User account">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                </a>
                <div class="relative">
                    <button id="mobile-cart-btn" class="text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400" aria-label="View shopping cart">
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                        </svg>
                        <span id="mobile-cart-count" class="absolute -top-2 -right-2 bg-primary-600 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">0</span>
                    </button>
                </div>
            </div>
        </div>
    </header>

    <section class="bg-gradient-to-r from-primary-500 to-primary-700 text-white py-16 md:py-24">
        <div class="container mx-auto px-4 flex flex-col md:flex-row items-center">
            <div class="md:w-1/2 mb-8 md:mb-0 animate-fadeIn">
                <h1 class="text-4xl md:text-5xl font-bold mb-4">Summer Collection 2025</h1>
                <p class="text-xl mb-6">Discover our latest trends and elevate your style with premium quality clothing.</p>
                <div class="flex space-x-4">
                    <a href="#" class="bg-white text-primary-600 px-6 py-3 rounded-md font-medium hover:bg-gray-100 transition" tabindex="0">Shop Now</a>
                    <a href="#" class="border border-white px-6 py-3 rounded-md font-medium hover:bg-white hover:text-primary-600 transition" tabindex="0">View Collection</a>
                </div>
            </div>
            <div class="md:w-1/2 flex justify-center animate-fadeIn" style="animation-delay: 0.2s;">
                <img src="https://via.placeholder.com/600x400/6366f1/ffffff?text=Fashion+Model" 
                     srcset="https://via.placeholder.com/300x200/6366f1/ffffff?text=Fashion+Model+300w 300w, 
                             https://via.placeholder.com/600x400/6366f1/ffffff?text=Fashion+Model+600w 600w, 
                             https://via.placeholder.com/900x600/6366f1/ffffff?text=Fashion+Model+900w 900w"
                     sizes="(max-width: 600px) 300px, (max-width: 900px) 600px, 900px"
                     alt="Fashion Model" 
                     class="rounded-lg shadow-xl max-w-full h-auto md:max-w-md" 
                     loading="lazy">
            </div>
        </div>
    </section>

    <section class="py-12 bg-white dark:bg-gray-900">
        <div class="container mx-auto px-4">
            <h2 class="text-3xl font-bold text-center mb-12 text-textLight dark:text-textDark">Shop by Category</h2>
            
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <a href="#" class="group relative overflow-hidden rounded-lg shadow-md hover:shadow-lg transition" tabindex="0">
                    <img src="https://via.placeholder.com/400x300/a5b4fc/ffffff?text=Men%27s+Clothing" 
                         srcset="https://via.placeholder.com/200x150/a5b4fc/ffffff?text=Men%27s+Clothing+200w 200w, 
                                 https://via.placeholder.com/400x300/a5b4fc/ffffff?text=Men%27s+Clothing+400w 400w"
                         sizes="(max-width: 768px) 200px, 400px"
                         alt="Men's Clothing" class="w-full h-48 object-cover transition duration-500 group-hover:scale-105" loading="lazy">
                    <div class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
                        <h3 class="text-white text-xl font-bold">Men's</h3>
                    </div>
                </a>
                
                <a href="#" class="group relative overflow-hidden rounded-lg shadow-md hover:shadow-lg transition" tabindex="0">
                    <img src="https://via.placeholder.com/400x300/c7d2fe/ffffff?text=Women%27s+Clothing" 
                         srcset="https://via.placeholder.com/200x150/c7d2fe/ffffff?text=Women%27s+Clothing+200w 200w, 
                                 https://via.placeholder.com/400x300/c7d2fe/ffffff?text=Women%27s+Clothing+400w 400w"
                         sizes="(max-width: 768px) 200px, 400px"
                         alt="Women's Clothing" class="w-full h-48 object-cover transition duration-500 group-hover:scale-105" loading="lazy">
                    <div class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
                        <h3 class="text-white text-xl font-bold">Women's</h3>
                    </div>
                </a>
                
                <a href="#" class="group relative overflow-hidden rounded-lg shadow-md hover:shadow-lg transition" tabindex="0">
                    <img src="https://via.placeholder.com/400x300/e0e7ff/1f2937?text=Accessories" 
                         srcset="https://via.placeholder.com/200x150/e0e7ff/1f2937?text=Accessories+200w 200w, 
                                 https://via.placeholder.com/400x300/e0e7ff/1f2937?text=Accessories+400w 400w"
                         sizes="(max-width: 768px) 200px, 400px"
                         alt="Accessories" class="w-full h-48 object-cover transition duration-500 group-hover:scale-105" loading="lazy">
                    <div class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
                        <h3 class="text-white text-xl font-bold">Accessories</h3>
                    </div>
                </a>
                
                <a href="#" class="group relative overflow-hidden rounded-lg shadow-md hover:shadow-lg transition" tabindex="0">
                    <img src="https://via.placeholder.com/400x300/eef2ff/1f2937?text=Footwear" 
                         srcset="https://via.placeholder.com/200x150/eef2ff/1f2937?text=Footwear+200w 200w, 
                                 https://via.placeholder.com/400x300/eef2ff/1f2937?text=Footwear+400w 400w"
                         sizes="(max-width: 768px) 200px, 400px"
                         alt="Footwear" class="w-full h-48 object-cover transition duration-500 group-hover:scale-105" loading="lazy">
                    <div class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
                        <h3 class="text-white text-xl font-bold">Footwear</h3>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <section class="py-12 bg-backgroundLight dark:bg-gray-800">
        <div class="container mx-auto px-4">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8">
                <h2 class="text-3xl font-bold text-textLight dark:text-textDark mb-4 md:mb-0">Featured Products</h2>
                <div class="flex flex-col sm:flex-row space-y-2 sm:space-y-0 sm:space-x-4 w-full md:w-auto">
                    <select id="sort-by" class="p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-textLight dark:text-textDark focus:ring-primary-500 focus:border-primary-500" aria-label="Sort products by">
                        <option value="popularity">Popularity</option>
                        <option value="price-asc">Price: Low to High</option>
                        <option value="price-desc">Price: High to Low</option>
                        <option value="newest">Newest Arrivals</option>
                    </select>
                    <button class="bg-gray-200 dark:bg-gray-700 text-textLight dark:text-textDark px-4 py-2 rounded-md hover:bg-gray-300 dark:hover:bg-gray-600 transition" aria-label="Apply filters">Apply Filters</button>
                </div>
            </div>
            
            <div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                <div class="bg-white dark:bg-gray-900 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition">
                    <div class="relative">
                        <img src="https://via.placeholder.com/400x300/818cf8/ffffff?text=Denim+Jacket" 
                             srcset="https://via.placeholder.com/200x150/818cf8/ffffff?text=Denim+Jacket+200w 200w, 
                                     https://via.placeholder.com/400x300/818cf8/ffffff?text=Denim+Jacket+400w 400w"
                             sizes="(max-width: 640px) 200px, (max-width: 768px) 300px, 400px"
                             alt="Classic Denim Jacket" class="w-full h-64 object-cover" loading="lazy">
                        <div class="absolute top-2 right-2 bg-danger text-white text-xs font-bold px-2 py-1 rounded">SALE</div>
                        <button class="quick-view-btn absolute bottom-2 left-1/2 -translate-x-1/2 bg-white dark:bg-gray-700 text-textLight dark:text-textDark px-4 py-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300"
                                data-id="1" data-name="Classic Denim Jacket" data-price="69.99" data-image="https://via.placeholder.com/600x400/818cf8/ffffff?text=Denim+Jacket"
                                aria-label="Quick view Classic Denim Jacket">Quick View</button>
                    </div>
                    <div class="p-4">
                        <h3 class="font-bold text-lg mb-1 text-textLight dark:text-textDark">Classic Denim Jacket</h3>
                        <div class="flex items-center mb-2">
                            <div class="flex text-accent">
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293c-.39-.39-1.023-.39-1.414 0l-7 7A1 1 0 003 11v6a1 1 0 001 1h6a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1h6a1 1 0 001-1v-6a1 1 0 00-.293-.707l-7-7z"></path></svg>
                            </div>
                            <span class="text-gray-600 dark:text-gray-400 text-sm ml-2">(42)</span>
                        </div>
                        <div class="flex items-center justify-between">
                            <div>
                                <span class="text-gray-500 dark:text-gray-400 line-through mr-2">$89.99</span>
                                <span class="font-bold text-primary-600 dark:text-primary-400">$69.99</span>
                            </div>
                            <button class="add-to-cart text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400" 
                                    data-id="1" data-name="Classic Denim Jacket" data-price="69.99" 
                                    data-image="https://via.placeholder.com/400x300/818cf8/ffffff?text=Denim+Jacket"
                                    aria-label="Add Classic Denim Jacket to cart">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white dark:bg-gray-900 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition">
                    <div class="relative">
                        <img src="https://via.placeholder.com/400x300/6366f1/ffffff?text=White+T-Shirt" 
                             srcset="https://via.placeholder.com/200x150/6366f1/ffffff?text=White+T-Shirt+200w 200w, 
                                     https://via.placeholder.com/400x300/6366f1/ffffff?text=White+T-Shirt+400w 400w"
                             sizes="(max-width: 640px) 200px, (max-width: 768px) 300px, 400px"
                             alt="Essential White Tee" class="w-full h-64 object-cover" loading="lazy">
                        <button class="quick-view-btn absolute bottom-2 left-1/2 -translate-x-1/2 bg-white dark:bg-gray-700 text-textLight dark:text-textDark px-4 py-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300"
                                data-id="2" data-name="Essential White Tee" data-price="24.99" data-image="https://via.placeholder.com/600x400/6366f1/ffffff?text=White+T-Shirt"
                                aria-label="Quick view Essential White Tee">Quick View</button>
                    </div>
                    <div class="p-4">
                        <h3 class="font-bold text-lg mb-1 text-textLight dark:text-textDark">Essential White Tee</h3>
                        <div class="flex items-center mb-2">
                            <div class="flex text-accent">
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293c-.39-.39-1.023-.39-1.414 0l-7 7A1 1 0 003 11v6a1 1 0 001 1h6a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1h6a1 1 0 001-1v-6a1 1 0 00-.293-.707l-7-7z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 4a1 1 0 011 1v1a1 1 0 11-2 0V7a1 1 0 011-1zm-4 7a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zm-4-4a1 1 0 011 1v1a1 1 0 11-2 0V9a1 1 0 011-1z"></path></svg>
                            </div>
                            <span class="text-gray-600 dark:text-gray-400 text-sm ml-2">(78)</span>
                        </div>
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-primary-600 dark:text-primary-400">$24.99</span>
                            <button class="add-to-cart text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400" 
                                    data-id="2" data-name="Essential White Tee" data-price="24.99"
                                    data-image="https://via.placeholder.com/400x300/6366f1/ffffff?text=White+T-Shirt"
                                    aria-label="Add Essential White Tee to cart">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="bg-white dark:bg-gray-900 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition">
                    <div class="relative">
                        <img src="https://via.placeholder.com/400x300/4f46e5/ffffff?text=Cargo+Pants" 
                             srcset="https://via.placeholder.com/200x150/4f46e5/ffffff?text=Cargo+Pants+200w 200w, 
                                     https://via.placeholder.com/400x300/4f46e5/ffffff?text=Cargo+Pants+400w 400w"
                             sizes="(max-width: 640px) 200px, (max-width: 768px) 300px, 400px"
                             alt="Stylish Cargo Pants" class="w-full h-64 object-cover" loading="lazy">
                        <div class="absolute top-2 left-2 bg-success text-white text-xs font-bold px-2 py-1 rounded">NEW</div>
                        <button class="quick-view-btn absolute bottom-2 left-1/2 -translate-x-1/2 bg-white dark:bg-gray-700 text-textLight dark:text-textDark px-4 py-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300"
                                data-id="3" data-name="Stylish Cargo Pants" data-price="54.99" data-image="https://via.placeholder.com/600x400/4f46e5/ffffff?text=Cargo+Pants"
                                aria-label="Quick view Stylish Cargo Pants">Quick View</button>
                    </div>
                    <div class="p-4">
                        <h3 class="font-bold text-lg mb-1 text-textLight dark:text-textDark">Stylish Cargo Pants</h3>
                        <div class="flex items-center mb-2">
                            <div class="flex text-accent">
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293c-.39-.39-1.023-.39-1.414 0l-7 7A1 1 0 003 11v6a1 1 0 001 1h6a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1h6a1 1 0 001-1v-6a1 1 0 00-.293-.707l-7-7z"></path></svg>
                            </div>
                            <span class="text-gray-600 dark:text-gray-400 text-sm ml-2">(55)</span>
                        </div>
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-primary-600 dark:text-primary-400">$54.99</span>
                            <button class="add-to-cart text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400" 
                                    data-id="3" data-name="Stylish Cargo Pants" data-price="54.99"
                                    data-image="https://via.placeholder.com/400x300/4f46e5/ffffff?text=Cargo+Pants"
                                    aria-label="Add Stylish Cargo Pants to cart">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="bg-white dark:bg-gray-900 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition">
                    <div class="relative">
                        <img src="https://via.placeholder.com/400x300/312e81/ffffff?text=Leather+Boots" 
                             srcset="https://via.placeholder.com/200x150/312e81/ffffff?text=Leather+Boots+200w 200w, 
                                     https://via.placeholder.com/400x300/312e81/ffffff?text=Leather+Boots+400w 400w"
                             sizes="(max-width: 640px) 200px, (max-width: 768px) 300px, 400px"
                             alt="Premium Leather Boots" class="w-full h-64 object-cover" loading="lazy">
                        <button class="quick-view-btn absolute bottom-2 left-1/2 -translate-x-1/2 bg-white dark:bg-gray-700 text-textLight dark:text-textDark px-4 py-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300"
                                data-id="4" data-name="Premium Leather Boots" data-price="120.00" data-image="https://via.placeholder.com/600x400/312e81/ffffff?text=Leather+Boots"
                                aria-label="Quick view Premium Leather Boots">Quick View</button>
                    </div>
                    <div class="p-4">
                        <h3 class="font-bold text-lg mb-1 text-textLight dark:text-textDark">Premium Leather Boots</h3>
                        <div class="flex items-center mb-2">
                            <div class="flex text-accent">
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293c-.39-.39-1.023-.39-1.414 0l-7 7A1 1 0 003 11v6a1 1 0 001 1h6a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1h6a1 1 0 001-1v-6a1 1 0 00-.293-.707l-7-7z"></path></svg>
                            </div>
                            <span class="text-gray-600 dark:text-gray-400 text-sm ml-2">(68)</span>
                        </div>
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-primary-600 dark:text-primary-400">$120.00</span>
                            <button class="add-to-cart text-textLight dark:text-textDark hover:text-primary-600 dark:hover:text-primary-400" 
                                    data-id="4" data-name="Premium Leather Boots" data-price="120.00"
                                    data-image="https://via.placeholder.com/400x300/312e81/ffffff?text=Leather+Boots"
                                    aria-label="Add Premium Leather Boots to cart">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="text-center mt-12">
                <a href="#" class="inline-block bg-primary-600 text-white px-8 py-3 rounded-md font-medium hover:bg-primary-700 transition">View All Products</a>
            </div>
        </div>
    </section>

    <section class="py-12 bg-white dark:bg-gray-900">
        <div class="container mx-auto px-4">
            <h2 class="text-3xl font-bold text-center mb-12 text-textLight dark:text-textDark">What Our Customers Say</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="bg-backgroundLight dark:bg-gray-800 p-6 rounded-lg shadow-md">
                    <div class="flex items-center mb-4">
                        <img src="https://via.placeholder.com/60x60/a5b4fc/ffffff?text=JD" alt="Customer Jane Doe" class="w-12 h-12 rounded-full mr-4">
                        <div>
                            <p class="font-bold text-textLight dark:text-textDark">Jane Doe</p>
                            <div class="flex text-accent text-sm">
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4 text-gray-300 dark:text-gray-600" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                            </div>
                        </div>
                    </div>
                    <p class="text-gray-700 dark:text-gray-300 leading-relaxed">"UrbanStyle has truly transformed my wardrobe! The quality of their clothing is exceptional, and their designs are always on-point. Highly recommend!"</p>
                </div>
                <div class="bg-backgroundLight dark:bg-gray-800 p-6 rounded-lg shadow-md">
                    <div class="flex items-center mb-4">
                        <img src="https://via.placeholder.com/60x60/c7d2fe/ffffff?text=AM" alt="Customer Alex Mark" class="w-12 h-12 rounded-full mr-4">
                        <div>
                            <p class="font-bold text-textLight dark:text-textDark">Alex Mark</p>
                            <div class="flex text-accent text-sm">
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                            </div>
                        </div>
                    </div>
                    <p class="text-gray-700 dark:text-gray-300 leading-relaxed">"Fast shipping and incredible customer service! I had an issue with my order, and they resolved it quickly and efficiently. Will definitely shop again."</p>
                </div>
                <div class="bg-backgroundLight dark:bg-gray-800 p-6 rounded-lg shadow-md">
                    <div class="flex items-center mb-4">
                        <img src="https://via.placeholder.com/60x60/e0e7ff/1f2937?text=SD" alt="Customer Sarah Davis" class="w-12 h-12 rounded-full mr-4">
                        <div>
                            <p class="font-bold text-textLight dark:text-textDark">Sarah Davis</p>
                            <div class="flex text-accent text-sm">
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.817 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.683-1.532 1.118l-2.817-2.034a1 1 0 00-1.176 0l-2.817 2.034c-.777.565-1.832-.197-1.532-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.929 8.729c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z"></path></svg>
                                <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293c-.39-.39-1.023-.39-1.414 0l-7 7A1 1 0 003 11v6a1 1 0 001 1h6a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1h6a1 1 0 001-1v-6a1 1 0 00-.293-.707l-7-7z"></path></svg>
                            </div>
                        </div>
                    </div>
                    <p class="text-gray-700 dark:text-gray-300 leading-relaxed">"The perfect blend of modern style and comfort. Every piece feels premium and lasts a long time. My go-to shop for all fashion needs."</p>
                </div>
            </div>
        </div>
    </section>

    <section class="bg-primary-600 text-white py-12">
        <div class="container mx-auto px-4 text-center">
            <h2 class="text-3xl font-bold mb-4">Join Our Newsletter</h2>
            <p class="text-xl mb-6">Stay up-to-date with our latest collections, exclusive offers, and more!</p>
            <form class="flex flex-col sm:flex-row justify-center items-center gap-4 max-w-lg mx-auto">
                <input type="email" placeholder="Enter your email" aria-label="Email for newsletter"
                       class="w-full sm:w-auto flex-grow px-4 py-3 rounded-md border border-white text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary-300" required>
                <button type="submit" class="bg-white text-primary-600 px-6 py-3 rounded-md font-medium hover:bg-gray-100 transition">Subscribe</button>
            </form>
        </div>
    </section>

    <footer class="bg-gray-800 dark:bg-gray-950 text-gray-300 py-10">
        <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
                <h3 class="text-white font-bold text-lg mb-4">UrbanStyle</h3>
                <p class="text-sm">Your ultimate destination for modern and stylish fashion.</p>
                <div class="flex space-x-4 mt-4">
                    <a href="#" class="text-gray-400 hover:text-white" aria-label="Facebook">
                        <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h3V2h-3c-3.87 0-5 3.13-5 7v2.5H8v4h3V22h4v-8.5z"></path></svg>
                    </a>
                    <a href="#" class="text-gray-400 hover:text-white" aria-label="Twitter">
                        <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M22.46 6c-.77.34-1.6.56-2.46.66.89-.53 1.57-1.37 1.89-2.37-.83.49-1.75.85-2.72 1.05-.79-.84-1.92-1.37-3.17-1.37-2.39 0-4.34 1.95-4.34 4.34 0 .34.04.67.11.98-3.61-.18-6.8-1.91-8.94-4.56-.37.64-.58 1.39-.58 2.19 0 1.5.76 2.82 1.92 3.61-.7-.02-1.35-.21-1.92-.53v.06c0 2.1 1.49 3.86 3.47 4.26-.36.1-.74.15-1.13.15-.28 0-.55-.03-.81-.08.55 1.72 2.14 2.98 4.02 3.01-1.48 1.16-3.34 1.86-5.36 1.86-.35 0-.69-.02-1.03-.06C3.4 20.37 5.75 21 8.25 21c9.93 0 15.36-8.22 15.36-15.36 0-.23-.01-.46-.01-.69.97-.7 1.8-1.57 2.46-2.55z"></path></svg>
                    </a>
                    <a href="#" class="text-gray-400 hover:text-white" aria-label="Instagram">
                        <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4c0 3.2-2.6 5.8-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8C2 4.6 4.6 2 7.8 2zm-.2 2.75A.75.75 0 117.375 5.5 1 1 0 007.6 4.75zM12 6.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zm0 2.5a3 3 0 110 6 3 3 0 010-6z"></path></svg>
                    </a>
                </div>
            </div>
            <div>
                <h3 class="text-white font-bold text-lg mb-4">Quick Links</h3>
                <ul class="space-y-2">
                    <li><a href="#" class="hover:text-white transition">Shop All</a></li>
                    <li><a href="#" class="hover:text-white transition">New Arrivals</a></li>
                    <li><a href="#" class="hover:text-white transition">Sale</a></li>
                    <li><a href="#" class="hover:text-white transition">FAQ</a></li>
                    <li><a href="#" class="hover:text-white transition">Shipping & Returns</a></li>
                </ul>
            </div>
            <div>
                <h3 class="text-white font-bold text-lg mb-4">Customer Service</h3>
                <ul class="space-y-2">
                    <li><a href="#" class="hover:text-white transition">Contact Us</a></li>
                    <li><a href="#" class="hover:text-white transition">Order Tracking</a></li>
                    <li><a href="#" class="hover:text-white transition">Privacy Policy</a></li>
                    <li><a href="#" class="hover:text-white transition">Terms of Service</a></li>
                </ul>
            </div>
            <div>
                <h3 class="text-white font-bold text-lg mb-4">Contact Info</h3>
                <p class="text-sm">123 Fashion Ave, Style City, SC 90210</p>
                <p class="text-sm mt-2">Email: info@urbanstyle.com</p>
                <p class="text-sm mt-2">Phone: +1 (555) 123-4567</p>
            </div>
        </div>
        <div class="border-t border-gray-700 mt-8 pt-8 text-center text-sm">
            <p>&copy; 2025 UrbanStyle. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Theme toggle logic
        const themeToggleBtn = document.getElementById('theme-toggle');
        const htmlElement = document.documentElement;
        const darkIcon = document.getElementById('theme-toggle-dark-icon');
        const lightIcon = document.getElementById('theme-toggle-light-icon');

        // On page load or when changing themes, best to add inline in `head` to avoid FOUC
        if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            htmlElement.classList.add('dark');
            darkIcon.classList.remove('hidden');
            lightIcon.classList.add('hidden');
        } else {
            htmlElement.classList.remove('dark');
            darkIcon.classList.add('hidden');
            lightIcon.classList.remove('hidden');
        }

        themeToggleBtn.addEventListener('click', () => {
            if (htmlElement.classList.contains('dark')) {
                htmlElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
                darkIcon.classList.add('hidden');
                lightIcon.classList.remove('hidden');
            } else {
                htmlElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
                darkIcon.classList.remove('hidden');
                lightIcon.classList.add('hidden');
            }
        });

        // Mobile menu toggle
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const closeMenuBtn = document.getElementById('close-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');

        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.add('open');
        });

        closeMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.remove('open');
        });

        // Close mobile menu when a link is clicked
        mobileMenu.querySelectorAll('nav a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.remove('open');
            });
        });

        // Cart dropdown logic
        const cartBtn = document.getElementById('cart-btn');
        const mobileCartBtn = document.getElementById('mobile-cart-btn');
        const cartDropdown = document.getElementById('cart-dropdown');
        const cartItemsContainer = document.getElementById('cart-items');
        const cartTotalSpan = document.getElementById('cart-total');
        const cartCountSpan = document.getElementById('cart-count');
        const mobileCartCountSpan = document.getElementById('mobile-cart-count');

        let cart = JSON.parse(localStorage.getItem('cart')) || [];

        function updateCartDisplay() {
            cartItemsContainer.innerHTML = '';
            let total = 0;
            if (cart.length === 0) {
                cartItemsContainer.innerHTML = '<p class="text-gray-500 text-center py-4">Your cart is empty</p>';
            } else {
                cart.forEach(item => {
                    const itemElement = document.createElement('div');
                    itemElement.classList.add('flex', 'items-center', 'justify-between', 'py-2', 'border-b', 'border-gray-200', 'dark:border-gray-700', 'last:border-b-0');
                    itemElement.innerHTML = `
                        <div class="flex items-center">
                            <img src="${item.image}" alt="${item.name}" class="w-12 h-12 object-cover rounded mr-3">
                            <div>
                                <p class="text-textLight dark:text-textDark font-medium">${item.name}</p>
                                <p class="text-gray-500 dark:text-gray-400 text-sm">$${item.price.toFixed(2)} x ${item.quantity}</p>
                            </div>
                        </div>
                        <button class="remove-from-cart text-red-500 hover:text-red-700" data-id="${item.id}" aria-label="Remove ${item.name} from cart">
                            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    `;
                    cartItemsContainer.appendChild(itemElement);
                    total += item.price * item.quantity;
                });
            }
            cartTotalSpan.textContent = `$${total.toFixed(2)}`;
            const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
            cartCountSpan.textContent = totalItems;
            mobileCartCountSpan.textContent = totalItems;
            localStorage.setItem('cart', JSON.stringify(cart));
        }

        function toggleCartDropdown(event) {
            cartDropdown.classList.toggle('open');
            // Close if clicking outside
            if (cartDropdown.classList.contains('open')) {
                document.addEventListener('click', closeCartOutside);
            } else {
                document.removeEventListener('click', closeCartOutside);
            }
            event.stopPropagation(); // Prevent immediate closing
        }

        function closeCartOutside(event) {
            if (!cartDropdown.contains(event.target) && !cartBtn.contains(event.target) && !mobileCartBtn.contains(event.target)) {
                cartDropdown.classList.remove('open');
                document.removeEventListener('click', closeCartOutside);
            }
        }

        cartBtn.addEventListener('click', toggleCartDropdown);
        mobileCartBtn.addEventListener('click', toggleCartDropdown); // For mobile cart button

        document.addEventListener('click', (event) => {
            if (event.target.classList.contains('add-to-cart')) {
                const id = event.target.dataset.id;
                const name = event.target.dataset.name;
                const price = parseFloat(event.target.dataset.price);
                const image = event.target.dataset.image;

                const existingItem = cart.find(item => item.id === id);
                if (existingItem) {
                    existingItem.quantity++;
                } else {
                    cart.push({ id, name, price, image, quantity: 1 });
                }
                updateCartDisplay();
                // Optional: Show a brief confirmation message or animation
            } else if (event.target.classList.contains('remove-from-cart')) {
                const idToRemove = event.target.dataset.id;
                cart = cart.filter(item => item.id !== idToRemove);
                updateCartDisplay();
            }
        });

        // Product Quick View Modal Logic
        const quickViewModal = document.getElementById('quick-view-modal');
        const closeQuickViewBtn = document.getElementById('close-quick-view');
        const quickViewImage = document.getElementById('quick-view-image');
        const quickViewName = document.getElementById('quick-view-name');
        const quickViewPrice = document.getElementById('quick-view-price');
        const quickViewAddToCartBtn = document.getElementById('quick-view-add-to-cart');

        document.querySelectorAll('.quick-view-btn').forEach(button => {
            button.addEventListener('click', (e) => {
                const productId = e.target.dataset.id;
                const productName = e.target.dataset.name;
                const productPrice = e.target.dataset.price;
                const productImage = e.target.dataset.image;

                quickViewImage.src = productImage;
                quickViewName.textContent = productName;
                quickViewPrice.textContent = `$${parseFloat(productPrice).toFixed(2)}`;
                quickViewAddToCartBtn.dataset.id = productId;
                quickViewAddToCartBtn.dataset.name = productName;
                quickViewAddToCartBtn.dataset.price = productPrice;
                quickViewAddToCartBtn.dataset.image = productImage;

                quickViewModal.classList.add('open');
                setTimeout(() => { // Small delay for the scale-up animation
                    quickViewModal.querySelector('div').classList.remove('scale-95', 'opacity-0');
                    quickViewModal.querySelector('div').classList.add('scale-100', 'opacity-100');
                }, 10);
            });
        });

        closeQuickViewBtn.addEventListener('click', () => {
            quickViewModal.querySelector('div').classList.remove('scale-100', 'opacity-100');
            quickViewModal.querySelector('div').classList.add('scale-95', 'opacity-0');
            setTimeout(() => { // Delay hiding the modal until animation finishes
                quickViewModal.classList.remove('open');
            }, 300);
        });

        // Close modal if clicked outside
        quickViewModal.addEventListener('click', (e) => {
            if (e.target === quickViewModal) {
                closeQuickViewBtn.click();
            }
        });

        // Initial cart display
        updateCartDisplay();

        // Simulate dynamic content loading / filtering (example for sort-by)
        const productGrid = document.getElementById('product-grid');
        const sortBySelect = document.getElementById('sort-by');

        sortBySelect.addEventListener('change', (e) => {
            const sortBy = e.target.value;
            // In a real application, you'd fetch data or re-sort existing data here
            console.log(`Sorting products by: ${sortBy}`);
            // This is just a placeholder; actual re-rendering logic would go here.
            // For a static HTML, this select primarily serves as a visual element.
        });

    </script>
</body>
</html>
"""

    # --- CHANGE THIS LINE TO YOUR DESIRED FILE NAME ---
    output_filename = "urbanstyle_shop.html"
    # --------------------------------------------------

    try:
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"HTML file '{output_filename}' generated successfully!")
    except IOError as e:
        print(f"Error writing file: {e}")

# This line calls the function to generate the HTML file when the script is run
if __name__ == "__main__":
    create_urbanstyle_html()