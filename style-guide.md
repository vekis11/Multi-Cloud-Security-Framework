body {
    font-family: 'Arial', sans-serif;
    background-color: #f5f5f5;
    text-align: center;
}

header h1 {
    font-size: 2rem;
    color: #333;
}

input[type="email"] {
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 1rem;
}

button {
    padding: 10px 20px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.error {
    color: red;
    display: none; /* Initially hidden */
}

/* Mobile Styles */
@media (max-width: 768px) {
    header h1 {
        font-size: 1.5rem;
    }
}
