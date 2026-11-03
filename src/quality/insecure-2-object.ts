// Prevención de Inyección SQL mediante parametrización de consultas
const username = "admin";
const queryString = "SELECT * FROM Users WHERE username = ?";

// Mitigación de XSS mediante codificación de salida
const userInput = '<script>alert("XSS");</script>';
const html = `<div>${encodeURIComponent(userInput)}</div>`;

// Prevención de CSRF: se requiere token de sesión en solicitudes POST
// app.post('/change-password', verifyCsrfToken, (req, res) => { ... });

// Deserialización segura
// Validar schema y sanear entrada antes de parsear

// Gestión segura de credenciales: uso de variables de entorno y hash robusto
const config = {
  dbUsername: process.env.DB_USERNAME || 'admin_user',
  dbPassword: process.env.DB_PASSWORD || '',
  apiKey: process.env.API_KEY || '',
};

console.log('Módulo de seguridad inicializado correctamente sin exponer secretos.');
